#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import permission_model as permission_model_

T = TypeVar('T', bound='RoleModel')


class RoleModel:
    """Implementation of the 'RoleModel' model.

    RoleModel denotes the Model for Role

    Attributes:
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
        'description': 'description',
        'p_id': 'id',
        'name': 'name',
        'permissions': 'permissions',
        'user_count': 'user_count',
    }

    def __init__(
        self,
        description: str,
        p_id: str,
        name: str,
        permissions: Sequence[permission_model_.PermissionModel],
        user_count: int,
    ) -> None:
        """Constructor for the RoleModel class."""

        # Initialize members of the class
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name
        self.permissions: Sequence[permission_model_.PermissionModel] = permissions
        self.user_count: int = user_count

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
        val = dictionary['description']
        val_description = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['permissions']

        val_permissions = None
        if val:
            val_permissions = list()
            for value in val:
                val_permissions.append(permission_model_.PermissionModel.from_dictionary(value))

        val = dictionary['user_count']
        val_user_count = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_permissions,  # type: ignore
            val_user_count,  # type: ignore
        )
