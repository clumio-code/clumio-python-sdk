#
# Copyright 2023. Clumio, Inc.
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
    _names = {
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
        account_native_id: str = None,
        aws_region: str = None,
        clumio_event_pub_id: str = None,
        configuration: str = None,
        intermediate_role_arn: str = None,
        properties: Mapping[str, str] = None,
        request_type: str = None,
        role_arn: str = None,
        role_external_id: str = None,
        token: str = None,
    ) -> None:
        """Constructor for the PostProcessAwsConnectionV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.clumio_event_pub_id: str = clumio_event_pub_id
        self.configuration: str = configuration
        self.intermediate_role_arn: str = intermediate_role_arn
        self.properties: Mapping[str, str] = properties
        self.request_type: str = request_type
        self.role_arn: str = role_arn
        self.role_external_id: str = role_external_id
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
        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        clumio_event_pub_id = dictionary.get('clumio_event_pub_id')
        configuration = dictionary.get('configuration')
        intermediate_role_arn = dictionary.get('intermediate_role_arn')
        properties = dictionary.get('properties')
        request_type = dictionary.get('request_type')
        role_arn = dictionary.get('role_arn')
        role_external_id = dictionary.get('role_external_id')
        token = dictionary.get('token')
        # Return an object of this model
        return cls(
            account_native_id,
            aws_region,
            clumio_event_pub_id,
            configuration,
            intermediate_role_arn,
            properties,
            request_type,
            role_arn,
            role_external_id,
            token,
        )
