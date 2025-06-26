#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import email_download_data_access_option

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
    _names = {'direct_download': 'direct_download', 'email': 'email'}

    def __init__(
        self,
        direct_download: object = None,
        email: email_download_data_access_option.EmailDownloadDataAccessOption = None,
    ) -> None:
        """Constructor for the FileRestoreTarget class."""

        # Initialize members of the class
        self.direct_download: object = direct_download
        self.email: email_download_data_access_option.EmailDownloadDataAccessOption = email

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
        direct_download = dictionary.get('direct_download')
        key = 'email'
        email = (
            email_download_data_access_option.EmailDownloadDataAccessOption.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(direct_download, email)
