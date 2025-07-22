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
    _names: dict[str, str] = {
        'inheriting_entity_id': 'inheriting_entity_id',
        'inheriting_entity_type': 'inheriting_entity_type',
        'policy_id': 'policy_id',
    }

    def __init__(
        self, inheriting_entity_id: str, inheriting_entity_type: str, policy_id: str
    ) -> None:
        """Constructor for the ProtectionInfo class."""

        # Initialize members of the class
        self.inheriting_entity_id: str = inheriting_entity_id
        self.inheriting_entity_type: str = inheriting_entity_type
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
        val = dictionary['inheriting_entity_id']
        val_inheriting_entity_id = val

        val = dictionary['inheriting_entity_type']
        val_inheriting_entity_type = val

        val = dictionary['policy_id']
        val_policy_id = val

        # Return an object of this model
        return cls(
            val_inheriting_entity_id,  # type: ignore
            val_inheriting_entity_type,  # type: ignore
            val_policy_id,  # type: ignore
        )
