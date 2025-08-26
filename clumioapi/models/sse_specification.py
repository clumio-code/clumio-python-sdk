#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='SSESpecification')


@dataclasses.dataclass
class SSESpecification:
    """Implementation of the 'SSESpecification' model.

        Represents the server-side encryption settings for a table.

        Attributes:
            KmsKeyType:
                Default, aws_managed, customer_managed.

            KmsMasterKeyId:
                The aws kms customer master key (cmk) arn that is used to encrypt the table.
    if this field is `null`, server-side encryption is the default encryption (aws owned cmk).
    otherwise, an aws-managed or customer-managed cmk exists having these values.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), use key id, amazon resource
    name (arn), alias name or alias arn to specify a key to be used for encrypting the restored table.
    in case of default encryption (aws owned cmk), specify this as `null`.

    """

    KmsKeyType: str | None = None
    KmsMasterKeyId: str | None = None

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
        val = dictionary.get('kms_key_type', None)
        val_kms_key_type = val

        val = dictionary.get('kms_master_key_id', None)
        val_kms_master_key_id = val

        # Return an object of this model
        return cls(
            val_kms_key_type,
            val_kms_master_key_id,
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
