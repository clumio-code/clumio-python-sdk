#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListGcpGcsAssetsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpGcsAssetsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpGcsAssetsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Id: Optional[dict[Literal['eq', 'in'], str | list]] = None
    ProtectionGroupId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    BucketId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    BucketName: Optional[dict[Literal['eq', 'in'], str | list]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains'], str]] = None
    AddedBy: Optional[dict[Literal['in'], list]] = None


@deprecated(
    'Use the ListGcpGcsAssetPitrIntervalsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpGcsAssetPitrIntervalsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpGcsAssetPitrIntervalsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Timestamp: Optional[dict[Literal['lte', 'gte'], str]] = None


class ListGcpGcsAssetsV1FilterTypeDef(TypedDict, total=False):
    id: Mapping[Literal['$eq', '$in'], str | list]
    protection_group_id: Mapping[Literal['$eq', '$in'], str | list]
    bucket_id: Mapping[Literal['$eq', '$in'], str | list]
    bucket_name: Mapping[Literal['$eq', '$in'], str | list]
    is_deleted: Mapping[Literal['$eq'], bool]
    name: Mapping[Literal['$eq', '$contains'], str]
    added_by: Mapping[Literal['$in'], list]


class ListGcpGcsAssetPitrIntervalsV1FilterTypeDef(TypedDict, total=False):
    timestamp: Mapping[Literal['$lte', '$gte'], str]
