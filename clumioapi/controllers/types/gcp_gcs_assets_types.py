#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListGcpGcsAssetsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq', 'in'], list | str]] = None
    ProtectionGroupId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    BucketId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    BucketName: Optional[dict[Literal['eq', 'in'], list | str]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains'], str]] = None
    AddedBy: Optional[dict[Literal['in'], list]] = None


class ListGcpGcsAssetPitrIntervalsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Timestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
