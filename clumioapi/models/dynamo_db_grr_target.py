#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    email_recipients_data_access_option as email_recipients_data_access_option_
import requests

T = TypeVar('T', bound='DynamoDBGrrTarget')


@dataclasses.dataclass
class DynamoDBGrrTarget:
    """Implementation of the 'DynamoDBGrrTarget' model.

    The destination information for the operation, representing the access optionfor
    the query results. Users can access the query results by direct download or
    byemail. The direct download (`direct_download`) option allows users to directly
    downloadthe restored file from the Clumio UI. The email (`email`) option allows
    users to accessthe restored file using a downloadable link they receive by
    email. If a target is notspecified, then `target` defaults to `direct_download`.

    Attributes:
        DirectDownload:
            {}`. if a target is not specified, then `target` defaults to
            `direct_download`.

        Email:
            Specifies a download link (accessible via emails) as the restore target. if not
            specified, `target` defaults to `direct_download`.

        Preview:
            Determines whether the query is preview only. if `true`, a preview of the
            query results will be provided in the response immediately.
            if `false` or omitted, a task will be queued to make results
            of the query available for asynchronous download.

    """

    DirectDownload: object | None = None
    Email: email_recipients_data_access_option_.EmailRecipientsDataAccessOption | None = None
    Preview: bool | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
