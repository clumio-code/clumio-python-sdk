#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListPolicyRulesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Id: Optional[dict[Literal['in'], list]] = None
