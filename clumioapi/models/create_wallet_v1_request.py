#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateWalletV1Request')


class CreateWalletV1Request:
    """Implementation of the 'CreateWalletV1Request' model.

    Attributes:
        account_native_id:
            AWS Account ID to associate with the wallet.
    """

    # Create a mapping from Model property names to API property names
    _names = {'account_native_id': 'account_native_id'}

    def __init__(self, account_native_id: str = None) -> None:
        """Constructor for the CreateWalletV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id

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
        account_native_id = dictionary.get('account_native_id')
        # Return an object of this model
        return cls(account_native_id)
