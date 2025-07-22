#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='BackupStatus')


class BackupStatus:
    """Implementation of the 'BackupStatus' model.

    BackupStatus is the status of the backup. Possible values are`success`,
    `partial_success`, `failure`, `no_backup`, and `unknown`. This valuedepends on
    `lookback_days`. If not specified, then this field has a value of `unknown`.

    Attributes:
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {}

    def __init__(
        self,
    ) -> None:
        """Constructor for the BackupStatus class."""

        # Initialize members of the class

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

        # Return an object of this model
        return cls()
