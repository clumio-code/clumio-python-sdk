#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_common_links as hateoas_common_links_
from clumioapi.models import rds_logical_preview_query_result as rds_logical_preview_query_result_
import requests

T = TypeVar('T', bound='RestoreRecordPreviewResponse')


@dataclasses.dataclass
class RestoreRecordPreviewResponse:
    """Implementation of the 'RestoreRecordPreviewResponse' model.

        Preview Success

        Attributes:
            Links:
                Hateoascommonlinks are the common fields for hateoas response.

            PreviewResult:
                The preview of the query result, if `preview:true` in the request.
    if preview was not set to true in the request, then the result of the query will be
    available for download asynchronously.

    """

    Links: hateoas_common_links_.HateoasCommonLinks | None = None
    PreviewResult: rds_logical_preview_query_result_.RDSLogicalPreviewQueryResult | None = None
    raw_response: Optional[requests.Response] = None

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
        val_links = hateoas_common_links_.HateoasCommonLinks.from_dictionary(val)

        val = dictionary.get('preview_result', None)
        val_preview_result = (
            rds_logical_preview_query_result_.RDSLogicalPreviewQueryResult.from_dictionary(val)
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
        model_instance.raw_response = response
        return model_instance
