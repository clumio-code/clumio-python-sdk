#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListRdsRestoredRecordsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AssetId: Optional[dict[Literal['eq'], str]] = None
    TaskId: Optional[dict[Literal['in'], list]] = None
