#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListEc2MssqlHostsProtectionInfoV1T(base_controller_filter_types.BaseControllerFilterTypes):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListEc2MssqlHostsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListEc2MssqlHostsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListEc2MssqlHostsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
    Id: Optional[dict[Literal['eq'], str]] = None
    Name: Optional[dict[Literal['contains'], str]] = None
    ProtectionInfo: Optional[ListEc2MssqlHostsProtectionInfoV1T] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    Status: Optional[dict[Literal['eq'], str]] = None


ListEc2MssqlHostsV1FilterTypeDef = TypedDict(
    'ListEc2MssqlHostsV1FilterTypeDef',
    {
        'environment_id': Mapping[Literal['$eq'], str],
        'id': Mapping[Literal['$eq'], str],
        'name': Mapping[Literal['$contains'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'protection_status': Mapping[Literal['$eq'], str],
        'status': Mapping[Literal['$eq'], str],
    },
    total=False,
)
