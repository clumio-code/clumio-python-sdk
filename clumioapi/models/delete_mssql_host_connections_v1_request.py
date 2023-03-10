#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DeleteMssqlHostConnectionsV1Request')


class DeleteMssqlHostConnectionsV1Request:
    """Implementation of the 'DeleteMssqlHostConnectionsV1Request' model.

    Attributes:
        endpoints:
            The endpoints of hosts to be deleted.
        group_id:

        subgroup_id:
            Performs the operation on a host within the specified management subgroup.
    """

    # Create a mapping from Model property names to API property names
    _names = {'endpoints': 'endpoints', 'group_id': 'group_id', 'subgroup_id': 'subgroup_id'}

    def __init__(
        self, endpoints: Sequence[str] = None, group_id: str = None, subgroup_id: str = None
    ) -> None:
        """Constructor for the DeleteMssqlHostConnectionsV1Request class."""

        # Initialize members of the class
        self.endpoints: Sequence[str] = endpoints
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
        endpoints = dictionary.get('endpoints')
        group_id = dictionary.get('group_id')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(endpoints, group_id, subgroup_id)
