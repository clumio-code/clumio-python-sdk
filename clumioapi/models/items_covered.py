#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ItemsCovered')


class ItemsCovered:
    """Implementation of the 'ItemsCovered' model.

    The items covered in the compliance report created by the report run.

    Attributes:
        asset_count:
            The count of covered assets of the report run.
        policy_count:
            The count of covered policies of the report run.
    """

    # Create a mapping from Model property names to API property names
    _names = {'asset_count': 'asset_count', 'policy_count': 'policy_count'}

    def __init__(self, asset_count: int = None, policy_count: int = None) -> None:
        """Constructor for the ItemsCovered class."""

        # Initialize members of the class
        self.asset_count: int = asset_count
        self.policy_count: int = policy_count

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
        asset_count = dictionary.get('asset_count')
        policy_count = dictionary.get('policy_count')
        # Return an object of this model
        return cls(asset_count, policy_count)
