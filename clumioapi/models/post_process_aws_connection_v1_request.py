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
        account_native_id: str,
        aws_region: str,
        clumio_event_pub_id: str,
        configuration: str,
        intermediate_role_arn: str,
        properties: Mapping[str, str],
        request_type: str,
        role_arn: str,
        role_external_id: str,
        token: str,
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
        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['clumio_event_pub_id']
        val_clumio_event_pub_id = val

        val = dictionary['configuration']
        val_configuration = val

        val = dictionary['intermediate_role_arn']
        val_intermediate_role_arn = val

        val = dictionary['properties']
        val_properties = val

        val = dictionary['request_type']
        val_request_type = val

        val = dictionary['role_arn']
        val_role_arn = val

        val = dictionary['role_external_id']
        val_role_external_id = val

        val = dictionary['token']
        val_token = val

        # Return an object of this model
        return cls(
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_clumio_event_pub_id,  # type: ignore
            val_configuration,  # type: ignore
            val_intermediate_role_arn,  # type: ignore
            val_properties,  # type: ignore
            val_request_type,  # type: ignore
            val_role_arn,  # type: ignore
            val_role_external_id,  # type: ignore
            val_token,  # type: ignore
        )
