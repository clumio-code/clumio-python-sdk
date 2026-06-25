#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListGcpGcsBucketsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq', 'in'], list | str]] = None
    NativeId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    ProjectId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    ProjectUuid: Optional[dict[Literal['eq', 'in'], list | str]] = None
    RegionUuid: Optional[dict[Literal['eq', 'in'], list | str]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains', 'in'], list | str]] = None
