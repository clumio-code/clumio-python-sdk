#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_rds_resource_restore_response
from clumioapi.models import restore_aws_rds_resource_v1_request
import requests
import retrying


class RestoredAwsRdsResourcesV1Controller:
    """A Controller to access Endpoints for restored-aws-rds-resources resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-rds-resources=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_aws_rds_resource(
        self,
        embed: str | None = None,
        body: restore_aws_rds_resource_v1_request.RestoreAwsRdsResourceV1Request | None = None,
        **kwargs,
    ) -> create_rds_resource_restore_response.CreateRdsResourceRestoreResponse:
        """Restores the specified RDS resource backup or snapshot to the specified target
        destination.

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return (
                create_rds_resource_restore_response.CreateRdsResourceRestoreResponse.from_response(
                    resp
                )
            )

        # Prepare query URL
        _url_path = '/restores/aws/rds-resources'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: create_rds_resource_restore_response.CreateRdsResourceRestoreResponse
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
            error_str = f'restore_aws_rds_resource for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsRdsResourcesV1ControllerPaginator:
    """A Controller to access Endpoints for restored-aws-rds-resources resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
