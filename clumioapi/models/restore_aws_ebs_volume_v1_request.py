#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_restore_source_v1 as ebs_restore_source_v1_
from clumioapi.models import ebs_restore_target_v1 as ebs_restore_target_v1_

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
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ebs_restore_source_v1_.EBSRestoreSourceV1 | None = None,
        target: ebs_restore_target_v1_.EBSRestoreTargetV1 | None = None,
    ) -> None:
        """Constructor for the RestoreAwsEbsVolumeV1Request class."""

        # Initialize members of the class
        self.source: ebs_restore_source_v1_.EBSRestoreSourceV1 | None = source
        self.target: ebs_restore_target_v1_.EBSRestoreTargetV1 | None = target

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
        val_source = ebs_restore_source_v1_.EBSRestoreSourceV1.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = ebs_restore_target_v1_.EBSRestoreTargetV1.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
