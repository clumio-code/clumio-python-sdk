#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateProtectionGroupInstantAccessEndpointV1Request')


class UpdateProtectionGroupInstantAccessEndpointV1Request:
    """Implementation of the 'UpdateProtectionGroupInstantAccessEndpointV1Request' model.

    Attributes:
        expiry_timestamp:
            The time that this endpoint expires, in RFC-3339 format. This will revert to
            default if no
            state passed.
        name:
            The user-assigned name of the S3 instant access endpoint. This will be removed
            if left empty.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'expiry_timestamp': 'expiry_timestamp', 'name': 'name'}

    def __init__(self, expiry_timestamp: str, name: str) -> None:
        """Constructor for the UpdateProtectionGroupInstantAccessEndpointV1Request class."""

        # Initialize members of the class
        self.expiry_timestamp: str = expiry_timestamp
        self.name: str = name

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

        # Return an object of this model
        return cls(
            val_expiry_timestamp,  # type: ignore
            val_name,  # type: ignore
        )
