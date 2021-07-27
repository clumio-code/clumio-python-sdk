#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_aws_ebs_volume_v1_request
import requests


class RestoredAwsEbsVolumesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-ebs-volumes resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def restore_aws_ebs_volume(
        self, body: restore_aws_ebs_volume_v1_request.RestoreAwsEbsVolumeV1Request = None
    ) -> object:
        """Restores the specified source EBS volume backup to the specified target
        destination. The source EBS volume must be one that was backup up by Clumio.

        Args:
            body:

        Returns:
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/aws/ebs-volumes'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/restored-aws-ebs-volumes=v1+json',
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_aws_ebs_volume.', errors
            )
        return resp