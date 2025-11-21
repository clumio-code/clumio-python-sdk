#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_environment_embedded as aws_environment_embedded_
from clumioapi.models import aws_environment_links as aws_environment_links_
from clumioapi.models import consolidated_config as consolidated_config_
import requests

T = TypeVar('T', bound='AWSEnvironment')


@dataclasses.dataclass
class AWSEnvironment:
    """Implementation of the 'AWSEnvironment' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountName:
            The name given to the account.

        AccountNativeId:
            The aws-assigned id of the account associated with the environment.

        AwsAz:
            The valid aws availability zones for the environment. for example, `us_west-2a`.

        AwsRegion:
            The aws region associated with the environment. for example, `us-west-2`.

        Config:
            The consolidated configuration of the clumio cloud protect and clumio cloud
            discover products for this connection.
            if this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.

        ConnectionGroupId:
            Clumio assigned id of the associated connection group (if any).

        ConnectionId:
            The clumio-assigned id of the connection associated with the environment.

        ConnectionManagementStatus:
            Management status of connection for the environment.

        ConnectionStatus:
            The status of the connection to the environment.

        Description:
            The user-provided account description.

        Id:
            The clumio-assigned id of the environment.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the
            environment.

        ServicesEnabled:
            The aws services enabled for this environment. possible values include "ebs",
            "rds" and "dynamodb".

        TemplatePermissionSet:
            Type of permissions in the template deployed for the environment.

        TemplateVersion:
            The clumio cloudformation template version used to deploy the cloudformation
            stack.

    """

    Embedded: aws_environment_embedded_.AWSEnvironmentEmbedded | None = None
    Links: aws_environment_links_.AWSEnvironmentLinks | None = None
    AccountName: str | None = None
    AccountNativeId: str | None = None
    AwsAz: Sequence[str] | None = None
    AwsRegion: str | None = None
    Config: consolidated_config_.ConsolidatedConfig | None = None
    ConnectionGroupId: str | None = None
    ConnectionId: str | None = None
    ConnectionManagementStatus: str | None = None
    ConnectionStatus: str | None = None
    Description: str | None = None
    Id: str | None = None
    OrganizationalUnitId: str | None = None
    ServicesEnabled: Sequence[str] | None = None
    TemplatePermissionSet: str | None = None
    TemplateVersion: int | None = None

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
        val_embedded = aws_environment_embedded_.AWSEnvironmentEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = aws_environment_links_.AWSEnvironmentLinks.from_dictionary(val)

        val = dictionary.get('account_name', None)
        val_account_name = val

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('config', None)
        val_config = consolidated_config_.ConsolidatedConfig.from_dictionary(val)

        val = dictionary.get('connection_group_id', None)
        val_connection_group_id = val

        val = dictionary.get('connection_id', None)
        val_connection_id = val

        val = dictionary.get('connection_management_status', None)
        val_connection_management_status = val

        val = dictionary.get('connection_status', None)
        val_connection_status = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('services_enabled', None)
        val_services_enabled = val

        val = dictionary.get('template_permission_set', None)
        val_template_permission_set = val

        val = dictionary.get('template_version', None)
        val_template_version = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_name,
            val_account_native_id,
            val_aws_az,
            val_aws_region,
            val_config,
            val_connection_group_id,
            val_connection_id,
            val_connection_management_status,
            val_connection_status,
            val_description,
            val_id,
            val_organizational_unit_id,
            val_services_enabled,
            val_template_permission_set,
            val_template_version,
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
