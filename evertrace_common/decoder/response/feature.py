from enum import Enum


class Feature(str, Enum):
    USER_ABI = 'user abi'
    KNOWN_FUNCTION = 'known function'
    KNOWN_ABI = 'known abi'
    BRUTEFORCE = 'bruteforce'
    NONAME = 'noname'
    UNKNOWN = 'unknown'
