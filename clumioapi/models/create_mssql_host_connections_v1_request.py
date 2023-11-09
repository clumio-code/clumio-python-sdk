#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateMssqlHostConnectionsV1Request')


class CreateMssqlHostConnectionsV1Request:
    """Implementation of the 'CreateMssqlHostConnectionsV1Request' model.

    Attributes:
        endpoints:
            The fully-qualified domain names or IP addresses of hosts to be connected.
        group_id:

        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the host.
        subgroup_id:
            Performs the operation on a host within the specified management subgroup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'endpoints': 'endpoints',
        'group_id': 'group_id',
        'organizational_unit_id': 'organizational_unit_id',
        'subgroup_id': 'subgroup_id',
    }

    def __init__(
        self,
        endpoints: Sequence[str] = None,
        group_id: str = None,
        organizational_unit_id: str = None,
        subgroup_id: str = None,
    ) -> None:
        """Constructor for the CreateMssqlHostConnectionsV1Request class."""

        # Initialize members of the class
        self.endpoints: Sequence[str] = endpoints
        self.group_id: str = group_id
        self.organizational_unit_id: str = organizational_unit_id
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
        organizational_unit_id = dictionary.get('organizational_unit_id')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(endpoints, group_id, organizational_unit_id, subgroup_id)
