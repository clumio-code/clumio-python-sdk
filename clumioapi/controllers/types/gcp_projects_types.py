#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListGcpProjectsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpProjectsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpProjectsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ProjectId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None


class ListGcpProjectsV1FilterTypeDef(TypedDict, total=False):
    project_id: Mapping[Literal['$eq', '$in'], str | list]
    is_deleted: Mapping[Literal['$eq'], bool]
