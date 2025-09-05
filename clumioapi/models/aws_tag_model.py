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

    def __init__(
        self,
        p_id: str | None = None,
        key: str | None = None,
        key_id: str | None = None,
        value: str | None = None,
    ) -> None:
        """Constructor for the AwsTagModel class."""

        # Initialize members of the class
        self.p_id: str | None = p_id
        self.key: str | None = key
        self.key_id: str | None = key_id
        self.value: str | None = value

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
        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('key', None)
        val_key = val

        val = dictionary.get('key_id', None)
        val_key_id = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_p_id,
            val_key,
            val_key_id,
            val_value,
        )
