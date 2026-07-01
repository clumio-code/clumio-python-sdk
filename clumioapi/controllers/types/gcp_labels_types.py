#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import TypedDict

from clumioapi.controllers.types import base_controller_filter_types
from typing_extensions import deprecated


@deprecated(
    'Use the ListGcpLabelKeysV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpLabelKeysV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpLabelKeysV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """


@deprecated(
    'Use the ListGcpLabelValuesV1FilterTypeDef dict instead. Retained for '
    'backward compatibility; scheduled for removal in a future major release.'
)
class ListGcpLabelValuesV1FilterT(base_controller_filter_types.BaseControllerFilterTypes):
    """Deprecated: pass a dict typed as ``ListGcpLabelValuesV1FilterTypeDef`` instead.

    Retained for backward compatibility and scheduled for removal in a future
    major release. The TypedDict mirrors the API reference 1:1, for example
    ``filter={'field_name': {'$eq': 'value'}}``.
    """


ListGcpLabelKeysV1FilterTypeDef = TypedDict(
    'ListGcpLabelKeysV1FilterTypeDef',
    {},
    total=False,
)

ListGcpLabelValuesV1FilterTypeDef = TypedDict(
    'ListGcpLabelValuesV1FilterTypeDef',
    {},
    total=False,
)
