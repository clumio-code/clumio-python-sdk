#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SSESpecification')


class SSESpecification:
    """Implementation of the 'SSESpecification' model.

    Represents the server-side encryption settings for a table.

    Attributes:
        kms_key_type:
            The server-side encryption KMS key type.
            This field will only be populated for [GET /datasources/aws/dynamodb-
            tables/{table_id}](#operation/read-aws-dynamodb-table)
            and [GET /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-
            dynamodb-table).
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table),
            `kms_master_key_id` must be specified
            in case of CUSTOMER_MANAGED. Possible values include: DEFAULT, AWS_MANAGED,
            CUSTOMER_MANAGED.
        kms_master_key_id:
            The AWS KMS customer master key (CMK) ARN that is used to encrypt the table.
            If this field is `null`, server-side encryption is the default encryption (AWS
            owned CMK).
            Otherwise, an AWS-managed or customer-managed CMK exists having these values.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), use
            key ID, Amazon Resource
            Name (ARN), alias name or alias ARN to specify a key to be used for encrypting
            the restored table.
            In case of default encryption (AWS owned CMK), specify this as `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {'kms_key_type': 'kms_key_type', 'kms_master_key_id': 'kms_master_key_id'}

    def __init__(self, kms_key_type: str = None, kms_master_key_id: str = None) -> None:
        """Constructor for the SSESpecification class."""

        # Initialize members of the class
        self.kms_key_type: str = kms_key_type
        self.kms_master_key_id: str = kms_master_key_id

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
        kms_key_type = dictionary.get('kms_key_type')
        kms_master_key_id = dictionary.get('kms_master_key_id')
        # Return an object of this model
        return cls(kms_key_type, kms_master_key_id)
