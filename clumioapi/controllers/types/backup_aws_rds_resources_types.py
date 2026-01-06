#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupAwsRdsResourcesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    ResourceId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], str | int]] = None


class ListAwsRdsResourcesOptionGroupsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    EnvironmentId: Optional[dict[Literal['eq'], str]] = None
