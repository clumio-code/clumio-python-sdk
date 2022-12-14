#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_restore_source
from clumioapi.models import ebs_restore_target

T = TypeVar('T', bound='RestoreAwsEbsVolumeV2Request')


class RestoreAwsEbsVolumeV2Request:
    """Implementation of the 'RestoreAwsEbsVolumeV2Request' model.

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
        source: ebs_restore_source.EBSRestoreSource = None,
        target: ebs_restore_target.EBSRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreAwsEbsVolumeV2Request class."""

        # Initialize members of the class
        self.source: ebs_restore_source.EBSRestoreSource = source
        self.target: ebs_restore_target.EBSRestoreTarget = target

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
            ebs_restore_source.EBSRestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            ebs_restore_target.EBSRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
