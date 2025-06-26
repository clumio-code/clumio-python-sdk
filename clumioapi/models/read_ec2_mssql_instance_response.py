#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_instance_embedded
from clumioapi.models import ec2_mssql_instance_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='ReadEC2MSSQLInstanceResponse')


class ReadEC2MSSQLInstanceResponse:
    """Implementation of the 'ReadEC2MSSQLInstanceResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the EC2 instance of the MSSQL
            instance.
        aws_region:
            The AWS region associated with the EC2 instance of the MSSQL instance.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the EC2 MSSQL
            instance.
        has_associated_availability_group:
            The boolean value represents if availability group is present in the instance.
        host_connection_id:
            The Clumio-assigned ID of the host connection containing the given mssql
            instance.
        host_endpoint:
            The user-provided endpoint of the host containing the given database.
        host_id:
            The Clumio-assigned ID of the host, containing the instance.
        p_id:
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
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'environment_id': 'environment_id',
        'has_associated_availability_group': 'has_associated_availability_group',
        'host_connection_id': 'host_connection_id',
        'host_endpoint': 'host_endpoint',
        'host_id': 'host_id',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'product_version': 'product_version',
        'protection_info': 'protection_info',
        'server_name': 'server_name',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: ec2_mssql_instance_embedded.EC2MSSQLInstanceEmbedded = None,
        links: ec2_mssql_instance_links.EC2MSSQLInstanceLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        environment_id: str = None,
        has_associated_availability_group: bool = None,
        host_connection_id: str = None,
        host_endpoint: str = None,
        host_id: str = None,
        p_id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        product_version: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        server_name: str = None,
        status: str = None,
    ) -> None:
        """Constructor for the ReadEC2MSSQLInstanceResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_instance_embedded.EC2MSSQLInstanceEmbedded = embedded
        self.links: ec2_mssql_instance_links.EC2MSSQLInstanceLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.environment_id: str = environment_id
        self.has_associated_availability_group: bool = has_associated_availability_group
        self.host_connection_id: str = host_connection_id
        self.host_endpoint: str = host_endpoint
        self.host_id: str = host_id
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.product_version: str = product_version
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.server_name: str = server_name
        self.status: str = status

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
            ec2_mssql_instance_embedded.EC2MSSQLInstanceEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            ec2_mssql_instance_links.EC2MSSQLInstanceLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        environment_id = dictionary.get('environment_id')
        has_associated_availability_group = dictionary.get('has_associated_availability_group')
        host_connection_id = dictionary.get('host_connection_id')
        host_endpoint = dictionary.get('host_endpoint')
        host_id = dictionary.get('host_id')
        p_id = dictionary.get('id')
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
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            aws_region,
            environment_id,
            has_associated_availability_group,
            host_connection_id,
            host_endpoint,
            host_id,
            p_id,
            name,
            organizational_unit_id,
            product_version,
            p_protection_info,
            server_name,
            status,
        )
