#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import key_schema_element as key_schema_element_
from clumioapi.models import projection as projection_

T = TypeVar('T', bound='LocalSecondaryIndex')


class LocalSecondaryIndex:
    """Implementation of the 'LocalSecondaryIndex' model.

    Represents the properties of a local secondary index.

    Attributes:
        index_name:
            The name of the local secondary index
        key_schema:
            The complete key schema for the local secondary index, consisting of one or more
            pairs of attribute names and key types.
        projection:
            Represents attributes that are copied (projected) from the table into an index.
            These are in addition to the
            primary key attributes and index key attributes, which are automatically
            projected.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'index_name': 'index_name',
        'key_schema': 'key_schema',
        'projection': 'projection',
    }

    def __init__(
        self,
        index_name: str | None = None,
        key_schema: Sequence[key_schema_element_.KeySchemaElement] | None = None,
        projection: projection_.Projection | None = None,
    ) -> None:
        """Constructor for the LocalSecondaryIndex class."""

        # Initialize members of the class
        self.index_name: str | None = index_name
        self.key_schema: Sequence[key_schema_element_.KeySchemaElement] | None = key_schema
        self.projection: projection_.Projection | None = projection

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
        val = dictionary.get('index_name', None)
        val_index_name = val

        val = dictionary.get('key_schema', None)

        val_key_schema = None
        if val:
            val_key_schema = list()
            for value in val:
                val_key_schema.append(key_schema_element_.KeySchemaElement.from_dictionary(value))

        val = dictionary.get('projection', None)
        val_projection = projection_.Projection.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_index_name,
            val_key_schema,
            val_projection,
        )
