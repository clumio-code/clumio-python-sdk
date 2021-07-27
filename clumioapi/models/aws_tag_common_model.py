#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AwsTagCommonModel')


class AwsTagCommonModel:
    """Implementation of the 'AwsTagCommonModel' model.

    A tag created through AWS Console which can be applied to EBS volumes.

    Attributes:
        key:
            The AWS-assigned tag key.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag.
        value:
            The AWS-assigned tag value.
    """

    # Create a mapping from Model property names to API property names
    _names = {'key': 'key', 'organizational_unit_id': 'organizational_unit_id', 'value': 'value'}

    def __init__(
        self, key: str = None, organizational_unit_id: str = None, value: str = None
    ) -> None:
        """Constructor for the AwsTagCommonModel class."""

        # Initialize members of the class
        self.key: str = key
        self.organizational_unit_id: str = organizational_unit_id
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
        key = dictionary.get('key')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(key, organizational_unit_id, value)
