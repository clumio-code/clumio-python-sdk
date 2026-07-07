#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListBackupAwsRdsResourceDatabasesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListBackupAwsRdsResourceDatabasesV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    """Deprecated: pass a dict typed as ``ListBackupAwsRdsResourceDatabasesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Name: Optional[dict[Literal['begins_with'], list]] = None


class ListBackupAwsRdsResourceDatabasesV1FilterTypeDef(TypedDict, total=False):
    name: Mapping[Literal['$begins_with'], list]
