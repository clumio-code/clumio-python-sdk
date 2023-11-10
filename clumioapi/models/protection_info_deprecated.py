#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import inherited_from

T = TypeVar('T', bound='ProtectionInfoDeprecated')


class ProtectionInfoDeprecated:
    """Implementation of the 'ProtectionInfoDeprecated' model.

    Attributes:
        inheritedFrom:

        policyId:
            PolicyID for the policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {'inheritedFrom': 'inheritedFrom', 'policyId': 'policyId'}

    def __init__(
        self, inheritedFrom: inherited_from.InheritedFrom = None, policyId: str = None
    ) -> None:
        """Constructor for the ProtectionInfoDeprecated class."""

        # Initialize members of the class
        self.inheritedFrom: inherited_from.InheritedFrom = inheritedFrom
        self.policyId: str = policyId

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
        key = 'inheritedFrom'
        inheritedFrom = (
            inherited_from.InheritedFrom.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        policyId = dictionary.get('policyId')
        # Return an object of this model
        return cls(inheritedFrom, policyId)
