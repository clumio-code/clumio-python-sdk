#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UserWithRole')


class UserWithRole:
    """Implementation of the 'UserWithRole' model.

    A user along with a role.

    Attributes:
        assigned_role:
            The Clumio-assigned ID of the role to be assigned to the user.
        user_id:
            The ID of the user.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'assigned_role': 'assigned_role', 'user_id': 'user_id'}

    def __init__(self, assigned_role: str, user_id: str) -> None:
        """Constructor for the UserWithRole class."""

        # Initialize members of the class
        self.assigned_role: str = assigned_role
        self.user_id: str = user_id

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
        val = dictionary['assigned_role']
        val_assigned_role = val

        val = dictionary['user_id']
        val_user_id = val

        # Return an object of this model
        return cls(
            val_assigned_role,  # type: ignore
            val_user_id,  # type: ignore
        )
