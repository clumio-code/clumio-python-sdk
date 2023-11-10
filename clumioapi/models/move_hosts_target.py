#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MoveHostsTarget')


class MoveHostsTarget:
    """Implementation of the 'MoveHostsTarget' model.

    The target configuration of the hosts to be moved.

    Attributes:
        group_id:

        subgroup_id:
            Performs the operation on a host within the specified subgroup id.
    """

    # Create a mapping from Model property names to API property names
    _names = {'group_id': 'group_id', 'subgroup_id': 'subgroup_id'}

    def __init__(self, group_id: str = None, subgroup_id: str = None) -> None:
        """Constructor for the MoveHostsTarget class."""

        # Initialize members of the class
        self.group_id: str = group_id
        self.subgroup_id: str = subgroup_id

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
        group_id = dictionary.get('group_id')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(group_id, subgroup_id)
