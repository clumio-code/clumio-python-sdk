#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_environment_embedded
from clumioapi.models import aws_environment_links
from clumioapi.models import consolidated_config

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
    _names = {
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
        embedded: aws_environment_embedded.AWSEnvironmentEmbedded = None,
        links: aws_environment_links.AWSEnvironmentLinks = None,
        account_name: str = None,
        account_native_id: str = None,
        aws_az: Sequence[str] = None,
        aws_region: str = None,
        config: consolidated_config.ConsolidatedConfig = None,
        connection_group_id: str = None,
        connection_id: str = None,
        connection_management_status: str = None,
        connection_status: str = None,
        description: str = None,
        p_id: str = None,
        organizational_unit_id: str = None,
        services_enabled: Sequence[str] = None,
        template_version: int = None,
    ) -> None:
        """Constructor for the AWSEnvironment class."""

        # Initialize members of the class
        self.embedded: aws_environment_embedded.AWSEnvironmentEmbedded = embedded
        self.links: aws_environment_links.AWSEnvironmentLinks = links
        self.account_name: str = account_name
        self.account_native_id: str = account_native_id
        self.aws_az: Sequence[str] = aws_az
        self.aws_region: str = aws_region
        self.config: consolidated_config.ConsolidatedConfig = config
        self.connection_group_id: str = connection_group_id
        self.connection_id: str = connection_id
        self.connection_management_status: str = connection_management_status
        self.connection_status: str = connection_status
        self.description: str = description
        self.p_id: str = p_id
        self.organizational_unit_id: str = organizational_unit_id
        self.services_enabled: Sequence[str] = services_enabled
        self.template_version: int = template_version

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
        key = '_embedded'
        embedded = (
            aws_environment_embedded.AWSEnvironmentEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            aws_environment_links.AWSEnvironmentLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_name = dictionary.get('account_name')
        account_native_id = dictionary.get('account_native_id')
        aws_az = dictionary.get('aws_az')
        aws_region = dictionary.get('aws_region')
        key = 'config'
        config = (
            consolidated_config.ConsolidatedConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        connection_group_id = dictionary.get('connection_group_id')
        connection_id = dictionary.get('connection_id')
        connection_management_status = dictionary.get('connection_management_status')
        connection_status = dictionary.get('connection_status')
        description = dictionary.get('description')
        p_id = dictionary.get('id')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        services_enabled = dictionary.get('services_enabled')
        template_version = dictionary.get('template_version')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_name,
            account_native_id,
            aws_az,
            aws_region,
            config,
            connection_group_id,
            connection_id,
            connection_management_status,
            connection_status,
            description,
            p_id,
            organizational_unit_id,
            services_enabled,
            template_version,
        )
