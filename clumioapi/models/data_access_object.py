#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import direct_download_data_access_object
from clumioapi.models import email_download_data_access_object

T = TypeVar('T', bound='DataAccessObject')


class DataAccessObject:
    """Implementation of the 'DataAccessObject' model.

    Specifies information about the data-access method for accessing the
    restoredfile.

    Attributes:
        direct_download:
            The details used to access the restored file if it was shared by direct
            download. If
            the restored file was shared by email (and not by direct download), then this
            field
            has a value of `null`.
        email:
            The details used to access the restored file, if it was shared by email. If the
            restored file was shared by direct download (and not email), then this field has
            a
            value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {'direct_download': 'direct_download', 'email': 'email'}

    def __init__(
        self,
        direct_download: direct_download_data_access_object.DirectDownloadDataAccessObject = None,
        email: email_download_data_access_object.EmailDownloadDataAccessObject = None,
    ) -> None:
        """Constructor for the DataAccessObject class."""

        # Initialize members of the class
        self.direct_download: direct_download_data_access_object.DirectDownloadDataAccessObject = (
            direct_download
        )
        self.email: email_download_data_access_object.EmailDownloadDataAccessObject = email

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
        key = 'direct_download'
        direct_download = (
            direct_download_data_access_object.DirectDownloadDataAccessObject.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'email'
        email = (
            email_download_data_access_object.EmailDownloadDataAccessObject.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(direct_download, email)
