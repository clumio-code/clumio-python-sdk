#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListAwsConnectionGroupsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsConnectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsConnectionGroupsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    AccountNativeId: Optional[dict[Literal['in'], list]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AccountAlias: Optional[dict[Literal['contains'], str]] = None
    ServicesEnabled: Optional[dict[Literal['contains', 'eq'], list]] = None


class ListAwsConnectionGroupsV1FilterTypeDef(TypedDict, total=False):
    account_native_id: Mapping[Literal['$in'], list]
    organizational_unit_id: Mapping[Literal['$in'], list]
    account_alias: Mapping[Literal['$contains'], str]
    services_enabled: Mapping[Literal['$contains', '$eq'], list]
