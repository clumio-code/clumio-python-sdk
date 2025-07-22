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
        embedded: object,
        links: ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks,
        account_native_id: str,
        aws_region: str,
        connection_id: str,
        endpoint: str,
        environment_id: str,
        has_associated_availability_group: bool,
        p_id: str,
        instance_count: int,
        is_part_of_fci: bool,
        organizational_unit_id: str,
        protection_info: protection_info_.ProtectionInfo,
        status: str,
    ) -> None:
        """Constructor for the EC2MSSQLInvHost class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.connection_id: str = connection_id
        self.endpoint: str = endpoint
        self.environment_id: str = environment_id
        self.has_associated_availability_group: bool = has_associated_availability_group
        self.p_id: str = p_id
        self.instance_count: int = instance_count
        self.is_part_of_fci: bool = is_part_of_fci
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo = protection_info
        self.status: str = status

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = val

        val = dictionary['_links']
        val_links = ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['connection_id']
        val_connection_id = val

        val = dictionary['endpoint']
        val_endpoint = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['has_associated_availability_group']
        val_has_associated_availability_group = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['instance_count']
        val_instance_count = val

        val = dictionary['is_part_of_fci']
        val_is_part_of_fci = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary['status']
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_connection_id,  # type: ignore
            val_endpoint,  # type: ignore
            val_environment_id,  # type: ignore
            val_has_associated_availability_group,  # type: ignore
            val_p_id,  # type: ignore
            val_instance_count,  # type: ignore
            val_is_part_of_fci,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_status,  # type: ignore
        )
