#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    direct_download_data_access_object as direct_download_data_access_object_
from clumioapi.models import email_download_data_access_object as email_download_data_access_object_
import requests

T = TypeVar('T', bound='DataAccessObject')


@dataclasses.dataclass
class DataAccessObject:
    """Implementation of the 'DataAccessObject' model.

        Specifies information about the data-access method for accessing the
        restoredfile.

        Attributes:
            DirectDownload:
                The details used to access the restored file if it was shared by direct download. if
    the restored file was shared by email (and not by direct download), then this field
    has a value of `null`.

            Email:
                The details used to access the restored file, if it was shared by email. if the
    restored file was shared by direct download (and not email), then this field has a
    value of `null`.

    """

    DirectDownload: direct_download_data_access_object_.DirectDownloadDataAccessObject | None = None
    Email: email_download_data_access_object_.EmailDownloadDataAccessObject | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
