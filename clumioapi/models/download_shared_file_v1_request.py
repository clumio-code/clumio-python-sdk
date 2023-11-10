#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DownloadSharedFileV1Request')


class DownloadSharedFileV1Request:
    """Implementation of the 'DownloadSharedFileV1Request' model.

    Attributes:
        email_link:
            The download link that was sent to you by email. To get the download link,
            open the email message, click "Download File" to launch the Clumio "Access
            Requested File" page, and copy the URL.
        passcode:
            The passcode used to access the restored file. Obtain the passcode from the
            user who generated the restored file.
    """

    # Create a mapping from Model property names to API property names
    _names = {'email_link': 'email_link', 'passcode': 'passcode'}

    def __init__(self, email_link: str = None, passcode: str = None) -> None:
        """Constructor for the DownloadSharedFileV1Request class."""

        # Initialize members of the class
        self.email_link: str = email_link
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
        email_link = dictionary.get('email_link')
        passcode = dictionary.get('passcode')
        # Return an object of this model
        return cls(email_link, passcode)
