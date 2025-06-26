#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_endpoint

T = TypeVar('T', bound='S3InstantAccessEndpointListEmbedded')


class S3InstantAccessEndpointListEmbedded:
    """Implementation of the 'S3InstantAccessEndpointListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(
        self, items: Sequence[s3_instant_access_endpoint.S3InstantAccessEndpoint] = None
    ) -> None:
        """Constructor for the S3InstantAccessEndpointListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[s3_instant_access_endpoint.S3InstantAccessEndpoint] = items

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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(
                    s3_instant_access_endpoint.S3InstantAccessEndpoint.from_dictionary(value)
                )

        # Return an object of this model
        return cls(items)
