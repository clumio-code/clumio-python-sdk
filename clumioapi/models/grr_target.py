#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='GrrTarget')


class GrrTarget:
    """Implementation of the 'GrrTarget' model.

    The query to perform on the source RDS database.

    Attributes:
        preview:
            Determines whether the query is preview only. If `true`, a preview of the
            query results will be provided in the response immediately.
            If `false` or omitted, a task will be queued to make the result
            of the query available for asynchronous download.
        query_statement:
            The SQL statement that is to be executed on the target database.
            For example, "SELECT * FROM employee WHERE id > 100"
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'preview': 'preview', 'query_statement': 'query_statement'}

    def __init__(self, preview: bool | None = None, query_statement: str | None = None) -> None:
        """Constructor for the GrrTarget class."""

        # Initialize members of the class
        self.preview: bool | None = preview
        self.query_statement: str | None = query_statement

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
        val = dictionary.get('preview', None)
        val_preview = val

        val = dictionary.get('query_statement', None)
        val_query_statement = val

        # Return an object of this model
        return cls(
            val_preview,
            val_query_statement,
        )
