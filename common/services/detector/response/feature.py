from enum import Enum


class Feature(str, Enum):
    SPECIAL = 'special'
    USER_ABI = 'user abi'
    DATABASE_ADDRESS = 'database address'
    DATABASE_HASH = 'database hash'
    DATABASE_ABI = 'database abi'
    UNKNOWN = 'unknown'
