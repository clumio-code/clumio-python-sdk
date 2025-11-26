#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupProtectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], int | str]] = None


class ListBackupProtectionGroupS3AssetsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    ProtectionGroupS3AssetId: Optional[dict[Literal['eq'], str]] = None
    ParentProtectionGroupBackupId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], int | str]] = None
    BucketRegion: Optional[dict[Literal['eq'], str]] = None
