#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links
from clumioapi.models import rds_logical_preview_query_result

T = TypeVar('T', bound='RestoreRecordPreviewResponse')


class RestoreRecordPreviewResponse:
    """Implementation of the 'RestoreRecordPreviewResponse' model.

    Preview Success

    Attributes:
        links:
            HateoasCommonLinks are the common fields for HATEOAS response.
        preview_result:
            The preview of the query result, if `preview:true` in the request.
            If preview was not set to true in the request, then the result of the query will
            be
            available for download asynchronously.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'preview_result': 'preview_result'}

    def __init__(
        self,
        links: hateoas_common_links.HateoasCommonLinks = None,
        preview_result: rds_logical_preview_query_result.RDSLogicalPreviewQueryResult = None,
    ) -> None:
        """Constructor for the RestoreRecordPreviewResponse class."""

        # Initialize members of the class
        self.links: hateoas_common_links.HateoasCommonLinks = links
        self.preview_result: rds_logical_preview_query_result.RDSLogicalPreviewQueryResult = (
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
            hateoas_common_links.HateoasCommonLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'preview_result'
        preview_result = (
            rds_logical_preview_query_result.RDSLogicalPreviewQueryResult.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links, preview_result)
