import sys, sqlite3, os, glob
sys.dont_write_bytecode = True

from .Styling import sd, bc
from .Config import CoreConfig
from .Commands import Command
from .Validity import Validation
from .Error import ErrorHandler

class Migrator:
    def __init__(self, Env: dict = None, Validator: Validation = None, Error: ErrorHandler = None) -> None:
        self.Env = Env
        self.Validator = Validator
        self.Error = Error

        self.MigrationsPath = "Database/Migrations/*.sql"

        self.ShouldRun = False

    def LoadSQLStatements(self) -> list:
        MigrationFiles = glob.glob(self.MigrationsPath)

        SQLStatements = []

        for MigrationFile in MigrationFiles:
            try:
                FileReader = open(MigrationFile, "r")
                SQLData = FileReader.read()
                FileReader.close()

                if(self.Validator.NotEmpty(SQLData)):
                    SQLStatements.append(SQLData.replace("\n", "").replace("\t", ""))
            except Exception as e:
                self.Error.Throw("database_migration", [MigrationFile, e])
                self.Error.AddToLog("error", f"Could not run migration file '{MigrationFile}' ({e})")
                
                quit()

        if(not self.Validator.NotEmpty(SQLStatements)):
            self.Error.Throw("database_migration_sql_load")
            self.Error.AddToLog("error", f"Could not load migration SQL statements")

            quit()
        
        return SQLStatements

class Database:
    def __init__(self, Env: dict = None, Config: CoreConfig = None) -> None:
        self.Env = Env
        self.Config = Config
        self.Validator = Validation()
        self.Error = ErrorHandler()

        self.Migrator = Migrator(self.Env, self.Validator, self.Error)

        self.DatabasePath = self.Env["DatabasePath"]
        
        self.Connection = None
        
        self.Connect()

        self.Interface = Interface(self.Env,self.Validator, self.Error, self, self.Config)
    
    def Connect(self) -> None:
        if(not os.path.isfile(self.DatabasePath)):
            self.Migrator.ShouldRun = True

        try:
            self.Connection = sqlite3.connect(self.DatabasePath)

            print(f"{sd.sBan}Connected to {bc.GC}{self.DatabasePath}{bc.BC}\n")
        except sqlite3.OperationalError as e:
            self.Error.Throw("database_connection", [self.DatabasePath, e])
            self.Error.AddToLog("error", f"Could not connect to database at '{self.DatabasePath}' ({e})")

            quit()

        self.RunMigrations()

    def RunMigrations(self) -> None:
        if(self.Migrator.ShouldRun):
            SQLStatements = self.Migrator.LoadSQLStatements()
            
            [self.Execute(SQLStatement) for SQLStatement in SQLStatements if(self.Validator.NotEmpty(SQLStatement))]

    def DoesTableExist(self, Table: str = None) -> bool:
        if(self.Validator.NotEmpty(Table)):
            return True
        
        return False

    def __GetTableColumns(self, Table: str = None) -> (list | None):
        if(self.Validator.NotEmpty(Table)):
            Cursor = self.Connection.cursor()
            Cols = Cursor.execute(f"PRAGMA table_info({Table});").fetchall()

            Columns = []

            [Columns.append(Col[1]) for Col in Cols if(self.Validator.NotEmpty(Col[1]))]

            if(self.Validator.NotEmpty(Columns)):
                return Columns

        return None

    def Execute(self, SQLQuery: str):
        self.Connection.execute(SQLQuery)

    def __FormatWhereString(self, Where: list = []) -> str:
        WhereString = ""

        if(self.Validator.NotEmpty(Where)):
            WherePackCounter = 0

            for WherePack in Where:
                if(len(WherePack) >= 3 and not len(WherePack) > 4):
                    Column = WherePack[0]
                    Operator = WherePack[1]
                    Value = WherePack[2]

                    if(type(Value) == str):
                        Value = f"'{Value}'"

                    Clause = ""
                    if(len(WherePack) == 4):
                        Clause = f" {WherePack[3]} "
                    
                    if(WherePackCounter == 0):
                        WhereString = " WHERE "
                    
                    WhereString += f"{Column} {Operator} {Value}"

                    if(WherePackCounter < len(WherePack) - 1):
                        WhereString += Clause
                    
                WherePackCounter += 1
                
        return WhereString

    def Select(self, Table: str = None, Where: list = []) -> (dict | list | None):
        if(self.Validator.NotEmpty(Table)):
            Table = Table.lower().strip()

            if(self.DoesTableExist(Table)):
                SQL = f"SELECT * FROM `{Table}`"
                SQL += self.__FormatWhereString(Where)

                Cursor = self.Connection.cursor()
                Rows = Cursor.execute(SQL).fetchall()

                Columns = self.__GetTableColumns(Table)
                ReturnableRows = []

                for Row in Rows:
                    RowData, ItemCounter = {}, 0

                    for Item in Row:
                        Column = Columns[ItemCounter]

                        RowData[Column] = Item
                        ItemCounter += 1
                    
                    if(len(Rows) == 1):
                        return RowData
                    elif(len(Rows) > 1):
                        if(self.Validator.NotEmpty(RowData)):
                            ReturnableRows.append(RowData)

                if(self.Validator.NotEmpty(ReturnableRows)):
                    return ReturnableRows
                else:
                    return None
            else:
                self.Error.Throw("database_select_invalid_table", Table)
                self.Error.AddToLog("error", f"Database.Select.Error: table '{Table}' does not exist")
        else:
            self.Error.Throw("database_select_none_type_table")
            self.Error.AddToLog("error", f"Database.Select.Error: table name is NoneType")

    def Insert(self, Table: str = None, Values: list = []) -> bool:
        if(self.Validator.NotEmpty(Table)):
            if(self.DoesTableExist(Table)):
                if(self.Validator.NotEmpty(Values)):
                    SQL = f"INSERT INTO `{Table}` (COLUMNS_STRING) VALUES (VALUES_STRING);"

                    Columns = self.__GetTableColumns(Table)
                    SQL = SQL.replace("COLUMNS_STRING", ", ".join(Columns))

                    ValuesString, ValuesCounter = "", 0

                    for Value in Values:
                        if(type(Value) == str):
                            Value = f"'{Value}'"

                        ValuesString += f"{Value}"

                        if(ValuesCounter < len(Values) - 1):
                            ValuesString += ", "

                        ValuesCounter += 1
                    
                    if(self.Validator.NotEmpty(ValuesString)):
                        SQL = SQL.replace("VALUES_STRING", ValuesString)

                        try:
                            Cursor = self.Connection.cursor()
                            Cursor.execute(SQL)
                            self.Connection.commit()
                            Cursor.close()

                            return True
                        except sqlite3.OperationalError as e:
                            print(self.Error.Throw("database_insert_execution_failure", [SQL, e]))
                            self.Error.AddToLog("error", f"Database.Insert.Error: execution failure ({e})")
                else:
                    self.Error.Throw("database_insert_missing_values")
                    self.Error.AddToLog("error", f"Database.Insert.Error: insert values are required")
            else:
                self.Error.Throw("database_insert_invalid_table", Table)
                self.Error.AddToLog("error", f"Database.Insert.Error: table '{Table}' does not exist")
        else:
            self.Error.Throw("database_insert_none_type_table")
            self.Error.AddToLog("error", f"Database.Insert.Error: table name is NoneType")
        
        return False

    def Update(self, Table: str = None, Set: dict = {}, Where: list = []) -> bool:
        if(self.Validator.NotEmpty(Table)):
            Table = Table.lower().strip()

            if(self.DoesTableExist(Table)):
                SQL = SQLOriginal = f"UPDATE `{Table}`"

                if(self.Validator.NotEmpty(Set)):
                    SetString, SetCounter = " SET ", 0

                    for Key, Value in Set.items():
                        if(type(Value) == str):
                            Value = f"'{Value}'"

                        SetString += f"{Key} = {Value}"
                        
                        if(SetCounter < len(Set.keys()) - 1):
                            SetString += ", "

                        SetCounter += 1
                    
                    if(SetString != " SET "):
                        WhereString = self.__FormatWhereString(Where)

                        SQL += f"{SetString}{WhereString}"
                
                if(SQL != SQLOriginal):
                    try:
                        Cursor = self.Connection.cursor()
                        Cursor.execute(SQL)
                        self.Connection.commit()
                        Cursor.close()

                        return True
                    except sqlite3.OperationalError as e:
                        self.Error.Throw("database_update_execution_failure", [SQL, e])
                        self.Error.AddToLog("error", f"Database.Select.Update: execution failed ({e})")
                else:
                    self.Error.Throw("database_update_malformed_sql", SQL)
                    self.Error.AddToLog("error", f"Database.Update.Error: SQL Query is malformed ({SQL})")
            else:
                self.Error.Throw("database_update_invalid_table", Table)
                self.Error.AddToLog("error", f"Database.Update.Error: table '{Table}' does not exist")
        else:
            self.Error.Throw("database_update_none_type_table")
            self.Error.AddToLog("error", f"Database.Update.Error: table name is NoneType")

        return False
        
    def Delete(self, Table: str = None, Where: list = []) -> bool:
        if(self.Validator.NotEmpty(Table)):
            Table = Table.lower().strip()

            if(self.DoesTableExist(Table)):
                SQL = f"DELETE FROM `{Table}`"
                SQL += self.__FormatWhereString(Where)

                try:
                    Cursor = self.Connection.cursor()
                    Cursor.execute(SQL)
                    self.Connection.commit()
                    Cursor.close()

                    return True
                except sqlite3.OperationalError as e:
                    self.Error.Throw("database_delete_execution_failure", [SQL, e])
                    self.Error.AddToLog("error", f"Database.Delete.Update: execution failed ({e})")
            else:
                self.Error.Throw("database_delete_invalid_table", Table)
                self.Error.AddToLog("error", f"Database.Delete.Error: table '{Table}' does not exist")
        else:
            self.Error.Throw("database_delete_none_type_table")
            self.Error.AddToLog("error", f"Database.Delete.Error: table name is NoneType")

        return False

class Interface:
    def __init__(self, Env: dict = None, Validator: Validation = None, Error: ErrorHandler = None, Database: Database = None, Config: CoreConfig = None) -> None:
        self.Env = Env
        self.Validator = Validator
        self.Error = Error
        self.Database = Database
        self.Config = Config

        self.Cmd = Command()

        self.Commands = {
            "list_websites": f"Use {bc.GC}list{bc.BC} to list all websites",
            "activate_website": f"Use {bc.GC}activate <website-id>{bc.BC} (website_id value is an MD5 hash)",
            "deactivate_website": f"Use {bc.GC}deactivate <website_id>{bc.BC} (website_id value is an MD5 hash)",
            "add_website": f"Use {bc.GC}add <website_name> <website_url>{bc.BC} (e.g {bc.GC}add example_website https://example-website.com{bc.BC})",
            "update_website": f"Use {bc.GC}update <type> <value>{bc.BC} to update a website (type value can be {bc.GC}name{bc.BC} or {bc.GC}url{bc.BC})",
            "delete_website": f"Use {bc.GC}delete <website_id>{bc.BC} (website_id value is an MD5 hash)"
        }

    def Help(self):
        HelpCounter = 0

        print()
        
        for Category, Description in self.Commands.items():
            if("_" in Category):
                CategoryPieces = Category.split("_")
                Category, CategoryCounter = "", 0

                for CategoryPiece in CategoryPieces:
                    Category += CategoryPiece.capitalize()

                    if(CategoryCounter < len(CategoryPieces) - 1):
                        Category += " "
                    
                    CategoryCounter += 1
            else:
                Category = Category.capitalize()
            
            if(len(Category) <= 14):
                print(f" {bc.BC}{Category}\t\t{Description}")
            else:
                print(f" {bc.BC}{Category}\t{Description}")
            
            if(HelpCounter == len(self.Commands.keys()) - 1):
                print()
            
            HelpCounter += 1

    def Stream(self, InterfaceCommand: str = None, ShowHelp: bool = False):
        if(ShowHelp):
            print(f"{bc.BC} Enter {bc.GC}help{bc.BC} to see all database commands\n")

        try:
            if(not self.Validator.NotEmpty(InterfaceCommand)):
                InterfaceCommand = str(input(f"{bc.BC} DB Interface ?>{bc.GC} ")).strip()
            
            if(self.Validator.NotEmpty(InterfaceCommand)):
                if(InterfaceCommand == "help"):
                    self.Help()
                elif(InterfaceCommand == "list"):
                    Websites = self.Database.Select("website_urls", [["is_active", "=", 1]])

                    if(self.Validator.NotEmpty(Websites)):
                        print()

                        for WebsiteData in Websites:
                            WebsiteID, WebsiteName, WebsiteUrl = WebsiteData["id"], WebsiteData["website_name"], WebsiteData["url"]

                            print(f"{bc.BC} | ID: {bc.GC}{WebsiteID}{bc.BC}")
                            print(f"{bc.BC} | Name: {bc.GC}{WebsiteName}{bc.BC}")
                            print(f"{bc.BC} | URL: {bc.GC}{WebsiteUrl}{bc.BC}\n")
                    else:
                        print(self.Error.Throw("database_interface_list_no_websites"), False)
                        self.Error.AddToLog("error", f"Could not list websites. No websites were found")

                    self.Stream(None)
                elif(InterfaceCommand.startswith("activate ") and InterfaceCommand != "activate "):
                    WebsiteID = InterfaceCommand.split(" ")[1]

                    if(self.Validator.ID(WebsiteID)):
                        Website = self.Database.Select("website_urls", [["id", "=", WebsiteID]])

                        if(self.Validator.NotEmpty(Website)):
                            if(self.Database.Update("website_urls", {"is_active": 1}, [["id", "=", WebsiteID]])):
                                print(f"\n{sd.sBan}Successfully activated {bc.GC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"Successfully activated website ID '{WebsiteID}'")
                            else:
                                print(f"\n{sd.eBan}There was a problem activating {bc.RC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"There was a problem activating website ID '{WebsiteID}'")
                        else:
                            print(f"\n{sd.eBan}Website ID {bc.RC}{WebsiteID}{bc.BC} does not exist\n")
                            self.Error.AddToLog("error", f"Could not activate website. Website ID '{WebsiteID}' does not exist")
                    else:
                        print(self.Error.Throw("database_interface_activate_invalid_id"))
                        self.Error.AddToLog("error", f"Could not activate website. Website ID '{WebsiteID}' is invalid")

                    self.Stream(None)
                elif(InterfaceCommand.startswith("deactivate ") and InterfaceCommand != "deactivate "):
                    WebsiteID = InterfaceCommand.split(" ")[1]
                    
                    if(self.Validator.ID(WebsiteID)):
                        Website = self.Database.Select("website_urls", [["id", "=", WebsiteID]])

                        if(self.Validator.NotEmpty(Website)):
                            if(self.Database.Update("website_urls", {"is_active": 0}, [["id", "=", WebsiteID]])):
                                print(f"\n{sd.sBan}Successfully deactivated {bc.GC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"Successfully deactivated website ID '{WebsiteID}'")
                            else:
                                print(f"\n{sd.eBan}There was a problem deactivating {bc.RC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"There was a problem deactivating website ID '{WebsiteID}'")
                        else:
                            print(f"\n{sd.eBan}Website ID {bc.RC}{WebsiteID}{bc.BC} does not exist\n")
                            self.Error.AddToLog("error", f"Could not deactivate website. Website ID '{WebsiteID}' does not exist")
                    else:
                        print(self.Error.Throw("database_interface_deactivate_invalid_id"))
                        self.Error.AddToLog("error", f"Could not deactivate website. Website ID '{WebsiteID}' is invalid")
                    
                    self.Stream(None)
                elif(InterfaceCommand.startswith("add ") and InterfaceCommand != "add "):
                    CommandPieces = InterfaceCommand.replace("add ", "").strip().split(" ")
                    
                    if(len(CommandPieces) == 2):
                        WebsiteName = CommandPieces[0]

                        if("_" in WebsiteName):
                            WebsiteNamePieces = WebsiteName.split("_")
                            WebsiteName, WebsiteNameCounter = "", 0

                            for WebsiteNamePiece in WebsiteNamePieces:
                                WebsiteName += WebsiteNamePiece.capitalize()

                                if(WebsiteNameCounter < len(WebsiteNamePieces) - 1):
                                    WebsiteName += " "
                                
                                WebsiteNameCounter += 1
                        else:
                            WebsiteName = WebsiteName.capitalize()

                        WebsiteID = self.Config.GenerateMD5(WebsiteName)
                        DateCreated = self.Config.UnixTimestamp()
                        
                        WebsiteUrl = CommandPieces[1]
                        
                        if(not "[USER]" in WebsiteUrl):
                            print(f"\n{sd.eBan} URL must contain {bc.GC}[USER]{bc.BC}\n")
                            self.Stream(None)

                        Website = self.Database.Select("website_urls", [["website_name", "=", WebsiteName, "OR"], ["url", "=", WebsiteUrl]])

                        if(not self.Validator.NotEmpty(Website)):
                            if(self.Database.Insert("website_urls", [WebsiteID, WebsiteName, WebsiteUrl, 1, DateCreated])):
                                print(f"\n{sd.sBan}Successfully added {bc.GC}{WebsiteName}{bc.BC}:{bc.GC}{WebsiteUrl}{bc.BC}\n")
                                self.Error.AddToLog("info", f"Added {WebsiteName}:{WebsiteUrl} to the database")
                            else:
                                print(f"\n{sd.eBan} There was a problem adding {bc.RC}{WebsiteName}{bc.BC}:{bc.RC}{WebsiteUrl}{bc.BC}\n")
                                self.Error.AddToLog("error", f"There was a problem adding {WebsiteName}:{WebsiteUrl} to the database")
                        else:
                            print(f"\n{sd.eBan} Website {bc.GC}{WebsiteName}{bc.BC}:{bc.GC}{WebsiteUrl}{bc.BC} already exists\n")
                            self.Error.AddToLog("info", f"Could not add {WebsiteName}:{WebsiteUrl} to the database. Website already exists")
                    else:
                        print(f"\n{sd.eBan} Command {bc.RC}add{bc.BC} must contain 2 parameters. E.g {bc.GC}add <website_name> <url>{bc.BC}\n")
                        self.Error.AddToLog("error", f"Could not add {WebsiteName}:{WebsiteUrl} to the database. Command must contain 2 parameters. E.g add <website_name> <url>")
                        
                    self.Stream(None)
                elif(InterfaceCommand.startswith("update ") and InterfaceCommand != "update "):
                    CommandPieces = InterfaceCommand.replace("update ", "").strip().split()

                    if(len(CommandPieces) == 3):
                        WebsiteID = CommandPieces[0]

                        if(self.Validator.ID(WebsiteID)):
                            Website = self.Database.Select("website_urls", [["id", "=", WebsiteID]])

                            if(self.Validator.NotEmpty(Website)):
                                if(CommandPieces[1].lower() in ["name", "url"]):
                                    UpdateType = CommandPieces[1].lower()

                                    if(UpdateType == "name"):
                                        UpdateType = "website_name"
                                        Value = CommandPieces[2]

                                        if("_" in Value):
                                            ValuePieces = Value.split("_")

                                            Value, ValueCounter = "", 0
                                            
                                            for ValuePiece in ValuePieces:
                                                Value += ValuePiece.capitalize()

                                                if(ValueCounter < len(ValuePieces) - 1):
                                                    Value += " "
                                                
                                                ValueCounter += 1
                                        else:
                                            Value = Value.capitalize()
                                    else:
                                        UpdateType = "url"
                                        Value = CommandPieces[2]

                                        if(not "[USER]" in Value):
                                            print(f"\n{sd.eBan} URL value must contain {bc.GC}[USER]{bc.BC}\n")
                                            self.Stream(None)
                                        
                                    if(self.Database.Update("website_urls", {UpdateType: Value}, [["id", "=", WebsiteID]])):
                                        print(f"\n{sd.sBan}Successfully updated website {bc.GC}{WebsiteID}{bc.BC} with {bc.GC}{UpdateType}{bc.BC} value {bc.GC}{Value}{bc.BC}\n")
                                        self.Error.AddToLog("info", f"Successfully updated website '{WebsiteID}' with '{UpdateType}' value '{Value}'")
                                    else:
                                        print(f"\n{sd.eBan} There was a problem updating website {bc.RC}{WebsiteID}{bc.BC} with {bc.RC}{UpdateType}{bc.BC} value {bc.RC}{Value}{bc.BC}\n")
                                        self.Error.AddToLog("error", f"There was a problem updating website '{WebsiteID}' with '{UpdateType}' value '{Value}'")
                                else:
                                    print(f"\n{sd.eBan} Command {bc.RC}update{bc.BC} must contain {bc.GC}name{bc.BC} or {bc.GC}url{bc.BC} as the 2nd parameter\n")
                                    self.Error.AddToLog("error", f"Could not update website in the database. Command must contain 'name' or 'url' as the 2nd parameter")
                            else:
                                print(f"\n{sd.eBan} Website ID {bc.RC}{WebsiteID}{bc.BC} does not exist\n")
                                self.Error.AddToLog("error", f"Could not update website. Website ID '{WebsiteID}' does not exist")
                        else:
                            print(self.Error.Throw("database_interface_update_invalid_id"))
                            self.Error.AddToLog("error", f"Could not update website. Website ID '{WebsiteID}' is invalid")
                    else:
                        print(f"\n{sd.eBan} Command {bc.RC}update{bc.BC} must contain 3 parameters. E.g {bc.GC}update website_id name|url value{bc.BC}\n")
                        self.Error.AddToLog("error", f"Could not update website in the database. Command must contain 3 parameters. E.g update website_id name|url value")
                elif(InterfaceCommand.startswith("delete ") and InterfaceCommand != "delete "):
                    WebsiteID = InterfaceCommand.replace("delete ", "").strip()

                    if(self.Validator.ID(WebsiteID)):
                        Website = self.Database.Select("website_urls", [["id", "=", WebsiteID]])

                        if(self.Validator.NotEmpty(Website)):
                            if(self.Database.Delete("website_urls", [["id", "=", WebsiteID]])):
                                print(f"\n{sd.sBan}Successfully deleted {bc.GC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"Successfully deleted website ID '{WebsiteID}'")
                            else:
                                print(f"\n{sd.eBan}There was a problem deleting {bc.RC}{WebsiteID}{bc.BC}\n")
                                self.Error.AddToLog("error", f"There was a problem deleting website ID '{WebsiteID}'")
                        else:
                            print(f"\n{sd.eBan}Website ID {bc.RC}{WebsiteID}{bc.BC} does not exist\n")
                            self.Error.AddToLog("error", f"Could not delete website. Website ID '{WebsiteID}' does not exist")
                    else:
                        print(self.Error.Throw("database_interface_delete_invalid_id"))
                        self.Error.AddToLog("error", f"Could not delete website. Website ID '{WebsiteID}' is invalid")
                    pass
                else:
                    print(self.Error.Throw("invalid_database_interface_command_value", InterfaceCommand))
            else:
                print(self.Error.Throw("empty_database_interface_command_value"))
            
            self.Stream()
        except KeyboardInterrupt:
            self.Cmd.Clear()
            
            return
