#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='IamInstanceProfileModel')


class IamInstanceProfileModel:
    """Implementation of the 'IamInstanceProfileModel' model.

    Denotes an IAM instance profile. An instance profile is a container for anIAM
    role that you can use to pass role information to an EC2 instance whenthe
    instance starts.

    Attributes:
        arn:
            The Amazon Resource Name (ARN) specifying the IAM instance profile.
        name:
            The AWS-assigned name of the IAM instance profile.
        native_id:
            The AWS-assigned ID of the IAM instance profile.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'arn': 'arn', 'name': 'name', 'native_id': 'native_id'}

    def __init__(
        self, arn: str | None = None, name: str | None = None, native_id: str | None = None
    ) -> None:
        """Constructor for the IamInstanceProfileModel class."""

        # Initialize members of the class
        self.arn: str | None = arn
        self.name: str | None = name
        self.native_id: str | None = native_id

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
        val = dictionary.get('arn', None)
        val_arn = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('native_id', None)
        val_native_id = val

        # Return an object of this model
        return cls(
            val_arn,
            val_name,
            val_native_id,
        )
