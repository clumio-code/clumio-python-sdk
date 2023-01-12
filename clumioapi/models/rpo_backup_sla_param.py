#
# Copyright 2021. Clumio, Inc.
#
import enum
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RPOBackupSLAParam')


class Unit(enum.Enum):
    hours = 1
    days = 2
    months = 3
    years = 4


class RPOBackupSLAParam:
    """Implementation of the 'RPOBackupSLAParam' model.

    The minimum frequency between backups for this SLA. Also known as the recovery
    point objective (RPO) interval.For example, to configure the minimum frequency
    between backups to be every 2 days, set `unit="days"` and `value=2`.To configure
    the SLA for on-demand backups, set `unit="on_demand"` and leave the `value`
    field empty.

    Attributes:
        unit:
            The measurement unit of the SLA parameter.
        value:
            The measurement value of the SLA parameter.
    """

    # Create a mapping from Model property names to API property names
    _names = {'unit': 'unit', 'value': 'value'}

    def __init__(self, unit: str = None, value: int = None) -> None:
        """Constructor for the RPOBackupSLAParam class."""

        # Initialize members of the class
        self.unit: str = unit
        self.value: int = value

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None

        # Extract variables from the dictionary
        unit = Unit[dictionary.get('unit')]

        value = dictionary.get('value')
        # Return an object of this model
        return cls(unit, value)
