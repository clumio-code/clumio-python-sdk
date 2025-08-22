#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object as object_
from clumioapi.models import protection_group_restore_target as protection_group_restore_target_

T = TypeVar('T', bound='RestoreProtectionGroupS3ObjectsV1Request')


class RestoreProtectionGroupS3ObjectsV1Request:
    """Implementation of the 'RestoreProtectionGroupS3ObjectsV1Request' model.

    Attributes:
        source:
            Objects to restore. These objects must
            belong to a single bucket.
        target:
            The destination where the protection group will be restored.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: Sequence[object_.Object] | None = None,
        target: protection_group_restore_target_.ProtectionGroupRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreProtectionGroupS3ObjectsV1Request class."""

        # Initialize members of the class
        self.source: Sequence[object_.Object] | None = source
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

        val_source = None
        if val:
            val_source = list()
            for value in val:
                val_source.append(object_.Object.from_dictionary(value))

        val = dictionary.get('target', None)
        val_target = protection_group_restore_target_.ProtectionGroupRestoreTarget.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
