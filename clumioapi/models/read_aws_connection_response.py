#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_connection_links as aws_connection_links_
from clumioapi.models import connection_resources_resp as connection_resources_resp_
from clumioapi.models import consolidated_config as consolidated_config_
from clumioapi.models import discover_config as discover_config_
from clumioapi.models import protect_config as protect_config_
import requests

T = TypeVar('T', bound='ReadAWSConnectionResponse')


@dataclasses.dataclass
class ReadAWSConnectionResponse:
    """Implementation of the 'ReadAWSConnectionResponse' model.

    Attributes:
        Etag:
            The etag value.

        Links:
            Urls to pages related to the resource.

        AccountName:
            The alias given to the account on aws.

        AccountNativeId:
            The aws-assigned id of the account associated with the connection.

        AwsRegion:
            The aws region associated with the connection. for example, `us-east-1`.

        ClumioAwsAccountId:
            Aws account id of the clumio control plane.

        ClumioAwsRegion:
            Aws region of the clumio control plane.

        Config:
            The consolidated configuration of the clumio cloud protect and clumio cloud
            discover products for this connection.
            if this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.

        ConnectionGroupId:
            Clumio assigned id of the associated connection group.

        ConnectionManagementStatus:
            Management status of connection.

        ConnectionStatus:
            The status of the connection considering all the deployments made for it.

        CreatedTimestamp:
            The timestamp of when the connection was created.

        DataPlaneAccountId:
            Aws account id of the data plane for the connection.

        DeploymentType:
            The deployment method with which the currently active connection was
            established.

        Description:
            The user-provided description for this connection.

        Discover:
            The configuration of the clumio discover product for this connection.
            if this connection is not configured for clumio discover, then this field has a
            value of `null`.

        ExternalId:
            Clumio assigned external id of the connection or of the associated connection
            group.

        Id:
            The clumio-assigned id of the connection.

        IngestionStatus:
            Status denoting whether ingestion has started for the connection.
            valid values are "initial", "in_progress", "failed", "completed".

        Namespace:
            K8s namespace.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the
            aws environment. if this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. for more information about organizational units, refer to the
            organizational-units documentation.

        Protect:
            The configuration of the clumio cloud protect product for this connection.
            if this connection is not configured for clumio cloud protect, then this field
            has a
            value of `null`.

        ProtectAssetTypesEnabled:
            The asset types enabled for protect.
            valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs",
            "icebergonglue", "icebergons3tables", "fsx"].

            note -
            1. ec2/ebs is required for ec2mssql.
            2. ebs as a value is deprecated in favor of ec2/ebs.

        Resources

        RetiredStackArn:
            The amazon resource name of the stale cloudformation stack when the connection
            was migrated to connection groups.
            note - this has to be removed from aws as well to delete the connection
            completely.

        ServicesEnabled:
            The services to be enabled for this configuration. valid values are
            ["discover"], ["discover", "protect"]. this is only set when the
            registration is created, the enabled services are obtained directly from
            the installed template after that. (deprecated as all connections will have
            both discover and protect enabled).

        StackArn:
            The amazon resource name of the installed and active cloudformation stack(if
            any) in aws.

        StackName:
            The name given to the installed and active cloudformation stack(if any) in aws.

        TargetSetupStatus:
            Status denoting whether target setup has started for the connection.
            valid values are "initial", "in_progress", "failed", "completed".

        TemplatePermissionSet

        Token:
            The 36-character clumio aws integration id token used to identify the
            installation of the cloudformation template on the account. this value
            will be pasted into the clumiotoken field when creating the
            cloudformation stack.

    """

    Etag: str | None = None
    Links: aws_connection_links_.AWSConnectionLinks | None = None
    AccountName: str | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    ClumioAwsAccountId: str | None = None
    ClumioAwsRegion: str | None = None
    Config: consolidated_config_.ConsolidatedConfig | None = None
    ConnectionGroupId: str | None = None
    ConnectionManagementStatus: str | None = None
    ConnectionStatus: str | None = None
    CreatedTimestamp: str | None = None
    DataPlaneAccountId: str | None = None
    DeploymentType: str | None = None
    Description: str | None = None
    Discover: discover_config_.DiscoverConfig | None = None
    ExternalId: str | None = None
    Id: str | None = None
    IngestionStatus: str | None = None
    Namespace: str | None = None
    OrganizationalUnitId: str | None = None
    Protect: protect_config_.ProtectConfig | None = None
    ProtectAssetTypesEnabled: Sequence[str] | None = None
    Resources: connection_resources_resp_.ConnectionResourcesResp | None = None
    RetiredStackArn: str | None = None
    ServicesEnabled: Sequence[str] | None = None
    StackArn: str | None = None
    StackName: str | None = None
    TargetSetupStatus: str | None = None
    TemplatePermissionSet: str | None = None
    Token: str | None = None
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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = aws_connection_links_.AWSConnectionLinks.from_dictionary(val)

        val = dictionary.get('account_name', None)
        val_account_name = val

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('clumio_aws_account_id', None)
        val_clumio_aws_account_id = val

        val = dictionary.get('clumio_aws_region', None)
        val_clumio_aws_region = val

        val = dictionary.get('config', None)
        val_config = consolidated_config_.ConsolidatedConfig.from_dictionary(val)

        val = dictionary.get('connection_group_id', None)
        val_connection_group_id = val

        val = dictionary.get('connection_management_status', None)
        val_connection_management_status = val

        val = dictionary.get('connection_status', None)
        val_connection_status = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('data_plane_account_id', None)
        val_data_plane_account_id = val

        val = dictionary.get('deployment_type', None)
        val_deployment_type = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('discover', None)
        val_discover = discover_config_.DiscoverConfig.from_dictionary(val)

        val = dictionary.get('external_id', None)
        val_external_id = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('ingestion_status', None)
        val_ingestion_status = val

        val = dictionary.get('namespace', None)
        val_namespace = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protect', None)
        val_protect = protect_config_.ProtectConfig.from_dictionary(val)

        val = dictionary.get('protect_asset_types_enabled', None)
        val_protect_asset_types_enabled = val

        val = dictionary.get('resources', None)
        val_resources = connection_resources_resp_.ConnectionResourcesResp.from_dictionary(val)

        val = dictionary.get('retired_stack_arn', None)
        val_retired_stack_arn = val

        val = dictionary.get('services_enabled', None)
        val_services_enabled = val

        val = dictionary.get('stack_arn', None)
        val_stack_arn = val

        val = dictionary.get('stack_name', None)
        val_stack_name = val

        val = dictionary.get('target_setup_status', None)
        val_target_setup_status = val

        val = dictionary.get('template_permission_set', None)
        val_template_permission_set = val

        val = dictionary.get('token', None)
        val_token = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_account_name,
            val_account_native_id,
            val_aws_region,
            val_clumio_aws_account_id,
            val_clumio_aws_region,
            val_config,
            val_connection_group_id,
            val_connection_management_status,
            val_connection_status,
            val_created_timestamp,
            val_data_plane_account_id,
            val_deployment_type,
            val_description,
            val_discover,
            val_external_id,
            val_id,
            val_ingestion_status,
            val_namespace,
            val_organizational_unit_id,
            val_protect,
            val_protect_asset_types_enabled,
            val_resources,
            val_retired_stack_arn,
            val_services_enabled,
            val_stack_arn,
            val_stack_name,
            val_target_setup_status,
            val_template_permission_set,
            val_token,
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
