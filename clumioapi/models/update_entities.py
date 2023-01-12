#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_model

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
    _names = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[entity_model.EntityModel] = None,
        remove: Sequence[entity_model.EntityModel] = None,
    ) -> None:
        """Constructor for the UpdateEntities class."""

        # Initialize members of the class
        self.add: Sequence[entity_model.EntityModel] = add
        self.remove: Sequence[entity_model.EntityModel] = remove

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
        add = None
        if dictionary.get('add'):
            add = list()
            for value in dictionary.get('add'):
                add.append(entity_model.EntityModel.from_dictionary(value))

        remove = None
        if dictionary.get('remove'):
            remove = list()
            for value in dictionary.get('remove'):
                remove.append(entity_model.EntityModel.from_dictionary(value))

        # Return an object of this model
        return cls(add, remove)
