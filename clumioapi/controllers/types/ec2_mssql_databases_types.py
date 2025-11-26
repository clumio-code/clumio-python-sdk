#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListEc2MssqlDatabasesProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListEc2MssqlDatabasesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Name: Optional[dict[Literal['contains'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListEc2MssqlDatabasesProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    BackupStatus: Optional[dict[Literal['in'], list]] = None
    Deactivated: Optional[dict[Literal['eq'], str]] = None
    InstanceId: Optional[dict[Literal['eq'], str]] = None
    HostId: Optional[dict[Literal['eq'], str]] = None
    AvailabilityGroupId: Optional[dict[Literal['eq'], str]] = None
    FailoverClusterId: Optional[dict[Literal['eq'], str]] = None
    Status: Optional[dict[Literal['eq'], str]] = None
    RecoveryModel: Optional[dict[Literal['in'], list]] = None
    Type: Optional[dict[Literal['eq'], str]] = None
    AccountIds: Optional[dict[Literal['in'], list]] = None


class ListEc2MssqlDatabasePitrIntervalsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    Timestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None
