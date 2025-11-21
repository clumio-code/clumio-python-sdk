#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='PostProcessKmsV1Request')


@dataclasses.dataclass
class PostProcessKmsV1Request:
    """Implementation of the 'PostProcessKmsV1Request' model.

    The body of the request.

    Attributes:
        AccountNativeId:
            The aws-assigned id of the account associated with the connection.

        AwsRegion:
            The aws region associated with the connection. for example, `us-east-1`.

        CreatedMultiRegionCmk:
            Whether the cmk was created or an existing cmk was used.

        IntermediateRoleArn:
            Role arn to be assumed before accessing clumiorole in customer account.

        MultiRegionCmkKeyId:
            The multi-region cmk key id.

        RequestType:
            Indicates whether this is a create, update or delete request.

        RoleArn:
            The arn of the role.

        RoleExternalId:
            The external id to use with the role.

        RoleId:
            The id of the role.

        Token:
            The 36-character clumio aws integration id token used to identify the
            installation of the cloudformation/terraform template on the account.

        Version:
            The cloudformation/terraform template version used.

    """

    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    CreatedMultiRegionCmk: bool | None = None
    IntermediateRoleArn: str | None = None
    MultiRegionCmkKeyId: str | None = None
    RequestType: str | None = None
    RoleArn: str | None = None
    RoleExternalId: str | None = None
    RoleId: str | None = None
    Token: str | None = None
    Version: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('created_multi_region_cmk', None)
        val_created_multi_region_cmk = val

        val = dictionary.get('intermediate_role_arn', None)
        val_intermediate_role_arn = val

        val = dictionary.get('multi_region_cmk_key_id', None)
        val_multi_region_cmk_key_id = val

        val = dictionary.get('request_type', None)
        val_request_type = val

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        val = dictionary.get('role_external_id', None)
        val_role_external_id = val

        val = dictionary.get('role_id', None)
        val_role_id = val

        val = dictionary.get('token', None)
        val_token = val

        val = dictionary.get('version', None)
        val_version = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_aws_region,
            val_created_multi_region_cmk,
            val_intermediate_role_arn,
            val_multi_region_cmk_key_id,
            val_request_type,
            val_role_arn,
            val_role_external_id,
            val_role_id,
            val_token,
            val_version,
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
