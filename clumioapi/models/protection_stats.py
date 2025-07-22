#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionStats')


class ProtectionStats:
    """Implementation of the 'ProtectionStats' model.

    Attributes:
        deactivated_count:
            The total number of entities associated with deactivated policies.
        protected_count:
            The number of entities with protection applied.
        unprotected_count:
            The number of entities without protection applied.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'deactivated_count': 'deactivated_count',
        'protected_count': 'protected_count',
        'unprotected_count': 'unprotected_count',
    }

    def __init__(
        self, deactivated_count: int, protected_count: int, unprotected_count: int
    ) -> None:
        """Constructor for the ProtectionStats class."""

        # Initialize members of the class
        self.deactivated_count: int = deactivated_count
        self.protected_count: int = protected_count
        self.unprotected_count: int = unprotected_count

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
        val = dictionary['deactivated_count']
        val_deactivated_count = val

        val = dictionary['protected_count']
        val_protected_count = val

        val = dictionary['unprotected_count']
        val_unprotected_count = val

        # Return an object of this model
        return cls(
            val_deactivated_count,  # type: ignore
            val_protected_count,  # type: ignore
            val_unprotected_count,  # type: ignore
        )
