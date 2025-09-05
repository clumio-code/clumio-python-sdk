#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ControlInfo')


class ControlInfo:
    """Implementation of the 'ControlInfo' model.

    The status per controls in the compliance report created by the report run.

    Attributes:
        compliant_count:
            The count of compliant items of the control.
        control_status:
            The compliance status of the control.
        name:
            The name of the control.
        non_compliant_count:
            The count of non-compliant items of the control.
        unknown_count:
            The count of unknown items of the control.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'compliant_count': 'compliant_count',
        'control_status': 'control_status',
        'name': 'name',
        'non_compliant_count': 'non_compliant_count',
        'unknown_count': 'unknown_count',
    }

    def __init__(
        self,
        compliant_count: int | None = None,
        control_status: str | None = None,
        name: str | None = None,
        non_compliant_count: int | None = None,
        unknown_count: int | None = None,
    ) -> None:
        """Constructor for the ControlInfo class."""

        # Initialize members of the class
        self.compliant_count: int | None = compliant_count
        self.control_status: str | None = control_status
        self.name: str | None = name
        self.non_compliant_count: int | None = non_compliant_count
        self.unknown_count: int | None = unknown_count

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('compliant_count', None)
        val_compliant_count = val

        val = dictionary.get('control_status', None)
        val_control_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('non_compliant_count', None)
        val_non_compliant_count = val

        val = dictionary.get('unknown_count', None)
        val_unknown_count = val

        # Return an object of this model
        return cls(
            val_compliant_count,
            val_control_status,
            val_name,
            val_non_compliant_count,
            val_unknown_count,
        )
