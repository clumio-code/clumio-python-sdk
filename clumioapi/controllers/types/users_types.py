#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListUsersV2FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListUsersV2FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListUsersV2FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Name: Optional[dict[Literal['contains'], str]] = None
    RoleId: Optional[dict[Literal['eq'], str]] = None
    OrganizationalUnitId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListUsersV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListUsersV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListUsersV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Name: Optional[dict[Literal['contains'], str]] = None


class ListUsersV2FilterTypeDef(TypedDict, total=False):
    name: Mapping[Literal['$contains'], str]
    role_id: Mapping[Literal['$eq'], str]
    organizational_unit_id: Mapping[Literal['$eq'], str]


class ListUsersV1FilterTypeDef(TypedDict, total=False):
    name: Mapping[Literal['$contains'], str]
