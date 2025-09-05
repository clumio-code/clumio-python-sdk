#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import share_file_restore_email_links as share_file_restore_email_links_

T = TypeVar('T', bound='ShareFileRestoreEmailResponse')


class ShareFileRestoreEmailResponse:
    """Implementation of the 'ShareFileRestoreEmailResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links'}

    def __init__(
        self, links: share_file_restore_email_links_.ShareFileRestoreEmailLinks | None = None
    ) -> None:
        """Constructor for the ShareFileRestoreEmailResponse class."""

        # Initialize members of the class
        self.links: share_file_restore_email_links_.ShareFileRestoreEmailLinks | None = links

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
        val = dictionary.get('_links', None)
        val_links = share_file_restore_email_links_.ShareFileRestoreEmailLinks.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_links,
        )
