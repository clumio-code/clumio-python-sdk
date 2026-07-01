#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListOrganizationalUnitsV2FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListOrganizationalUnitsV2FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListOrganizationalUnitsV2FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ParentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], str]] = None
    Id: Optional[dict[Literal['in'], list]] = None


@deprecated(
    'Use the ListOrganizationalUnitsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListOrganizationalUnitsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListOrganizationalUnitsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ParentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], str]] = None
    Id: Optional[dict[Literal['in'], list]] = None


class ListOrganizationalUnitsV2FilterTypeDef(TypedDict, total=False):
    parent_id: Mapping[Literal['$eq'], str]
    name: Mapping[Literal['$contains'], str]
    id: Mapping[Literal['$in'], list]


class ListOrganizationalUnitsV1FilterTypeDef(TypedDict, total=False):
    parent_id: Mapping[Literal['$eq'], str]
    name: Mapping[Literal['$contains'], str]
    id: Mapping[Literal['$in'], list]
