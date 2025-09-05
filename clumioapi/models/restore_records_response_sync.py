#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_query_preview_result as dynamo_db_query_preview_result_
from clumioapi.models import restore_records_links_sync as restore_records_links_sync_

T = TypeVar('T', bound='RestoreRecordsResponseSync')


class RestoreRecordsResponseSync:
    """Implementation of the 'RestoreRecordsResponseSync' model.

    Records preview success

    Attributes:
        links:
            URLs to pages related to the resource.
        preview_result:
            If preview was not set to true in the request, then the result of the query will
            be
            available for download asynchronously and this field has a value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'preview_result': 'preview_result'}

    def __init__(
        self,
        links: restore_records_links_sync_.RestoreRecordsLinksSync | None = None,
        preview_result: dynamo_db_query_preview_result_.DynamoDBQueryPreviewResult | None = None,
    ) -> None:
        """Constructor for the RestoreRecordsResponseSync class."""

        # Initialize members of the class
        self.links: restore_records_links_sync_.RestoreRecordsLinksSync | None = links
        self.preview_result: dynamo_db_query_preview_result_.DynamoDBQueryPreviewResult | None = (
            preview_result
        )

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
