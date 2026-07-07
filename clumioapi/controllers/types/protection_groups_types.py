#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListProtectionGroupsProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListProtectionGroupsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListProtectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListProtectionGroupsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    IsDeleted: Optional[dict[Literal['eq', 'in'], bool | list]] = None
    Name: Optional[dict[Literal['contains', 'eq'], str]] = None
    ProtectionInfo: Optional[ListProtectionGroupsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None


ListProtectionGroupsV1FilterTypeDef = TypedDict(
    'ListProtectionGroupsV1FilterTypeDef',
    {
        'is_deleted': Mapping[Literal['$eq', '$in'], bool | list],
        'name': Mapping[Literal['$contains', '$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
        'organizational_unit_id': Mapping[Literal['$in'], list],
    },
    total=False,
)
