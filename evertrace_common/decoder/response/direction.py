from enum import Enum


class Direction(str, Enum):
    Internal = 'internal'
    ExternalIn = 'external in'
    ExternalOut = 'external out'

    @classmethod
    def from_msg_type(cls, msg_type: int) -> 'Direction':
        name = cls._member_names_[msg_type]
        return cls._member_map_[name]  # noqa type is Direction

    def is_internal(self) -> bool:
        return self is self.Internal
