#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_server_side_encryption_rule as s3_server_side_encryption_rule_

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
    _names: dict[str, str] = {'rules': 'rules'}

    def __init__(
        self,
        rules: Sequence[s3_server_side_encryption_rule_.S3ServerSideEncryptionRule] | None = None,
    ) -> None:
        """Constructor for the S3ServerSideEncryptionConfiguration class."""

        # Initialize members of the class
        self.rules: Sequence[s3_server_side_encryption_rule_.S3ServerSideEncryptionRule] | None = (
            rules
        )

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
        val = dictionary.get('rules', None)

        val_rules = None
        if val:
            val_rules = list()
            for value in val:
                val_rules.append(
                    s3_server_side_encryption_rule_.S3ServerSideEncryptionRule.from_dictionary(
                        value
                    )
                )

        # Return an object of this model
        return cls(
            val_rules,
        )
