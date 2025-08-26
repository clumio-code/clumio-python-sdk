#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import role_for_organizational_units as role_for_organizational_units_
import requests

T = TypeVar('T', bound='EntityGroupAssignmentUpdates')


@dataclasses.dataclass
class EntityGroupAssignmentUpdates:
    """Implementation of the 'EntityGroupAssignmentUpdates' model.

        Updates to the organizational units along with the role assigned to the user.

        Attributes:
            Add:
                The clumio-assigned ids of the organizational units, with the clumio-assigned id of the role
    to be assigned to the user.

            Remove:
                The clumio-assigned ids of the organizational units, with the clumio-assigned id of the role
    to be unassigned to the user.

    """

    Add: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = None
    Remove: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('add', None)

        val_add = []
        if val:
            for value in val:
                val_add.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        val = dictionary.get('remove', None)

        val_remove = []
        if val:
            for value in val:
                val_remove.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_add,
            val_remove,
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
