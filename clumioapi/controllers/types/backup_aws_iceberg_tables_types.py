#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupAwsIcebergTablesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    TableId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt', 'lt'], int | str]] = None
    Type: Optional[dict[Literal['in'], list]] = None
    MetadataRecordId: Optional[dict[Literal['eq'], str]] = None
    BackupRegion: Optional[dict[Literal['eq'], str]] = None
