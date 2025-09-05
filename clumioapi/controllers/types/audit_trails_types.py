#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAuditTrailsPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['in'], list]] = None
    Type: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['in'], list]] = None


class ListAuditTrailsParentEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Type: Optional[dict[Literal['in'], list]] = None
    Value: Optional[dict[Literal['in'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None


class ListAuditTrailsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    StartTimestamp: Optional[dict[Literal['gte', 'lt', 'eq'], str | int]] = None
    Category: Optional[dict[Literal['in'], list]] = None
    Action: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    UserEmail: Optional[dict[Literal['in'], list]] = None
    IpAddress: Optional[dict[Literal['eq'], str]] = None
    PrimaryEntity: Optional[ListAuditTrailsPrimaryEntityV1T] = None
    ParentEntity: Optional[ListAuditTrailsParentEntityV1T] = None
    OrganizationalUnitId: Optional[dict[Literal['eq'], str]] = None
