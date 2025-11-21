#
# Copyright 2025. Clumio, A Commvault Company.
#

from typing import Literal, Optional

from clumioapi.controllers.types import base_controller_filter_types


class ListAwsS3BucketsV1BucketMatcherT(base_controller_filter_types.BaseControllerFilterTypes):
    AwsTag: Optional[
        dict[
            Literal['eq', 'not_eq', 'contains', 'not_contains', 'all', 'not_all', 'in', 'not_in'],
            list | dict,
        ]
    ] = None
    AwsAccountNativeId: Optional[dict[Literal['eq', 'in'], list | str]] = None
    AccountNativeIddeprecated: Optional[dict[Literal['eq', 'in'], list | str]] = None
    AwsRegion: Optional[dict[Literal['eq', 'in'], list | str]] = None
