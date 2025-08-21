#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_grr_source as dynamo_db_grr_source_
from clumioapi.models import dynamo_db_grr_target as dynamo_db_grr_target_
from clumioapi.models import dynamo_dbgrr_query_filter as dynamo_dbgrr_query_filter_

T = TypeVar('T', bound='RestoreRecordsAwsDynamodbTableV1Request')


class RestoreRecordsAwsDynamodbTableV1Request:
    """Implementation of the 'RestoreRecordsAwsDynamodbTableV1Request' model.

    Attributes:
        query_filter:
            Filters based on which DynamoDB backup records are filtered in the query.
        source:
            The parameters for initiating a DynamoDB table backup query from a backup.
        target:
            The destination information for the operation, representing the access option
            for the query results. Users can access the query results by direct download or
            by
            email. The direct download (`direct_download`) option allows users to directly
            download
            the restored file from the Clumio UI. The email (`email`) option allows users to
            access
            the restored file using a downloadable link they receive by email. If a target
            is not
            specified, then `target` defaults to `direct_download`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'query_filter': 'query_filter',
        'source': 'source',
        'target': 'target',
    }

    def __init__(
        self,
        query_filter: dynamo_dbgrr_query_filter_.DynamoDBGRRQueryFilter | None = None,
        source: dynamo_db_grr_source_.DynamoDBGrrSource | None = None,
        target: dynamo_db_grr_target_.DynamoDBGrrTarget | None = None,
    ) -> None:
        """Constructor for the RestoreRecordsAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.query_filter: dynamo_dbgrr_query_filter_.DynamoDBGRRQueryFilter | None = query_filter
        self.source: dynamo_db_grr_source_.DynamoDBGrrSource | None = source
        self.target: dynamo_db_grr_target_.DynamoDBGrrTarget | None = target

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
