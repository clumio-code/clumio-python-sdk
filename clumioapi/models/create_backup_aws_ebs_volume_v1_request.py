#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateBackupAwsEbsVolumeV1Request')


class CreateBackupAwsEbsVolumeV1Request:
    """Implementation of the 'CreateBackupAwsEbsVolumeV1Request' model.

    Attributes:
        volume_id:
            Performs the operation on the EBS volume with the specified Clumio-assigned ID.
    """

    # Create a mapping from Model property names to API property names
    _names = {'volume_id': 'volume_id'}

    def __init__(self, volume_id: str = None) -> None:
        """Constructor for the CreateBackupAwsEbsVolumeV1Request class."""

        # Initialize members of the class
        self.volume_id: str = volume_id

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
        volume_id = dictionary.get('volume_id')
        # Return an object of this model
        return cls(volume_id)
