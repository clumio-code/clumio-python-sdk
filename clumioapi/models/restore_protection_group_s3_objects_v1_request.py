#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object
from clumioapi.models import protection_group_restore_target

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
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: Sequence[object.Object] = None,
        target: protection_group_restore_target.ProtectionGroupRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreProtectionGroupS3ObjectsV1Request class."""

        # Initialize members of the class
        self.source: Sequence[object.Object] = source
        self.target: protection_group_restore_target.ProtectionGroupRestoreTarget = target

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
        source = None
        if dictionary.get('source'):
            source = list()
            for value in dictionary.get('source'):
                source.append(object.Object.from_dictionary(value))

        key = 'target'
        target = (
            protection_group_restore_target.ProtectionGroupRestoreTarget.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
