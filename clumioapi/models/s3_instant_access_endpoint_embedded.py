#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3InstantAccessEndpointEmbedded')


class S3InstantAccessEndpointEmbedded:
    """Implementation of the 'S3InstantAccessEndpointEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_protection_group_s3_asset:
            Embeds the associated protection group S3 asset
    """

    # Create a mapping from Model property names to API property names
    _names = {'read_protection_group_s3_asset': 'read-protection-group-s3-asset'}

    def __init__(self, read_protection_group_s3_asset: object = None) -> None:
        """Constructor for the S3InstantAccessEndpointEmbedded class."""

        # Initialize members of the class
        self.read_protection_group_s3_asset: object = read_protection_group_s3_asset

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
        read_protection_group_s3_asset = dictionary.get('read-protection-group-s3-asset')
        # Return an object of this model
        return cls(read_protection_group_s3_asset)
