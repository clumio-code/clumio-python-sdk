#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    generate_restored_file_passcode_links as generate_restored_file_passcode_links_

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
    _names: dict[str, str] = {'links': '_links', 'passcode': 'passcode'}

    def __init__(
        self,
        links: (
            generate_restored_file_passcode_links_.GenerateRestoredFilePasscodeLinks | None
        ) = None,
        passcode: str | None = None,
    ) -> None:
        """Constructor for the GenerateRestoredFilePasscodeResponse class."""

        # Initialize members of the class
        self.links: (
            generate_restored_file_passcode_links_.GenerateRestoredFilePasscodeLinks | None
        ) = links
        self.passcode: str | None = passcode

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
        val_links = generate_restored_file_passcode_links_.GenerateRestoredFilePasscodeLinks.from_dictionary(
            val
        )

        val = dictionary.get('passcode', None)
        val_passcode = val

        # Return an object of this model
        return cls(
            val_links,
            val_passcode,
        )
