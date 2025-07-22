#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_column as rds_database_table_column_

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
    _names: dict[str, str] = {'columns': 'columns', 'rows': 'rows'}

    def __init__(
        self,
        columns: Sequence[rds_database_table_column_.RDSDatabaseTableColumn],
        rows: Sequence[Sequence[str]],
    ) -> None:
        """Constructor for the RDSLogicalPreviewQueryResult class."""

        # Initialize members of the class
        self.columns: Sequence[rds_database_table_column_.RDSDatabaseTableColumn] = columns
        self.rows: Sequence[Sequence[str]] = rows

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

        # Extract variables from the dictionary
        val = dictionary['columns']

        val_columns = None
        if val:
            val_columns = list()
            for value in val:
                val_columns.append(
                    rds_database_table_column_.RDSDatabaseTableColumn.from_dictionary(value)
                )

        val = dictionary['rows']
        val_rows = val

        # Return an object of this model
        return cls(
            val_columns,  # type: ignore
            val_rows,  # type: ignore
        )
