#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListEc2MssqlAvailabilityGroupsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListEc2MssqlAvailabilityGroupsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    Name: Optional[dict[Literal['contains'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListEc2MssqlAvailabilityGroupsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    Status: Optional[dict[Literal['eq'], str]] = None
    HostId: Optional[dict[Literal['eq'], str]] = None
    AccountIds: Optional[dict[Literal['in'], list]] = None
