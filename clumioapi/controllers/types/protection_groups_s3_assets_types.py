#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListProtectionGroupS3AssetsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListProtectionGroupS3AssetsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    BucketId: Optional[dict[Literal['eq'], str]] = None
    BucketName: Optional[dict[Literal['eq', 'contains'], list | str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListProtectionGroupS3AssetsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AddedBy: Optional[dict[Literal['in'], list]] = None
    IsSupported: Optional[dict[Literal['eq'], bool]] = None


class ListProtectionGroupS3AssetPitrIntervalsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    Timestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
