#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_restore_source as ebs_restore_source_
from clumioapi.models import ebs_restore_target as ebs_restore_target_

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
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ebs_restore_source_.EBSRestoreSource | None = None,
        target: ebs_restore_target_.EBSRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreAwsEbsVolumeV2Request class."""

        # Initialize members of the class
        self.source: ebs_restore_source_.EBSRestoreSource | None = source
        self.target: ebs_restore_target_.EBSRestoreTarget | None = target

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
        val_source = ebs_restore_source_.EBSRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = ebs_restore_target_.EBSRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
