#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_rule_and_operator
from clumioapi.models import s3_tag

T = TypeVar('T', bound='S3ReplicationRuleFilter')


class S3ReplicationRuleFilter:
    """Implementation of the 'S3ReplicationRuleFilter' model.

    A filter that identifies the subset of objectsto which the replication rule
    applies.

    Attributes:
        p_and:
            A container for specifying rule filters. The filters
            determine the subset of objects to which the rule applies.
        prefix:
            An object key name prefix that identifies the
            subset of objects to which the rule applies.
        tag:
            A container of a key value name pair.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_and': 'and', 'prefix': 'prefix', 'tag': 'tag'}

    def __init__(
        self,
        p_and: s3_replication_rule_and_operator.S3ReplicationRuleAndOperator = None,
        prefix: str = None,
        tag: s3_tag.S3Tag = None,
    ) -> None:
        """Constructor for the S3ReplicationRuleFilter class."""

        # Initialize members of the class
        self.p_and: s3_replication_rule_and_operator.S3ReplicationRuleAndOperator = p_and
        self.prefix: str = prefix
        self.tag: s3_tag.S3Tag = tag

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
        key = 'and'
        p_and = (
            s3_replication_rule_and_operator.S3ReplicationRuleAndOperator.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        prefix = dictionary.get('prefix')
        key = 'tag'
        tag = s3_tag.S3Tag.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None

        # Return an object of this model
        return cls(p_and, prefix, tag)
