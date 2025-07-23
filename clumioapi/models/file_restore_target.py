#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import email_download_data_access_option as email_download_data_access_option_

T = TypeVar('T', bound='FileRestoreTarget')


class FileRestoreTarget:
    """Implementation of the 'FileRestoreTarget' model.

    The destination information for the file level restore, representing the access
    optionfor the restored file. Users can access the restored file by direct
    download or byemail. The direct download (`direct_download`) option allows users
    to directly downloadthe restored file from the Clumio UI. The email (`email`)
    option allows users to accessthe restored file using a downloadable link they
    receive by email. If a target is notspecified, then `target` defaults to
    `direct_download`.

    Attributes:
        direct_download:
            Specifies the Clumio UI as the restore target for direct download. Optionally
            set
            `direct_download: {}`. If a target is not specified, then `target` defaults to
            `direct_download`.
        email:
            Specifies a download link (accessible via email) as the restore target. If not
            specified, `target` defaults to `direct_download`. If you specify `email`, also
            send the user the passcode that gets generated from this request (see `passcode`
            in
            the response). After the user clicks the download link, they must enter the
            passcode to access the files.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'direct_download': 'direct_download', 'email': 'email'}

    def __init__(
        self,
        direct_download: object | None = None,
        email: email_download_data_access_option_.EmailDownloadDataAccessOption | None = None,
    ) -> None:
        """Constructor for the FileRestoreTarget class."""

        # Initialize members of the class
        self.direct_download: object | None = direct_download
        self.email: email_download_data_access_option_.EmailDownloadDataAccessOption | None = email

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
        val_direct_download = val

        val = dictionary.get('email', None)
        val_email = (
            email_download_data_access_option_.EmailDownloadDataAccessOption.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_direct_download,
            val_email,
        )
