#
# Copyright 2021. Clumio, Inc.
#

import json

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
        self, body: restore_aws_ebs_volume_v1_request.RestoreAwsEbsVolumeV1Request = None
    ) -> restore_ebs_response_v1.RestoreEBSResponseV1:
        """TODO: Add comment

        Args:
            body:

        Returns:
            restore_ebs_response_v1.RestoreEBSResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/aws/ebs-volumes'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_aws_ebs_volume.', errors
            )

        return restore_ebs_response_v1.RestoreEBSResponseV1.from_dictionary(resp)
