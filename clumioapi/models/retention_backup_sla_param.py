#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RetentionBackupSLAParam')


class RetentionBackupSLAParam:
    """Implementation of the 'RetentionBackupSLAParam' model.

    The retention time for this SLA. For example, to retain the backup for 1 month,
    set `unit="months"` and `value=1`.

    Attributes:
        unit:
            The measurement unit of the SLA parameter. Values include `hours`, `days`,
            `months`, and `years`.
        value:
            The measurement value of the SLA parameter.
    """

    # Create a mapping from Model property names to API property names
    _names = {'unit': 'unit', 'value': 'value'}

    def __init__(self, unit: str = None, value: int = None) -> None:
        """Constructor for the RetentionBackupSLAParam class."""

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
