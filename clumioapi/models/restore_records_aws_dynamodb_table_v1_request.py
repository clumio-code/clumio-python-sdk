#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_grr_source
from clumioapi.models import dynamo_db_grr_target
from clumioapi.models import dynamo_dbgrr_query_filter

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
    _names = {'query_filter': 'query_filter', 'source': 'source', 'target': 'target'}

    def __init__(
        self,
        query_filter: dynamo_dbgrr_query_filter.DynamoDBGRRQueryFilter = None,
        source: dynamo_db_grr_source.DynamoDBGrrSource = None,
        target: dynamo_db_grr_target.DynamoDBGrrTarget = None,
    ) -> None:
        """Constructor for the RestoreRecordsAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.query_filter: dynamo_dbgrr_query_filter.DynamoDBGRRQueryFilter = query_filter
        self.source: dynamo_db_grr_source.DynamoDBGrrSource = source
        self.target: dynamo_db_grr_target.DynamoDBGrrTarget = target

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
        key = 'query_filter'
        query_filter = (
            dynamo_dbgrr_query_filter.DynamoDBGRRQueryFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'source'
        source = (
            dynamo_db_grr_source.DynamoDBGrrSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            dynamo_db_grr_target.DynamoDBGrrTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(query_filter, source, target)
