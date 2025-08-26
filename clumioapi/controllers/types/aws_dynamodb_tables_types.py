#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsDynamodbTablesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsDynamodbTablesProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsDynamodbTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], list]] = None
    TableNativeId: Optional[dict[Literal['eq'], str]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    Tags: Optional[ListAwsDynamodbTablesTagsV1T] = None
    ProtectionInfo: Optional[ListAwsDynamodbTablesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
