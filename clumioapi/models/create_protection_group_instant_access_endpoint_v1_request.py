#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_source

T = TypeVar('T', bound='CreateProtectionGroupInstantAccessEndpointV1Request')


class CreateProtectionGroupInstantAccessEndpointV1Request:
    """Implementation of the 'CreateProtectionGroupInstantAccessEndpointV1Request' model.

    Attributes:
        expiry_timestamp:
            The time that this endpoint expires at in RFC-3339 format.
        name:
            The user-assigned name of the S3 instant access endpoint.
        source:
            The parameters for creating a S3 instant access endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'expiry_timestamp': 'expiry_timestamp', 'name': 'name', 'source': 'source'}

    def __init__(
        self,
        expiry_timestamp: str = None,
        name: str = None,
        source: s3_instant_access_source.S3InstantAccessSource = None,
    ) -> None:
        """Constructor for the CreateProtectionGroupInstantAccessEndpointV1Request class."""

        # Initialize members of the class
        self.expiry_timestamp: str = expiry_timestamp
        self.name: str = name
        self.source: s3_instant_access_source.S3InstantAccessSource = source

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
        expiry_timestamp = dictionary.get('expiry_timestamp')
        name = dictionary.get('name')
        key = 'source'
        source = (
            s3_instant_access_source.S3InstantAccessSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(expiry_timestamp, name, source)
