#
# Copyright 2023. Clumio, A Commvault Company.
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

    def __init__(
        self,
        api_token: str = '',
        client: rest3client.RESTclient | None = None,
        hostname: str = '',
        raw_response: bool = False,
        organizational_unit_context: str = '',
        custom_headers: Mapping[str, str] | None = None,
    ) -> None:
        api_token = api_token or os.getenv('API_TOKEN') or ''
        if not api_token:
            raise ValueError(
                'api_token must be provided either as a parameter to the Configuration constructor or'
                'as an environment variable named API_TOKEN.'
            )
        self.api_token: str = api_token
        if hostname:
            self.hostname = hostname
        if api_token is None:
            raise clumio_exception.ClumioException(
                reason='api_token required for making the API call is missing. It must either be'
                'passed as a Configuration constructor parameter or the environment variable'
                'API_TOKEN must be set.'
            )
        self.client = client
        self.raw_response = raw_response
        self.organizational_unit_context = organizational_unit_context
        self.custom_headers = custom_headers
