#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='M365GroupingCriteria')


class M365GroupingCriteria:
    """Implementation of the 'M365GroupingCriteria' model.

    The entity type used to group organizational units for Microsoft 365 resources.

    Attributes:
        is_editable:
            Determines whether or not this data group is editable. If false, then an
            organizational unit uses this data group.
            To edit this data group, all organizational units using it must be deleted.
        p_type:
            The entity type used to group organizational units for Microsoft 365 resources.

            +---------------------+------------------------+
            |     Entity Type     |        Details         |
            +=====================+========================+
            | microsoft365_domain | Microsoft 365 account. |
            +---------------------+------------------------+
            | microsoft365_group  | Microsoft 365 group.   |
            +---------------------+------------------------+
    """

    # Create a mapping from Model property names to API property names
    _names = {'is_editable': 'is_editable', 'p_type': 'type'}

    def __init__(self, is_editable: bool = None, p_type: str = None) -> None:
        """Constructor for the M365GroupingCriteria class."""

        # Initialize members of the class
        self.is_editable: bool = is_editable
        self.p_type: str = p_type

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
        is_editable = dictionary.get('is_editable')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(is_editable, p_type)
