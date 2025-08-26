#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rds_database_table_embedded as rds_database_table_embedded_
from clumioapi.models import rds_database_table_links as rds_database_table_links_
import requests

T = TypeVar('T', bound='ReadRDSDatabaseTableResponse')


@dataclasses.dataclass
class ReadRDSDatabaseTableResponse:
    """Implementation of the 'ReadRDSDatabaseTableResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Name:
            The name of the table within the specified rds database.

    """

    Embedded: rds_database_table_embedded_.RDSDatabaseTableEmbedded | None = None
    Links: rds_database_table_links_.RDSDatabaseTableLinks | None = None
    Name: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
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
        val = dictionary.get('_embedded', None)
        val_embedded = rds_database_table_embedded_.RDSDatabaseTableEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = rds_database_table_links_.RDSDatabaseTableLinks.from_dictionary(val)

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_name,
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
        model_instance.raw_response = response
        return model_instance
