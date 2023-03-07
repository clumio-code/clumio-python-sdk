#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_outer_embedded
from clumioapi.models import restore_file_links

T = TypeVar('T', bound='RestoreFileResponse')


class RestoreFileResponse:
    """Implementation of the 'RestoreFileResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the restored file.
        passcode:
            The passcode that the end-user must use to access the restored
            file, in the case the restored file was emailed to the end-user as part
            of transparent data access.
        task_id:
            The Clumio-assigned ID of the task created by this restore request.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'p_id': 'id',
        'passcode': 'passcode',
        'task_id': 'task_id',
    }

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = None,
        links: restore_file_links.RestoreFileLinks = None,
        p_id: str = None,
        passcode: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the RestoreFileResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = embedded
        self.links: restore_file_links.RestoreFileLinks = links
        self.p_id: str = p_id
        self.passcode: str = passcode
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
            restore_file_links.RestoreFileLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        passcode = dictionary.get('passcode')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, p_id, passcode, task_id)
