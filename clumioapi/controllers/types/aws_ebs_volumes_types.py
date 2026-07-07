#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsEbsVolumesProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsEbsVolumesTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


@deprecated(
    'Use the ListAwsEbsVolumesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsEbsVolumesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsEbsVolumesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains', 'eq'], str]] = None
    VolumeNativeId: Optional[dict[Literal['eq', 'contains'], str]] = None
    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    ProtectionStatus: Optional[dict[Literal['eq', 'in'], str | list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    ProtectionInfo: Optional[ListAwsEbsVolumesProtectionInfoV1T] = None
    Tags: Optional[ListAwsEbsVolumesTagsV1T] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None


ListAwsEbsVolumesV1FilterTypeDef = TypedDict(
    'ListAwsEbsVolumesV1FilterTypeDef',
    {
        'environment_id': Mapping[Literal['$eq'], str],
        'name': Mapping[Literal['$contains', '$eq'], str],
        'volume_native_id': Mapping[Literal['$eq', '$contains'], str],
        'account_native_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$eq', '$in'], str | list],
        'deactivated': Mapping[Literal['$eq'], str],
        'backup_status': Mapping[Literal['$in'], list],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'tags.id': Mapping[Literal['$all'], list],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
    },
    total=False,
)
