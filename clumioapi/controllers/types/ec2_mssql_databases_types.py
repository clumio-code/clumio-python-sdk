#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListEc2MssqlDatabasesProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListEc2MssqlDatabasesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListEc2MssqlDatabasesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListEc2MssqlDatabasesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

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


@deprecated(
    'Use the ListEc2MssqlDatabasePitrIntervalsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListEc2MssqlDatabasePitrIntervalsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListEc2MssqlDatabasePitrIntervalsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Timestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None


ListEc2MssqlDatabasesV1FilterTypeDef = TypedDict(
    'ListEc2MssqlDatabasesV1FilterTypeDef',
    {
        'name': Mapping[Literal['$contains'], str],
        'environment_id': Mapping[Literal['$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$eq'], str],
        'backup_status': Mapping[Literal['$in'], list],
        'deactivated': Mapping[Literal['$eq'], str],
        'instance_id': Mapping[Literal['$eq'], str],
        'host_id': Mapping[Literal['$eq'], str],
        'availability_group_id': Mapping[Literal['$eq'], str],
        'failover_cluster_id': Mapping[Literal['$eq'], str],
        'status': Mapping[Literal['$eq'], str],
        'recovery_model': Mapping[Literal['$in'], list],
        'type': Mapping[Literal['$eq'], str],
        'account_ids': Mapping[Literal['$in'], list],
    },
    total=False,
)


class ListEc2MssqlDatabasePitrIntervalsV1FilterTypeDef(TypedDict, total=False):
    timestamp: Mapping[Literal['$lte', '$gt'], str | int]
