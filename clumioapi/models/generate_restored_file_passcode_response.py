#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import generate_restored_file_passcode_links

T = TypeVar('T', bound='GenerateRestoredFilePasscodeResponse')


class GenerateRestoredFilePasscodeResponse:
    """Implementation of the 'GenerateRestoredFilePasscodeResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        passcode:
            The new passcode that has been generated for the restored file. Send the
            passcode to the email recipient, who must use it to access the restored file.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'passcode': 'passcode'}

    def __init__(
        self,
        links: generate_restored_file_passcode_links.GenerateRestoredFilePasscodeLinks = None,
        passcode: str = None,
    ) -> None:
        """Constructor for the GenerateRestoredFilePasscodeResponse class."""

        # Initialize members of the class
        self.links: generate_restored_file_passcode_links.GenerateRestoredFilePasscodeLinks = links
        self.passcode: str = passcode

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
            generate_restored_file_passcode_links.GenerateRestoredFilePasscodeLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        passcode = dictionary.get('passcode')
        # Return an object of this model
        return cls(links, passcode)
