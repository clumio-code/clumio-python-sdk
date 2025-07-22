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
        compliant_count: int,
        control_status: str,
        name: str,
        non_compliant_count: int,
        unknown_count: int,
    ) -> None:
        """Constructor for the ControlInfo class."""

        # Initialize members of the class
        self.compliant_count: int = compliant_count
        self.control_status: str = control_status
        self.name: str = name
        self.non_compliant_count: int = non_compliant_count
        self.unknown_count: int = unknown_count

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
        val = dictionary['compliant_count']
        val_compliant_count = val

        val = dictionary['control_status']
        val_control_status = val

        val = dictionary['name']
        val_name = val

        val = dictionary['non_compliant_count']
        val_non_compliant_count = val

        val = dictionary['unknown_count']
        val_unknown_count = val

        # Return an object of this model
        return cls(
            val_compliant_count,  # type: ignore
            val_control_status,  # type: ignore
            val_name,  # type: ignore
            val_non_compliant_count,  # type: ignore
            val_unknown_count,  # type: ignore
        )
