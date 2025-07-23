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
    ) -> Union[
        restore_ec2_response.RestoreEC2Response,
        tuple[requests.Response, Optional[restore_ec2_response.RestoreEC2Response]],
    ]:
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            restore_ec2_response.RestoreEC2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_aws_ec2_instance.', errors
            )

        if self.config.raw_response:
            return resp, restore_ec2_response.RestoreEC2Response.from_dictionary(resp.json())
        return restore_ec2_response.RestoreEC2Response.from_dictionary(resp.json())
