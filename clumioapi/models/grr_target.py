#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='GrrTarget')


@dataclasses.dataclass
class GrrTarget:
    """Implementation of the 'GrrTarget' model.

    The query to perform on the source RDS database.

    Attributes:
        Preview:
            Determines whether the query is preview only. if `true`, a preview of the
            query results will be provided in the response immediately.
            if `false` or omitted, a task will be queued to make the result
            of the query available for asynchronous download.

        QueryStatement:
            The sql statement that is to be executed on the target database.
            for example, "select * from employee where id > 100".

    """

    Preview: bool | None = None
    QueryStatement: str | None = None

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
        val = dictionary.get('preview', None)
        val_preview = val

        val = dictionary.get('query_statement', None)
        val_query_statement = val

        # Return an object of this model
        return cls(
            val_preview,
            val_query_statement,
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
