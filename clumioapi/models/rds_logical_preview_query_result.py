#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_column

T = TypeVar('T', bound='RDSLogicalPreviewQueryResult')


class RDSLogicalPreviewQueryResult:
    """Implementation of the 'RDSLogicalPreviewQueryResult' model.

    The preview of the query result, if `preview:true` in the request.If preview was
    not set to true in the request, then the result of the query will beavailable
    for download asynchronously.

    Attributes:
        columns:
            The columns of the previewed query result.
        rows:
            The rows of the previewed query result.
    """

    # Create a mapping from Model property names to API property names
    _names = {'columns': 'columns', 'rows': 'rows'}

    def __init__(
        self,
        columns: Sequence[rds_database_table_column.RDSDatabaseTableColumn] = None,
        rows: Sequence[Sequence[str]] = None,
    ) -> None:
        """Constructor for the RDSLogicalPreviewQueryResult class."""

        # Initialize members of the class
        self.columns: Sequence[rds_database_table_column.RDSDatabaseTableColumn] = columns
        self.rows: Sequence[Sequence[str]] = rows

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
        columns = None
        if dictionary.get('columns'):
            columns = list()
            for value in dictionary.get('columns'):
                columns.append(
                    rds_database_table_column.RDSDatabaseTableColumn.from_dictionary(value)
                )

        rows = dictionary.get('rows')
        # Return an object of this model
        return cls(columns, rows)
