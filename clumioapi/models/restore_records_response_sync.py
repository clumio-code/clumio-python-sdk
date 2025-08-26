#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamo_db_query_preview_result as dynamo_db_query_preview_result_
from clumioapi.models import restore_records_links_sync as restore_records_links_sync_
import requests

T = TypeVar('T', bound='RestoreRecordsResponseSync')


@dataclasses.dataclass
class RestoreRecordsResponseSync:
    """Implementation of the 'RestoreRecordsResponseSync' model.

        Records preview success

        Attributes:
            Links:
                Urls to pages related to the resource.

            PreviewResult:
                If preview was not set to true in the request, then the result of the query will be
    available for download asynchronously and this field has a value of `null`.

    """

    Links: restore_records_links_sync_.RestoreRecordsLinksSync | None = None
    PreviewResult: dynamo_db_query_preview_result_.DynamoDBQueryPreviewResult | None = None

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
        val = dictionary.get('_links', None)
        val_links = restore_records_links_sync_.RestoreRecordsLinksSync.from_dictionary(val)

        val = dictionary.get('preview_result', None)
        val_preview_result = (
            dynamo_db_query_preview_result_.DynamoDBQueryPreviewResult.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_links,
            val_preview_result,
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
