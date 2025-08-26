#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='UpdateProtectionGroupInstantAccessEndpointRoleV1Request')


@dataclasses.dataclass
class UpdateProtectionGroupInstantAccessEndpointRoleV1Request:
    """Implementation of the 'UpdateProtectionGroupInstantAccessEndpointRoleV1Request' model.

        Attributes:
            UpdatedRoleAlias:
                The updated descriptive alias of the iam role. the current alias will be retained if
    empty updated_role_alias is passed.

            UpdatedRoleArn:
                The updated arn of the iam role to allow access to the endpoint. the role must be
    accessible from an aws account registered with clumio. the current arn will be retained
    if empty updated_role_arn is passed.

    """

    UpdatedRoleAlias: str | None = None
    UpdatedRoleArn: str | None = None

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
        val = dictionary.get('updated_role_alias', None)
        val_updated_role_alias = val

        val = dictionary.get('updated_role_arn', None)
        val_updated_role_arn = val

        # Return an object of this model
        return cls(
            val_updated_role_alias,
            val_updated_role_arn,
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
