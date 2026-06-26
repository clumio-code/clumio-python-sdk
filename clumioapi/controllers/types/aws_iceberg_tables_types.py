#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsIcebergTablesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsIcebergTablesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsIcebergTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListAwsIcebergTablesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
    AccountNativeId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    TableName: Optional[dict[Literal['contains', 'eq'], str]] = None
    CatalogType: Optional[dict[Literal['in'], list]] = None
    Catalog: Optional[dict[Literal['contains', 'eq'], str]] = None
    Namespace: Optional[dict[Literal['contains', 'eq'], str]] = None
    Tags: Optional[ListAwsIcebergTablesTagsV1T] = None
