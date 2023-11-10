#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateMssqlHostConnectionCredentialsV1Request')


class CreateMssqlHostConnectionCredentialsV1Request:
    """Implementation of the 'CreateMssqlHostConnectionCredentialsV1Request' model.

    Attributes:
        endpoint:
            Performs the operation on a host within the specified endpoint.
        group_id:

        subgroup_id:
            Performs the operation on a host within the specified subgroup.
    """

    # Create a mapping from Model property names to API property names
    _names = {'endpoint': 'endpoint', 'group_id': 'group_id', 'subgroup_id': 'subgroup_id'}

    def __init__(self, endpoint: str = None, group_id: str = None, subgroup_id: str = None) -> None:
        """Constructor for the CreateMssqlHostConnectionCredentialsV1Request class."""

        # Initialize members of the class
        self.endpoint: str = endpoint
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
        endpoint = dictionary.get('endpoint')
        group_id = dictionary.get('group_id')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(endpoint, group_id, subgroup_id)
