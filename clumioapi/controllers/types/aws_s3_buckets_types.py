#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsS3BucketsTagsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['all'], list]] = None


class ListAwsS3BucketsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains', 'in'], list]] = None
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
    Tags: Optional[ListAwsS3BucketsTagsV1T] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AssetId: Optional[dict[Literal['in'], list]] = None
    EventBridgeEnabled: Optional[dict[Literal['eq'], str]] = None
    IsVersioningEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsEncryptionEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsReplicationEnabled: Optional[dict[Literal['eq'], bool]] = None
    IsSupported: Optional[dict[Literal['eq'], bool]] = None
    IsActive: Optional[dict[Literal['eq'], bool]] = None
    ProtectionMethod: Optional[dict[Literal['eq', 'in'], list | str]] = None
    AwsTag: Optional[
        dict[
            Literal['eq', 'not_eq', 'contains', 'not_contains', 'all', 'not_all', 'in', 'not_in'],
            list | str,
        ]
    ] = None
    AwsAccountNativeId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    AccountNativeIddeprecated: Optional[dict[Literal['eq', 'in'], list | str]] = None
    AwsRegion: Optional[dict[Literal['eq', 'in'], list | str]] = None
