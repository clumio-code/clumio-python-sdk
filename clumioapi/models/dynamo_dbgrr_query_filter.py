#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_key_filter as dynamo_db_key_filter_
from clumioapi.models import dynamo_db_restore_key_filters as dynamo_db_restore_key_filters_
from clumioapi.models import dynamo_dbgrr_attribute_filter as dynamo_dbgrr_attribute_filter_

T = TypeVar('T', bound='DynamoDBGRRQueryFilter')


class DynamoDBGRRQueryFilter:
    """Implementation of the 'DynamoDBGRRQueryFilter' model.

    Filters based on which DynamoDB backup records are filtered in the query.

    Attributes:
        attribute_filters:
            Attribute filters of the DynamoDB table.
        key_filters:
            Key filters of the DynamoDB table.
        partition_key:
            Partition Key value of the DynamoDB table.
            Deprecated: Use PartitionKeyFilter instead.
        partition_key_filter:
            Key filter of the DynamoDB table.
        sort_key_filter:
            Key filter of the DynamoDB table.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'attribute_filters': 'attribute_filters',
        'key_filters': 'key_filters',
        'partition_key': 'partition_key',
        'partition_key_filter': 'partition_key_filter',
        'sort_key_filter': 'sort_key_filter',
    }

    def __init__(
        self,
        attribute_filters: (
            Sequence[dynamo_dbgrr_attribute_filter_.DynamoDBGRRAttributeFilter] | None
        ) = None,
        key_filters: (
            Sequence[dynamo_db_restore_key_filters_.DynamoDBRestoreKeyFilters] | None
        ) = None,
        partition_key: str | None = None,
        partition_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None,
        sort_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None,
    ) -> None:
        """Constructor for the DynamoDBGRRQueryFilter class."""

        # Initialize members of the class
        self.attribute_filters: (
            Sequence[dynamo_dbgrr_attribute_filter_.DynamoDBGRRAttributeFilter] | None
        ) = attribute_filters
        self.key_filters: (
            Sequence[dynamo_db_restore_key_filters_.DynamoDBRestoreKeyFilters] | None
        ) = key_filters
        self.partition_key: str | None = partition_key
        self.partition_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = (
            partition_key_filter
        )
        self.sort_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = sort_key_filter

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
        val = dictionary.get('attribute_filters', None)

        val_attribute_filters = None
        if val:
            val_attribute_filters = list()
            for value in val:
                val_attribute_filters.append(
                    dynamo_dbgrr_attribute_filter_.DynamoDBGRRAttributeFilter.from_dictionary(value)
                )

        val = dictionary.get('key_filters', None)

        val_key_filters = None
        if val:
            val_key_filters = list()
            for value in val:
                val_key_filters.append(
                    dynamo_db_restore_key_filters_.DynamoDBRestoreKeyFilters.from_dictionary(value)
                )

        val = dictionary.get('partition_key', None)
        val_partition_key = val

        val = dictionary.get('partition_key_filter', None)
        val_partition_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        val = dictionary.get('sort_key_filter', None)
        val_sort_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_attribute_filters,
            val_key_filters,
            val_partition_key,
            val_partition_key_filter,
            val_sort_key_filter,
        )
