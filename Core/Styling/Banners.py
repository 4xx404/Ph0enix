from Core.Styling.Colors import bc

class sd:
    Tick = u'\u2713'
    Cross = u'\u2717'
    iBan = f"{bc.BC} |{bc.GC}i{bc.BC}|" # Info banner"
    sBan = f"{bc.BC} |{bc.GC}{Tick}{bc.BC}|" # Success banner"
    eBan = f"{bc.BC} |{bc.RC}{Cross}{bc.BC}|{bc.RC} ERROR:{bc.BC}" # Error banner"

    Author = f"{bc.BC}\n\t| Author:{bc.RC} 4{bc.GC}x{bc.BC}x{bc.RC}4{bc.GC}0{bc.BC}4 \t\t     |\n"
    Version = f"{bc.BC}\t| Version:{bc.RC} 3{bc.GC}.{bc.BC}0 \t\t\t     |\n"
    Github = f"{bc.BC}\t| Github:{bc.RC} h{bc.GC}t{bc.BC}t{bc.RC}p{bc.GC}s{bc.BC}:{bc.RC}/{bc.GC}/{bc.BC}g{bc.RC}i{bc.GC}t{bc.BC}h{bc.RC}u{bc.GC}b{bc.BC}.{bc.RC}c{bc.GC}o{bc.BC}m{bc.RC}/{bc.GC}4{bc.BC}x{bc.RC}x{bc.GC}4{bc.BC}0{bc.RC}4{bc.GC}/ {bc.BC}|\n"

    logo = bc.BC + '''
    .------..------..------..------..------..------..------..------..------.
    |'''+bc.GC+'''P'''+bc.BC+'''.--. ||'''+bc.GC+'''H'''+bc.BC+'''.--. ||'''+bc.GC+'''0'''+bc.BC+'''.--. ||'''+bc.GC+'''E'''+bc.BC+'''.--. ||'''+bc.GC+'''N'''+bc.BC+'''.--. ||'''+bc.GC+'''I'''+bc.BC+'''.--. ||'''+bc.GC+'''X'''+bc.BC+'''.--. ||'''+bc.GC+'''V'''+bc.BC+'''.--. ||'''+bc.GC+'''3'''+bc.BC+'''.--. |
    | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
    | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
    | "--"'''+bc.GC+'''P'''+bc.BC+'''|| "--"'''+bc.GC+'''H'''+bc.BC+'''|| "--"'''+bc.GC+'''0'''+bc.BC+'''|| "--"'''+bc.GC+'''E'''+bc.BC+'''|| "--"'''+bc.GC+'''N'''+bc.BC+'''|| "--"'''+bc.GC+'''I'''+bc.BC+'''|| "--"'''+bc.GC+'''X'''+bc.BC+'''|| "--"'''+bc.GC+'''V'''+bc.BC+'''|| "--"'''+bc.GC+'''2'''+bc.BC+'''|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
    ''' + Author + Version + Github
