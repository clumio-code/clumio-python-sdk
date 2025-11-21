#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replication_rule_and_operator as s3_replication_rule_and_operator_
from clumioapi.models import s3_tag as s3_tag_
import requests

T = TypeVar('T', bound='S3ReplicationRuleFilter')


@dataclasses.dataclass
class S3ReplicationRuleFilter:
    """Implementation of the 'S3ReplicationRuleFilter' model.

    A filter that identifies the subset of objectsto which the replication rule
    applies.

    Attributes:
        And:
            A container for specifying rule filters. the filters
            determine the subset of objects to which the rule applies.

        Prefix:
            An object key name prefix that identifies the
            subset of objects to which the rule applies.

        Tag:
            A container of a key value name pair.

    """

    And: s3_replication_rule_and_operator_.S3ReplicationRuleAndOperator | None = None
    Prefix: str | None = None
    Tag: s3_tag_.S3Tag | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('and', None)
        val_and = s3_replication_rule_and_operator_.S3ReplicationRuleAndOperator.from_dictionary(
            val
        )

        val = dictionary.get('prefix', None)
        val_prefix = val

        val = dictionary.get('tag', None)
        val_tag = s3_tag_.S3Tag.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_and,
            val_prefix,
            val_tag,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
