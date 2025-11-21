#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import role_for_organizational_units as role_for_organizational_units_
import requests

T = TypeVar('T', bound='CreateUserV2Request')


@dataclasses.dataclass
class CreateUserV2Request:
    """Implementation of the 'CreateUserV2Request' model.

    Attributes:
        AccessControlConfiguration:
            List of clumio-assigned ids of the organizational units along with the clumio-
            assigned id of the role
            to assign to the user.

        Email:
            The email address of the user to be added to clumio.

        FullName:
            The full name of the user to be added to clumio. for example, type the user's
            first name and last name.
            the name displays on the user management screen and in the body of the email
            invitation.

    """

    AccessControlConfiguration: (
        Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None
    ) = None
    Email: str | None = None
    FullName: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('access_control_configuration', None)

        val_access_control_configuration = []
        if val:
            for value in val:
                val_access_control_configuration.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        val = dictionary.get('email', None)
        val_email = val

        val = dictionary.get('full_name', None)
        val_full_name = val

        # Return an object of this model
        return cls(
            val_access_control_configuration,
            val_email,
            val_full_name,
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
        return model_instance
