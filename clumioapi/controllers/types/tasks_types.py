#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListTasksPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Value: Optional[dict[Literal['contains'], str]] = None
    Id: Optional[dict[Literal['eq', 'in'], str | list]] = None


class ListTasksParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['contains'], str]] = None


@deprecated(
    'Use the ListTasksV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListTasksV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListTasksV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    PrimaryEntity: Optional[ListTasksPrimaryEntityV1T] = None
    ParentEntity: Optional[ListTasksParentEntityV1T] = None
    CreatedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    Type: Optional[dict[Literal['in'], list]] = None
    Category: Optional[dict[Literal['in'], list]] = None
    Genre: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None


ListTasksV1FilterTypeDef = TypedDict(
    'ListTasksV1FilterTypeDef',
    {
        'primary_entity.value': Mapping[Literal['$contains'], str],
        'primary_entity.id': Mapping[Literal['$eq', '$in'], str | list],
        'parent_entity.id': Mapping[Literal['$eq'], str],
        'parent_entity.value': Mapping[Literal['$contains'], str],
        'created_timestamp': Mapping[Literal['$lte', '$gte'], str],
        'type': Mapping[Literal['$in'], list],
        'category': Mapping[Literal['$in'], list],
        'genre': Mapping[Literal['$in'], list],
        'status': Mapping[Literal['$in'], list],
        'id': Mapping[Literal['$in'], list],
    },
    total=False,
)
