#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='TimeUnitParam')


class TimeUnitParam:
    """Implementation of the 'TimeUnitParam' model.

    The time unit used in control definition.

    Attributes:
        unit:
            Unit indicates the unit for time unit param.
        value:
            Value indicates the value for time unit param.
    """

    # Create a mapping from Model property names to API property names
    _names = {'unit': 'unit', 'value': 'value'}

    def __init__(self, unit: str = None, value: int = None) -> None:
        """Constructor for the TimeUnitParam class."""

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
        unit = dictionary.get('unit')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(unit, value)
