#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsEnvironmentsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AccountNativeId: Optional[dict[Literal['eq', 'begins_with'], str | list]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    ConnectionStatus: Optional[dict[Literal['eq'], str]] = None
    ServicesEnabled: Optional[dict[Literal['contains'], str]] = None
