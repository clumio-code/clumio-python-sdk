#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListConsolidatedAlertsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Type: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListConsolidatedAlertsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListConsolidatedAlertsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListConsolidatedAlertsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Status: Optional[dict[Literal['in'], list]] = None
    RaisedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    ParentEntity: Optional[ListConsolidatedAlertsParentEntityV1T] = None


ListConsolidatedAlertsV1FilterTypeDef = TypedDict(
    'ListConsolidatedAlertsV1FilterTypeDef',
    {
        'status': Mapping[Literal['$in'], list],
        'raised_timestamp': Mapping[Literal['$lte', '$gte'], str],
        'parent_entity.id': Mapping[Literal['$eq'], str],
        'parent_entity.type': Mapping[Literal['$eq'], str],
    },
    total=False,
)
