#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_source as s3_instant_access_source_

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
    _names: dict[str, str] = {
        'expiry_timestamp': 'expiry_timestamp',
        'name': 'name',
        'source': 'source',
    }

    def __init__(
        self,
        expiry_timestamp: str | None = None,
        name: str | None = None,
        source: s3_instant_access_source_.S3InstantAccessSource | None = None,
    ) -> None:
        """Constructor for the CreateProtectionGroupInstantAccessEndpointV1Request class."""

        # Initialize members of the class
        self.expiry_timestamp: str | None = expiry_timestamp
        self.name: str | None = name
        self.source: s3_instant_access_source_.S3InstantAccessSource | None = source

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
        val = dictionary.get('expiry_timestamp', None)
        val_expiry_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('source', None)
        val_source = s3_instant_access_source_.S3InstantAccessSource.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_expiry_timestamp,
            val_name,
            val_source,
        )
