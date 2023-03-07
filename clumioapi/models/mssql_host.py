#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_host_embedded
from clumioapi.models import mssql_host_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='MssqlHost')


class MssqlHost:
    """Implementation of the 'MssqlHost' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        endpoint:
            The user-provided endpoint of the host containing the given database.
        group_id:
            The Clumio-assigned ID of the management group to which the host belongs.
        has_associated_availability_group:
            Determines whether or not an availability group is present in the host.
        host_connection_status:
            Connection status of MSSQL Host
        p_id:
            The Clumio-assigned ID of the Host.
        instance_count:
            The number of instances present in the host.
        is_part_of_fci:
            IsPartOfFCI is a boolean field representing if the Host is part of Failover
            Cluster
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the host.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        status:
            The status of the Host, Possible values include 'active' and 'inactive'.
        subgroup_id:
            The Clumio-assigned ID of the management subgroup to which the host belongs.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'endpoint': 'endpoint',
        'group_id': 'group_id',
        'has_associated_availability_group': 'has_associated_availability_group',
        'host_connection_status': 'host_connection_status',
        'p_id': 'id',
        'instance_count': 'instance_count',
        'is_part_of_fci': 'is_part_of_fci',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'status': 'status',
        'subgroup_id': 'subgroup_id',
    }

    def __init__(
        self,
        embedded: mssql_host_embedded.MssqlHostEmbedded = None,
        links: mssql_host_links.MssqlHostLinks = None,
        endpoint: str = None,
        group_id: str = None,
        has_associated_availability_group: bool = None,
        host_connection_status: str = None,
        p_id: str = None,
        instance_count: int = None,
        is_part_of_fci: bool = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        status: str = None,
        subgroup_id: str = None,
    ) -> None:
        """Constructor for the MssqlHost class."""

        # Initialize members of the class
        self.embedded: mssql_host_embedded.MssqlHostEmbedded = embedded
        self.links: mssql_host_links.MssqlHostLinks = links
        self.endpoint: str = endpoint
        self.group_id: str = group_id
        self.has_associated_availability_group: bool = has_associated_availability_group
        self.host_connection_status: str = host_connection_status
        self.p_id: str = p_id
        self.instance_count: int = instance_count
        self.is_part_of_fci: bool = is_part_of_fci
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.status: str = status
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
        key = '_embedded'
        embedded = (
            mssql_host_embedded.MssqlHostEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            mssql_host_links.MssqlHostLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        endpoint = dictionary.get('endpoint')
        group_id = dictionary.get('group_id')
        has_associated_availability_group = dictionary.get('has_associated_availability_group')
        host_connection_status = dictionary.get('host_connection_status')
        p_id = dictionary.get('id')
        instance_count = dictionary.get('instance_count')
        is_part_of_fci = dictionary.get('is_part_of_fci')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        status = dictionary.get('status')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(
            embedded,
            links,
            endpoint,
            group_id,
            has_associated_availability_group,
            host_connection_status,
            p_id,
            instance_count,
            is_part_of_fci,
            organizational_unit_id,
            p_protection_info,
            status,
            subgroup_id,
        )
