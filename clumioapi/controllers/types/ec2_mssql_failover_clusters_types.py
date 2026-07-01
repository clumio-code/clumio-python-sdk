#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListEc2MssqlFailoverClustersProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListEc2MssqlFailoverClustersV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListEc2MssqlFailoverClustersV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListEc2MssqlFailoverClustersV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Name: Optional[dict[Literal['contains'], str]] = None
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListEc2MssqlFailoverClustersProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    AccountIds: Optional[dict[Literal['in'], list]] = None


ListEc2MssqlFailoverClustersV1FilterTypeDef = TypedDict(
    'ListEc2MssqlFailoverClustersV1FilterTypeDef',
    {
        'name': Mapping[Literal['$contains'], str],
        'environment_id': Mapping[Literal['$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$eq'], str],
        'account_ids': Mapping[Literal['$in'], list],
    },
    total=False,
)
