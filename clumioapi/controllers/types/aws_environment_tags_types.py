#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListAwsEnvironmentTagsProtectionInfoV1T(
    base_controller_filter_types.BaseControllerFilterTypes
):
    PolicyId: Optional[dict[Literal['eq'], str]] = None


@deprecated(
    'Use the ListAwsEnvironmentTagsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListAwsEnvironmentTagsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListAwsEnvironmentTagsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    KeyId: Optional[dict[Literal['eq'], str]] = None
    Value: Optional[dict[Literal['contains'], str]] = None
    ProtectionStatus: Optional[dict[Literal['eq'], str]] = None
    ProtectionInfo: Optional[ListAwsEnvironmentTagsProtectionInfoV1T] = None
    Id: Optional[dict[Literal['in'], list]] = None


ListAwsEnvironmentTagsV1FilterTypeDef = TypedDict(
    'ListAwsEnvironmentTagsV1FilterTypeDef',
    {
        'key_id': Mapping[Literal['$eq'], str],
        'value': Mapping[Literal['$contains'], str],
        'protection_status': Mapping[Literal['$eq'], str],
        'protection_info.policy_id': Mapping[Literal['$eq'], str],
        'id': Mapping[Literal['$in'], list],
    },
    total=False,
)
