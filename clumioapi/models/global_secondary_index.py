#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import key_schema_element
from clumioapi.models import projection
from clumioapi.models import provisioned_throughput

T = TypeVar('T', bound='GlobalSecondaryIndex')


class GlobalSecondaryIndex:
    """Implementation of the 'GlobalSecondaryIndex' model.

    Represents the properties of a global secondary index.

    Attributes:
        index_name:
            The name of the global secondary index.
        key_schema:
            The complete key schema for a global secondary index, which consists of one or
            more
            pairs of attribute names and key types.
        projection:
            Represents attributes that are copied (projected) from the table into an index.
            These are in addition to the
            primary key attributes and index key attributes, which are automatically
            projected.
        provisioned_throughput:
            Represents the provisioned throughput settings for a DynamoDB table.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'index_name': 'index_name',
        'key_schema': 'key_schema',
        'projection': 'projection',
        'provisioned_throughput': 'provisioned_throughput',
    }

    def __init__(
        self,
        index_name: str = None,
        key_schema: Sequence[key_schema_element.KeySchemaElement] = None,
        projection: projection.Projection = None,
        provisioned_throughput: provisioned_throughput.ProvisionedThroughput = None,
    ) -> None:
        """Constructor for the GlobalSecondaryIndex class."""

        # Initialize members of the class
        self.index_name: str = index_name
        self.key_schema: Sequence[key_schema_element.KeySchemaElement] = key_schema
        self.projection: projection.Projection = projection
        self.provisioned_throughput: provisioned_throughput.ProvisionedThroughput = (
            provisioned_throughput
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
        index_name = dictionary.get('index_name')
        key_schema = None
        if dictionary.get('key_schema'):
            key_schema = list()
            for value in dictionary.get('key_schema'):
                key_schema.append(key_schema_element.KeySchemaElement.from_dictionary(value))

        key = 'projection'
        p_projection = (
            projection.Projection.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'provisioned_throughput'
        p_provisioned_throughput = (
            provisioned_throughput.ProvisionedThroughput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(index_name, key_schema, p_projection, p_provisioned_throughput)
