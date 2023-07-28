#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_connection_links
from clumioapi.models import consolidated_config
from clumioapi.models import discover_config
from clumioapi.models import protect_config

T = TypeVar('T', bound='ReadAWSConnectionResponse')


class ReadAWSConnectionResponse:
    """Implementation of the 'ReadAWSConnectionResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        account_name:
            The alias given to the account on AWS.
        account_native_id:
            The AWS-assigned ID of the account associated with the connection.
        aws_region:
            The AWS region associated with the connection. For example, `us-east-1`.
        clumio_aws_account_id:
            AWS AccountId of Clumio Control Plane
        clumio_aws_region:
            AWS Region of Clumio Control Plane
        config:
            The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
            Discover products for this connection.
            If this connection is deprecated to use unconsolidated configuration, then this
            field has a
            value of `null`.
        connection_status:
            The status of the connection. Possible values include "connecting",
            "connected", and "unlinked".
        created_timestamp:
            The timestamp of when the connection was created.
        description:
            The user-provided description for this connection.
        discover:
            The configuration of the Clumio Discover product for this connection.
            If this connection is not configured for Clumio Discover, then this field has a
            value of `null`.
        p_id:
            The Clumio-assigned ID of the connection.
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
            Valid values are any of ["EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3"].
        services_enabled:
            The services to be enabled for this configuration. Valid values are
            ["discover"], ["discover", "protect"]. This is only set when the
            registration is created, the enabled services are obtained directly from
            the installed template after that. (Deprecated as all connections will have
            both discover and protect enabled)
        stack_arn:
            The Amazon Resource Name of the installed CloudFormation stack in this AWS
            account
        stack_name:
            The name given to the installed CloudFormation stack on AWS.
        token:
            The 36-character Clumio AWS integration ID token used to identify the
            installation of the CloudFormation template on the account. This value
            will be pasted into the ClumioToken field when creating the
            CloudFormation stack.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'account_name': 'account_name',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'clumio_aws_account_id': 'clumio_aws_account_id',
        'clumio_aws_region': 'clumio_aws_region',
        'config': 'config',
        'connection_status': 'connection_status',
        'created_timestamp': 'created_timestamp',
        'description': 'description',
        'discover': 'discover',
        'p_id': 'id',
        'namespace': 'namespace',
        'organizational_unit_id': 'organizational_unit_id',
        'protect': 'protect',
        'protect_asset_types_enabled': 'protect_asset_types_enabled',
        'services_enabled': 'services_enabled',
        'stack_arn': 'stack_arn',
        'stack_name': 'stack_name',
        'token': 'token',
    }

    def __init__(
        self,
        etag: str = None,
        links: aws_connection_links.AWSConnectionLinks = None,
        account_name: str = None,
        account_native_id: str = None,
        aws_region: str = None,
        clumio_aws_account_id: str = None,
        clumio_aws_region: str = None,
        config: consolidated_config.ConsolidatedConfig = None,
        connection_status: str = None,
        created_timestamp: str = None,
        description: str = None,
        discover: discover_config.DiscoverConfig = None,
        p_id: str = None,
        namespace: str = None,
        organizational_unit_id: str = None,
        protect: protect_config.ProtectConfig = None,
        protect_asset_types_enabled: Sequence[str] = None,
        services_enabled: Sequence[str] = None,
        stack_arn: str = None,
        stack_name: str = None,
        token: str = None,
    ) -> None:
        """Constructor for the ReadAWSConnectionResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: aws_connection_links.AWSConnectionLinks = links
        self.account_name: str = account_name
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.clumio_aws_account_id: str = clumio_aws_account_id
        self.clumio_aws_region: str = clumio_aws_region
        self.config: consolidated_config.ConsolidatedConfig = config
        self.connection_status: str = connection_status
        self.created_timestamp: str = created_timestamp
        self.description: str = description
        self.discover: discover_config.DiscoverConfig = discover
        self.p_id: str = p_id
        self.namespace: str = namespace
        self.organizational_unit_id: str = organizational_unit_id
        self.protect: protect_config.ProtectConfig = protect
        self.protect_asset_types_enabled: Sequence[str] = protect_asset_types_enabled
        self.services_enabled: Sequence[str] = services_enabled
        self.stack_arn: str = stack_arn
        self.stack_name: str = stack_name
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
        etag = dictionary.get('_etag')
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

        connection_status = dictionary.get('connection_status')
        created_timestamp = dictionary.get('created_timestamp')
        description = dictionary.get('description')
        key = 'discover'
        discover = (
            discover_config.DiscoverConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        namespace = dictionary.get('namespace')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protect'
        protect = (
            protect_config.ProtectConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protect_asset_types_enabled = dictionary.get('protect_asset_types_enabled')
        services_enabled = dictionary.get('services_enabled')
        stack_arn = dictionary.get('stack_arn')
        stack_name = dictionary.get('stack_name')
        token = dictionary.get('token')
        # Return an object of this model
        return cls(
            etag,
            links,
            account_name,
            account_native_id,
            aws_region,
            clumio_aws_account_id,
            clumio_aws_region,
            config,
            connection_status,
            created_timestamp,
            description,
            discover,
            p_id,
            namespace,
            organizational_unit_id,
            protect,
            protect_asset_types_enabled,
            services_enabled,
            stack_arn,
            stack_name,
            token,
        )
