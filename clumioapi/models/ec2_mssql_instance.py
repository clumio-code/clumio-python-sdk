#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssql_instance_embedded as ec2_mssql_instance_embedded_
from clumioapi.models import ec2_mssql_instance_links as ec2_mssql_instance_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='EC2MSSQLInstance')


@dataclasses.dataclass
class EC2MSSQLInstance:
    """Implementation of the 'EC2MSSQLInstance' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the ec2 instance of the mssql
            instance.

        AwsRegion:
            The aws region associated with the ec2 instance of the mssql instance.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the ec2 mssql
            instance.

        HasAssociatedAvailabilityGroup:
            The boolean value represents if availability group is present in the instance.

        HostConnectionId:
            The clumio-assigned id of the host connection containing the given mssql
            instance.

        HostEndpoint:
            The user-provided endpoint of the host containing the given database.

        HostId:
            The clumio-assigned id of the host, containing the instance.

        Id:
            The clumio-assigned id of the instance.

        Name:
            The microsoft sql assigned name of the instance.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the instance.

        ProductVersion:
            Product version of the instance.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        ServerName:
            The microsoft sql assigned server name of the instance.

        Status:
            The status of the instance, possible values include 'active' and 'inactive'.

    """

    Embedded: ec2_mssql_instance_embedded_.EC2MSSQLInstanceEmbedded | None = None
    Links: ec2_mssql_instance_links_.EC2MSSQLInstanceLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    EnvironmentId: str | None = None
    HasAssociatedAvailabilityGroup: bool | None = None
    HostConnectionId: str | None = None
    HostEndpoint: str | None = None
    HostId: str | None = None
    Id: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProductVersion: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    ServerName: str | None = None
    Status: str | None = None

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
        val_id = val

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
            val_id,
            val_name,
            val_organizational_unit_id,
            val_product_version,
            val_protection_info,
            val_server_name,
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
        return model_instance
