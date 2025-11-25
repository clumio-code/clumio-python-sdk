#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CreateUserV1Request')


@dataclasses.dataclass
class CreateUserV1Request:
    """Implementation of the 'CreateUserV1Request' model.

    Attributes:
        AssignedRole:
            The clumio-assigned id of the role to assign to the user.
            the available roles can be retrieved via the [get /roles](#operation/list-roles)
            api.
            when not set, the role is determined as follows

            +-------------+---------------------------+----------------+
            |   inviter   |       assigned ous        | resulting role |
            +=============+===========================+================+
            | super admin | global ou is assigned     | super admin    |
            +-------------+---------------------------+----------------+
            | super admin | global ou is not assigned | ou admin       |
            +-------------+---------------------------+----------------+
            | ou admin    | any                       | ou admin       |
            +-------------+---------------------------+----------------+

        Email:
            The email address of the user to be added to clumio.

        FullName:
            The full name of the user to be added to clumio. for example, type the user's
            first name and last name.
            the name displays on the user management screen and in the body of the email
            invitation.

        OrganizationalUnitIds:
            The clumio-assigned ids of the organizational units to be assigned to the user.

    """

    AssignedRole: str | None = None
    Email: str | None = None
    FullName: str | None = None
    OrganizationalUnitIds: Sequence[str] | None = None

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
        val = dictionary.get('assigned_role', None)
        val_assigned_role = val

        val = dictionary.get('email', None)
        val_email = val

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('organizational_unit_ids', None)
        val_organizational_unit_ids = val

        # Return an object of this model
        return cls(
            val_assigned_role,
            val_email,
            val_full_name,
            val_organizational_unit_ids,
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
