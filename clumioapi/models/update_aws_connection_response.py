#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_connection_links
from clumioapi.models import connection_resources_resp
from clumioapi.models import consolidated_config
from clumioapi.models import discover_config
from clumioapi.models import protect_config

T = TypeVar('T', bound='UpdateAWSConnectionResponse')


class UpdateAWSConnectionResponse:
    """Implementation of the 'UpdateAWSConnectionResponse' model.

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
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS"].

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
    _names = {
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
        links: aws_connection_links.AWSConnectionLinks = None,
        account_name: str = None,
        account_native_id: str = None,
        aws_region: str = None,
        clumio_aws_account_id: str = None,
        clumio_aws_region: str = None,
        config: consolidated_config.ConsolidatedConfig = None,
        connection_group_id: str = None,
        connection_management_status: str = None,
        connection_status: str = None,
        created_timestamp: str = None,
        data_plane_account_id: str = None,
        deployment_type: str = None,
        description: str = None,
        discover: discover_config.DiscoverConfig = None,
        external_id: str = None,
        p_id: str = None,
        ingestion_status: str = None,
        namespace: str = None,
        organizational_unit_id: str = None,
        protect: protect_config.ProtectConfig = None,
        protect_asset_types_enabled: Sequence[str] = None,
        resources: connection_resources_resp.ConnectionResourcesResp = None,
        retired_stack_arn: str = None,
        services_enabled: Sequence[str] = None,
        stack_arn: str = None,
        stack_name: str = None,
        target_setup_status: str = None,
        template_permission_set: str = None,
        token: str = None,
    ) -> None:
        """Constructor for the UpdateAWSConnectionResponse class."""

        # Initialize members of the class
        self.links: aws_connection_links.AWSConnectionLinks = links
        self.account_name: str = account_name
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.clumio_aws_account_id: str = clumio_aws_account_id
        self.clumio_aws_region: str = clumio_aws_region
        self.config: consolidated_config.ConsolidatedConfig = config
        self.connection_group_id: str = connection_group_id
        self.connection_management_status: str = connection_management_status
        self.connection_status: str = connection_status
        self.created_timestamp: str = created_timestamp
        self.data_plane_account_id: str = data_plane_account_id
        self.deployment_type: str = deployment_type
        self.description: str = description
        self.discover: discover_config.DiscoverConfig = discover
        self.external_id: str = external_id
        self.p_id: str = p_id
        self.ingestion_status: str = ingestion_status
        self.namespace: str = namespace
        self.organizational_unit_id: str = organizational_unit_id
        self.protect: protect_config.ProtectConfig = protect
        self.protect_asset_types_enabled: Sequence[str] = protect_asset_types_enabled
        self.resources: connection_resources_resp.ConnectionResourcesResp = resources
        self.retired_stack_arn: str = retired_stack_arn
        self.services_enabled: Sequence[str] = services_enabled
        self.stack_arn: str = stack_arn
        self.stack_name: str = stack_name
        self.target_setup_status: str = target_setup_status
        self.template_permission_set: str = template_permission_set
        self.token: str = token

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
        key = '_links'
        links = (
            aws_connection_links.AWSConnectionLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_name = dictionary.get('account_name')
        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        clumio_aws_account_id = dictionary.get('clumio_aws_account_id')
        clumio_aws_region = dictionary.get('clumio_aws_region')
        key = 'config'
        config = (
            consolidated_config.ConsolidatedConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        connection_group_id = dictionary.get('connection_group_id')
        connection_management_status = dictionary.get('connection_management_status')
        connection_status = dictionary.get('connection_status')
        created_timestamp = dictionary.get('created_timestamp')
        data_plane_account_id = dictionary.get('data_plane_account_id')
        deployment_type = dictionary.get('deployment_type')
        description = dictionary.get('description')
        key = 'discover'
        discover = (
            discover_config.DiscoverConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        external_id = dictionary.get('external_id')
        p_id = dictionary.get('id')
        ingestion_status = dictionary.get('ingestion_status')
        namespace = dictionary.get('namespace')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protect'
        protect = (
            protect_config.ProtectConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protect_asset_types_enabled = dictionary.get('protect_asset_types_enabled')
        key = 'resources'
        resources = (
            connection_resources_resp.ConnectionResourcesResp.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        retired_stack_arn = dictionary.get('retired_stack_arn')
        services_enabled = dictionary.get('services_enabled')
        stack_arn = dictionary.get('stack_arn')
        stack_name = dictionary.get('stack_name')
        target_setup_status = dictionary.get('target_setup_status')
        template_permission_set = dictionary.get('template_permission_set')
        token = dictionary.get('token')
        # Return an object of this model
        return cls(
            links,
            account_name,
            account_native_id,
            aws_region,
            clumio_aws_account_id,
            clumio_aws_region,
            config,
            connection_group_id,
            connection_management_status,
            connection_status,
            created_timestamp,
            data_plane_account_id,
            deployment_type,
            description,
            discover,
            external_id,
            p_id,
            ingestion_status,
            namespace,
            organizational_unit_id,
            protect,
            protect_asset_types_enabled,
            resources,
            retired_stack_arn,
            services_enabled,
            stack_arn,
            stack_name,
            target_setup_status,
            template_permission_set,
            token,
        )
