#
# Copyright 2021. Clumio, Inc.
#

import os
from typing import Mapping

from clumioapi.exceptions import clumio_exception
import rest3client


class Configuration:
    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    Attributes:
        hostname: Hostname of the API server.
        client: If passed, it will be used as the client to make REST API calls. Otherwise a default
            client will be used.
    """

    # The base Uri for API calls
    hostname: str = 'api.clumio.com'
    base_path: str = '/api'

    def __init__(
        self,
        api_token: str = None,
        client: rest3client.RESTclient = None,
        hostname: str = None,
        organizational_unit_context: str = '',
        custom_headers: Mapping[str, str] = None,
    ) -> None:
        self.api_token: str = api_token or os.getenv('API_TOKEN')
        if hostname:
            self.hostname = hostname
        if api_token is None:
            raise clumio_exception.ClumioException(
                reason='api_token required for making the API call is missing. It must either be'
                'passed as a Configuration constructor parameter or the environment variable'
                'API_TOKEN must be set',
                errors=None,
            )
        self.client = client
        self.organizational_unit_context = organizational_unit_context
        self.custom_headers = custom_headers
