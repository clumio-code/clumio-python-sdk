#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamo_db_grr_source as dynamo_db_grr_source_
from clumioapi.models import dynamo_db_grr_target as dynamo_db_grr_target_
from clumioapi.models import dynamo_dbgrr_query_filter as dynamo_dbgrr_query_filter_
import requests

T = TypeVar('T', bound='RestoreRecordsAwsDynamodbTableV1Request')


@dataclasses.dataclass
class RestoreRecordsAwsDynamodbTableV1Request:
    """Implementation of the 'RestoreRecordsAwsDynamodbTableV1Request' model.

        Attributes:
            QueryFilter:
                Filters based on which dynamodb backup records are filtered in the query.

            Source:
                The parameters for initiating a dynamodb table backup query from a backup.

            Target:
                The destination information for the operation, representing the access option
    for the query results. users can access the query results by direct download or by
    email. the direct download (`direct_download`) option allows users to directly download
    the restored file from the clumio ui. the email (`email`) option allows users to access
    the restored file using a downloadable link they receive by email. if a target is not
    specified, then `target` defaults to `direct_download`.

    """

    QueryFilter: dynamo_dbgrr_query_filter_.DynamoDBGRRQueryFilter | None = None
    Source: dynamo_db_grr_source_.DynamoDBGrrSource | None = None
    Target: dynamo_db_grr_target_.DynamoDBGrrTarget | None = None

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
        val = dictionary.get('query_filter', None)
        val_query_filter = dynamo_dbgrr_query_filter_.DynamoDBGRRQueryFilter.from_dictionary(val)

        val = dictionary.get('source', None)
        val_source = dynamo_db_grr_source_.DynamoDBGrrSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = dynamo_db_grr_target_.DynamoDBGrrTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_query_filter,
            val_source,
            val_target,
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
