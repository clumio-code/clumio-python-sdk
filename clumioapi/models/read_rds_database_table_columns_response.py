#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_column as rds_database_table_column_
from clumioapi.models import rds_database_table_column_links as rds_database_table_column_links_

T = TypeVar('T', bound='ReadRDSDatabaseTableColumnsResponse')


class ReadRDSDatabaseTableColumnsResponse:
    """Implementation of the 'ReadRDSDatabaseTableColumnsResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        columns:
            The columns of the table with the specified ID.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'columns': 'columns'}

    def __init__(
        self,
        links: rds_database_table_column_links_.RDSDatabaseTableColumnLinks | None = None,
        columns: Sequence[rds_database_table_column_.RDSDatabaseTableColumn] | None = None,
    ) -> None:
        """Constructor for the ReadRDSDatabaseTableColumnsResponse class."""

        # Initialize members of the class
        self.links: rds_database_table_column_links_.RDSDatabaseTableColumnLinks | None = links
        self.columns: Sequence[rds_database_table_column_.RDSDatabaseTableColumn] | None = columns

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
        val = dictionary.get('_links', None)
        val_links = rds_database_table_column_links_.RDSDatabaseTableColumnLinks.from_dictionary(
            val
        )

        val = dictionary.get('columns', None)

        val_columns = None
        if val:
            val_columns = list()
            for value in val:
                val_columns.append(
                    rds_database_table_column_.RDSDatabaseTableColumn.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_links,
            val_columns,
        )
