#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListGcpGcsBucketsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpGcsBucketsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpGcsBucketsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Id: Optional[dict[Literal['eq', 'in'], str | list]] = None
    NativeId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    ProjectId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    ProjectUuid: Optional[dict[Literal['eq', 'in'], str | list]] = None
    RegionUuid: Optional[dict[Literal['eq', 'in'], str | list]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains', 'in'], str | list]] = None


class ListGcpGcsBucketsV1FilterTypeDef(TypedDict, total=False):
    id: Mapping[Literal['$eq', '$in'], str | list]
    native_id: Mapping[Literal['$eq', '$in'], str | list]
    project_id: Mapping[Literal['$eq', '$in'], str | list]
    project_uuid: Mapping[Literal['$eq', '$in'], str | list]
    region_uuid: Mapping[Literal['$eq', '$in'], str | list]
    is_deleted: Mapping[Literal['$eq'], bool]
    name: Mapping[Literal['$eq', '$contains', '$in'], str | list]
