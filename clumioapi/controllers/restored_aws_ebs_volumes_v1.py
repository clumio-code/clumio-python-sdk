#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any
import urllib.parse

from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_aws_ebs_volume_v1_request
import requests


class RestoredAwsEbsVolumesV1Controller:
    """A Controller to access Endpoints for restored-aws-ebs-volumes resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-ebs-volumes=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_aws_ebs_volume(
        self,
        body: restore_aws_ebs_volume_v1_request.RestoreAwsEbsVolumeV1Request | None = None,
        **kwargs,
    ) -> object:
        """TODO: Add comment

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/restores/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}

        resp_instance: object
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


class RestoredAwsEbsVolumesV1ControllerPaginator:
    """A Controller to access Endpoints for restored-aws-ebs-volumes resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
