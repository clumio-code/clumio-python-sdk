#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    direct_download_data_access_object as direct_download_data_access_object_
from clumioapi.models import email_download_data_access_object as email_download_data_access_object_

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
    _names: dict[str, str] = {'direct_download': 'direct_download', 'email': 'email'}

    def __init__(
        self,
        direct_download: (
            direct_download_data_access_object_.DirectDownloadDataAccessObject | None
        ) = None,
        email: email_download_data_access_object_.EmailDownloadDataAccessObject | None = None,
    ) -> None:
        """Constructor for the DataAccessObject class."""

        # Initialize members of the class
        self.direct_download: (
            direct_download_data_access_object_.DirectDownloadDataAccessObject | None
        ) = direct_download
        self.email: email_download_data_access_object_.EmailDownloadDataAccessObject | None = email

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
        val = dictionary.get('direct_download', None)
        val_direct_download = (
            direct_download_data_access_object_.DirectDownloadDataAccessObject.from_dictionary(val)
        )

        val = dictionary.get('email', None)
        val_email = (
            email_download_data_access_object_.EmailDownloadDataAccessObject.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_direct_download,
            val_email,
        )
