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
from clumioapi.models import restore_aws_ebs_volume_v1_request
from clumioapi.models import restore_ebs_response_v1
import requests


class RestoredAwsEbsVolumesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-ebs-volumes resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-ebs-volumes=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_aws_ebs_volume(
        self,
        body: restore_aws_ebs_volume_v1_request.RestoreAwsEbsVolumeV1Request | None = None,
        **kwargs,
    ) -> restore_ebs_response_v1.RestoreEBSResponseV1:
        """TODO: Add comment

        Args:
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return restore_ebs_response_v1.RestoreEBSResponseV1.from_response(response)

        # Prepare query URL
        _url_path = '/restores/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}

        resp_instance: restore_ebs_response_v1.RestoreEBSResponseV1
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
            error_str = f'restore_aws_ebs_volume for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsEbsVolumesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-ebs-volumes resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = RestoredAwsEbsVolumesV1Controller(config)
