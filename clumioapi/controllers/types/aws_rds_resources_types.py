#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsRdsResourcesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsRdsResourcesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListAwsRdsResourcesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsRdsResourcesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsRdsResourcesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ResourceNativeId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Engine: Optional[dict[Literal['eq'], str]] = None
    Tags: Optional[ListAwsRdsResourcesTagsV1T] = None
    Type: Optional[dict[Literal['in'], list]] = None
    ProtectionInfo: Optional[ListAwsRdsResourcesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None


ListAwsRdsResourcesV1FilterTypeDef = TypedDict(
    'ListAwsRdsResourcesV1FilterTypeDef',
    {
        'resource_native_id': Mapping[Literal['$eq'], str],
        'name': Mapping[Literal['$contains'], str],
        'account_native_id': Mapping[Literal['$eq'], str],
        'environment_id': Mapping[Literal['$eq'], str],
        'engine': Mapping[Literal['$eq'], str],
        'tags.id': Mapping[Literal['$all'], list],
        'type': Mapping[Literal['$in'], list],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
        'backup_status': Mapping[Literal['$in'], list],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
    },
    total=False,
)
