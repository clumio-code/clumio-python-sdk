#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import update_entities as update_entities_
from clumioapi.models import update_user_assignments as update_user_assignments_
import requests

T = TypeVar('T', bound='PatchOrganizationalUnitV1Request')


@dataclasses.dataclass
class PatchOrganizationalUnitV1Request:
    """Implementation of the 'PatchOrganizationalUnitV1Request' model.

    Attributes:
        Description:
            A description of the organizational unit.

        Entities:
            Updates to the entities in the organizational unit.
            adding or removing entities from the ou is an asynchronous operation.
            the response has a task id which can be used to track the progress of the
            operation.

        Name:
            Unique name assigned to the organizational unit.

        Users:
            Updates to the user assignments.

    """

    Description: str | None = None
    Entities: update_entities_.UpdateEntities | None = None
    Name: str | None = None
    Users: update_user_assignments_.UpdateUserAssignments | None = None

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('entities', None)
        val_entities = update_entities_.UpdateEntities.from_dictionary(val)

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('users', None)
        val_users = update_user_assignments_.UpdateUserAssignments.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_description,
            val_entities,
            val_name,
            val_users,
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
