#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_environment_embedded as aws_environment_embedded_
from clumioapi.models import aws_environment_links as aws_environment_links_
from clumioapi.models import consolidated_config as consolidated_config_

T = TypeVar('T', bound='AWSEnvironment')


class AWSEnvironment:
    """Implementation of the 'AWSEnvironment' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_name:
            The name given to the account.
        account_native_id:
            The AWS-assigned ID of the account associated with the environment.
        aws_az:
            The valid AWS availability zones for the environment. For example, `us_west-2a`.
        aws_region:
            The AWS region associated with the environment. For example, `us-west-2`.
        config:
            The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
            Discover products for this connection.
            If this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.
        connection_group_id:
            Clumio assigned ID of the associated connection group (if any).
        connection_id:
            The Clumio-assigned ID of the connection associated with the environment.
        connection_management_status:
            Management status of connection for the environment.
        connection_status:
            The status of the connection to the environment.
        description:
            The user-provided account description.
        p_id:
            The Clumio-assigned ID of the environment.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            environment.
        services_enabled:
            The AWS services enabled for this environment. Possible values include "ebs",
            "rds" and "dynamodb".
        template_version:
            The Clumio CloudFormation template version used to deploy the CloudFormation
            stack.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_name': 'account_name',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'config': 'config',
        'connection_group_id': 'connection_group_id',
        'connection_id': 'connection_id',
        'connection_management_status': 'connection_management_status',
        'connection_status': 'connection_status',
        'description': 'description',
        'p_id': 'id',
        'organizational_unit_id': 'organizational_unit_id',
        'services_enabled': 'services_enabled',
        'template_version': 'template_version',
    }

    def __init__(
        self,
        embedded: aws_environment_embedded_.AWSEnvironmentEmbedded | None = None,
        links: aws_environment_links_.AWSEnvironmentLinks | None = None,
        account_name: str | None = None,
        account_native_id: str | None = None,
        aws_az: Sequence[str] | None = None,
        aws_region: str | None = None,
        config: consolidated_config_.ConsolidatedConfig | None = None,
        connection_group_id: str | None = None,
        connection_id: str | None = None,
        connection_management_status: str | None = None,
        connection_status: str | None = None,
        description: str | None = None,
        p_id: str | None = None,
        organizational_unit_id: str | None = None,
        services_enabled: Sequence[str] | None = None,
        template_version: int | None = None,
    ) -> None:
        """Constructor for the AWSEnvironment class."""

        # Initialize members of the class
        self.embedded: aws_environment_embedded_.AWSEnvironmentEmbedded | None = embedded
        self.links: aws_environment_links_.AWSEnvironmentLinks | None = links
        self.account_name: str | None = account_name
        self.account_native_id: str | None = account_native_id
        self.aws_az: Sequence[str] | None = aws_az
        self.aws_region: str | None = aws_region
        self.config: consolidated_config_.ConsolidatedConfig | None = config
        self.connection_group_id: str | None = connection_group_id
        self.connection_id: str | None = connection_id
        self.connection_management_status: str | None = connection_management_status
        self.connection_status: str | None = connection_status
        self.description: str | None = description
        self.p_id: str | None = p_id
        self.organizational_unit_id: str | None = organizational_unit_id
        self.services_enabled: Sequence[str] | None = services_enabled
        self.template_version: int | None = template_version

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
        val_p_id = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('services_enabled', None)
        val_services_enabled = val

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
            val_p_id,
            val_organizational_unit_id,
            val_services_enabled,
            val_template_version,
        )
