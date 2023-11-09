#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_inv_host_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='ReadEC2MSSQLInvHostResponse')


class ReadEC2MSSQLInvHostResponse:
    """Implementation of the 'ReadEC2MSSQLInvHostResponse' model.

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
    _names = {
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
        embedded: object = None,
        links: ec2_mssql_inv_host_links.EC2MSSQLInvHostLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        connection_id: str = None,
        endpoint: str = None,
        environment_id: str = None,
        has_associated_availability_group: bool = None,
        p_id: str = None,
        instance_count: int = None,
        is_part_of_fci: bool = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        status: str = None,
    ) -> None:
        """Constructor for the ReadEC2MSSQLInvHostResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: ec2_mssql_inv_host_links.EC2MSSQLInvHostLinks = links
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
        self.protection_info: protection_info.ProtectionInfo = protection_info
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
        embedded = dictionary.get('_embedded')
        key = '_links'
        links = (
            ec2_mssql_inv_host_links.EC2MSSQLInvHostLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        connection_id = dictionary.get('connection_id')
        endpoint = dictionary.get('endpoint')
        environment_id = dictionary.get('environment_id')
        has_associated_availability_group = dictionary.get('has_associated_availability_group')
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
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            aws_region,
            connection_id,
            endpoint,
            environment_id,
            has_associated_availability_group,
            p_id,
            instance_count,
            is_part_of_fci,
            organizational_unit_id,
            p_protection_info,
            status,
        )
