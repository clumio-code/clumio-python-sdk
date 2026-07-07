#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListBackupAwsEc2InstancesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListBackupAwsEc2InstancesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListBackupAwsEc2InstancesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    InstanceId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None


class ListBackupAwsEc2InstancesV1FilterTypeDef(TypedDict, total=False):
    instance_id: Mapping[Literal['$eq'], str]
    start_timestamp: Mapping[Literal['$lte', '$gt'], str | int]
