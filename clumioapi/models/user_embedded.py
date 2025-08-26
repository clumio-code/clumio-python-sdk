#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import role_model as role_model_
import requests

T = TypeVar('T', bound='UserEmbedded')


@dataclasses.dataclass
class UserEmbedded:
    """Implementation of the 'UserEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        ReadRole:
            Embeds the associated role details in the response.

    """

    ReadRole: Sequence[role_model_.RoleModel] | None = None

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
        val = dictionary.get('read-role', None)

        val_read_role = []
        if val:
            for value in val:
                val_read_role.append(role_model_.RoleModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_read_role,
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
