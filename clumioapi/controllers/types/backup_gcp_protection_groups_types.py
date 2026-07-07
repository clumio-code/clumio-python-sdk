#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListBackupGcpProtectionGroupsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListBackupGcpProtectionGroupsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListBackupGcpProtectionGroupsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None


class ListBackupGcpProtectionGroupsV1FilterTypeDef(TypedDict, total=False):
    protection_group_id: Mapping[Literal['$eq'], str]
    start_timestamp: Mapping[Literal['$lte', '$gt'], str | int]
