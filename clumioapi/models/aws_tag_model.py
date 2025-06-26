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
    _names = {'p_id': 'id', 'key': 'key', 'key_id': 'key_id', 'value': 'value'}

    def __init__(
        self, p_id: str = None, key: str = None, key_id: str = None, value: str = None
    ) -> None:
        """Constructor for the AwsTagModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.key: str = key
        self.key_id: str = key_id
        self.value: str = value

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
        p_id = dictionary.get('id')
        key = dictionary.get('key')
        key_id = dictionary.get('key_id')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(p_id, key, key_id, value)
