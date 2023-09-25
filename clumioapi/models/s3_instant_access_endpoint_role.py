#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3InstantAccessEndpointRole')


class S3InstantAccessEndpointRole:
    """Implementation of the 'S3InstantAccessEndpointRole' model.

    Attributes:
        alias:
            The alias of the IAM role given by the user in the UI.
        arn:
            The ARN of the IAM role.
        p_id:
            The ID of the IAM role. Used as an identifier in the API URL.
        last_modified_timestamp:
            The time when the role was last modified, in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'alias': 'alias',
        'arn': 'arn',
        'p_id': 'id',
        'last_modified_timestamp': 'last_modified_timestamp',
    }

    def __init__(
        self,
        alias: str = None,
        arn: str = None,
        p_id: str = None,
        last_modified_timestamp: str = None,
    ) -> None:
        """Constructor for the S3InstantAccessEndpointRole class."""

        # Initialize members of the class
        self.alias: str = alias
        self.arn: str = arn
        self.p_id: str = p_id
        self.last_modified_timestamp: str = last_modified_timestamp

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
        alias = dictionary.get('alias')
        arn = dictionary.get('arn')
        p_id = dictionary.get('id')
        last_modified_timestamp = dictionary.get('last_modified_timestamp')
        # Return an object of this model
        return cls(alias, arn, p_id, last_modified_timestamp)
