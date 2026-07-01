#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsIcebergTablesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsIcebergTablesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


@deprecated(
    'Use the ListAwsIcebergTablesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsIcebergTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsIcebergTablesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListAwsIcebergTablesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None
    AccountNativeId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    TableName: Optional[dict[Literal['contains', 'eq'], str]] = None
    CatalogType: Optional[dict[Literal['in'], list]] = None
    Catalog: Optional[dict[Literal['contains', 'eq'], str]] = None
    Namespace: Optional[dict[Literal['contains', 'eq'], str]] = None
    Tags: Optional[ListAwsIcebergTablesTagsV1T] = None


ListAwsIcebergTablesV1FilterTypeDef = TypedDict(
    'ListAwsIcebergTablesV1FilterTypeDef',
    {
        'environment_id': Mapping[Literal['$eq'], str],
        'deactivated': Mapping[Literal['$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'backup_status': Mapping[Literal['$in'], list],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
        'account_native_id': Mapping[Literal['$eq', '$in'], str | list],
        'table_name': Mapping[Literal['$contains', '$eq'], str],
        'catalog_type': Mapping[Literal['$in'], list],
        'catalog': Mapping[Literal['$contains', '$eq'], str],
        'namespace': Mapping[Literal['$contains', '$eq'], str],
        'tags.id': Mapping[Literal['$all'], list],
    },
    total=False,
)
