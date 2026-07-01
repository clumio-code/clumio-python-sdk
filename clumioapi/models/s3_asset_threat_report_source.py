#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import s3_asset_backup_time_range as s3_asset_backup_time_range_
from clumioapi.models import s3_asset_threat_scan_task as s3_asset_threat_scan_task_
from clumioapi.models import \
    threat_report_protection_group_backup as threat_report_protection_group_backup_
import requests

T = TypeVar('T', bound='S3AssetThreatReportSource')


@dataclasses.dataclass
class S3AssetThreatReportSource:
    """Implementation of the 'S3AssetThreatReportSource' model.

    The parameters to specify how to generate the threat report for protection group
    S3 asset.Must set exactly one of the options.

    Attributes:
        BackupTimeRange:
            The parameters to generate the report of malicious objects detected within
            backup time range.

        ProtectionGroupBackup:
            The parameters to specify s3 asset backup by protection group and s3 asset id.

        S3AssetBackupId:
            Option to generate threat report using s3assetbackupid.
            this is an clumio-assigned id of the protection group s3 asset backup. use the
            [get /backups/protection-groups/s3-assets](#operation/list-backup-protection-
            group-s3-assets)
            endpoint to fetch valid values.

        ThreatScanTask:
            The parameters to generate the report of malicious objects detected in a
            specific threat scan task.

    """

    BackupTimeRange: s3_asset_backup_time_range_.S3AssetBackupTimeRange | None = None
    ProtectionGroupBackup: (
        threat_report_protection_group_backup_.ThreatReportProtectionGroupBackup | None
    ) = None
    S3AssetBackupId: str | None = None
    ThreatScanTask: s3_asset_threat_scan_task_.S3AssetThreatScanTask | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('backup_time_range', None)
        val_backup_time_range = s3_asset_backup_time_range_.S3AssetBackupTimeRange.from_dictionary(
            val
        )

        val = dictionary.get('protection_group_backup', None)
        val_protection_group_backup = threat_report_protection_group_backup_.ThreatReportProtectionGroupBackup.from_dictionary(
            val
        )

        val = dictionary.get('s3_asset_backup_id', None)
        val_s3_asset_backup_id = val

        val = dictionary.get('threat_scan_task', None)
        val_threat_scan_task = s3_asset_threat_scan_task_.S3AssetThreatScanTask.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_backup_time_range,
            val_protection_group_backup,
            val_s3_asset_backup_id,
            val_threat_scan_task,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
