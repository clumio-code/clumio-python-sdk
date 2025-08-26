#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_tag as s3_tag_
import requests

T = TypeVar('T', bound='S3ReplicationRuleAndOperator')


@dataclasses.dataclass
class S3ReplicationRuleAndOperator:
    """Implementation of the 'S3ReplicationRuleAndOperator' model.

        A container for specifying rule filters. The filtersdetermine the subset of
        objects to which the rule applies.

        Attributes:
            Prefix:
                An object key name prefix that identifies
    the subset of objects to which the rule applies.

            Tags:
                An array of tags containing key and value pairs.

    """

    Prefix: str | None = None
    Tags: Sequence[s3_tag_.S3Tag] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(s3_tag_.S3Tag.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_prefix,
            val_tags,
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
