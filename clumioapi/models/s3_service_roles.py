#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3ServiceRoles')


class S3ServiceRoles:
    """Implementation of the 'S3ServiceRoles' model.

    Attributes:
        continuous_backups_role_arn:
            Role assumable by Event Bridge to send event notifications.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'continuous_backups_role_arn': 'continuous_backups_role_arn'}

    def __init__(self, continuous_backups_role_arn: str) -> None:
        """Constructor for the S3ServiceRoles class."""

        # Initialize members of the class
        self.continuous_backups_role_arn: str = continuous_backups_role_arn

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
        val = dictionary['continuous_backups_role_arn']
        val_continuous_backups_role_arn = val

        # Return an object of this model
        return cls(
            val_continuous_backups_role_arn,  # type: ignore
        )
