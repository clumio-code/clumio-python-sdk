#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_key_filter as dynamo_db_key_filter_

T = TypeVar('T', bound='DynamoDBRestoreKeyFilters')


class DynamoDBRestoreKeyFilters:
    """Implementation of the 'DynamoDBRestoreKeyFilters' model.

    Key filters based on which DynamoDB backup records are filtered.

    Attributes:
        partition_key_filter:
            Key filter of the DynamoDB table.
        sort_key_filter:
            Key filter of the DynamoDB table.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'partition_key_filter': 'partition_key_filter',
        'sort_key_filter': 'sort_key_filter',
    }

    def __init__(
        self,
        partition_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None,
        sort_key_filter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None,
    ) -> None:
        """Constructor for the DynamoDBRestoreKeyFilters class."""

        # Initialize members of the class
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
        val = dictionary.get('partition_key_filter', None)
        val_partition_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        val = dictionary.get('sort_key_filter', None)
        val_sort_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_partition_key_filter,
            val_sort_key_filter,
        )
