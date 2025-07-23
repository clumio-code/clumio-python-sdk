#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_model as entity_model_

T = TypeVar('T', bound='UpdateEntities')


class UpdateEntities:
    """Implementation of the 'UpdateEntities' model.

    Updates to the entities in the organizational unit.Adding or removing entities
    from the OU is an asynchronous operation.The response has a task ID which can be
    used to track the progress of the operation.

    Attributes:
        add:
            List of entities to add to the organizational unit.
        remove:
            List of entities to remove from the organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[entity_model_.EntityModel] | None = None,
        remove: Sequence[entity_model_.EntityModel] | None = None,
    ) -> None:
        """Constructor for the UpdateEntities class."""

        # Initialize members of the class
        self.add: Sequence[entity_model_.EntityModel] | None = add
        self.remove: Sequence[entity_model_.EntityModel] | None = remove

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('add', None)

        val_add = None
        if val:
            val_add = list()
            for value in val:
                val_add.append(entity_model_.EntityModel.from_dictionary(value))

        val = dictionary.get('remove', None)

        val_remove = None
        if val:
            val_remove = list()
            for value in val:
                val_remove.append(entity_model_.EntityModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_add,
            val_remove,
        )
