#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsConnectionsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AccountNativeId: Optional[dict[Literal['begins_with', 'in'], list]] = None
    AwsRegion: Optional[dict[Literal['in'], list]] = None
    AccountAlias: Optional[dict[Literal['contains'], list]] = None
    ConnectionType: Optional[dict[Literal['eq'], str]] = None
    ConnectionStatus: Optional[dict[Literal['eq', 'in'], list | str]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    ServicesEnabled: Optional[dict[Literal['contains'], list]] = None
