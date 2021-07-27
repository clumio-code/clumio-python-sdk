#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateUserV1Request')


class CreateUserV1Request:
    """Implementation of the 'CreateUserV1Request' model.

    Attributes:
        email:
            The email address of the user to be added to Clumio.
        full_name:
            The full name of the user to be added to Clumio. For example, enter the user's
            first name and last name.
            The name appears in the User Management screen and in the body of the email
            invitation.
        organizational_unit_ids:
            The Clumio-assigned IDs of the organizational units to be assigned to the user.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'email': 'email',
        'full_name': 'full_name',
        'organizational_unit_ids': 'organizational_unit_ids',
    }

    def __init__(
        self,
        email: str = None,
        full_name: str = None,
        organizational_unit_ids: Sequence[str] = None,
    ) -> None:
        """Constructor for the CreateUserV1Request class."""

        # Initialize members of the class
        self.email: str = email
        self.full_name: str = full_name
        self.organizational_unit_ids: Sequence[str] = organizational_unit_ids

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
        email = dictionary.get('email')
        full_name = dictionary.get('full_name')
        organizational_unit_ids = dictionary.get('organizational_unit_ids')
        # Return an object of this model
        return cls(email, full_name, organizational_unit_ids)