#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListIndividualAlertsPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Type: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['contains'], list]] = None


class ListIndividualAlertsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Type: Optional[dict[Literal['eq'], str]] = None


class ListIndividualAlertsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Type: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    Severity: Optional[dict[Literal['in'], list]] = None
    RaisedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    UpdatedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ClearedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ConsolidatedAlertId: Optional[dict[Literal['eq'], str]] = None
    PrimaryEntity: Optional[ListIndividualAlertsPrimaryEntityV1T] = None
    ParentEntity: Optional[ListIndividualAlertsParentEntityV1T] = None
