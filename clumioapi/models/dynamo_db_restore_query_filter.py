#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamo_db_key_filter as dynamo_db_key_filter_
from clumioapi.models import dynamo_db_restore_key_filters as dynamo_db_restore_key_filters_
from clumioapi.models import dynamo_dbgrr_attribute_filter as dynamo_dbgrr_attribute_filter_
import requests

T = TypeVar('T', bound='DynamoDBRestoreQueryFilter')


@dataclasses.dataclass
class DynamoDBRestoreQueryFilter:
    """Implementation of the 'DynamoDBRestoreQueryFilter' model.

    Filters based on which DynamoDB backup records are filtered.

    Attributes:
        AttributeFilters:
            Attribute filters of the dynamodb table.

        KeyFilters:
            Key filters of the dynamodb table.

        PartitionKeyFilter:
            Key filter of the dynamodb table.

        SortKeyFilter:
            Key filter of the dynamodb table.

    """

    AttributeFilters: Sequence[dynamo_dbgrr_attribute_filter_.DynamoDBGRRAttributeFilter] | None = (
        None
    )
    KeyFilters: Sequence[dynamo_db_restore_key_filters_.DynamoDBRestoreKeyFilters] | None = None
    PartitionKeyFilter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None
    SortKeyFilter: dynamo_db_key_filter_.DynamoDBKeyFilter | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('attribute_filters', None)

        val_attribute_filters = []
        if val:
            for value in val:
                val_attribute_filters.append(
                    dynamo_dbgrr_attribute_filter_.DynamoDBGRRAttributeFilter.from_dictionary(value)
                )

        val = dictionary.get('key_filters', None)

        val_key_filters = []
        if val:
            for value in val:
                val_key_filters.append(
                    dynamo_db_restore_key_filters_.DynamoDBRestoreKeyFilters.from_dictionary(value)
                )

        val = dictionary.get('partition_key_filter', None)
        val_partition_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        val = dictionary.get('sort_key_filter', None)
        val_sort_key_filter = dynamo_db_key_filter_.DynamoDBKeyFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_attribute_filters,
            val_key_filters,
            val_partition_key_filter,
            val_sort_key_filter,
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
