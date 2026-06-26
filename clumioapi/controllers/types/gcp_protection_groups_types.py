#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListGcpProtectionGroupsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListGcpProtectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['eq', 'in'], list | str]] = None
    NativeId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    IsDeleted: Optional[dict[Literal['eq'], bool]] = None
    Name: Optional[dict[Literal['eq', 'contains'], str]] = None
    ProtectionInfo: Optional[ListGcpProtectionGroupsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
