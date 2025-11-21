#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListTasksPrimaryEntityV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Value: Optional[dict[Literal['contains'], str]] = None
    Id: Optional[dict[Literal['contains'], str]] = None


class ListTasksV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    PrimaryEntity: Optional[ListTasksPrimaryEntityV1T] = None
    CreatedTimestamp: Optional[dict[Literal['lte', 'gte'], str]] = None
    Type: Optional[dict[Literal['in'], list]] = None
    Category: Optional[dict[Literal['in'], list]] = None
    Genre: Optional[dict[Literal['in'], list]] = None
    Status: Optional[dict[Literal['in'], list]] = None
    Id: Optional[dict[Literal['in'], list]] = None
