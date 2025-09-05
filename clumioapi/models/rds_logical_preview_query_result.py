#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rds_database_table_column as rds_database_table_column_
import requests

T = TypeVar('T', bound='RDSLogicalPreviewQueryResult')


@dataclasses.dataclass
class RDSLogicalPreviewQueryResult:
    """Implementation of the 'RDSLogicalPreviewQueryResult' model.

        The preview of the query result, if `preview:true` in the request.If preview was
        not set to true in the request, then the result of the query will beavailable
        for download asynchronously.

        Attributes:
            Columns:
    The columns of the previewed query result.

            Rows:
    The rows of the previewed query result.

    """

    Columns: Sequence[rds_database_table_column_.RDSDatabaseTableColumn] | None = None
    Rows: Sequence[Sequence[str]] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('columns', None)

        val_columns = []
        if val:
            for value in val:
                val_columns.append(
                    rds_database_table_column_.RDSDatabaseTableColumn.from_dictionary(value)
                )

        val = dictionary.get('rows', None)
        val_rows = val

        # Return an object of this model
        return cls(
            val_columns,
            val_rows,
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
