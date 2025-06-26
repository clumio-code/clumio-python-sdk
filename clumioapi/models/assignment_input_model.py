#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assignment_entity

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
    _names = {'action': 'action', 'entity': 'entity', 'policy_id': 'policy_id'}

    def __init__(
        self,
        action: str = None,
        entity: assignment_entity.AssignmentEntity = None,
        policy_id: str = None,
    ) -> None:
        """Constructor for the AssignmentInputModel class."""

        # Initialize members of the class
        self.action: str = action
        self.entity: assignment_entity.AssignmentEntity = entity
        self.policy_id: str = policy_id

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
        action = dictionary.get('action')
        key = 'entity'
        entity = (
            assignment_entity.AssignmentEntity.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        policy_id = dictionary.get('policy_id')
        # Return an object of this model
        return cls(action, entity, policy_id)
