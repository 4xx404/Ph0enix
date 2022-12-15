import emojis
from .Colors import bc

class sd:
    iBan: str = emojis.encode(f" :information_source:{bc.BC} ")
    sBan: str = emojis.encode(f" :white_check_mark:{bc.BC} ")
    eBan: str = emojis.encode(f" :x:{bc.RC} ERROR:{bc.BC}")

    Author = f"{bc.BC}\n\t| Author:{bc.RC} 4{bc.GC}x{bc.BC}x{bc.RC}4{bc.GC}0{bc.BC}4 \t\t     |\n"
    Contributors = f"{bc.BC}\n\t| Contributors:{bc.RC} j{bc.GC}c{bc.BC}a{bc.RC}l{bc.GC}a{bc.BC}b{bc.RC}r{bc.GC}e{bc.BC}s \t\t     |\n"
    Version = f"{bc.BC}\t| Version:{bc.RC} 3{bc.GC}.{bc.BC}0 \t\t\t     |\n"
    Github = f"{bc.BC}\t| Github:{bc.RC} h{bc.GC}t{bc.BC}t{bc.RC}p{bc.GC}s{bc.BC}:{bc.RC}/{bc.GC}/{bc.BC}g{bc.RC}i{bc.GC}t{bc.BC}h{bc.RC}u{bc.GC}b{bc.BC}.{bc.RC}c{bc.GC}o{bc.BC}m{bc.RC}/{bc.GC}4{bc.BC}x{bc.RC}x{bc.GC}4{bc.BC}0{bc.RC}4{bc.GC}/ {bc.BC}|\n"

    Logo = f'''{bc.BC}
    .------..------..------..------..------..------..------..------..------.
    |{bc.GC}P{bc.BC}.--. ||{bc.GC}H{bc.BC}.--. ||{bc.GC}0{bc.BC}.--. ||{bc.GC}E{bc.BC}.--. ||{bc.GC}N{bc.BC}.--. ||{bc.GC}I{bc.BC}.--. ||{bc.GC}X{bc.BC}.--. ||{bc.GC}V{bc.BC}.--. ||{bc.GC}3{bc.BC}.--. |
    | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
    | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
    | "--"{bc.GC}P{bc.BC}|| "--"{bc.GC}H{bc.BC}|| "--"{bc.GC}0{bc.BC}|| "--"{bc.GC}E{bc.BC}|| "--"{bc.GC}N{bc.BC}|| "--"{bc.GC}I{bc.BC}|| "--"{bc.GC}X{bc.BC}|| "--"{bc.GC}V{bc.BC}|| "--"{bc.GC}3{bc.BC}|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
    {Author}{Contributors}{Version}{Github}'''
