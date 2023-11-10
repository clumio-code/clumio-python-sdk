#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_embedded
from clumioapi.models import organizational_unit_links_for_delete

T = TypeVar('T', bound='DeleteOrganizationalUnitResponse')


class DeleteOrganizationalUnitResponse:
    """Implementation of the 'DeleteOrganizationalUnitResponse' model.

    Accepted

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        task_id:
            The Clumio-assigned ID of the task associated with this organizational unit.
            The progress of the task can be monitored using the
            [GET /tasks/{task_id}](#operation/read-task) endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: entity_group_embedded.EntityGroupEmbedded = None,
        links: organizational_unit_links_for_delete.OrganizationalUnitLinksForDelete = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the DeleteOrganizationalUnitResponse class."""

        # Initialize members of the class
        self.embedded: entity_group_embedded.EntityGroupEmbedded = embedded
        self.links: organizational_unit_links_for_delete.OrganizationalUnitLinksForDelete = links
        self.task_id: str = task_id

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
            entity_group_embedded.EntityGroupEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            organizational_unit_links_for_delete.OrganizationalUnitLinksForDelete.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, task_id)
