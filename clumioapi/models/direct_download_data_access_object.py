#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DirectDownloadDataAccessObject')


class DirectDownloadDataAccessObject:
    """Implementation of the 'DirectDownloadDataAccessObject' model.

    The details used to access the restored file if it was shared by direct
    download. Ifthe restored file was shared by email (and not by direct download),
    then this fieldhas a value of `null`.

    Attributes:
        download_link:
            The download link used to access the restored file through direct download.
        retrieved_by:
            The email address of the user who initiated the file level restore.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'download_link': 'download_link', 'retrieved_by': 'retrieved_by'}

    def __init__(self, download_link: str | None = None, retrieved_by: str | None = None) -> None:
        """Constructor for the DirectDownloadDataAccessObject class."""

        # Initialize members of the class
        self.download_link: str | None = download_link
        self.retrieved_by: str | None = retrieved_by

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
        val = dictionary.get('download_link', None)
        val_download_link = val

        val = dictionary.get('retrieved_by', None)
        val_retrieved_by = val

        # Return an object of this model
        return cls(
            val_download_link,
            val_retrieved_by,
        )
