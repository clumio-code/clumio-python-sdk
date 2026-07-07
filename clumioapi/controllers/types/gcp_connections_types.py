#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListGcpConnectionsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpConnectionsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpConnectionsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ProjectId: Optional[dict[Literal['contains'], str]] = None
    ProjectName: Optional[dict[Literal['contains'], str]] = None
    ConnectionStatus: Optional[dict[Literal['in'], list]] = None


class ListGcpConnectionsV1FilterTypeDef(TypedDict, total=False):
    project_id: Mapping[Literal['$contains'], str]
    project_name: Mapping[Literal['$contains'], str]
    connection_status: Mapping[Literal['$in'], list]
