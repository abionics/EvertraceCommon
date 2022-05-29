from enum import Enum


class Feature(str, Enum):
    SPECIAL = 'special'
    USER_ABI = 'user_abi'
    ADDRESS = 'address'
    HASH = 'hash'
    KNOWN_ABI = 'known_abi'
    UNKNOWN = 'unknown'
