#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsEbsVolumesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsEbsVolumesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsEbsVolumesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains', 'eq'], list | str]] = None
    VolumeNativeId: Optional[dict[Literal['eq', 'contains'], list | str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    ProtectionStatus: Optional[dict[Literal['eq', 'in'], list | str]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    ProtectionInfo: Optional[ListAwsEbsVolumesProtectionInfoV1T] = None
    Tags: Optional[ListAwsEbsVolumesTagsV1T] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
