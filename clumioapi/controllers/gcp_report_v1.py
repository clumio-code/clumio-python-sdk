#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any
import urllib.parse

from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import gcs_asset_error_report_v1_request
from clumioapi.models import gcs_asset_error_report_v1_response
from clumioapi.models import gcs_protection_group_error_report_v1_request
from clumioapi.models import gcs_protection_group_error_report_v1_response
import requests


class GcpReportV1Controller:
    """A Controller to access Endpoints for gcp-report resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-report=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def gcs_asset_error_report(
        self,
        embed: str | None = None,
        body: gcs_asset_error_report_v1_request.GcsAssetErrorReportV1Request | None = None,
        **kwargs,
    ) -> gcs_asset_error_report_v1_response.GcsAssetErrorReportV1Response:
        """Returns task ID

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +-----------------+----------------------------------------------------------+
                | Embeddable Link |                       Description                        |
                +=================+==========================================================+
                | read-task       | Embeds the associated task in the response. For example, |
                |                 | embed=read-task                                          |
                |                 |                                                          |
                +-----------------+----------------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return gcs_asset_error_report_v1_response.GcsAssetErrorReportV1Response.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/report/gcs/gcs-asset'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: gcs_asset_error_report_v1_response.GcsAssetErrorReportV1Response
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
            error_str = f'gcs_asset_error_report for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def gcs_protection_group_error_report(
        self,
        embed: str | None = None,
        body: (
            gcs_protection_group_error_report_v1_request.GcsProtectionGroupErrorReportV1Request
            | None
        ) = None,
        **kwargs,
    ) -> gcs_protection_group_error_report_v1_response.GcsProtectionGroupErrorReportV1Response:
        """Returns task ID

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +-----------------+----------------------------------------------------------+
                | Embeddable Link |                       Description                        |
                +=================+==========================================================+
                | read-task       | Embeds the associated task in the response. For example, |
                |                 | embed=read-task                                          |
                |                 |                                                          |
                +-----------------+----------------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return gcs_protection_group_error_report_v1_response.GcsProtectionGroupErrorReportV1Response.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/report/gcs/protection-group'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: (
            gcs_protection_group_error_report_v1_response.GcsProtectionGroupErrorReportV1Response
        )
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
            error_str = f'gcs_protection_group_error_report for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpReportV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-report resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
