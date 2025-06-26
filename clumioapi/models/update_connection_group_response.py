#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import connection_group_links
from clumioapi.models import consolidated_config

T = TypeVar('T', bound='UpdateConnectionGroupResponse')


class UpdateConnectionGroupResponse:
    """Implementation of the 'UpdateConnectionGroupResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        account_name:
            The alias given to the associated account in AWS.
        account_native_ids:
            The AWS-assigned IDs of the accounts associated with the Connection Group.
        asset_types_enabled:
            List of asset types connected via the connection-group.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        aws_regions:
            The AWS regions associated with the with the Connection Group.
        config:
            The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
            Discover products for this connection.
            If this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.
        created_timestamp:
            The timestamp of when the connection was created.
        deployment_template_url:
            Clumio's S3 URL that contains the template to create the required resources in
            the
            given account(s) according to the request.
        description:
            User-provided description for this connection group.
        external_id:
            Clumio assigned external ID for the connection group, should be used while
            creating the AWS stack.
        p_id:
            The Clumio-assigned ID of the Connection Group, should be used as the token
            while creating the stack in AWS.
        intended_account_native_ids:
            The AWS Account IDs that are intended to be associated with the Connection
            Group.
        intended_asset_types:
            THe asset types that are intended to be connected via connection-group.
        intended_aws_regions:
            The AWS regions that are intended to be connected with the Connection Group.
        master_aws_account_id:
            The master account which manages the connection-group's stack.
        master_region:
            The master region which manages the connection-group's stack.
        ongoing_stack_operation:
            Ongoing Operation of the deployed and active stack of ConnectionGroup.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            AWS environment. If this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. For more information about organizational units, refer to the
            Organizational-Units documentation.
        stack_arn:
            The Amazon Resource Name of the installed CloudFormation stack in AWS.
        stack_name:
            The name given to the installed CloudFormation stack in AWS.
        status:
            The status of the Connection Group based on the stack in associated AWS account.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'account_name': 'account_name',
        'account_native_ids': 'account_native_ids',
        'asset_types_enabled': 'asset_types_enabled',
        'aws_regions': 'aws_regions',
        'config': 'config',
        'created_timestamp': 'created_timestamp',
        'deployment_template_url': 'deployment_template_url',
        'description': 'description',
        'external_id': 'external_id',
        'p_id': 'id',
        'intended_account_native_ids': 'intended_account_native_ids',
        'intended_asset_types': 'intended_asset_types',
        'intended_aws_regions': 'intended_aws_regions',
        'master_aws_account_id': 'master_aws_account_id',
        'master_region': 'master_region',
        'ongoing_stack_operation': 'ongoing_stack_operation',
        'organizational_unit_id': 'organizational_unit_id',
        'stack_arn': 'stack_arn',
        'stack_name': 'stack_name',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: object = None,
        etag: str = None,
        links: connection_group_links.ConnectionGroupLinks = None,
        account_name: str = None,
        account_native_ids: Sequence[str] = None,
        asset_types_enabled: Sequence[str] = None,
        aws_regions: Sequence[str] = None,
        config: consolidated_config.ConsolidatedConfig = None,
        created_timestamp: str = None,
        deployment_template_url: str = None,
        description: str = None,
        external_id: str = None,
        p_id: str = None,
        intended_account_native_ids: Sequence[str] = None,
        intended_asset_types: Sequence[str] = None,
        intended_aws_regions: Sequence[str] = None,
        master_aws_account_id: str = None,
        master_region: str = None,
        ongoing_stack_operation: str = None,
        organizational_unit_id: str = None,
        stack_arn: str = None,
        stack_name: str = None,
        status: str = None,
    ) -> None:
        """Constructor for the UpdateConnectionGroupResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.etag: str = etag
        self.links: connection_group_links.ConnectionGroupLinks = links
        self.account_name: str = account_name
        self.account_native_ids: Sequence[str] = account_native_ids
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_regions: Sequence[str] = aws_regions
        self.config: consolidated_config.ConsolidatedConfig = config
        self.created_timestamp: str = created_timestamp
        self.deployment_template_url: str = deployment_template_url
        self.description: str = description
        self.external_id: str = external_id
        self.p_id: str = p_id
        self.intended_account_native_ids: Sequence[str] = intended_account_native_ids
        self.intended_asset_types: Sequence[str] = intended_asset_types
        self.intended_aws_regions: Sequence[str] = intended_aws_regions
        self.master_aws_account_id: str = master_aws_account_id
        self.master_region: str = master_region
        self.ongoing_stack_operation: str = ongoing_stack_operation
        self.organizational_unit_id: str = organizational_unit_id
        self.stack_arn: str = stack_arn
        self.stack_name: str = stack_name
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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            connection_group_links.ConnectionGroupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_name = dictionary.get('account_name')
        account_native_ids = dictionary.get('account_native_ids')
        asset_types_enabled = dictionary.get('asset_types_enabled')
        aws_regions = dictionary.get('aws_regions')
        key = 'config'
        config = (
            consolidated_config.ConsolidatedConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        created_timestamp = dictionary.get('created_timestamp')
        deployment_template_url = dictionary.get('deployment_template_url')
        description = dictionary.get('description')
        external_id = dictionary.get('external_id')
        p_id = dictionary.get('id')
        intended_account_native_ids = dictionary.get('intended_account_native_ids')
        intended_asset_types = dictionary.get('intended_asset_types')
        intended_aws_regions = dictionary.get('intended_aws_regions')
        master_aws_account_id = dictionary.get('master_aws_account_id')
        master_region = dictionary.get('master_region')
        ongoing_stack_operation = dictionary.get('ongoing_stack_operation')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        stack_arn = dictionary.get('stack_arn')
        stack_name = dictionary.get('stack_name')
        status = dictionary.get('status')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            account_name,
            account_native_ids,
            asset_types_enabled,
            aws_regions,
            config,
            created_timestamp,
            deployment_template_url,
            description,
            external_id,
            p_id,
            intended_account_native_ids,
            intended_asset_types,
            intended_aws_regions,
            master_aws_account_id,
            master_region,
            ongoing_stack_operation,
            organizational_unit_id,
            stack_arn,
            stack_name,
            status,
        )
