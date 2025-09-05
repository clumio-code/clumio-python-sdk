#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EntityGroupAssignmentUpdatesV1')


@dataclasses.dataclass
class EntityGroupAssignmentUpdatesV1:
    """Implementation of the 'EntityGroupAssignmentUpdatesV1' model.

        Updates to the organizational unit assignments.

        Attributes:
            Add:
    The clumio-assigned ids of the organizational units to be assigned to the user.

            Remove:
    The clumio-assigned ids of the organizational units to be unassigned to the user.

    """

    Add: Sequence[str] | None = None
    Remove: Sequence[str] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val_add = val

        val = dictionary.get('remove', None)
        val_remove = val

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
