#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_column
from clumioapi.models import rds_database_table_column_links

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
    _names = {'links': '_links', 'columns': 'columns'}

    def __init__(
        self,
        links: rds_database_table_column_links.RDSDatabaseTableColumnLinks = None,
        columns: Sequence[rds_database_table_column.RDSDatabaseTableColumn] = None,
    ) -> None:
        """Constructor for the ReadRDSDatabaseTableColumnsResponse class."""

        # Initialize members of the class
        self.links: rds_database_table_column_links.RDSDatabaseTableColumnLinks = links
        self.columns: Sequence[rds_database_table_column.RDSDatabaseTableColumn] = columns

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
        key = '_links'
        links = (
            rds_database_table_column_links.RDSDatabaseTableColumnLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        columns = None
        if dictionary.get('columns'):
            columns = list()
            for value in dictionary.get('columns'):
                columns.append(
                    rds_database_table_column.RDSDatabaseTableColumn.from_dictionary(value)
                )

        # Return an object of this model
        return cls(links, columns)
