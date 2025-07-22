#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_environment_list_embedded as aws_environment_list_embedded_
from clumioapi.models import aws_environment_list_links as aws_environment_list_links_

T = TypeVar('T', bound='ListAWSEnvironmentsResponse')


class ListAWSEnvironmentsResponse:
    """Implementation of the 'ListAWSEnvironmentsResponse' model.

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
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: aws_environment_list_embedded_.AWSEnvironmentListEmbedded,
        links: aws_environment_list_links_.AWSEnvironmentListLinks,
        current_count: int,
        limit: int,
        start: str,
    ) -> None:
        """Constructor for the ListAWSEnvironmentsResponse class."""

        # Initialize members of the class
        self.embedded: aws_environment_list_embedded_.AWSEnvironmentListEmbedded = embedded
        self.links: aws_environment_list_links_.AWSEnvironmentListLinks = links
        self.current_count: int = current_count
        self.limit: int = limit
        self.start: str = start

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = aws_environment_list_embedded_.AWSEnvironmentListEmbedded.from_dictionary(
            val
        )

        val = dictionary['_links']
        val_links = aws_environment_list_links_.AWSEnvironmentListLinks.from_dictionary(val)

        val = dictionary['current_count']
        val_current_count = val

        val = dictionary['limit']
        val_limit = val

        val = dictionary['start']
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_current_count,  # type: ignore
            val_limit,  # type: ignore
            val_start,  # type: ignore
        )
