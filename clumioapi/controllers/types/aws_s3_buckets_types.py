#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsS3BucketsTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


@deprecated(
    'Use the ListAwsS3BucketsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsS3BucketsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsS3BucketsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains', 'in'], str | list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None
    Tags: Optional[ListAwsS3BucketsTagsV1T] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AssetId: Optional[dict[Literal['in'], list]] = None
    EventBridgeEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsVersioningEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsEncryptionEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsReplicationEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsSupported: Optional[dict[Literal['eq'], bool]] = None
    IsActive: Optional[dict[Literal['eq'], bool]] = None
    ProtectionMethod: Optional[dict[Literal['eq', 'in'], str | list]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    AwsTag: Optional[
        dict[
            Literal['eq', 'not_eq', 'contains', 'not_contains', 'all', 'not_all', 'in', 'not_in'],
            dict | list,
        ]
    ] = None
    AwsAccountNativeId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    AccountNativeIddeprecated: Optional[dict[Literal['eq', 'in'], str | list]] = None
    AwsRegion: Optional[dict[Literal['eq', 'in'], str | list]] = None


ListAwsS3BucketsV1FilterTypeDef = TypedDict(
    'ListAwsS3BucketsV1FilterTypeDef',
    {
        'environment_id': Mapping[Literal['$eq'], str],
        'name': Mapping[Literal['$contains', '$in'], str | list],
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
        'tags.id': Mapping[Literal['$all'], list],
        'organizational_unit_id': Mapping[Literal['$in'], list],
        'asset_id': Mapping[Literal['$in'], list],
        'event_bridge_enabled': Mapping[Literal['$eq'], bool],
        'is_versioning_enabled': Mapping[Literal['$eq'], bool],
        'is_encryption_enabled': Mapping[Literal['$eq'], bool],
        'is_replication_enabled': Mapping[Literal['$eq'], bool],
        'is_supported': Mapping[Literal['$eq'], bool],
        'is_active': Mapping[Literal['$eq'], bool],
        'protection_method': Mapping[Literal['$eq', '$in'], str | list],
        'backup_status': Mapping[Literal['$in'], list],
        'aws_tag': Mapping[
            Literal[
                '$eq', '$not_eq', '$contains', '$not_contains', '$all', '$not_all', '$in', '$not_in'
            ],
            dict | list,
        ],
        'aws_account_native_id': Mapping[Literal['$eq', '$in'], str | list],
        'account_native_idDeprecated': Mapping[Literal['$eq', '$in'], str | list],
        'aws_region': Mapping[Literal['$eq', '$in'], str | list],
    },
    total=False,
)
