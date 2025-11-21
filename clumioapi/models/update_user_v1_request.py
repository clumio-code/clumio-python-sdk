#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    entity_group_assignment_updates_v1 as entity_group_assignment_updates_v1_
import requests

T = TypeVar('T', bound='UpdateUserV1Request')


@dataclasses.dataclass
class UpdateUserV1Request:
    """Implementation of the 'UpdateUserV1Request' model.

    Attributes:
        AssignedRole:
            Updates the role assigned to the user.
            the available roles can be retrieved via the [get /roles](#operation/list-roles)
            api.

        FullName:
            The full name of the user that is to replace the existing full name.
            for example, enter the user's first name and last name.

        IsEnabled:
            If `true`, enables a user who has been disabled from clumio,
            returning the user to its previous "activated" or "invited" status. if `false`,
            disables a user from clumio.
            the user will not be able log in to clumio until another clumio user re-enables
            the account.

        OrganizationalUnitAssignmentUpdates:
            Updates to the organizational unit assignments.

    """

    AssignedRole: str | None = None
    FullName: str | None = None
    IsEnabled: bool | None = None
    OrganizationalUnitAssignmentUpdates: (
        entity_group_assignment_updates_v1_.EntityGroupAssignmentUpdatesV1 | None
    ) = None

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

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        val = dictionary.get('organizational_unit_assignment_updates', None)
        val_organizational_unit_assignment_updates = (
            entity_group_assignment_updates_v1_.EntityGroupAssignmentUpdatesV1.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_assigned_role,
            val_full_name,
            val_is_enabled,
            val_organizational_unit_assignment_updates,
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
