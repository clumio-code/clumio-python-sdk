#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import retention_backup_sla_param as retention_backup_sla_param_
from clumioapi.models import rpo_backup_sla_param as rpo_backup_sla_param_

T = TypeVar('T', bound='BackupSLA')


class BackupSLA:
    """Implementation of the 'BackupSLA' model.

    backup_sla captures the SLA parametersbackup_sla captures the SLA parameters

    Attributes:
        retention_duration:
            The retention time for this SLA. For example, to retain the backup for 1 month,
            set `unit="months"` and `value=1`.
        rpo_frequency:
            The minimum frequency between backups for this SLA. Also known as the recovery
            point objective (RPO) interval.
            For example, to configure the minimum frequency between backups to be every 2
            days, set `unit="days"` and `value=2`.
            To configure the SLA for on-demand backups, set `unit="on_demand"` and leave the
            `value` field empty.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'retention_duration': 'retention_duration',
        'rpo_frequency': 'rpo_frequency',
    }

    def __init__(
        self,
        retention_duration: retention_backup_sla_param_.RetentionBackupSLAParam | None = None,
        rpo_frequency: rpo_backup_sla_param_.RPOBackupSLAParam | None = None,
    ) -> None:
        """Constructor for the BackupSLA class."""

        # Initialize members of the class
        self.retention_duration: retention_backup_sla_param_.RetentionBackupSLAParam | None = (
            retention_duration
        )
        self.rpo_frequency: rpo_backup_sla_param_.RPOBackupSLAParam | None = rpo_frequency

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
        val = dictionary.get('retention_duration', None)
        val_retention_duration = (
            retention_backup_sla_param_.RetentionBackupSLAParam.from_dictionary(val)
        )

        val = dictionary.get('rpo_frequency', None)
        val_rpo_frequency = rpo_backup_sla_param_.RPOBackupSLAParam.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_retention_duration,
            val_rpo_frequency,
        )
