#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_server_side_encryption_rule

T = TypeVar('T', bound='S3ServerSideEncryptionConfiguration')


class S3ServerSideEncryptionConfiguration:
    """Implementation of the 'S3ServerSideEncryptionConfiguration' model.

    Specifies the default server-side-encryption configuration.

    Attributes:
        rules:
            Container for information about a particular server-side encryption
            configuration rule.
    """

    # Create a mapping from Model property names to API property names
    _names = {'rules': 'rules'}

    def __init__(
        self, rules: Sequence[s3_server_side_encryption_rule.S3ServerSideEncryptionRule] = None
    ) -> None:
        """Constructor for the S3ServerSideEncryptionConfiguration class."""

        # Initialize members of the class
        self.rules: Sequence[s3_server_side_encryption_rule.S3ServerSideEncryptionRule] = rules

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
        rules = None
        if dictionary.get('rules'):
            rules = list()
            for value in dictionary.get('rules'):
                rules.append(
                    s3_server_side_encryption_rule.S3ServerSideEncryptionRule.from_dictionary(value)
                )

        # Return an object of this model
        return cls(rules)
