#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_model

T = TypeVar('T', bound='UserEmbedded')


class UserEmbedded:
    """Implementation of the 'UserEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_role:
            Embeds the associated Role details in the response
    """

    # Create a mapping from Model property names to API property names
    _names = {'read_role': 'read-role'}

    def __init__(self, read_role: Sequence[role_model.RoleModel] = None) -> None:
        """Constructor for the UserEmbedded class."""

        # Initialize members of the class
        self.read_role: Sequence[role_model.RoleModel] = read_role

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
        read_role = None
        if dictionary.get('read-role'):
            read_role = list()
            for value in dictionary.get('read-role'):
                read_role.append(role_model.RoleModel.from_dictionary(value))

        # Return an object of this model
        return cls(read_role)
