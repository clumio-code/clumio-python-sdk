#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListOrganizationalUnitsV2FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ParentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None


class ListOrganizationalUnitsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ParentId: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None
