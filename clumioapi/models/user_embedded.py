#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_model as role_model_

T = TypeVar('T', bound='UserEmbedded')


class UserEmbedded:
    """Implementation of the 'UserEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_role:
            Embeds the associated Role details in the response
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'read_role': 'read-role'}

    def __init__(self, read_role: Sequence[role_model_.RoleModel]) -> None:
        """Constructor for the UserEmbedded class."""

        # Initialize members of the class
        self.read_role: Sequence[role_model_.RoleModel] = read_role

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
        val = dictionary['read-role']

        val_read_role = None
        if val:
            val_read_role = list()
            for value in val:
                val_read_role.append(role_model_.RoleModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_read_role,  # type: ignore
        )
