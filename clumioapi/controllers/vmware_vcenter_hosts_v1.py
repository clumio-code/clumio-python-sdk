#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_hosts_response
from clumioapi.models import read_host_response
import requests


class VmwareVcenterHostsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-hosts resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-hosts=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_vmware_vcenter_hosts(
        self, vcenter_id: str, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_hosts_response.ListHostsResponse,
        tuple[requests.Response, Optional[list_hosts_response.ListHostsResponse]],
    ]:
        """Returns a list of hosts in the specified vCenter server.

        Args:
            vcenter_id:
                Performs the operation on the vCenter server with the specified ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------+------------------+-------------------------------------+
                |        Field        | Filter Condition |             Description             |
                +=====================+==================+=====================================+
                | is_standalone       | $eq              | The standalone status of the host.  |
                |                     |                  | Set to "true" to retrieve           |
                |                     |                  | standalone hosts. Set to "false" to |
                |                     |                  | retrieve shared hosts that are part |
                |                     |                  | of clusters. For example, filter={" |
                |                     |                  | is_standalone":{"$eq":true}}        |
                +---------------------+------------------+-------------------------------------+
                | compute_resource.id | $eq              | The VMware-assigned Managed Object  |
                |                     |                  | Reference (MoRef) ID of the compute |
                |                     |                  | resource from which this host       |
                |                     |                  | draws. For example, filter={"comput |
                |                     |                  | e_resource.id":{"$eq":"domain-      |
                |                     |                  | s4298"}}                            |
                +---------------------+------------------+-------------------------------------+
                | datacenter.id       | $eq              | The VMware-assigned Managed Object  |
                |                     |                  | Reference (MoRef) ID of the data    |
                |                     |                  | center in which this host resides.  |
                |                     |                  | For example, filter={"datacenter.id |
                |                     |                  | ":{"$eq":"datacenter-9301"}}        |
                +---------------------+------------------+-------------------------------------+
                | is_supported        | $eq              | Determines whether the host can be  |
                |                     |                  | used as a restore destination. If   |
                |                     |                  | true, the host can be used as a     |
                |                     |                  | restore destination and backups can |
                |                     |                  | be restored to the host. For        |
                |                     |                  | example, filter={"is_supported":{"$ |
                |                     |                  | eq":true}}                          |
                +---------------------+------------------+-------------------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                compute_resource.id
                datacenter.id

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_hosts_response.ListHostsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/hosts'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

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
                'Error occurred while executing list_vmware_vcenter_hosts.', errors
            )

        if self.config.raw_response:
            return resp, list_hosts_response.ListHostsResponse.from_dictionary(resp.json())
        return list_hosts_response.ListHostsResponse.from_dictionary(resp)

    def read_vmware_vcenter_host(
        self, vcenter_id: str, host_id: str, **kwargs
    ) -> Union[
        read_host_response.ReadHostResponse,
        tuple[requests.Response, Optional[read_host_response.ReadHostResponse]],
    ]:
        """Returns a representation of the specified host.

        Args:
            vcenter_id:
                Performs the operation on a host within the specified vCenter server.
            host_id:
                Performs the operation on the host with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_host_response.ReadHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/hosts/{host_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'host_id': host_id}
        )
        _query_parameters = {}

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
                'Error occurred while executing read_vmware_vcenter_host.', errors
            )

        if self.config.raw_response:
            return resp, read_host_response.ReadHostResponse.from_dictionary(resp.json())
        return read_host_response.ReadHostResponse.from_dictionary(resp)
