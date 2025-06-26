#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_model
from clumioapi.models import user_with_role

T = TypeVar('T', bound='CreateOrganizationalUnitV2Request')


class CreateOrganizationalUnitV2Request:
    """Implementation of the 'CreateOrganizationalUnitV2Request' model.

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
            List of user IDs, with role, to assign this organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'description': 'description',
        'entities': 'entities',
        'name': 'name',
        'parent_id': 'parent_id',
        'users': 'users',
    }

    def __init__(
        self,
        description: str = None,
        entities: Sequence[entity_model.EntityModel] = None,
        name: str = None,
        parent_id: str = None,
        users: Sequence[user_with_role.UserWithRole] = None,
    ) -> None:
        """Constructor for the CreateOrganizationalUnitV2Request class."""

        # Initialize members of the class
        self.description: str = description
        self.entities: Sequence[entity_model.EntityModel] = entities
        self.name: str = name
        self.parent_id: str = parent_id
        self.users: Sequence[user_with_role.UserWithRole] = users

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
        description = dictionary.get('description')
        entities = None
        if dictionary.get('entities'):
            entities = list()
            for value in dictionary.get('entities'):
                entities.append(entity_model.EntityModel.from_dictionary(value))

        name = dictionary.get('name')
        parent_id = dictionary.get('parent_id')
        users = None
        if dictionary.get('users'):
            users = list()
            for value in dictionary.get('users'):
                users.append(user_with_role.UserWithRole.from_dictionary(value))

        # Return an object of this model
        return cls(description, entities, name, parent_id, users)
