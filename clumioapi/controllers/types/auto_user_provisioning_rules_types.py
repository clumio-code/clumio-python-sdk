#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAutoUserProvisioningRulesV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    Name: Optional[dict[Literal['contains'], str]] = None
    RoleId: Optional[dict[Literal['eq'], str]] = None
    OrganizationalUnitId: Optional[dict[Literal['eq'], str]] = None
