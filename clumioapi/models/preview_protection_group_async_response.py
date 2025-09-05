#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    preview_protection_group_async_links as preview_protection_group_async_links_

T = TypeVar('T', bound='PreviewProtectionGroupAsyncResponse')


class PreviewProtectionGroupAsyncResponse:
    """Implementation of the 'PreviewProtectionGroupAsyncResponse' model.

    Success (Async)

    Attributes:
        links:
            URLs to pages related to the resource.
        preview_id:
            The identifier for the requested preview which is used to fetch results of the
            preview.
            Note that this field is given only for async request.
        task_id:
            The Clumio-assigned ID of the task created by this restore request.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
            Note that this field is given only for async request.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'preview_id': 'preview_id', 'task_id': 'task_id'}

    def __init__(
        self,
        links: preview_protection_group_async_links_.PreviewProtectionGroupAsyncLinks | None = None,
        preview_id: str | None = None,
        task_id: str | None = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupAsyncResponse class."""

        # Initialize members of the class
        self.links: (
            preview_protection_group_async_links_.PreviewProtectionGroupAsyncLinks | None
        ) = links
        self.preview_id: str | None = preview_id
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
        val = dictionary.get('_links', None)
        val_links = (
            preview_protection_group_async_links_.PreviewProtectionGroupAsyncLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('preview_id', None)
        val_preview_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_preview_id,
            val_task_id,
        )
