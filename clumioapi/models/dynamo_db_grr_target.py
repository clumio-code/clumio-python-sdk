#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import email_recipients_data_access_option

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
    _names = {'direct_download': 'direct_download', 'email': 'email', 'preview': 'preview'}

    def __init__(
        self,
        direct_download: object = None,
        email: email_recipients_data_access_option.EmailRecipientsDataAccessOption = None,
        preview: bool = None,
    ) -> None:
        """Constructor for the DynamoDBGrrTarget class."""

        # Initialize members of the class
        self.direct_download: object = direct_download
        self.email: email_recipients_data_access_option.EmailRecipientsDataAccessOption = email
        self.preview: bool = preview

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
            email_recipients_data_access_option.EmailRecipientsDataAccessOption.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        preview = dictionary.get('preview')
        # Return an object of this model
        return cls(direct_download, email, preview)
