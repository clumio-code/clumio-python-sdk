#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import permission_model
from clumioapi.models import role_links

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
    _names = {
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
        etag: str = None,
        links: role_links.RoleLinks = None,
        description: str = None,
        p_id: str = None,
        name: str = None,
        permissions: Sequence[permission_model.PermissionModel] = None,
        user_count: int = None,
    ) -> None:
        """Constructor for the ReadRoleResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: role_links.RoleLinks = links
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name
        self.permissions: Sequence[permission_model.PermissionModel] = permissions
        self.user_count: int = user_count

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            role_links.RoleLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        description = dictionary.get('description')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        permissions = None
        if dictionary.get('permissions'):
            permissions = list()
            for value in dictionary.get('permissions'):
                permissions.append(permission_model.PermissionModel.from_dictionary(value))

        user_count = dictionary.get('user_count')
        # Return an object of this model
        return cls(etag, links, description, p_id, name, permissions, user_count)
