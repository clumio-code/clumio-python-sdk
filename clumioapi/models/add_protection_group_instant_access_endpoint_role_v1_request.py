#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='AddProtectionGroupInstantAccessEndpointRoleV1Request')


@dataclasses.dataclass
class AddProtectionGroupInstantAccessEndpointRoleV1Request:
    """Implementation of the 'AddProtectionGroupInstantAccessEndpointRoleV1Request' model.

        Attributes:
            IsAllowExternalAccount:
                Allow the addition of a role from an external account. this requires a feature flag to be enabled, contact support@clumio.com.

            RoleAlias:
                Descriptive alias of the iam role.

            RoleArn:
                Arn of the iam role to allow access the endpoint. the role must be accessible from aws account
    registered with clumio.

    """

    IsAllowExternalAccount: bool | None = None
    RoleAlias: str | None = None
    RoleArn: str | None = None

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
        val = dictionary.get('is_allow_external_account', None)
        val_is_allow_external_account = val

        val = dictionary.get('role_alias', None)
        val_role_alias = val

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        # Return an object of this model
        return cls(
            val_is_allow_external_account,
            val_role_alias,
            val_role_arn,
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
