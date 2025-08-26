#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import permission_model as permission_model_
from clumioapi.models import role_links as role_links_
import requests

T = TypeVar('T', bound='ReadRoleResponse')


@dataclasses.dataclass
class ReadRoleResponse:
    """Implementation of the 'ReadRoleResponse' model.

    Attributes:
        Etag:
            Etag value.

        Links:
            Urls to pages related to the resource.

        Description:
            A description of the role.

        Id:
            The clumio-assigned id of the role.

        Name:
            Unique name assigned to the role.

        Permissions:
            Permissions contained in the role.

        UserCount:
            Number of users to whom the role has been assigned.

    """

    Etag: str | None = None
    Links: role_links_.RoleLinks | None = None
    Description: str | None = None
    Id: str | None = None
    Name: str | None = None
    Permissions: Sequence[permission_model_.PermissionModel] | None = None
    UserCount: int | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = role_links_.RoleLinks.from_dictionary(val)

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('permissions', None)

        val_permissions = []
        if val:
            for value in val:
                val_permissions.append(permission_model_.PermissionModel.from_dictionary(value))

        val = dictionary.get('user_count', None)
        val_user_count = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_description,
            val_id,
            val_name,
            val_permissions,
            val_user_count,
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
        model_instance.raw_response = response
        return model_instance
