#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_embedded as rds_database_table_embedded_
from clumioapi.models import rds_database_table_links as rds_database_table_links_

T = TypeVar('T', bound='RDSDatabaseTable')


class RDSDatabaseTable:
    """Implementation of the 'RDSDatabaseTable' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        name:
            The name of the table within the specified RDS database.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links', 'name': 'name'}

    def __init__(
        self,
        embedded: rds_database_table_embedded_.RDSDatabaseTableEmbedded,
        links: rds_database_table_links_.RDSDatabaseTableLinks,
        name: str,
    ) -> None:
        """Constructor for the RDSDatabaseTable class."""

        # Initialize members of the class
        self.embedded: rds_database_table_embedded_.RDSDatabaseTableEmbedded = embedded
        self.links: rds_database_table_links_.RDSDatabaseTableLinks = links
        self.name: str = name

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
        val = dictionary['_embedded']
        val_embedded = rds_database_table_embedded_.RDSDatabaseTableEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = rds_database_table_links_.RDSDatabaseTableLinks.from_dictionary(val)

        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_name,  # type: ignore
        )
