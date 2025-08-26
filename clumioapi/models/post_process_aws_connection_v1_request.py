#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='PostProcessAwsConnectionV1Request')


@dataclasses.dataclass
class PostProcessAwsConnectionV1Request:
    """Implementation of the 'PostProcessAwsConnectionV1Request' model.

        The body of the request.

        Attributes:
            AccountNativeId:
                The aws-assigned id of the account associated with the connection.

            AwsRegion:
                The aws region associated with the connection. for example, `us-east-1`.

            ClumioEventPubId:
                Clumioeventpubid is the clumio event pub sns topic id.

            Configuration:
                Configuration represents the aws connection configuration in json string format.

            IntermediateRoleArn:
                Role arn to be assumed before accessing clumiorole in customer account.

            Properties:
                Properties is a key value map meant to be used for passing additional information
    like resource ids/arns.

            RequestType:
                Requesttype indicates whether this is a create, update or delete request.

            RoleArn:
                Rolearn is the arn of the clumioiamrole created in the customer account.

            RoleExternalId:
                Role external id is the unique string passed while creating the aws resources .

            Token:
                The 36-character clumio aws integration id token used to identify the
    installation of the cloudformation/terraform template on the account.

    """

    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    ClumioEventPubId: str | None = None
    Configuration: str | None = None
    IntermediateRoleArn: str | None = None
    Properties: Mapping[str, str] | None = None
    RequestType: str | None = None
    RoleArn: str | None = None
    RoleExternalId: str | None = None
    Token: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
