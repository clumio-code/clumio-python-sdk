#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListBackupAwsRdsResourcesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListBackupAwsRdsResourcesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListBackupAwsRdsResourcesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ResourceId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None


@deprecated(
    'Use the ListAwsRdsResourcesOptionGroupsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsRdsResourcesOptionGroupsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListAwsRdsResourcesOptionGroupsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    EnvironmentId: Optional[dict[Literal['eq'], str]] = None


class ListBackupAwsRdsResourcesV1FilterTypeDef(TypedDict, total=False):
    resource_id: Mapping[Literal['$eq'], str]
    start_timestamp: Mapping[Literal['$lte', '$gt'], str | int]


class ListAwsRdsResourcesOptionGroupsV1FilterTypeDef(TypedDict, total=False):
    environment_id: Mapping[Literal['$eq'], str]
