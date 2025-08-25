#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupAwsEbsVolumesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    VolumeId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], int | str]] = None


class ListBackupAwsEbsVolumesV2FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    VolumeId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], int | str]] = None
