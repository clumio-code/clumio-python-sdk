#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListReportDownloadsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListReportDownloadsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListReportDownloadsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    StartTimestamp: Optional[dict[Literal['gte', 'lt'], str | int]] = None
    ReportType: Optional[dict[Literal['in'], list]] = None


class ListReportDownloadsV1FilterTypeDef(TypedDict, total=False):
    start_timestamp: Mapping[Literal['$gte', '$lt'], str | int]
    report_type: Mapping[Literal['$in'], list]
