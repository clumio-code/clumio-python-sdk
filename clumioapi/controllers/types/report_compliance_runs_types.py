#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListComplianceReportRunsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Status: Optional[dict[Literal['in'], list]] = None
    ComplianceStatus: Optional[dict[Literal['in'], list]] = None
