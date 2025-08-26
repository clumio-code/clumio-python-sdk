#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsEnvironmentTagsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


class ListAwsEnvironmentTagsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    KeyId: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['contains'], list]] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListAwsEnvironmentTagsProtectionInfoV1T] = None
    Id: Optional[dict[Literal['in'], list]] = None
