#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AssetProtectionControl')


class AssetProtectionControl:
    """Implementation of the 'AssetProtectionControl' model.

    The control for asset protection.

    Attributes:
        should_ignore_deactivated_policy:
            Whether the report should ignore deactivated policy or not.
    """

    # Create a mapping from Model property names to API property names
    _names = {'should_ignore_deactivated_policy': 'should_ignore_deactivated_policy'}

    def __init__(self, should_ignore_deactivated_policy: bool = None) -> None:
        """Constructor for the AssetProtectionControl class."""

        # Initialize members of the class
        self.should_ignore_deactivated_policy: bool = should_ignore_deactivated_policy

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
        should_ignore_deactivated_policy = dictionary.get('should_ignore_deactivated_policy')
        # Return an object of this model
        return cls(should_ignore_deactivated_policy)
