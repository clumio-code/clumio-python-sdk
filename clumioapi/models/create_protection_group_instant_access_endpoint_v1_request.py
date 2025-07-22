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
        expiry_timestamp: str,
        name: str,
        source: s3_instant_access_source_.S3InstantAccessSource,
    ) -> None:
        """Constructor for the CreateProtectionGroupInstantAccessEndpointV1Request class."""

        # Initialize members of the class
        self.expiry_timestamp: str = expiry_timestamp
        self.name: str = name
        self.source: s3_instant_access_source_.S3InstantAccessSource = source

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
        val = dictionary['expiry_timestamp']
        val_expiry_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['source']
        val_source = s3_instant_access_source_.S3InstantAccessSource.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_expiry_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_source,  # type: ignore
        )
