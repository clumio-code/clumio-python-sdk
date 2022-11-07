#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import set_bucket_properties_response_links

T = TypeVar('T', bound='SetBucketPropertiesResponse')


class SetBucketPropertiesResponse:
    """Implementation of the 'SetBucketPropertiesResponse' model.

    Accepted

    Attributes:
        links:

    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links'}

    def __init__(
        self, links: set_bucket_properties_response_links.SetBucketPropertiesResponseLinks = None
    ) -> None:
        """Constructor for the SetBucketPropertiesResponse class."""

        # Initialize members of the class
        self.links: set_bucket_properties_response_links.SetBucketPropertiesResponseLinks = links

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
            set_bucket_properties_response_links.SetBucketPropertiesResponseLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links)
