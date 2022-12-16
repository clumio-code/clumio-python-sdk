#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_links
from clumioapi.models import read_task_hateoas_outer_embedded

T = TypeVar('T', bound='OnDemandMssqlBackupResponse')


class OnDemandMssqlBackupResponse:
    """Implementation of the 'OnDemandMssqlBackupResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links'}

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = None,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
    ) -> None:
        """Constructor for the OnDemandMssqlBackupResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = embedded
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links

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
            read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links)
