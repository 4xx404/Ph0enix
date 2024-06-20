#!/usr/bin/python3
import sys, os, logging
sys.dont_write_bytecode = True

from Core.Styling import *

from .Validity import Validation

class ErrorHandler:
    def __init__(self):
        self.Validator = Validation()

        self.DefinedErrors = [
            "database_connection",
            "database_migration",
            "database_migration_sql_load",
            "database_select_none_type_table",
            "database_select_invalid_table",

            "database_insert_none_type_table",
            "database_insert_invalid_table",
            "database_insert_missing_values",
            "database_insert_execution_failure",

            "database_update_none_type_table",
            "database_update_invalid_table",
            "database_update_malformed_sql",
            "database_update_execution_failure",

            "database_delete_none_type_table",
            "database_delete_invalid_table",
            "database_delete_execution_failure",

            "empty_database_interface_command_value",
            "invalid_database_interface_command_value",
            "database_interface_list_no_websites",
            "database_interface_activate_invalid_id",
            "database_interface_deactivate_invalid_id",
            "database_interface_update_invalid_id",
            "database_interface_delete_invalid_id",

            "empty_command_stream_value",

            "empty_username_value",
            "username_length_too_short",
            "link_username_replacement_chunk_not_found",
            "none_200_response",
        ]

        self.LogFileName = "app.log"

    def Throw(self, ErrorType: str = None, ErrorData: any = None) -> (str | None):
        if(self.Validator.NotEmpty(ErrorType) and ErrorType.lower() in self.DefinedErrors):
            # Database Errors
            if(ErrorType == "database_connection"):
                return f"\n{sd.eBan} Could not connect to database at {bc.RC}{ErrorData[0]}\n\n {ErrorData[1]}{bc.BC}\n"
            elif(ErrorType == "database_migration"):
                return f"\n{sd.eBan} Could not run migration file {bc.RC}{ErrorData[0]}\n\n {ErrorData[1]}{bc.BC}\n"
            elif(ErrorType == "database_migration_sql_load"):
                return f"\n{sd.eBan} Could not load migration SQL statements\n"
            elif(ErrorType == "database_select_none_type_table"):
                return f"\n{sd.eBan} Database.Select.Error: table name is NoneType\n"
            elif(ErrorType == "database_select_invalid_table"):
                return f"\n{sd.eBan} Database.Select.Error: table {bc.RC}{ErrorData}{bc.BC} does not exist\n"
            
            elif(ErrorType == "database_insert_none_type_table"):
                return f"\n{sd.eBan} Database.Insert.Error: table name is NoneType\n"
            elif(ErrorType == "database_insert_invalid_table"):
                return f"\n{sd.eBan} Database.Insert.Error: table {bc.RC}{ErrorData}{bc.BC} does not exist\n"
            elif(ErrorType == "database_insert_missing_values"):
                return f"\n{sd.eBan} Database.Insert.Error: insert values are required\n"
            elif(ErrorType == "database_insert_execution_failure"):
                return f"\n{sd.eBan} Database.Insert.Error: execution failed ({bc.RC}{ErrorData[0]}{bc.BC})\n{bc.RC}{ErrorData[1]}{bc.BC}\n\n"
            
            elif(ErrorType == "database_update_none_type_table"):
                return f"\n{sd.eBan} Database.Update.Error: table name is NoneType\n"    
            elif(ErrorType == "database_update_invalid_table"):
                return f"\n{sd.eBan} Database.Update.Error: table {bc.RC}{ErrorData}{bc.BC} does not exist\n"
            elif(ErrorType == "database_update_malformed_sql"):
                return f"\n{sd.eBan} Database.Update.Error: malformed SQL query ({bc.RC}{ErrorData}{bc.BC})\n"
            elif(ErrorType == "database_update_execution_failure"):
                return f"\n{sd.eBan} Database.Update.Error: execution failed ({bc.RC}{ErrorData[0]}{bc.BC})\n{bc.RC}{ErrorData[1]}{bc.BC}\n\n"
            
            elif(ErrorType == "database_delete_none_type_table"):
                return f"\n{sd.eBan} Database.Update.Error: table name is NoneType\n"
            elif(ErrorType == "database_delete_invalid_table"):
                return f"\n{sd.eBan} Database.Delete.Error: table {bc.RC}{ErrorData}{bc.BC} does not exist\n"
            elif(ErrorType == "database_delete_execution_failure"):
                return f"\n{sd.eBan} Database.Delete.Error: execution failed ({bc.RC}{ErrorData[0]}{bc.BC})\n{bc.RC}{ErrorData[1]}{bc.BC}\n\n"
            
            # Database Command Stream Errors
            elif(ErrorType == "empty_database_interface_command_value"):
                return f"\n{sd.eBan} Database.Interface.Error: command cannot be empty\n"
            elif(ErrorType == "invalid_database_interface_command_value"):
                return f"\n{sd.eBan} Database.Interface.Error: invalid command {bc.RC}{ErrorData}{bc.BC}\n"
            elif(ErrorType == "database_interface_list_no_websites"):
                return f"\n{sd.eBan} Database.Interface.Error.List: No websites were found."
            elif(ErrorType == "database_interface_activate_invalid_id"):
                return f"\n{sd.eBan} Database.Interface.Error.Activate: invalid website_id, must be MD5 hash"
            elif(ErrorType == "database_interface_deactivate_invalid_id"):
                return f"\n{sd.eBan} Database.Interface.Error.Deactivate: invalid website_id, must be MD5 hash"
            elif(ErrorType == "database_interface_update_invalid_id"):
                return f"\n{sd.eBan} Database.Interface.Error.Update: invalid website_id, must be MD5 hash"
            elif(ErrorType == "database_interface_delete_invalid_id"):
                return f"\n{sd.eBan} Database.Interface.Error.Delete: invalid website_id, must be MD5 hash"

            # Main Command Stream Errors
            elif(ErrorType == "empty_command_stream_value"):
                return f"{sd.eBan} Command value cannot be empty\n"
            
            elif(ErrorType == "empty_username_value"):
                return f"\n{sd.eBan} Username value cannot be empty\n"
            elif(ErrorType == "username_length_too_short"):
                return f"\n{sd.eBan} Invalid Username {bc.RC}{ErrorData}{bc.BC}, length must be 3 or more characters\n"
            elif(ErrorType == "link_username_replacement_chunk_not_found"):
                return f"\n{sd.eBan} Link {bc.RC}{ErrorData}{bc.BC} does not include {bc.RC}\"[USER]\"{bc.BC} to replace the username\n"
            elif(ErrorType == "none_200_response"):
                return f"\n{sd.eBan} Got no response from {bc.RC}{ErrorData}{bc.BC}\n"
        else:
            if(ErrorType == None):
                return f"\n{sd.eBan} Error Type cannot be None\n"    
            else:
                return f"\n{sd.eBan} Undefined Error Type {bc.RC}{ErrorType}{bc.BC}\n"
    
    def CreateLogFile(self) -> None:
        # Remove the old log file if it exists
        if(os.path.isfile(self.LogFileName)):
            os.remove(self.LogFileName)

        # Create a new log file
        logging.basicConfig(
            level=logging.INFO,
            filename=self.LogFileName,
            filemode="w",
            format="%(levelname)s - %(message)s"
        )

    def AddToLog(self, Type: str = None, Message: str = None) -> None:
        if(Type and Message):
            Type = Type.lower().strip()

            if(Type == "info"):
                logging.info(Message)
            elif(Type == "error"):
                logging.error(Message)