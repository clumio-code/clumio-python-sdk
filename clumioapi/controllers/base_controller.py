#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Mapping, Optional

import rest3client

from clumioapi import api_helper, configuration


class BaseController:
    """All controllers inherit from this base class.

    Attributes:
        client: The HttpClient which a specific controller instance will use.
            By default all the controller objects share the same HttpClient.
            A user can use his own custom HttpClient as well.
    """

    client: rest3client.RESTclient = None

    global_headers: Mapping[str, Any] = {'user-agent': 'CLUMIOSDK'}

    def __init__(self, config: configuration.Configuration) -> None:
        """Constructor of the class."""
        self.client = config.client
        if self.client is None:
            self.client: rest3client.RESTclient = rest3client.RESTclient(
                hostname=config.hostname, bearer_token=config.api_token
            )
