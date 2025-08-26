#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListPolicyDefinitionsOperationsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Type: Optional[dict[Literal['in'], list]] = None


class ListPolicyDefinitionsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    Name: Optional[dict[Literal['eq', 'begins_with'], list | str]] = None
    Operations: Optional[ListPolicyDefinitionsOperationsV1T] = None
    ActivationStatus: Optional[dict[Literal['eq'], str]] = None
