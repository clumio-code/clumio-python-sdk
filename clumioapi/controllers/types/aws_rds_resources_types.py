#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsRdsResourcesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsRdsResourcesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsRdsResourcesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ResourceNativeId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], list]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Engine: Optional[dict[Literal['eq'], str]] = None
    Tags: Optional[ListAwsRdsResourcesTagsV1T] = None
    Type: Optional[dict[Literal['in'], list]] = None
    ProtectionInfo: Optional[ListAwsRdsResourcesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
