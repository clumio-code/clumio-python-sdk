#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AssignPolicyAction')


class AssignPolicyAction:
    """Implementation of the 'AssignPolicyAction' model.

    Apply a policy to assets.

    Attributes:
        policy_id:
            The policy to be applied to the assets.
    """

    # Create a mapping from Model property names to API property names
    _names = {'policy_id': 'policy_id'}

    def __init__(self, policy_id: str = None) -> None:
        """Constructor for the AssignPolicyAction class."""

        # Initialize members of the class
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
        policy_id = dictionary.get('policy_id')
        # Return an object of this model
        return cls(policy_id)
