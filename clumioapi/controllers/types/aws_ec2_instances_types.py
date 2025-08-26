#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsEc2InstancesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsEc2InstancesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsEc2InstancesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains', 'eq'], list | str]] = None
    InstanceNativeId: Optional[dict[Literal['eq', 'contains'], list | str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListAwsEc2InstancesProtectionInfoV1T] = None
    Tags: Optional[ListAwsEc2InstancesTagsV1T] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
    AvailabilityZone: Optional[dict[Literal['eq'], str]] = None
