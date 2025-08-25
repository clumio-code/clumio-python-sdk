#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListEc2MssqlHostsProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListEc2MssqlHostsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Id: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], list]] = None
    ProtectionInfo: Optional[ListEc2MssqlHostsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    Status: Optional[dict[Literal['eq'], str]] = None
