#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_query_preview_result
from clumioapi.models import restore_records_links_sync

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
    _names = {'links': '_links', 'preview_result': 'preview_result'}

    def __init__(
        self,
        links: restore_records_links_sync.RestoreRecordsLinksSync = None,
        preview_result: dynamo_db_query_preview_result.DynamoDBQueryPreviewResult = None,
    ) -> None:
        """Constructor for the RestoreRecordsResponseSync class."""

        # Initialize members of the class
        self.links: restore_records_links_sync.RestoreRecordsLinksSync = links
        self.preview_result: dynamo_db_query_preview_result.DynamoDBQueryPreviewResult = (
            preview_result
        )

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
        key = '_links'
        links = (
            restore_records_links_sync.RestoreRecordsLinksSync.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'preview_result'
        preview_result = (
            dynamo_db_query_preview_result.DynamoDBQueryPreviewResult.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links, preview_result)
