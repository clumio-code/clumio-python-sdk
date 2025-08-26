#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateWalletV1Request')


class CreateWalletV1Request:
    """Implementation of the 'CreateWalletV1Request' model.

    Attributes:
        account_native_id:
            AWS Account ID to associate with the wallet.
        aws_region:
            The AWS Region to associate with the wallet.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'account_native_id': 'account_native_id', 'aws_region': 'aws_region'}

    def __init__(self, account_native_id: str | None = None, aws_region: str | None = None) -> None:
        """Constructor for the CreateWalletV1Request class."""

        # Initialize members of the class
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region

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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_aws_region,
        )
