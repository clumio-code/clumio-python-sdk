#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_links

T = TypeVar('T', bound='DeleteRuleResponse')


class DeleteRuleResponse:
    """Implementation of the 'DeleteRuleResponse' model.

    Attributes:
        links:
            Embedded responses related to the resource.
        preview_id:
            The Clumio-assigned ID of the preview generated by this request. Only valid if
            `execution_type` is set to `dryrun`.
        task_id:
            The Clumio-assigned ID of the task generated by this request.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'preview_id': 'preview_id', 'task_id': 'task_id'}

    def __init__(
        self,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        preview_id: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the DeleteRuleResponse class."""

        # Initialize members of the class
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links
        self.preview_id: str = preview_id
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
        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        preview_id = dictionary.get('preview_id')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(links, preview_id, task_id)
