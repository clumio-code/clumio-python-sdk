#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsS3BucketsV1BucketMatcherT(base_controller_filter_types.BaseControllerFilterTypes):
    AwsTag: Optional[
        dict[
            Literal['eq', 'not_eq', 'contains', 'not_contains', 'all', 'not_all', 'in', 'not_in'],
            dict | list,
        ]
    ] = None
    AwsAccountNativeId: Optional[dict[Literal['eq', 'in'], str | list]] = None
    AccountNativeIddeprecated: Optional[dict[Literal['eq', 'in'], str | list]] = None
    AwsRegion: Optional[dict[Literal['eq', 'in'], str | list]] = None
