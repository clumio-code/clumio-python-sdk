#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import retention_backup_sla_param
from clumioapi.models import rpo_backup_sla_param

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
    _names = {'retention_duration': 'retention_duration', 'rpo_frequency': 'rpo_frequency'}

    def __init__(
        self,
        retention_duration: retention_backup_sla_param.RetentionBackupSLAParam = None,
        rpo_frequency: rpo_backup_sla_param.RPOBackupSLAParam = None,
    ) -> None:
        """Constructor for the BackupSLA class."""

        # Initialize members of the class
        self.retention_duration: retention_backup_sla_param.RetentionBackupSLAParam = (
            retention_duration
        )
        self.rpo_frequency: rpo_backup_sla_param.RPOBackupSLAParam = rpo_frequency

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
        key = 'retention_duration'
        retention_duration = (
            retention_backup_sla_param.RetentionBackupSLAParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'rpo_frequency'
        rpo_frequency = (
            rpo_backup_sla_param.RPOBackupSLAParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(retention_duration, rpo_frequency)
