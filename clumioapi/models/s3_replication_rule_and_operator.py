#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_tag

T = TypeVar('T', bound='S3ReplicationRuleAndOperator')


class S3ReplicationRuleAndOperator:
    """Implementation of the 'S3ReplicationRuleAndOperator' model.

    A container for specifying rule filters. The filtersdetermine the subset of
    objects to which the rule applies.

    Attributes:
        prefix:
            An object key name prefix that identifies
            the subset of objects to which the rule applies.
        tags:
            An array of tags containing key and value pairs.
    """

    # Create a mapping from Model property names to API property names
    _names = {'prefix': 'prefix', 'tags': 'tags'}

    def __init__(self, prefix: str = None, tags: Sequence[s3_tag.S3Tag] = None) -> None:
        """Constructor for the S3ReplicationRuleAndOperator class."""

        # Initialize members of the class
        self.prefix: str = prefix
        self.tags: Sequence[s3_tag.S3Tag] = tags

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
        prefix = dictionary.get('prefix')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(s3_tag.S3Tag.from_dictionary(value))

        # Return an object of this model
        return cls(prefix, tags)
