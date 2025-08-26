#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_aws_ec2_instance_v1_request
from clumioapi.models import restore_ec2_response
import requests


class RestoredAwsEc2InstancesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-ec2-instances resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-ec2-instances=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_aws_ec2_instance(
        self,
        embed: str | None = None,
        body: restore_aws_ec2_instance_v1_request.RestoreAwsEc2InstanceV1Request | None = None,
        **kwargs,
    ) -> restore_ec2_response.RestoreEC2Response:
        """Restores the specified EC2 instance backup to the specified target destination.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return restore_ec2_response.RestoreEC2Response.from_response(response)

        # Prepare query URL
        _url_path = '/restores/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: restore_ec2_response.RestoreEC2Response
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'restore_aws_ec2_instance for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsEc2InstancesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-ec2-instances resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = RestoredAwsEc2InstancesV1Controller(config)
