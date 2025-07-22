#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links as hateoas_common_links_
from clumioapi.models import rds_logical_preview_query_result as rds_logical_preview_query_result_

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
    _names: dict[str, str] = {'links': '_links', 'preview_result': 'preview_result'}

    def __init__(
        self,
        links: hateoas_common_links_.HateoasCommonLinks,
        preview_result: rds_logical_preview_query_result_.RDSLogicalPreviewQueryResult,
    ) -> None:
        """Constructor for the RestoreRecordPreviewResponse class."""

        # Initialize members of the class
        self.links: hateoas_common_links_.HateoasCommonLinks = links
        self.preview_result: rds_logical_preview_query_result_.RDSLogicalPreviewQueryResult = (
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

        # Extract variables from the dictionary
        val = dictionary['_links']
        val_links = hateoas_common_links_.HateoasCommonLinks.from_dictionary(val)

        val = dictionary['preview_result']
        val_preview_result = (
            rds_logical_preview_query_result_.RDSLogicalPreviewQueryResult.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_preview_result,  # type: ignore
        )
