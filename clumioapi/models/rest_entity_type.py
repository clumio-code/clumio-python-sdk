#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RestEntityType')


class RestEntityType:
    """Implementation of the 'RestEntityType' model.

    Type is mostly an asset type or the type of Entity. Some examples
    are"restored_file", "aws_ebs_volume",  etc.

    Attributes:
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {}

    def __init__(
        self,
    ) -> None:
        """Constructor for the RestEntityType class."""

        # Initialize members of the class

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

        # Return an object of this model
        return cls()
