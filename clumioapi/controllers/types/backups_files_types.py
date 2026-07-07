#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListFilesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListFilesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListFilesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    AssetType: Optional[dict[Literal['eq'], str]] = None
    AssetId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['regex'], str]] = None


class ListFilesV1FilterTypeDef(TypedDict, total=False):
    asset_type: Mapping[Literal['$eq'], str]
    asset_id: Mapping[Literal['$eq'], str]
    name: Mapping[Literal['$regex'], str]
