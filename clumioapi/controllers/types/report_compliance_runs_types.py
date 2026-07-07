#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListComplianceReportRunsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListComplianceReportRunsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListComplianceReportRunsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Status: Optional[dict[Literal['in'], list]] = None
    ComplianceStatus: Optional[dict[Literal['in'], list]] = None


class ListComplianceReportRunsV1FilterTypeDef(TypedDict, total=False):
    status: Mapping[Literal['$in'], list]
    compliance_status: Mapping[Literal['$in'], list]
