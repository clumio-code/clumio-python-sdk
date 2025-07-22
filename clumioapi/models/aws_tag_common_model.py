#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AwsTagCommonModel')


class AwsTagCommonModel:
    """Implementation of the 'AwsTagCommonModel' model.

    A tag created through AWS Console which can be applied to EBS volumes.

    Attributes:
        key:
            The AWS-assigned tag key.
        value:
            The AWS-assigned tag value.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'key': 'key', 'value': 'value'}

    def __init__(self, key: str, value: str) -> None:
        """Constructor for the AwsTagCommonModel class."""

        # Initialize members of the class
        self.key: str = key
        self.value: str = value

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
        val = dictionary['key']
        val_key = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_key,  # type: ignore
            val_value,  # type: ignore
        )
