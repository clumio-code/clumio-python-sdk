#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_restore_source as protection_group_restore_source_
from clumioapi.models import protection_group_restore_target as protection_group_restore_target_

T = TypeVar('T', bound='RestoreProtectionGroupV1Request')


class RestoreProtectionGroupV1Request:
    """Implementation of the 'RestoreProtectionGroupV1Request' model.

    Attributes:
        source:
            The parameters for initiating a protection group restore from a backup.
        target:
            The destination where the protection group will be restored.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: protection_group_restore_source_.ProtectionGroupRestoreSource | None = None,
        target: protection_group_restore_target_.ProtectionGroupRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreProtectionGroupV1Request class."""

        # Initialize members of the class
        self.source: protection_group_restore_source_.ProtectionGroupRestoreSource | None = source
        self.target: protection_group_restore_target_.ProtectionGroupRestoreTarget | None = target

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
        val = dictionary.get('source', None)
        val_source = protection_group_restore_source_.ProtectionGroupRestoreSource.from_dictionary(
            val
        )

        val = dictionary.get('target', None)
        val_target = protection_group_restore_target_.ProtectionGroupRestoreTarget.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
