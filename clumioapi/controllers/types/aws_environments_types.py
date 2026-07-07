#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListAwsEnvironmentsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsEnvironmentsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsEnvironmentsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    AccountNativeId: Optional[dict[Literal['eq', 'begins_with'], str | list]] = None
    AwsRegion: Optional[dict[Literal['eq'], str]] = None
    ConnectionStatus: Optional[dict[Literal['eq'], str]] = None
    ServicesEnabled: Optional[dict[Literal['contains'], str]] = None


class ListAwsEnvironmentsV1FilterTypeDef(TypedDict, total=False):
    account_native_id: Mapping[Literal['$eq', '$begins_with'], str | list]
    aws_region: Mapping[Literal['$eq'], str]
    connection_status: Mapping[Literal['$eq'], str]
    services_enabled: Mapping[Literal['$contains'], str]
