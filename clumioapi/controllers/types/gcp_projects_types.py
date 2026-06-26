#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListGcpProjectsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ProjectId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
