#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_instance_embedded as ec2_mssql_instance_embedded_
from clumioapi.models import ec2_mssql_instance_links as ec2_mssql_instance_links_
from clumioapi.models import protection_info as protection_info_

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
    _names: dict[str, str] = {
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
        embedded: ec2_mssql_instance_embedded_.EC2MSSQLInstanceEmbedded | None = None,
        links: ec2_mssql_instance_links_.EC2MSSQLInstanceLinks | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        environment_id: str | None = None,
        has_associated_availability_group: bool | None = None,
        host_connection_id: str | None = None,
        host_endpoint: str | None = None,
        host_id: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        product_version: str | None = None,
        protection_info: protection_info_.ProtectionInfo | None = None,
        server_name: str | None = None,
        status: str | None = None,
    ) -> None:
        """Constructor for the ReadEC2MSSQLInstanceResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_instance_embedded_.EC2MSSQLInstanceEmbedded | None = embedded
        self.links: ec2_mssql_instance_links_.EC2MSSQLInstanceLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.environment_id: str | None = environment_id
        self.has_associated_availability_group: bool | None = has_associated_availability_group
        self.host_connection_id: str | None = host_connection_id
        self.host_endpoint: str | None = host_endpoint
        self.host_id: str | None = host_id
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.product_version: str | None = product_version
        self.protection_info: protection_info_.ProtectionInfo | None = protection_info
        self.server_name: str | None = server_name
        self.status: str | None = status

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_embedded', None)
        val_embedded = ec2_mssql_instance_embedded_.EC2MSSQLInstanceEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_instance_links_.EC2MSSQLInstanceLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('has_associated_availability_group', None)
        val_has_associated_availability_group = val

        val = dictionary.get('host_connection_id', None)
        val_host_connection_id = val

        val = dictionary.get('host_endpoint', None)
        val_host_endpoint = val

        val = dictionary.get('host_id', None)
        val_host_id = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('product_version', None)
        val_product_version = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('server_name', None)
        val_server_name = val

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_environment_id,
            val_has_associated_availability_group,
            val_host_connection_id,
            val_host_endpoint,
            val_host_id,
            val_p_id,
            val_name,
            val_organizational_unit_id,
            val_product_version,
            val_protection_info,
            val_server_name,
            val_status,
        )
