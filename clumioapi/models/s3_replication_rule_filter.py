#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_rule_and_operator as s3_replication_rule_and_operator_
from clumioapi.models import s3_tag as s3_tag_

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
    _names: dict[str, str] = {'p_and': 'and', 'prefix': 'prefix', 'tag': 'tag'}

    def __init__(
        self,
        p_and: s3_replication_rule_and_operator_.S3ReplicationRuleAndOperator,
        prefix: str,
        tag: s3_tag_.S3Tag,
    ) -> None:
        """Constructor for the S3ReplicationRuleFilter class."""

        # Initialize members of the class
        self.p_and: s3_replication_rule_and_operator_.S3ReplicationRuleAndOperator = p_and
        self.prefix: str = prefix
        self.tag: s3_tag_.S3Tag = tag

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
        val = dictionary['and']
        val_p_and = s3_replication_rule_and_operator_.S3ReplicationRuleAndOperator.from_dictionary(
            val
        )

        val = dictionary['prefix']
        val_prefix = val

        val = dictionary['tag']
        val_tag = s3_tag_.S3Tag.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_and,  # type: ignore
            val_prefix,  # type: ignore
            val_tag,  # type: ignore
        )
