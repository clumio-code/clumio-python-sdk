#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListBackupAwsRdsResourceDatabaseTablesV1FilterT(
    base_controller_filter_types.BaseControllerFilterTypes
):
    Name: Optional[dict[Literal['begins_with'], list]] = None
