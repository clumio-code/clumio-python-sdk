#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListReportDownloadsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    StartTimestamp: Optional[dict[Literal['gte', 'lt'], int | str]] = None
    ReportType: Optional[dict[Literal['in'], list]] = None
