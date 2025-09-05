#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListProtectionGroupInstantAccessEndpointsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    ProtectionGroupId: Optional[dict[Literal['eq'], str]] = None
    ProtectionGroupS3AssetId: Optional[dict[Literal['eq'], str]] = None
