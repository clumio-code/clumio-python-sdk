#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assignment_entity as assignment_entity_

T = TypeVar('T', bound='AssignmentInputModel')


class AssignmentInputModel:
    """Implementation of the 'AssignmentInputModel' model.

    The portion of the policy assignment used for updates/creations

    Attributes:
        action:
            The action to be executed by this request.
            Possible values include "assign" and "unassign".
        entity:
            An entity being assigned or unassigned a policy.
        policy_id:
            The Clumio-assigned ID of the policy to be applied to the requested entities.
            If `action: assign`, then this parameter is required.
            Otherwise, it must not be provided.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'action': 'action', 'entity': 'entity', 'policy_id': 'policy_id'}

    def __init__(
        self,
        action: str | None = None,
        entity: assignment_entity_.AssignmentEntity | None = None,
        policy_id: str | None = None,
    ) -> None:
        """Constructor for the AssignmentInputModel class."""

        # Initialize members of the class
        self.action: str | None = action
        self.entity: assignment_entity_.AssignmentEntity | None = entity
        self.policy_id: str | None = policy_id

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
