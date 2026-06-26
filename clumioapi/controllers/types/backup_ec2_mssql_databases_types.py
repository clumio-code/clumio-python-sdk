#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupEc2MssqlDatabasesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    DatabaseId: Optional[dict[Literal['eq'], str]] = None
    StartTimestamp: Optional[dict[Literal['lte', 'gt'], int | str]] = None
    Type: Optional[dict[Literal['in'], list]] = None
