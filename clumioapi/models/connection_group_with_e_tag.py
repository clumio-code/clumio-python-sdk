#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import connection_group_links as connection_group_links_
from clumioapi.models import consolidated_config as consolidated_config_
import requests

T = TypeVar('T', bound='ConnectionGroupWithETag')


@dataclasses.dataclass
class ConnectionGroupWithETag:
    """Implementation of the 'ConnectionGroupWithETag' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Etag:
            The etag value.

        Links:
            Urls to pages related to the resource.

        AccountName:
            The alias given to the associated account in aws.

        AccountNativeIds:
            The aws-assigned ids of the accounts associated with the connection group.

        AssetTypesEnabled:
            List of asset types connected via the connection-group.
            valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs",
            "icebergonglue", "icebergons3tables", "fsx"].

            note -
            1. ec2/ebs is required for ec2mssql.
            2. ebs as a value is deprecated in favor of ec2/ebs.

        AwsRegions:
            The aws regions associated with the with the connection group.

        Config:
            The consolidated configuration of the clumio cloud protect and clumio cloud
            discover products for this connection.
            if this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.

        CreatedTimestamp:
            The timestamp of when the connection was created.

        DeploymentTemplateUrl:
            Clumio's s3 url that contains the template to create the required resources in
            the
            given account(s) according to the request.

        Description:
            User-provided description for this connection group.

        ExternalId:
            Clumio assigned external id for the connection group, should be used while
            creating the aws stack.

        Id:
            The clumio-assigned id of the connection group, should be used as the token
            while creating the stack in aws.

        IntendedAccountNativeIds:
            The aws account ids that are intended to be associated with the connection
            group.

        IntendedAssetTypes:
            The asset types that are intended to be connected via connection-group.

        IntendedAwsRegions:
            The aws regions that are intended to be connected with the connection group.

        MasterAwsAccountId:
            The master account which manages the connection-group's stack.

        MasterRegion:
            The master region which manages the connection-group's stack.

        OngoingStackOperation:
            Ongoing operation of the deployed and active stack of connectiongroup.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the
            aws environment. if this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. for more information about organizational units, refer to the
            organizational-units documentation.

        StackArn:
            The amazon resource name of the installed cloudformation stack in aws.

        StackName:
            The name given to the installed cloudformation stack in aws.

        Status:
            The status of the connection group based on the stack in associated aws account.

        TemplatePermissionSet

    """

    Embedded: object | None = None
    Etag: str | None = None
    Links: connection_group_links_.ConnectionGroupLinks | None = None
    AccountName: str | None = None
    AccountNativeIds: Sequence[str] | None = None
    AssetTypesEnabled: Sequence[str] | None = None
    AwsRegions: Sequence[str] | None = None
    Config: consolidated_config_.ConsolidatedConfig | None = None
    CreatedTimestamp: str | None = None
    DeploymentTemplateUrl: str | None = None
    Description: str | None = None
    ExternalId: str | None = None
    Id: str | None = None
    IntendedAccountNativeIds: Sequence[str] | None = None
    IntendedAssetTypes: Sequence[str] | None = None
    IntendedAwsRegions: Sequence[str] | None = None
    MasterAwsAccountId: str | None = None
    MasterRegion: str | None = None
    OngoingStackOperation: str | None = None
    OrganizationalUnitId: str | None = None
    StackArn: str | None = None
    StackName: str | None = None
    Status: str | None = None
    TemplatePermissionSet: str | None = None

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

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = connection_group_links_.ConnectionGroupLinks.from_dictionary(val)

        val = dictionary.get('account_name', None)
        val_account_name = val

        val = dictionary.get('account_native_ids', None)
        val_account_native_ids = val

        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('aws_regions', None)
        val_aws_regions = val

        val = dictionary.get('config', None)
        val_config = consolidated_config_.ConsolidatedConfig.from_dictionary(val)

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('deployment_template_url', None)
        val_deployment_template_url = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('external_id', None)
        val_external_id = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('intended_account_native_ids', None)
        val_intended_account_native_ids = val

        val = dictionary.get('intended_asset_types', None)
        val_intended_asset_types = val

        val = dictionary.get('intended_aws_regions', None)
        val_intended_aws_regions = val

        val = dictionary.get('master_aws_account_id', None)
        val_master_aws_account_id = val

        val = dictionary.get('master_region', None)
        val_master_region = val

        val = dictionary.get('ongoing_stack_operation', None)
        val_ongoing_stack_operation = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('stack_arn', None)
        val_stack_arn = val

        val = dictionary.get('stack_name', None)
        val_stack_name = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('template_permission_set', None)
        val_template_permission_set = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_account_name,
            val_account_native_ids,
            val_asset_types_enabled,
            val_aws_regions,
            val_config,
            val_created_timestamp,
            val_deployment_template_url,
            val_description,
            val_external_id,
            val_id,
            val_intended_account_native_ids,
            val_intended_asset_types,
            val_intended_aws_regions,
            val_master_aws_account_id,
            val_master_region,
            val_ongoing_stack_operation,
            val_organizational_unit_id,
            val_stack_arn,
            val_stack_name,
            val_status,
            val_template_permission_set,
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
