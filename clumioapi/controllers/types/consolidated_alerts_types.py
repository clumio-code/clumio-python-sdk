#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListConsolidatedAlertsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Type: Optional[dict[Literal['eq'], str]] = None


class ListConsolidatedAlertsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Status: Optional[dict[Literal['in'], list]] = None
    RaisedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ParentEntity: Optional[ListConsolidatedAlertsParentEntityV1T] = None
