#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_model as entity_model_

T = TypeVar('T', bound='CreateOrganizationalUnitV1Request')


class CreateOrganizationalUnitV1Request:
    """Implementation of the 'CreateOrganizationalUnitV1Request' model.

    Attributes:
        description:
            A description of the organizational unit.
        entities:
            List of entities to add to the organizational unit. Adding entities to the OU is
            an asynchronous operation.
            The response will has a task ID, which can be used to track the progress of the
            operation.
        name:
            Unique name assigned to the organizational unit.
        parent_id:
            The Clumio-assigned ID of the parent organizational unit under which the new
            organizational unit is to be created.
            If absent, the new organizational unit is created under the current
            organizational unit.
        users:
            List of user IDs to assign this organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'entities': 'entities',
        'name': 'name',
        'parent_id': 'parent_id',
        'users': 'users',
    }

    def __init__(
        self,
        description: str,
        entities: Sequence[entity_model_.EntityModel],
        name: str,
        parent_id: str,
        users: Sequence[str],
    ) -> None:
        """Constructor for the CreateOrganizationalUnitV1Request class."""

        # Initialize members of the class
        self.description: str = description
        self.entities: Sequence[entity_model_.EntityModel] = entities
        self.name: str = name
        self.parent_id: str = parent_id
        self.users: Sequence[str] = users

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
        val = dictionary['description']
        val_description = val

        val = dictionary['entities']

        val_entities = None
        if val:
            val_entities = list()
            for value in val:
                val_entities.append(entity_model_.EntityModel.from_dictionary(value))

        val = dictionary['name']
        val_name = val

        val = dictionary['parent_id']
        val_parent_id = val

        val = dictionary['users']
        val_users = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_entities,  # type: ignore
            val_name,  # type: ignore
            val_parent_id,  # type: ignore
            val_users,  # type: ignore
        )
