#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_rule

T = TypeVar('T', bound='S3ReplicationConfiguration')


class S3ReplicationConfiguration:
    """Implementation of the 'S3ReplicationConfiguration' model.

    A container for replication rules with a maximum sizeof 2MB and a maximum of
    1,000 rules.

    Attributes:
        role:
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM)
            role that Amazon S3 assumes when replicating objects.
        rules:
            Specifies which Amazon S3 objects to replicate and where to store the replicas.
    """

    # Create a mapping from Model property names to API property names
    _names = {'role': 'role', 'rules': 'rules'}

    def __init__(
        self, role: str = None, rules: Sequence[s3_replication_rule.S3ReplicationRule] = None
    ) -> None:
        """Constructor for the S3ReplicationConfiguration class."""

        # Initialize members of the class
        self.role: str = role
        self.rules: Sequence[s3_replication_rule.S3ReplicationRule] = rules

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
        role = dictionary.get('role')
        rules = None
        if dictionary.get('rules'):
            rules = list()
            for value in dictionary.get('rules'):
                rules.append(s3_replication_rule.S3ReplicationRule.from_dictionary(value))

        # Return an object of this model
        return cls(role, rules)
