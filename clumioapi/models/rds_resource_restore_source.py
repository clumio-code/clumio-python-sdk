#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_resource_restore_source_air_gap_options
from clumioapi.models import rds_resource_restore_source_pitr_options

T = TypeVar('T', bound='RdsResourceRestoreSource')


class RdsResourceRestoreSource:
    """Implementation of the 'RdsResourceRestoreSource' model.

    The RDS resource backup or snapshot to be restored.  Only one of these fields
    should be set.

    Attributes:
        backup:
            The parameters for initiating an RDS restore from a backup.
        snapshot:
            The parameters for initiating an RDS restore from a snapshot.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup': 'backup', 'snapshot': 'snapshot'}

    def __init__(
        self,
        backup: rds_resource_restore_source_air_gap_options.RdsResourceRestoreSourceAirGapOptions = None,
        snapshot: rds_resource_restore_source_pitr_options.RdsResourceRestoreSourcePitrOptions = None,
    ) -> None:
        """Constructor for the RdsResourceRestoreSource class."""

        # Initialize members of the class
        self.backup: rds_resource_restore_source_air_gap_options.RdsResourceRestoreSourceAirGapOptions = (
            backup
        )
        self.snapshot: rds_resource_restore_source_pitr_options.RdsResourceRestoreSourcePitrOptions = (
            snapshot
        )

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
        key = 'backup'
        backup = (
            rds_resource_restore_source_air_gap_options.RdsResourceRestoreSourceAirGapOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'snapshot'
        snapshot = (
            rds_resource_restore_source_pitr_options.RdsResourceRestoreSourcePitrOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(backup, snapshot)
