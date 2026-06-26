#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListGcpConnectionsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ProjectId: Optional[dict[Literal['contains'], str]] = None
    ProjectName: Optional[dict[Literal['contains'], str]] = None
    ConnectionStatus: Optional[dict[Literal['in'], list]] = None
