from enum import Enum


class PortDirection(Enum):
    INPUT = "input"
    OUTPUT = "output"
    INOUT = "inout"

    @staticmethod
    def fromString(direction: str):
        if direction == "input":
            return PortDirection.INPUT
        elif direction == "output":
            return PortDirection.OUTPUT
        elif direction == "inout":
            return PortDirection.INOUT
        else:
            return None

    @staticmethod
    def toString(direction: "PortDirection"):
        return direction.value.lower() if direction is not None else None


class PortType(Enum):
    """
    Enum class representing different types of ports in a Verilog netlist.

    Attributes:
        WIRE: A port of type wire.
        REG: A port of type reg.
        INTEGER: A port of type integer.
        REAL: A port of type real.
        TIME: A port of type time.
        PARAMETER: A port of type parameter.
        LOCALPARAM: A port of type localparam.
    """

    WIRE = "wire"
    REG = "reg"
    INTEGER = "integer"
    REAL = "real"
    TIME = "time"
    PARAMETER = "parameter"
    LOCALPARAM = "localparam"

    @staticmethod
    def fromString(type: str) -> "PortType":
        """
        Converts a string representation of a port type to its corresponding
        PortType enum value.

        Args:
            type (str): The string representation of the port type.

        Returns:
            PortType: The corresponding PortType enum value, or None if not found.
        """
        if type == "wire":
            return PortType.WIRE
        elif type == "reg":
            return PortType.REG
        elif type == "integer":
            return PortType.INTEGER
        elif type == "real":
            return PortType.REAL
        elif type == "time":
            return PortType.TIME
        elif type == "parameter":
            return PortType.PARAMETER
        elif type == "localparam":
            return PortType.LOCALPARAM
        else:
            return None

    @staticmethod
    def toString(type: "PortType") -> str:
        """
        Converts a PortType enum value to its string representation.

        Args:
            type (PortType): The PortType enum value.

        Returns:
            str: The string representation of the PortType, or None if input is None.
        """
        return type.value if type is not None else None
