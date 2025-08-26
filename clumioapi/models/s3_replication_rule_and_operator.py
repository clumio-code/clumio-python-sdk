#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_tag as s3_tag_

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
    _names: dict[str, str] = {'prefix': 'prefix', 'tags': 'tags'}

    def __init__(
        self, prefix: str | None = None, tags: Sequence[s3_tag_.S3Tag] | None = None
    ) -> None:
        """Constructor for the S3ReplicationRuleAndOperator class."""

        # Initialize members of the class
        self.prefix: str | None = prefix
        self.tags: Sequence[s3_tag_.S3Tag] | None = tags

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
        val = dictionary.get('prefix', None)
        val_prefix = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(s3_tag_.S3Tag.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_prefix,
            val_tags,
        )
