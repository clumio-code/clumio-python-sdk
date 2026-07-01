#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListProtectionGroupS3AssetsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListProtectionGroupS3AssetsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListProtectionGroupS3AssetsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListProtectionGroupS3AssetsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    AccountNativeId: Optional[dict[Literal['eq'], str]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    BucketId: Optional[dict[Literal['eq'], str]] = None
    BucketName: Optional[dict[Literal['eq', 'contains'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None
    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListProtectionGroupS3AssetsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AddedBy: Optional[dict[Literal['in'], list]] = None
    IsSupported: Optional[dict[Literal['eq'], bool]] = None


@deprecated(
    'Use the ListProtectionGroupS3AssetPitrIntervalsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListProtectionGroupS3AssetPitrIntervalsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListProtectionGroupS3AssetPitrIntervalsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Timestamp: Optional[dict[Literal['lte', 'gte'], str]] = None


ListProtectionGroupS3AssetsV1FilterTypeDef = TypedDict(
    'ListProtectionGroupS3AssetsV1FilterTypeDef',
    {
        'account_native_id': Mapping[Literal['$eq'], str],
        'aws_region': Mapping[Literal['$eq'], str],
        'bucket_id': Mapping[Literal['$eq'], str],
        'bucket_name': Mapping[Literal['$eq', '$contains'], str],
        'environment_id': Mapping[Literal['$eq'], str],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
        'protection_group_id': Mapping[Literal['$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
        'backup_status': Mapping[Literal['$in'], list],
        'organizational_unit_id': Mapping[Literal['$in'], list],
        'added_by': Mapping[Literal['$in'], list],
        'is_supported': Mapping[Literal['$eq'], bool],
    },
    total=False,
)


class ListProtectionGroupS3AssetPitrIntervalsV1FilterTypeDef(TypedDict, total=False):
    timestamp: Mapping[Literal['$lte', '$gte'], str]
