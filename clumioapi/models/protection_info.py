#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionInfo')


class ProtectionInfo:
    """Implementation of the 'ProtectionInfo' model.

    The protection policy applied to this resource. If the resource is not
    protected, then this field has a value of `null`.

    Attributes:
        inheriting_entity_id:
            The ID of the entity from which protection was inherited.
            If protection was not inherited, then this field has a value of `null`.
        inheriting_entity_type:
            The type of entity from which protection was inherited.
            If protection was not inherited, then this field has a value of `null`.
            Entities from which protection can be inherited include the following:

            +------------------------+----------+
            | Inheriting Entity Type | Details  |
            +========================+==========+
            | aws_tag                | AWS tag. |
            +------------------------+----------+
        policy_id:
            A system-generated ID assigned to the policy protecting this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'inheriting_entity_id': 'inheriting_entity_id',
        'inheriting_entity_type': 'inheriting_entity_type',
        'policy_id': 'policy_id',
    }

    def __init__(
        self,
        inheriting_entity_id: str = None,
        inheriting_entity_type: str = None,
        policy_id: str = None,
    ) -> None:
        """Constructor for the ProtectionInfo class."""

        # Initialize members of the class
        self.inheriting_entity_id: str = inheriting_entity_id
        self.inheriting_entity_type: str = inheriting_entity_type
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
        inheriting_entity_id = dictionary.get('inheriting_entity_id')
        inheriting_entity_type = dictionary.get('inheriting_entity_type')
        policy_id = dictionary.get('policy_id')
        # Return an object of this model
        return cls(inheriting_entity_id, inheriting_entity_type, policy_id)
