#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_connection_links as aws_connection_links_
from clumioapi.models import connection_resources_resp as connection_resources_resp_
from clumioapi.models import consolidated_config as consolidated_config_
from clumioapi.models import discover_config as discover_config_
from clumioapi.models import protect_config as protect_config_

T = TypeVar('T', bound='AWSConnection')


class AWSConnection:
    """Implementation of the 'AWSConnection' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        account_name:
            The alias given to the account on AWS.
        account_native_id:
            The AWS-assigned ID of the account associated with the connection.
        aws_region:
            The AWS region associated with the connection. For example, `us-east-1`.
        clumio_aws_account_id:
            AWS account ID of the Clumio control plane.
        clumio_aws_region:
            AWS region of the Clumio control plane
        config:
            The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
            Discover products for this connection.
            If this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.
        connection_group_id:
            Clumio assigned ID of the associated connection group.
        connection_management_status:
            Management status of connection.
        connection_status:
            The status of the connection considering all the deployments made for it.
        created_timestamp:
            The timestamp of when the connection was created.
        data_plane_account_id:
            AWS account ID of the data plane for the connection.
        deployment_type:
            The deployment method with which the currently active connection was
            established.
        description:
            The user-provided description for this connection.
        discover:
            The configuration of the Clumio Discover product for this connection.
            If this connection is not configured for Clumio Discover, then this field has a
            value of `null`.
        external_id:
            Clumio assigned external ID of the connection or of the associated connection
            group.
        p_id:
            The Clumio-assigned ID of the connection.
        ingestion_status:
            Status denoting whether Ingestion has started for the connection.
            Valid values are "initial", "in_progress", "failed", "completed".
        namespace:
            K8S Namespace
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            AWS environment. If this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. For more information about organizational units, refer to the
            Organizational-Units documentation.
        protect:
            The configuration of the Clumio Cloud Protect product for this connection.
            If this connection is not configured for Clumio Cloud Protect, then this field
            has a
            value of `null`.
        protect_asset_types_enabled:
            The asset types enabled for protect.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "IcebergOnGlue"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        resources:

        retired_stack_arn:
            The Amazon Resource Name of the stale CloudFormation stack when the connection
            was migrated to connection groups.
            NOTE - This has to be removed from AWS as well to delete the connection
            completely.
        services_enabled:
            The services to be enabled for this configuration. Valid values are
            ["discover"], ["discover", "protect"]. This is only set when the
            registration is created, the enabled services are obtained directly from
            the installed template after that. (Deprecated as all connections will have
            both discover and protect enabled)
        stack_arn:
            The Amazon Resource Name of the installed and active CloudFormation stack(if
            any) in AWS.
        stack_name:
            The name given to the installed and active CloudFormation stack(if any) in AWS.
        target_setup_status:
            Status denoting whether Target Setup has started for the connection.
            Valid values are "initial", "in_progress", "failed", "completed".
        template_permission_set:

        token:
            The 36-character Clumio AWS integration ID token used to identify the
            installation of the CloudFormation template on the account. This value
            will be pasted into the ClumioToken field when creating the
            CloudFormation stack.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'account_name': 'account_name',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'clumio_aws_account_id': 'clumio_aws_account_id',
        'clumio_aws_region': 'clumio_aws_region',
        'config': 'config',
        'connection_group_id': 'connection_group_id',
        'connection_management_status': 'connection_management_status',
        'connection_status': 'connection_status',
        'created_timestamp': 'created_timestamp',
        'data_plane_account_id': 'data_plane_account_id',
        'deployment_type': 'deployment_type',
        'description': 'description',
        'discover': 'discover',
        'external_id': 'external_id',
        'p_id': 'id',
        'ingestion_status': 'ingestion_status',
        'namespace': 'namespace',
        'organizational_unit_id': 'organizational_unit_id',
        'protect': 'protect',
        'protect_asset_types_enabled': 'protect_asset_types_enabled',
        'resources': 'resources',
        'retired_stack_arn': 'retired_stack_arn',
        'services_enabled': 'services_enabled',
        'stack_arn': 'stack_arn',
        'stack_name': 'stack_name',
        'target_setup_status': 'target_setup_status',
        'template_permission_set': 'template_permission_set',
        'token': 'token',
    }

    def __init__(
        self,
        links: aws_connection_links_.AWSConnectionLinks | None = None,
        account_name: str | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        clumio_aws_account_id: str | None = None,
        clumio_aws_region: str | None = None,
        config: consolidated_config_.ConsolidatedConfig | None = None,
        connection_group_id: str | None = None,
        connection_management_status: str | None = None,
        connection_status: str | None = None,
        created_timestamp: str | None = None,
        data_plane_account_id: str | None = None,
        deployment_type: str | None = None,
        description: str | None = None,
        discover: discover_config_.DiscoverConfig | None = None,
        external_id: str | None = None,
        p_id: str | None = None,
        ingestion_status: str | None = None,
        namespace: str | None = None,
        organizational_unit_id: str | None = None,
        protect: protect_config_.ProtectConfig | None = None,
        protect_asset_types_enabled: Sequence[str] | None = None,
        resources: connection_resources_resp_.ConnectionResourcesResp | None = None,
        retired_stack_arn: str | None = None,
        services_enabled: Sequence[str] | None = None,
        stack_arn: str | None = None,
        stack_name: str | None = None,
        target_setup_status: str | None = None,
        template_permission_set: str | None = None,
        token: str | None = None,
    ) -> None:
        """Constructor for the AWSConnection class."""

        # Initialize members of the class
        self.links: aws_connection_links_.AWSConnectionLinks | None = links
        self.account_name: str | None = account_name
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.clumio_aws_account_id: str | None = clumio_aws_account_id
        self.clumio_aws_region: str | None = clumio_aws_region
        self.config: consolidated_config_.ConsolidatedConfig | None = config
        self.connection_group_id: str | None = connection_group_id
        self.connection_management_status: str | None = connection_management_status
        self.connection_status: str | None = connection_status
        self.created_timestamp: str | None = created_timestamp
        self.data_plane_account_id: str | None = data_plane_account_id
        self.deployment_type: str | None = deployment_type
        self.description: str | None = description
        self.discover: discover_config_.DiscoverConfig | None = discover
        self.external_id: str | None = external_id
        self.p_id: str | None = p_id
        self.ingestion_status: str | None = ingestion_status
        self.namespace: str | None = namespace
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protect: protect_config_.ProtectConfig | None = protect
        self.protect_asset_types_enabled: Sequence[str] | None = protect_asset_types_enabled
        self.resources: connection_resources_resp_.ConnectionResourcesResp | None = resources
        self.retired_stack_arn: str | None = retired_stack_arn
        self.services_enabled: Sequence[str] | None = services_enabled
        self.stack_arn: str | None = stack_arn
        self.stack_name: str | None = stack_name
        self.target_setup_status: str | None = target_setup_status
        self.template_permission_set: str | None = template_permission_set
        self.token: str | None = token

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
        val_p_id = val

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
            val_p_id,
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
