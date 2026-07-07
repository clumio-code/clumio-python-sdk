#
# Copyright 2025. Clumio, A Commvault Company.
#

from collections.abc import Mapping
from typing import Literal, Optional, TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


class ListPolicyDefinitionsOperationsV1T(base_controller_filter_types.BaseControllerFilterTypes):
    Type: Optional[dict[Literal['in'], list]] = None


@deprecated(
    'Use the ListPolicyDefinitionsV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListPolicyDefinitionsV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListPolicyDefinitionsV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """

    Name: Optional[dict[Literal['eq', 'begins_with'], str | list]] = None
    Operations: Optional[ListPolicyDefinitionsOperationsV1T] = None
    ActivationStatus: Optional[dict[Literal['eq'], str]] = None


ListPolicyDefinitionsV1FilterTypeDef = TypedDict(
    'ListPolicyDefinitionsV1FilterTypeDef',
    {
        'name': Mapping[Literal['$eq', '$begins_with'], str | list],
        'operations.type': Mapping[Literal['$in'], list],
        'activation_status': Mapping[Literal['$eq'], str],
    },
    total=False,
)
