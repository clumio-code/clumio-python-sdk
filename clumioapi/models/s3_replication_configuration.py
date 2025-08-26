#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replication_rule as s3_replication_rule_
import requests

T = TypeVar('T', bound='S3ReplicationConfiguration')


@dataclasses.dataclass
class S3ReplicationConfiguration:
    """Implementation of the 'S3ReplicationConfiguration' model.

        A container for replication rules with a maximum sizeof 2MB and a maximum of
        1,000 rules.

        Attributes:
            Role:
                The amazon resource name (arn) of the aws identity and access management (iam)
    role that amazon s3 assumes when replicating objects.

            Rules:
                Specifies which amazon s3 objects to replicate and where to store the replicas.

    """

    Role: str | None = None
    Rules: Sequence[s3_replication_rule_.S3ReplicationRule] | None = None

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
        val = dictionary.get('role', None)
        val_role = val

        val = dictionary.get('rules', None)

        val_rules = []
        if val:
            for value in val:
                val_rules.append(s3_replication_rule_.S3ReplicationRule.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_role,
            val_rules,
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
