#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    rds_resource_restore_source_air_gap_options as rds_resource_restore_source_air_gap_options_
from clumioapi.models import \
    rds_resource_restore_source_pitr_options as rds_resource_restore_source_pitr_options_

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
    _names: dict[str, str] = {'backup': 'backup', 'snapshot': 'snapshot'}

    def __init__(
        self,
        backup: (
            rds_resource_restore_source_air_gap_options_.RdsResourceRestoreSourceAirGapOptions
            | None
        ) = None,
        snapshot: (
            rds_resource_restore_source_pitr_options_.RdsResourceRestoreSourcePitrOptions | None
        ) = None,
    ) -> None:
        """Constructor for the RdsResourceRestoreSource class."""

        # Initialize members of the class
        self.backup: (
            rds_resource_restore_source_air_gap_options_.RdsResourceRestoreSourceAirGapOptions
            | None
        ) = backup
        self.snapshot: (
            rds_resource_restore_source_pitr_options_.RdsResourceRestoreSourcePitrOptions | None
        ) = snapshot

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
        val = dictionary.get('backup', None)
        val_backup = rds_resource_restore_source_air_gap_options_.RdsResourceRestoreSourceAirGapOptions.from_dictionary(
            val
        )

        val = dictionary.get('snapshot', None)
        val_snapshot = rds_resource_restore_source_pitr_options_.RdsResourceRestoreSourcePitrOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_backup,
            val_snapshot,
        )
