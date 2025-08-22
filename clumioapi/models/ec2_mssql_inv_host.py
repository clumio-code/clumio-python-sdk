#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_inv_host_links as ec2_mssql_inv_host_links_
from clumioapi.models import protection_info as protection_info_

T = TypeVar('T', bound='EC2MSSQLInvHost')


class EC2MSSQLInvHost:
    """Implementation of the 'EC2MSSQLInvHost' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            EC2MSSQLInvHostLinks contains links related to ec2 mssql host
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the EC2 instance of the MSSQL
            host.
        aws_region:
            The AWS region associated with the EC2 instance of the MSSQL host.
        connection_id:
            The Clumio-assigned ID of the host connection.
        endpoint:
            The user-provided endpoint of the host containing the given database.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the EC2 MSSQL
            host.
        has_associated_availability_group:
            Determines whether or not an availability group is present in the host.
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
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'connection_id': 'connection_id',
        'endpoint': 'endpoint',
        'environment_id': 'environment_id',
        'has_associated_availability_group': 'has_associated_availability_group',
        'p_id': 'id',
        'instance_count': 'instance_count',
        'is_part_of_fci': 'is_part_of_fci',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: object | None = None,
        links: ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        connection_id: str | None = None,
        endpoint: str | None = None,
        environment_id: str | None = None,
        has_associated_availability_group: bool | None = None,
        p_id: str | None = None,
        instance_count: int | None = None,
        is_part_of_fci: bool | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_.ProtectionInfo | None = None,
        status: str | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLInvHost class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.connection_id: str | None = connection_id
        self.endpoint: str | None = endpoint
        self.environment_id: str | None = environment_id
        self.has_associated_availability_group: bool | None = has_associated_availability_group
        self.p_id: str | None = p_id
        self.instance_count: int | None = instance_count
        self.is_part_of_fci: bool | None = is_part_of_fci
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo | None = protection_info
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
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('connection_id', None)
        val_connection_id = val

        val = dictionary.get('endpoint', None)
        val_endpoint = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('has_associated_availability_group', None)
        val_has_associated_availability_group = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('instance_count', None)
        val_instance_count = val

        val = dictionary.get('is_part_of_fci', None)
        val_is_part_of_fci = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_connection_id,
            val_endpoint,
            val_environment_id,
            val_has_associated_availability_group,
            val_p_id,
            val_instance_count,
            val_is_part_of_fci,
            val_organizational_unit_id,
            val_protection_info,
            val_status,
        )
