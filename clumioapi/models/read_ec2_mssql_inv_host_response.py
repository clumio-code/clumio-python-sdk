#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssql_inv_host_links as ec2_mssql_inv_host_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='ReadEC2MSSQLInvHostResponse')


@dataclasses.dataclass
class ReadEC2MSSQLInvHostResponse:
    """Implementation of the 'ReadEC2MSSQLInvHostResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Ec2mssqlinvhostlinks contains links related to ec2 mssql host
            urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the ec2 instance of the mssql
            host.

        AwsRegion:
            The aws region associated with the ec2 instance of the mssql host.

        ConnectionId:
            The clumio-assigned id of the host connection.

        Endpoint:
            The user-provided endpoint of the host containing the given database.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the ec2 mssql
            host.

        HasAssociatedAvailabilityGroup:
            Determines whether or not an availability group is present in the host.

        Id:
            The clumio-assigned id of the host.

        InstanceCount:
            The number of instances present in the host.

        IsPartOfFci:
            Ispartoffci is a boolean field representing if the host is part of failover
            cluster.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the host.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        Status:
            The status of the host, possible values include 'active' and 'inactive'.

    """

    Embedded: object | None = None
    Links: ec2_mssql_inv_host_links_.EC2MSSQLInvHostLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    ConnectionId: str | None = None
    Endpoint: str | None = None
    EnvironmentId: str | None = None
    HasAssociatedAvailabilityGroup: bool | None = None
    Id: str | None = None
    InstanceCount: int | None = None
    IsPartOfFci: bool | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    Status: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val_id = val

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
            val_id,
            val_instance_count,
            val_is_part_of_fci,
            val_organizational_unit_id,
            val_protection_info,
            val_status,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        model_instance.raw_response = response
        return model_instance
