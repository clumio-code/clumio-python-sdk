#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import connection_group_links as connection_group_links_
from clumioapi.models import consolidated_config as consolidated_config_

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
    _names: dict[str, str] = {
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
        embedded: object,
        etag: str,
        links: connection_group_links_.ConnectionGroupLinks,
        account_name: str,
        account_native_ids: Sequence[str],
        asset_types_enabled: Sequence[str],
        aws_regions: Sequence[str],
        config: consolidated_config_.ConsolidatedConfig,
        created_timestamp: str,
        deployment_template_url: str,
        description: str,
        external_id: str,
        p_id: str,
        intended_account_native_ids: Sequence[str],
        intended_asset_types: Sequence[str],
        intended_aws_regions: Sequence[str],
        master_aws_account_id: str,
        master_region: str,
        ongoing_stack_operation: str,
        organizational_unit_id: str,
        stack_arn: str,
        stack_name: str,
        status: str,
    ) -> None:
        """Constructor for the UpdateConnectionGroupResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.etag: str = etag
        self.links: connection_group_links_.ConnectionGroupLinks = links
        self.account_name: str = account_name
        self.account_native_ids: Sequence[str] = account_native_ids
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_regions: Sequence[str] = aws_regions
        self.config: consolidated_config_.ConsolidatedConfig = config
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

        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = connection_group_links_.ConnectionGroupLinks.from_dictionary(val)

        val = dictionary['account_name']
        val_account_name = val

        val = dictionary['account_native_ids']
        val_account_native_ids = val

        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['aws_regions']
        val_aws_regions = val

        val = dictionary['config']
        val_config = consolidated_config_.ConsolidatedConfig.from_dictionary(val)

        val = dictionary['created_timestamp']
        val_created_timestamp = val

        val = dictionary['deployment_template_url']
        val_deployment_template_url = val

        val = dictionary['description']
        val_description = val

        val = dictionary['external_id']
        val_external_id = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['intended_account_native_ids']
        val_intended_account_native_ids = val

        val = dictionary['intended_asset_types']
        val_intended_asset_types = val

        val = dictionary['intended_aws_regions']
        val_intended_aws_regions = val

        val = dictionary['master_aws_account_id']
        val_master_aws_account_id = val

        val = dictionary['master_region']
        val_master_region = val

        val = dictionary['ongoing_stack_operation']
        val_ongoing_stack_operation = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['stack_arn']
        val_stack_arn = val

        val = dictionary['stack_name']
        val_stack_name = val

        val = dictionary['status']
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_account_name,  # type: ignore
            val_account_native_ids,  # type: ignore
            val_asset_types_enabled,  # type: ignore
            val_aws_regions,  # type: ignore
            val_config,  # type: ignore
            val_created_timestamp,  # type: ignore
            val_deployment_template_url,  # type: ignore
            val_description,  # type: ignore
            val_external_id,  # type: ignore
            val_p_id,  # type: ignore
            val_intended_account_native_ids,  # type: ignore
            val_intended_asset_types,  # type: ignore
            val_intended_aws_regions,  # type: ignore
            val_master_aws_account_id,  # type: ignore
            val_master_region,  # type: ignore
            val_ongoing_stack_operation,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_stack_arn,  # type: ignore
            val_stack_name,  # type: ignore
            val_status,  # type: ignore
        )
