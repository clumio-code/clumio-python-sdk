#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

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
    ) -> Union[
        restore_ebs_response_v1.RestoreEBSResponseV1,
        tuple[requests.Response, Optional[restore_ebs_response_v1.RestoreEBSResponseV1]],
    ]:
        """TODO: Add comment

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            restore_ebs_response_v1.RestoreEBSResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_aws_ebs_volume.', errors
            )

        obj = restore_ebs_response_v1.RestoreEBSResponseV1.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
