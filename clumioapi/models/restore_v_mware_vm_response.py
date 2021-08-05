#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_links

T = TypeVar('T', bound='RestoreVMwareVMResponse')


class RestoreVMwareVMResponse:
    """Implementation of the 'RestoreVMwareVMResponse' model.

    Attributes:
        embedded:
            URLs to pages related to the resource.
        links:
            URLs to pages related to the resource.
        task_id:
            The Clumio-assigned ID of the task created by this restore request. The progress
            of the task can be monitored using the `GET /tasks/{task_id}` endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the RestoreVMwareVMResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_links.ReadTaskHateoasLinks = embedded
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links
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
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, task_id)
