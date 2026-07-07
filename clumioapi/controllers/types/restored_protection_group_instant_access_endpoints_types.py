#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListProtectionGroupInstantAccessEndpointsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListProtectionGroupInstantAccessEndpointsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListProtectionGroupInstantAccessEndpointsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    ProtectionGroupS3AssetId: Optional[dict[Literal['eq'], str]] = None


class ListProtectionGroupInstantAccessEndpointsV1FilterTypeDef(TypedDict, total=False):
    protection_group_id: Mapping[Literal['$eq'], str]
    protection_group_s3_asset_id: Mapping[Literal['$eq'], str]
