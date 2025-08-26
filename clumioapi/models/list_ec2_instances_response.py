#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_instance_list_embedded as ec2_instance_list_embedded_
from clumioapi.models import ec2_instance_list_links as ec2_instance_list_links_

T = TypeVar('T', bound='ListEc2InstancesResponse')


class ListEc2InstancesResponse:
    """Implementation of the 'ListEc2InstancesResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page number used to get this response.
            Pages are indexed starting from 1 (i.e., `"start": "1"`).
        total_count:
            The total number of items, summed across all pages.
        total_pages_count:
            The total number of pages of results.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
        'total_count': 'total_count',
        'total_pages_count': 'total_pages_count',
    }

    def __init__(
        self,
        embedded: ec2_instance_list_embedded_.Ec2InstanceListEmbedded | None = None,
        links: ec2_instance_list_links_.EC2InstanceListLinks | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
        total_count: int | None = None,
        total_pages_count: int | None = None,
    ) -> None:
        """Constructor for the ListEc2InstancesResponse class."""

        # Initialize members of the class
        self.embedded: ec2_instance_list_embedded_.Ec2InstanceListEmbedded | None = embedded
        self.links: ec2_instance_list_links_.EC2InstanceListLinks | None = links
        self.current_count: int | None = current_count
        self.limit: int | None = limit
        self.start: str | None = start
        self.total_count: int | None = total_count
        self.total_pages_count: int | None = total_pages_count

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
        val_embedded = ec2_instance_list_embedded_.Ec2InstanceListEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_instance_list_links_.EC2InstanceListLinks.from_dictionary(val)

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        val = dictionary.get('total_count', None)
        val_total_count = val

        val = dictionary.get('total_pages_count', None)
        val_total_pages_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_start,
            val_total_count,
            val_total_pages_count,
        )
