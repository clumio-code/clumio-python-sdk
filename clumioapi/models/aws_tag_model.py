#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AwsTagModel')


class AwsTagModel:
    """Implementation of the 'AwsTagModel' model.

    A tag created through AWS console which can be applied to EBS volumes.

    Attributes:
        p_id:
            The Clumio-assigned ID of the AWS tag.
        key:
            The AWS-assigned tag key.
        key_id:
            The Clumio-assigned ID of the AWS key.
        value:
            The AWS-assigned tag value.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_id': 'id', 'key': 'key', 'key_id': 'key_id', 'value': 'value'}

    def __init__(self, p_id: str, key: str, key_id: str, value: str) -> None:
        """Constructor for the AwsTagModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.key: str = key
        self.key_id: str = key_id
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
        val = dictionary['id']
        val_p_id = val

        val = dictionary['key']
        val_key = val

        val = dictionary['key_id']
        val_key_id = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_key,  # type: ignore
            val_key_id,  # type: ignore
            val_value,  # type: ignore
        )
