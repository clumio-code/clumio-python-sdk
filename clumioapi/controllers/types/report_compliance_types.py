#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListComplianceReportConfigurationsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListComplianceReportConfigurationsV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListComplianceReportConfigurationsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    ReportName: Optional[dict[Literal['contains'], str]] = None
    ComplianceStatus: Optional[dict[Literal['eq'], str]] = None


class ListComplianceReportConfigurationsV1FilterTypeDef(TypedDict, total=False):
    report_name: Mapping[Literal['$contains'], str]
    compliance_status: Mapping[Literal['$eq'], str]
