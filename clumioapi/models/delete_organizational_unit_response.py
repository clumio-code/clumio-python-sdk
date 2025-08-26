#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_embedded as entity_group_embedded_
from clumioapi.models import \
    organizational_unit_links_for_delete as organizational_unit_links_for_delete_

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
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: entity_group_embedded_.EntityGroupEmbedded | None = None,
        links: organizational_unit_links_for_delete_.OrganizationalUnitLinksForDelete | None = None,
        task_id: str | None = None,
    ) -> None:
        """Constructor for the DeleteOrganizationalUnitResponse class."""

        # Initialize members of the class
        self.embedded: entity_group_embedded_.EntityGroupEmbedded | None = embedded
        self.links: (
            organizational_unit_links_for_delete_.OrganizationalUnitLinksForDelete | None
        ) = links
        self.task_id: str | None = task_id

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
        val = dictionary.get('_embedded', None)
        val_embedded = entity_group_embedded_.EntityGroupEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = (
            organizational_unit_links_for_delete_.OrganizationalUnitLinksForDelete.from_dictionary(
                val
            )
        )

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_task_id,
        )
