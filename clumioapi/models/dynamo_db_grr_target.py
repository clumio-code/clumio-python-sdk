#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    email_recipients_data_access_option as email_recipients_data_access_option_

T = TypeVar('T', bound='DynamoDBGrrTarget')


class DynamoDBGrrTarget:
    """Implementation of the 'DynamoDBGrrTarget' model.

    The destination information for the operation, representing the access optionfor
    the query results. Users can access the query results by direct download or
    byemail. The direct download (`direct_download`) option allows users to directly
    downloadthe restored file from the Clumio UI. The email (`email`) option allows
    users to accessthe restored file using a downloadable link they receive by
    email. If a target is notspecified, then `target` defaults to `direct_download`.

    Attributes:
        direct_download:
            Specifies the Clumio UI as the restore target for direct download. Optionally
            set
            `direct_download: {}`. If a target is not specified, then `target` defaults to
            `direct_download`.
        email:
            Specifies a download link (accessible via emails) as the restore target. If not
            specified, `target` defaults to `direct_download`.
        preview:
            Determines whether the query is preview only. If `true`, a preview of the
            query results will be provided in the response immediately.
            If `false` or omitted, a task will be queued to make results
            of the query available for asynchronous download.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'direct_download': 'direct_download',
        'email': 'email',
        'preview': 'preview',
    }

    def __init__(
        self,
        direct_download: object | None = None,
        email: email_recipients_data_access_option_.EmailRecipientsDataAccessOption | None = None,
        preview: bool | None = None,
    ) -> None:
        """Constructor for the DynamoDBGrrTarget class."""

        # Initialize members of the class
        self.direct_download: object | None = direct_download
        self.email: email_recipients_data_access_option_.EmailRecipientsDataAccessOption | None = (
            email
        )
        self.preview: bool | None = preview

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
            email_recipients_data_access_option_.EmailRecipientsDataAccessOption.from_dictionary(
                val
            )
        )

        val = dictionary.get('preview', None)
        val_preview = val

        # Return an object of this model
        return cls(
            val_direct_download,
            val_email,
            val_preview,
        )
