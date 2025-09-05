#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PostProcessAwsConnectionV1Request')


class PostProcessAwsConnectionV1Request:
    """Implementation of the 'PostProcessAwsConnectionV1Request' model.

    The body of the request.

    Attributes:
        account_native_id:
            The AWS-assigned ID of the account associated with the connection.
        aws_region:
            The AWS region associated with the connection. For example, `us-east-1`.
        clumio_event_pub_id:
            ClumioEventPubId is the Clumio Event Pub SNS topic ID.
        configuration:
            Configuration represents the AWS connection configuration in json string format
        intermediate_role_arn:
            Role arn to be assumed before accessing ClumioRole in customer account
        properties:
            Properties is a key value map meant to be used for passing additional
            information
            like resource IDs/ARNs.
        request_type:
            RequestType indicates whether this is a Create, Update or Delete request
        role_arn:
            RoleArn is the ARN of the ClumioIAMRole created in the customer account
        role_external_id:
            Role External Id is the unique string passed while creating the AWS resources .
        token:
            The 36-character Clumio AWS integration ID token used to identify the
            installation of the CloudFormation/Terraform template on the account.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'clumio_event_pub_id': 'clumio_event_pub_id',
        'configuration': 'configuration',
        'intermediate_role_arn': 'intermediate_role_arn',
        'properties': 'properties',
        'request_type': 'request_type',
        'role_arn': 'role_arn',
        'role_external_id': 'role_external_id',
        'token': 'token',
    }

    def __init__(
        self,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        clumio_event_pub_id: str | None = None,
        configuration: str | None = None,
        intermediate_role_arn: str | None = None,
        properties: Mapping[str, str] | None = None,
        request_type: str | None = None,
        role_arn: str | None = None,
        role_external_id: str | None = None,
        token: str | None = None,
    ) -> None:
        """Constructor for the PostProcessAwsConnectionV1Request class."""

        # Initialize members of the class
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.clumio_event_pub_id: str | None = clumio_event_pub_id
        self.configuration: str | None = configuration
        self.intermediate_role_arn: str | None = intermediate_role_arn
        self.properties: Mapping[str, str] | None = properties
        self.request_type: str | None = request_type
        self.role_arn: str | None = role_arn
        self.role_external_id: str | None = role_external_id
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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('clumio_event_pub_id', None)
        val_clumio_event_pub_id = val

        val = dictionary.get('configuration', None)
        val_configuration = val

        val = dictionary.get('intermediate_role_arn', None)
        val_intermediate_role_arn = val

        val = dictionary.get('properties', None)
        val_properties = val

        val = dictionary.get('request_type', None)
        val_request_type = val

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        val = dictionary.get('role_external_id', None)
        val_role_external_id = val

        val = dictionary.get('token', None)
        val_token = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_aws_region,
            val_clumio_event_pub_id,
            val_configuration,
            val_intermediate_role_arn,
            val_properties,
            val_request_type,
            val_role_arn,
            val_role_external_id,
            val_token,
        )
