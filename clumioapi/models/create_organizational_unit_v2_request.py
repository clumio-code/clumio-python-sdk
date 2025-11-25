#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import entity_model as entity_model_
from clumioapi.models import user_with_role as user_with_role_
import requests

T = TypeVar('T', bound='CreateOrganizationalUnitV2Request')


@dataclasses.dataclass
class CreateOrganizationalUnitV2Request:
    """Implementation of the 'CreateOrganizationalUnitV2Request' model.

    Attributes:
        Description:
            A description of the organizational unit.

        Entities:
            List of entities to add to the organizational unit. adding entities to the ou is
            an asynchronous operation.
            the response will has a task id, which can be used to track the progress of the
            operation.

        Name:
            Unique name assigned to the organizational unit.

        ParentId:
            The clumio-assigned id of the parent organizational unit under which the new
            organizational unit is to be created.
            if absent, the new organizational unit is created under the current
            organizational unit.

        Users:
            List of user ids, with role, to assign this organizational unit.

    """

    Description: str | None = None
    Entities: Sequence[entity_model_.EntityModel] | None = None
    Name: str | None = None
    ParentId: str | None = None
    Users: Sequence[user_with_role_.UserWithRole] | None = None

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

        val_entities = []
        if val:
            for value in val:
                val_entities.append(entity_model_.EntityModel.from_dictionary(value))

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('parent_id', None)
        val_parent_id = val

        val = dictionary.get('users', None)

        val_users = []
        if val:
            for value in val:
                val_users.append(user_with_role_.UserWithRole.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_description,
            val_entities,
            val_name,
            val_parent_id,
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
