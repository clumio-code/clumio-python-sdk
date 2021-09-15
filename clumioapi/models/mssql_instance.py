#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_instance_embedded
from clumioapi.models import mssql_instance_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='MssqlInstance')


class MssqlInstance:
    """Implementation of the 'MssqlInstance' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        group_id:
            The Clumio-assigned ID of the management group to which the host belongs.
        has_associated_availability_group:
            The boolean value represents if availability group is present in the instance.
        host_endpoint:
            The user-provided endpoint of the host containing the given database.
        host_id:
            The Clumio-assigned ID of the host, containing the instance.
        id:
            The Clumio-assigned ID of the Instance.
        name:
            The Microsoft SQL assigned name of the instance.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the instance.
        product_version:
            Product Version of the instance.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        server_name:
            The Microsoft SQL assigned server name of the instance.
        status:
            The status of the Instance, Possible values include 'active' and 'inactive'.
        subgroup_id:
            The Clumio-assigned ID of the management subgroup to which the host belongs.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'group_id': 'group_id',
        'has_associated_availability_group': 'has_associated_availability_group',
        'host_endpoint': 'host_endpoint',
        'host_id': 'host_id',
        'id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'product_version': 'product_version',
        'protection_info': 'protection_info',
        'server_name': 'server_name',
        'status': 'status',
        'subgroup_id': 'subgroup_id',
    }

    def __init__(
        self,
        embedded: mssql_instance_embedded.MssqlInstanceEmbedded = None,
        links: mssql_instance_links.MssqlInstanceLinks = None,
        group_id: str = None,
        has_associated_availability_group: bool = None,
        host_endpoint: str = None,
        host_id: str = None,
        id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        product_version: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        server_name: str = None,
        status: str = None,
        subgroup_id: str = None,
    ) -> None:
        """Constructor for the MssqlInstance class."""

        # Initialize members of the class
        self.embedded: mssql_instance_embedded.MssqlInstanceEmbedded = embedded
        self.links: mssql_instance_links.MssqlInstanceLinks = links
        self.group_id: str = group_id
        self.has_associated_availability_group: bool = has_associated_availability_group
        self.host_endpoint: str = host_endpoint
        self.host_id: str = host_id
        self.id: str = id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.product_version: str = product_version
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.server_name: str = server_name
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
            mssql_instance_embedded.MssqlInstanceEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            mssql_instance_links.MssqlInstanceLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        group_id = dictionary.get('group_id')
        has_associated_availability_group = dictionary.get('has_associated_availability_group')
        host_endpoint = dictionary.get('host_endpoint')
        host_id = dictionary.get('host_id')
        id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        product_version = dictionary.get('product_version')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        server_name = dictionary.get('server_name')
        status = dictionary.get('status')
        subgroup_id = dictionary.get('subgroup_id')
        # Return an object of this model
        return cls(
            embedded,
            links,
            group_id,
            has_associated_availability_group,
            host_endpoint,
            host_id,
            id,
            name,
            organizational_unit_id,
            product_version,
            p_protection_info,
            server_name,
            status,
            subgroup_id,
        )
