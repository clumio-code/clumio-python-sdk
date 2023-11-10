#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_for_organizational_units

T = TypeVar('T', bound='CreateUserV2Request')


class CreateUserV2Request:
    """Implementation of the 'CreateUserV2Request' model.

    Attributes:
        access_control_configuration:
            List of Clumio-assigned IDs of the organizational units along with the Clumio-
            assigned ID of the role
            to assign to the user.
        email:
            The email address of the user to be added to Clumio.
        full_name:
            The full name of the user to be added to Clumio. For example, type the user's
            first name and last name.
            The name displays on the User Management screen and in the body of the email
            invitation.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'access_control_configuration': 'access_control_configuration',
        'email': 'email',
        'full_name': 'full_name',
    }

    def __init__(
        self,
        access_control_configuration: Sequence[
            role_for_organizational_units.RoleForOrganizationalUnits
        ] = None,
        email: str = None,
        full_name: str = None,
    ) -> None:
        """Constructor for the CreateUserV2Request class."""

        # Initialize members of the class
        self.access_control_configuration: Sequence[
            role_for_organizational_units.RoleForOrganizationalUnits
        ] = access_control_configuration
        self.email: str = email
        self.full_name: str = full_name

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
        access_control_configuration = None
        if dictionary.get('access_control_configuration'):
            access_control_configuration = list()
            for value in dictionary.get('access_control_configuration'):
                access_control_configuration.append(
                    role_for_organizational_units.RoleForOrganizationalUnits.from_dictionary(value)
                )

        email = dictionary.get('email')
        full_name = dictionary.get('full_name')
        # Return an object of this model
        return cls(access_control_configuration, email, full_name)
