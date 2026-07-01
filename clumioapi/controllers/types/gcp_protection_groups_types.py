#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListGcpProtectionGroupsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListGcpProtectionGroupsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpProtectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpProtectionGroupsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Id: Optional[dict[Literal['eq', 'in'], str | list]] = None
    NativeId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains'], str]] = None
    ProtectionInfo: Optional[ListGcpProtectionGroupsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None


ListGcpProtectionGroupsV1FilterTypeDef = TypedDict(
    'ListGcpProtectionGroupsV1FilterTypeDef',
    {
        'id': Mapping[Literal['$eq', '$in'], str | list],
        'native_id': Mapping[Literal['$eq', '$in'], str | list],
        'is_deleted': Mapping[Literal['$eq'], bool],
        'name': Mapping[Literal['$eq', '$contains'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
    },
    total=False,
)
