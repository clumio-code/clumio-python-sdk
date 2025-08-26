#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsConnectionGroupsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AccountNativeId: Optional[dict[Literal['in'], list]] = None
    OrganizationalUnitId: Optional[dict[Literal['in'], list]] = None
    AccountAlias: Optional[dict[Literal['contains'], list]] = None
    ServicesEnabled: Optional[dict[Literal['contains', 'eq'], list | str]] = None
