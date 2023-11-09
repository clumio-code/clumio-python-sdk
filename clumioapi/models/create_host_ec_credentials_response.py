#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import host_links

T = TypeVar('T', bound='CreateHostECCredentialsResponse')


class CreateHostECCredentialsResponse:
    """Implementation of the 'CreateHostECCredentialsResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        edge_connector_credentials:
            The edge connector credentials for the host. This token is required during the
            installation of the MSI.
        endpoint:
            The user-provided endpoint used to connect the host.
        group_id:
            The Clumio-assigned ID of the management group associated with the host.
        p_id:
            The Clumio-assigned ID of the Host.
        last_heartbeat_timestamp:
            The timestamp of the last successful heartbeat of this host. Represented in
            RFC-3339 format.
        name:
            Name of the Host.
        status:
            The connection status of the Host. Possible values include `connected`,
            `disconnected`, `connection_pending`, and `invalid_token`.
        subgroup_id:
            The Clumio-assigned ID of the management subgroup associated with the host.
        uuid:
            The Clumio-assigned UUID of the host. This UUID is used for filtering hosts
            during list operations.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'edge_connector_credentials': 'edge_connector_credentials',
        'endpoint': 'endpoint',
        'group_id': 'group_id',
        'p_id': 'id',
        'last_heartbeat_timestamp': 'last_heartbeat_timestamp',
        'name': 'name',
        'status': 'status',
        'subgroup_id': 'subgroup_id',
        'uuid': 'uuid',
    }

    def __init__(
        self,
        links: host_links.HostLinks = None,
        edge_connector_credentials: str = None,
        endpoint: str = None,
        group_id: str = None,
        p_id: str = None,
        last_heartbeat_timestamp: str = None,
        name: str = None,
        status: str = None,
        subgroup_id: str = None,
        uuid: str = None,
    ) -> None:
        """Constructor for the CreateHostECCredentialsResponse class."""

        # Initialize members of the class
        self.links: host_links.HostLinks = links
        self.edge_connector_credentials: str = edge_connector_credentials
        self.endpoint: str = endpoint
        self.group_id: str = group_id
        self.p_id: str = p_id
        self.last_heartbeat_timestamp: str = last_heartbeat_timestamp
        self.name: str = name
        self.status: str = status
        self.subgroup_id: str = subgroup_id
        self.uuid: str = uuid

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
        key = '_links'
        links = (
            host_links.HostLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        edge_connector_credentials = dictionary.get('edge_connector_credentials')
        endpoint = dictionary.get('endpoint')
        group_id = dictionary.get('group_id')
        p_id = dictionary.get('id')
        last_heartbeat_timestamp = dictionary.get('last_heartbeat_timestamp')
        name = dictionary.get('name')
        status = dictionary.get('status')
        subgroup_id = dictionary.get('subgroup_id')
        uuid = dictionary.get('uuid')
        # Return an object of this model
        return cls(
            links,
            edge_connector_credentials,
            endpoint,
            group_id,
            p_id,
            last_heartbeat_timestamp,
            name,
            status,
            subgroup_id,
            uuid,
        )
