#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'asset_count': 'asset_count', 'policy_count': 'policy_count'}

    def __init__(self, asset_count: int, policy_count: int) -> None:
        """Constructor for the ItemsCovered class."""

        # Initialize members of the class
        self.asset_count: int = asset_count
        self.policy_count: int = policy_count

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
        val = dictionary['asset_count']
        val_asset_count = val

        val = dictionary['policy_count']
        val_policy_count = val

        # Return an object of this model
        return cls(
            val_asset_count,  # type: ignore
            val_policy_count,  # type: ignore
        )
