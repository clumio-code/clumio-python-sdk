#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListComplianceReportConfigurationsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    ReportName: Optional[dict[Literal['contains'], str]] = None
    ComplianceStatus: Optional[dict[Literal['eq'], str]] = None
