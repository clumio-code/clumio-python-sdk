#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListBackupAwsIcebergTablesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListBackupAwsIcebergTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListBackupAwsIcebergTablesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    TableId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt', 'lt'], str | int]] = None
    Type: Optional[dict[Literal['in'], list]] = None
    MetadataRecordId: Optional[dict[Literal['eq'], str]] = None
    BackupRegion: Optional[dict[Literal['eq'], str]] = None


class ListBackupAwsIcebergTablesV1FilterTypeDef(TypedDict, total=False):
    table_id: Mapping[Literal['$eq'], str]
    start_timestamp: Mapping[Literal['$lte', '$gt', '$lt'], str | int]
    type: Mapping[Literal['$in'], list]
    metadata_record_id: Mapping[Literal['$eq'], str]
    backup_region: Mapping[Literal['$eq'], str]
