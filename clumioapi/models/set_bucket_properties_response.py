#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    set_bucket_properties_response_links as set_bucket_properties_response_links_

T = TypeVar('T', bound='SetBucketPropertiesResponse')


class SetBucketPropertiesResponse:
    """Implementation of the 'SetBucketPropertiesResponse' model.

    Accepted

    Attributes:
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links'}

    def __init__(
        self, links: set_bucket_properties_response_links_.SetBucketPropertiesResponseLinks
    ) -> None:
        """Constructor for the SetBucketPropertiesResponse class."""

        # Initialize members of the class
        self.links: set_bucket_properties_response_links_.SetBucketPropertiesResponseLinks = links

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
        val = dictionary['_links']
        val_links = (
            set_bucket_properties_response_links_.SetBucketPropertiesResponseLinks.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
        )
