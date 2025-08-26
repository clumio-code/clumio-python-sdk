#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import assignment_entity as assignment_entity_
import requests

T = TypeVar('T', bound='AssignmentInputModel')


@dataclasses.dataclass
class AssignmentInputModel:
    """Implementation of the 'AssignmentInputModel' model.

        The portion of the policy assignment used for updates/creations

        Attributes:
            Action:
                The action to be executed by this request.
    possible values include "assign" and "unassign".

            Entity:
                An entity being assigned or unassigned a policy.

            PolicyId:
                Assign`, then this parameter is required.
    otherwise, it must not be provided.

    """

    Action: str | None = None
    Entity: assignment_entity_.AssignmentEntity | None = None
    PolicyId: str | None = None

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
        val = dictionary.get('action', None)
        val_action = val

        val = dictionary.get('entity', None)
        val_entity = assignment_entity_.AssignmentEntity.from_dictionary(val)

        val = dictionary.get('policy_id', None)
        val_policy_id = val

        # Return an object of this model
        return cls(
            val_action,
            val_entity,
            val_policy_id,
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
