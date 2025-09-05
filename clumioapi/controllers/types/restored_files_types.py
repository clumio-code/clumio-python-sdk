#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListRestoredFilesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    AssetType: Optional[dict[Literal['eq'], str]] = None
    AssetId: Optional[dict[Literal['eq'], str]] = None
