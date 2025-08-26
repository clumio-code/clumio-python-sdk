#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListProtectionGroupsProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListProtectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    IsDeleted: Optional[dict[Literal['eq', 'in'], list | bool]] = None
    Name: Optional[dict[Literal['contains', 'eq'], list | str]] = None
    ProtectionInfo: Optional[ListProtectionGroupsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
