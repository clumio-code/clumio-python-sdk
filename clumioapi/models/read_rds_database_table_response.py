#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_database_table_embedded
from clumioapi.models import rds_database_table_links

T = TypeVar('T', bound='ReadRDSDatabaseTableResponse')


class ReadRDSDatabaseTableResponse:
    """Implementation of the 'ReadRDSDatabaseTableResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        name:
            The name of the table within the specified RDS database.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'name': 'name'}

    def __init__(
        self,
        embedded: rds_database_table_embedded.RDSDatabaseTableEmbedded = None,
        links: rds_database_table_links.RDSDatabaseTableLinks = None,
        name: str = None,
    ) -> None:
        """Constructor for the ReadRDSDatabaseTableResponse class."""

        # Initialize members of the class
        self.embedded: rds_database_table_embedded.RDSDatabaseTableEmbedded = embedded
        self.links: rds_database_table_links.RDSDatabaseTableLinks = links
        self.name: str = name

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
        key = '_embedded'
        embedded = (
            rds_database_table_embedded.RDSDatabaseTableEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            rds_database_table_links.RDSDatabaseTableLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        name = dictionary.get('name')
        # Return an object of this model
        return cls(embedded, links, name)
