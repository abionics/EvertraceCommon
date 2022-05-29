from enum import Enum


class Feature(str, Enum):
    SPECIAL = 'special'
    USER_ABI = 'user abi'
    KNOWN_FUNCTION = 'known function'
    KNOWN_ABI = 'known abi'
    BRUTEFORCE = 'bruteforce'
    NONAME = 'noname'
    UNKNOWN = 'unknown'
