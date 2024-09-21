from enum import Enum


class OPType(Enum):
    def __str__(self):
        return self.value

    @staticmethod
    def fromString(op: str):
        raise NotImplementedError()
