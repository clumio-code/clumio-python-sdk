#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import preview_s3_bucket_links

T = TypeVar('T', bound='PreviewS3BucketResponse')


class PreviewS3BucketResponse:
    """Implementation of the 'PreviewS3BucketResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        preview_id:
            The identifier for the requested preview which is used to fetch results of the
            preview.
        task_id:
            The Clumio-assigned ID of the task created by this preview request.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'preview_id': 'preview_id', 'task_id': 'task_id'}

    def __init__(
        self,
        links: preview_s3_bucket_links.PreviewS3BucketLinks = None,
        preview_id: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the PreviewS3BucketResponse class."""

        # Initialize members of the class
        self.links: preview_s3_bucket_links.PreviewS3BucketLinks = links
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
            preview_s3_bucket_links.PreviewS3BucketLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        preview_id = dictionary.get('preview_id')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(links, preview_id, task_id)
