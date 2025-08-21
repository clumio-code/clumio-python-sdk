#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import permission_model as permission_model_
from clumioapi.models import role_links as role_links_

T = TypeVar('T', bound='ReadRoleResponse')


class ReadRoleResponse:
    """Implementation of the 'ReadRoleResponse' model.

    Attributes:
        etag:
            ETag value
        links:
            URLs to pages related to the resource.
        description:
            A description of the role.
        p_id:
            The Clumio-assigned ID of the role.
        name:
            Unique name assigned to the role.
        permissions:
            Permissions contained in the role.
        user_count:
            Number of users to whom the role has been assigned.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'etag': '_etag',
        'links': '_links',
        'description': 'description',
        'p_id': 'id',
        'name': 'name',
        'permissions': 'permissions',
        'user_count': 'user_count',
    }

    def __init__(
        self,
        etag: str | None = None,
        links: role_links_.RoleLinks | None = None,
        description: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        permissions: Sequence[permission_model_.PermissionModel] | None = None,
        user_count: int | None = None,
    ) -> None:
        """Constructor for the ReadRoleResponse class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: role_links_.RoleLinks | None = links
        self.description: str | None = description
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.permissions: Sequence[permission_model_.PermissionModel] | None = permissions
        self.user_count: int | None = user_count

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = role_links_.RoleLinks.from_dictionary(val)

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('permissions', None)

        val_permissions = None
        if val:
            val_permissions = list()
            for value in val:
                val_permissions.append(permission_model_.PermissionModel.from_dictionary(value))

        val = dictionary.get('user_count', None)
        val_user_count = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_description,
            val_p_id,
            val_name,
            val_permissions,
            val_user_count,
        )
