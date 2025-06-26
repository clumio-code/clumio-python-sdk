#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_key_filter
from clumioapi.models import dynamo_dbgrr_attribute_filter

T = TypeVar('T', bound='DynamoDBGRRQueryFilter')


class DynamoDBGRRQueryFilter:
    """Implementation of the 'DynamoDBGRRQueryFilter' model.

    Filters based on which DynamoDB backup records are filtered in the query.

    Attributes:
        attribute_filters:
            Attribute filters of the DynamoDB table.
        partition_key:
            Partition Key value of the DynamoDB table.
            Deprecated: Use PartitionKeyFilter instead.
        partition_key_filter:
            Key filter of the DynamoDB table.
        sort_key_filter:
            Key filter of the DynamoDB table.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'attribute_filters': 'attribute_filters',
        'partition_key': 'partition_key',
        'partition_key_filter': 'partition_key_filter',
        'sort_key_filter': 'sort_key_filter',
    }

    def __init__(
        self,
        attribute_filters: Sequence[
            dynamo_dbgrr_attribute_filter.DynamoDBGRRAttributeFilter
        ] = None,
        partition_key: str = None,
        partition_key_filter: dynamo_db_key_filter.DynamoDBKeyFilter = None,
        sort_key_filter: dynamo_db_key_filter.DynamoDBKeyFilter = None,
    ) -> None:
        """Constructor for the DynamoDBGRRQueryFilter class."""

        # Initialize members of the class
        self.attribute_filters: Sequence[
            dynamo_dbgrr_attribute_filter.DynamoDBGRRAttributeFilter
        ] = attribute_filters
        self.partition_key: str = partition_key
        self.partition_key_filter: dynamo_db_key_filter.DynamoDBKeyFilter = partition_key_filter
        self.sort_key_filter: dynamo_db_key_filter.DynamoDBKeyFilter = sort_key_filter

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
        attribute_filters = None
        if dictionary.get('attribute_filters'):
            attribute_filters = list()
            for value in dictionary.get('attribute_filters'):
                attribute_filters.append(
                    dynamo_dbgrr_attribute_filter.DynamoDBGRRAttributeFilter.from_dictionary(value)
                )

        partition_key = dictionary.get('partition_key')
        key = 'partition_key_filter'
        partition_key_filter = (
            dynamo_db_key_filter.DynamoDBKeyFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'sort_key_filter'
        sort_key_filter = (
            dynamo_db_key_filter.DynamoDBKeyFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(attribute_filters, partition_key, partition_key_filter, sort_key_filter)
