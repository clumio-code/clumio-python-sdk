#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsDynamodbTablesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsDynamodbTablesProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListAwsDynamodbTablesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsDynamodbTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsDynamodbTablesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], str]] = None
    TableNativeId: Optional[dict[Literal['eq'], str]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    Tags: Optional[ListAwsDynamodbTablesTagsV1T] = None
    ProtectionInfo: Optional[ListAwsDynamodbTablesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None


ListAwsDynamodbTablesV1FilterTypeDef = TypedDict(
    'ListAwsDynamodbTablesV1FilterTypeDef',
    {
        'environment_id': Mapping[Literal['$eq'], str],
        'name': Mapping[Literal['$contains'], str],
        'table_native_id': Mapping[Literal['$eq'], str],
        'aws_region': Mapping[Literal['$eq'], str],
        'account_native_id': Mapping[Literal['$eq'], str],
        'tags.id': Mapping[Literal['$all'], list],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
        'backup_status': Mapping[Literal['$in'], list],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
    },
    total=False,
)
