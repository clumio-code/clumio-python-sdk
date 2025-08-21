#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='WalletLinks')


class WalletLinks:
    """Implementation of the 'WalletLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_wallet:
            A resource-specific HATEOAS link.
        list_wallet_keys:
            A resource-specific HATEOAS link.
        refresh_wallet:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_wallet': 'delete-wallet',
        'list_wallet_keys': 'list-wallet-keys',
        'refresh_wallet': 'refresh-wallet',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        delete_wallet: hateoas_link_.HateoasLink | None = None,
        list_wallet_keys: hateoas_link_.HateoasLink | None = None,
        refresh_wallet: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the WalletLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.delete_wallet: hateoas_link_.HateoasLink | None = delete_wallet
        self.list_wallet_keys: hateoas_link_.HateoasLink | None = list_wallet_keys
        self.refresh_wallet: hateoas_link_.HateoasLink | None = refresh_wallet

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
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('delete-wallet', None)
        val_delete_wallet = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-wallet-keys', None)
        val_list_wallet_keys = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('refresh-wallet', None)
        val_refresh_wallet = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_delete_wallet,
            val_list_wallet_keys,
            val_refresh_wallet,
        )
