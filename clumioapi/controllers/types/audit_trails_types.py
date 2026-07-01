#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAuditTrailsPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['in'], list]] = None
    Type: Optional[dict[Literal['in'], list]] = None
    Value: Optional[dict[Literal['in'], list]] = None


class ListAuditTrailsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Type: Optional[dict[Literal['in'], list]] = None
    Value: Optional[dict[Literal['in'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None


@deprecated(
    'Use the ListAuditTrailsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAuditTrailsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAuditTrailsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    StartTimestamp: Optional[dict[Literal['gte', 'lt', 'eq'], str | int]] = None
    Category: Optional[dict[Literal['in'], list]] = None
    Action: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    UserEmail: Optional[dict[Literal['in'], list]] = None
    IpAddress: Optional[dict[Literal['eq'], str]] = None
    PrimaryEntity: Optional[ListAuditTrailsPrimaryEntityV1T] = None
    ParentEntity: Optional[ListAuditTrailsParentEntityV1T] = None
    OrganizationalUnitId: Optional[dict[Literal['eq'], str]] = None


ListAuditTrailsV1FilterTypeDef = TypedDict(
    'ListAuditTrailsV1FilterTypeDef',
    {
        'start_timestamp': Mapping[Literal['$gte', '$eq', '$lt'], str | int],
        'category': Mapping[Literal['$in'], list],
        'action': Mapping[Literal['$in'], list],
        'status': Mapping[Literal['$in'], list],
        'user_email': Mapping[Literal['$in'], list],
        'ip_address': Mapping[Literal['$eq'], str],
        'primary_entity.id': Mapping[Literal['$in'], list],
        'primary_entity.type': Mapping[Literal['$in'], list],
        'primary_entity.value': Mapping[Literal['$in'], list],
        'parent_entity.type': Mapping[Literal['$in'], list],
        'parent_entity.value': Mapping[Literal['$in'], list],
        'parent_entity.id': Mapping[Literal['$in'], list],
        'organizational_unit_id': Mapping[Literal['$eq'], str],
    },
    total=False,
)
