#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_restore_source_v1
from clumioapi.models import ebs_restore_target_v1

T = TypeVar('T', bound='RestoreAwsEbsVolumeV1Request')


class RestoreAwsEbsVolumeV1Request:
    """Implementation of the 'RestoreAwsEbsVolumeV1Request' model.

    Attributes:
        source:
            The EBS volume backup to be restored.
        target:
            The configuration of the EBS volume to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ebs_restore_source_v1.EBSRestoreSourceV1 = None,
        target: ebs_restore_target_v1.EBSRestoreTargetV1 = None,
    ) -> None:
        """Constructor for the RestoreAwsEbsVolumeV1Request class."""

        # Initialize members of the class
        self.source: ebs_restore_source_v1.EBSRestoreSourceV1 = source
        self.target: ebs_restore_target_v1.EBSRestoreTargetV1 = target

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
        key = 'source'
        source = (
            ebs_restore_source_v1.EBSRestoreSourceV1.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            ebs_restore_target_v1.EBSRestoreTargetV1.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
