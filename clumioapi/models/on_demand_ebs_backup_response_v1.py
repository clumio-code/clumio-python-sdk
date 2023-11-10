#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_ebs_backup_links
from clumioapi.models import read_task_hateoas_outer_embedded

T = TypeVar('T', bound='OnDemandEBSBackupResponseV1')


class OnDemandEBSBackupResponseV1:
    """Implementation of the 'OnDemandEBSBackupResponseV1' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        task_id:
            The Clumio-assigned ID of the task created for EBS backup.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = None,
        links: on_demand_ebs_backup_links.OnDemandEBSBackupLinks = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the OnDemandEBSBackupResponseV1 class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = embedded
        self.links: on_demand_ebs_backup_links.OnDemandEBSBackupLinks = links
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
            read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            on_demand_ebs_backup_links.OnDemandEBSBackupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, task_id)
