#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import share_file_restore_email_links

T = TypeVar('T', bound='ShareFileRestoreEmailResponse')


class ShareFileRestoreEmailResponse:
    """Implementation of the 'ShareFileRestoreEmailResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links'}

    def __init__(
        self, links: share_file_restore_email_links.ShareFileRestoreEmailLinks = None
    ) -> None:
        """Constructor for the ShareFileRestoreEmailResponse class."""

        # Initialize members of the class
        self.links: share_file_restore_email_links.ShareFileRestoreEmailLinks = links

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
        key = '_links'
        links = (
            share_file_restore_email_links.ShareFileRestoreEmailLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links)
