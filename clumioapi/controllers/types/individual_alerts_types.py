#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListIndividualAlertsPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq', 'in'], str | list]] = None
    Type: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['contains'], str]] = None


class ListIndividualAlertsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Type: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListIndividualAlertsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListIndividualAlertsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListIndividualAlertsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Type: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    Severity: Optional[dict[Literal['in'], list]] = None
    RaisedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    UpdatedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ClearedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ConsolidatedAlertId: Optional[dict[Literal['eq'], str]] = None
    PrimaryEntity: Optional[ListIndividualAlertsPrimaryEntityV1T] = None
    ParentEntity: Optional[ListIndividualAlertsParentEntityV1T] = None


ListIndividualAlertsV1FilterTypeDef = TypedDict(
    'ListIndividualAlertsV1FilterTypeDef',
    {
        'type': Mapping[Literal['$in'], list],
        'status': Mapping[Literal['$in'], list],
        'severity': Mapping[Literal['$in'], list],
        'raised_timestamp': Mapping[Literal['$lte', '$gte'], str],
        'updated_timestamp': Mapping[Literal['$lte', '$gte'], str],
        'cleared_timestamp': Mapping[Literal['$lte', '$gte'], str],
        'consolidated_alert_id': Mapping[Literal['$eq'], str],
        'primary_entity.id': Mapping[Literal['$eq', '$in'], str | list],
        'primary_entity.type': Mapping[Literal['$eq'], str],
        'primary_entity.value': Mapping[Literal['$contains'], str],
        'parent_entity.id': Mapping[Literal['$eq'], str],
        'parent_entity.type': Mapping[Literal['$eq'], str],
    },
    total=False,
)
