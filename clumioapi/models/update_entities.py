#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import entity_model as entity_model_
import requests

T = TypeVar('T', bound='UpdateEntities')


@dataclasses.dataclass
class UpdateEntities:
    """Implementation of the 'UpdateEntities' model.

    Updates to the entities in the organizational unit.Adding or removing entities
    from the OU is an asynchronous operation.The response has a task ID which can be
    used to track the progress of the operation.

    Attributes:
        Add:
            List of entities to add to the organizational unit.

        Remove:
            List of entities to remove from the organizational unit.

    """

    Add: Sequence[entity_model_.EntityModel] | None = None
    Remove: Sequence[entity_model_.EntityModel] | None = None

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
                val_add.append(entity_model_.EntityModel.from_dictionary(value))

        val = dictionary.get('remove', None)

        val_remove = []
        if val:
            for value in val:
                val_remove.append(entity_model_.EntityModel.from_dictionary(value))

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
