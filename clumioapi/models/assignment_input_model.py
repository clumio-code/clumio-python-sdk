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
        self, action: str, entity: assignment_entity_.AssignmentEntity, policy_id: str
    ) -> None:
        """Constructor for the AssignmentInputModel class."""

        # Initialize members of the class
        self.action: str = action
        self.entity: assignment_entity_.AssignmentEntity = entity
        self.policy_id: str = policy_id

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
        val = dictionary['action']
        val_action = val

        val = dictionary['entity']
        val_entity = assignment_entity_.AssignmentEntity.from_dictionary(val)

        val = dictionary['policy_id']
        val_policy_id = val

        # Return an object of this model
        return cls(
            val_action,  # type: ignore
            val_entity,  # type: ignore
            val_policy_id,  # type: ignore
        )
