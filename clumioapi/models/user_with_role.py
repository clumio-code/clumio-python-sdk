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
    _names = {'assigned_role': 'assigned_role', 'user_id': 'user_id'}

    def __init__(self, assigned_role: str = None, user_id: str = None) -> None:
        """Constructor for the UserWithRole class."""

        # Initialize members of the class
        self.assigned_role: str = assigned_role
        self.user_id: str = user_id

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
        assigned_role = dictionary.get('assigned_role')
        user_id = dictionary.get('user_id')
        # Return an object of this model
        return cls(assigned_role, user_id)
