#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RetentionBackupSLAParam')


class RetentionBackupSLAParam:
    """Implementation of the 'RetentionBackupSLAParam' model.

    The retention time for this SLA. For example, to retain the backup for 1 month,
    set `unit="months"` and `value=1`.

    Attributes:
        unit:
            The measurement unit of the SLA parameter.
        value:
            The measurement value of the SLA parameter.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'unit': 'unit', 'value': 'value'}

    def __init__(self, unit: str, value: int) -> None:
        """Constructor for the RetentionBackupSLAParam class."""

        # Initialize members of the class
        self.unit: str = unit
        self.value: int = value

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        # Extract variables from the dictionary
        val = dictionary['unit']
        val_unit = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_unit,  # type: ignore
            val_value,  # type: ignore
        )
