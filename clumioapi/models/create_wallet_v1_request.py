#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CreateWalletV1Request')


@dataclasses.dataclass
class CreateWalletV1Request:
    """Implementation of the 'CreateWalletV1Request' model.

    Attributes:
        AccountNativeId:
            Aws account id to associate with the wallet.

        AwsRegion:
            The aws region to associate with the wallet.

    """

    AccountNativeId: str | None = None
    AwsRegion: str | None = None

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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_aws_region,
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
