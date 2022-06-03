from enum import Enum


class Feature(str, Enum):
    SPECIAL = 'special'
    USER_ABI = 'user abi'
    DATABASE_CONTRACT = 'database contract'
    DATABASE_ABI = 'database abi'
    KNOWN_FUNCTION = 'known function'
    BRUTEFORCE = 'bruteforce'
    NONAME = 'noname'
    UNKNOWN = 'unknown'
