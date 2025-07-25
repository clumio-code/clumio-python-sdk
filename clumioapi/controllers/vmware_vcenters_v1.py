#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_vcenters_response
from clumioapi.models import read_vcenter_response
import requests


class VmwareVcentersV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenters resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenters=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_vmware_vcenters(
        self, limit: int = None, start: str = None, embed: str = None, **kwargs
    ) -> Union[
        list_vcenters_response.ListVcentersResponse,
        tuple[requests.Response, Optional[list_vcenters_response.ListVcentersResponse]],
    ]:
        """Returns a list of vCenter servers.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------------------+---------------------------------------+
                |           Embeddable Link            |              Description              |
                +======================================+=======================================+
                | read-vmware-vcenter-compliance-stats | Embeds the compliance statistics of   |
                |                                      | VMs into each vCenter server of the   |
                |                                      | response. For example, embed=read-    |
                |                                      | vmware-vcenter-compliance-stats       |
                +--------------------------------------+---------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_vcenters_response.ListVcentersResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/vmware/vcenters'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'embed': embed}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenters.', errors
            )

        if self.config.raw_response:
            return resp, list_vcenters_response.ListVcentersResponse.from_dictionary(resp.json())
        return list_vcenters_response.ListVcentersResponse.from_dictionary(resp)

    def read_vmware_vcenter(self, vcenter_id: str, embed: str = None, **kwargs) -> Union[
        read_vcenter_response.ReadVcenterResponse,
        tuple[requests.Response, Optional[read_vcenter_response.ReadVcenterResponse]],
    ]:
        """Returns a representation of the specified vCenter server.

        Args:
            vcenter_id:
                Performs the operation on the vCenter server with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------------------+---------------------------------------+
                |           Embeddable Link            |              Description              |
                +======================================+=======================================+
                | read-vmware-vcenter-compliance-stats | Embeds the compliance statistics of   |
                |                                      | VMs into each vCenter server of the   |
                |                                      | response. For example, embed=read-    |
                |                                      | vmware-vcenter-compliance-stats       |
                +--------------------------------------+---------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_vcenter_response.ReadVcenterResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/vmware/vcenters/{vcenter_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter.', errors
            )

        if self.config.raw_response:
            return resp, read_vcenter_response.ReadVcenterResponse.from_dictionary(resp.json())
        return read_vcenter_response.ReadVcenterResponse.from_dictionary(resp)
