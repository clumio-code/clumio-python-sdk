#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_resource_pools_response
from clumioapi.models import read_resource_pool_response
import requests


class VmwareVcenterResourcePoolsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-resource-pools resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-resource-pools=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_vmware_vcenter_resource_pools(
        self, vcenter_id: str, limit: int = None, start: str = None, filter: str = None
    ) -> list_resource_pools_response.ListResourcePoolsResponse:
        """Returns a list of resource pools in the specified vCenter server.

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

                +----------------------+------------------+------------------------------------+
                |        Field         | Filter Condition |            Description             |
                +======================+==================+====================================+
                | *parent.id           | $eq              | The VMware-assigned ID number of   |
                |                      |                  | the compute resource or resource   |
                |                      |                  | pool associated as the parent of   |
                |                      |                  | this resource pool. For example, f |
                |                      |                  | ilter={"parent.id":{"$eq":"resgrou |
                |                      |                  | p-28544"}}                         |
                +----------------------+------------------+------------------------------------+
                | *datacenter.id       | $eq              | The VMware-assigned Managed Object |
                |                      |                  | Reference (MoRef) ID of the data   |
                |                      |                  | center associated with this        |
                |                      |                  | resource pool. For example, filter |
                |                      |                  | ={"datacenter.id":{"$eq":"datacent |
                |                      |                  | er-9301"}}                         |
                +----------------------+------------------+------------------------------------+
                | *compute_resource.id | $eq              | The VMware-assigned Managed Object |
                |                      |                  | Reference (MoRef) ID of the        |
                |                      |                  | compute resource associated with   |
                |                      |                  | this resource pool. For example, f |
                |                      |                  | ilter={"compute_resource.id":{"$eq |
                |                      |                  | ":"domain-s4298"}}                 |
                +----------------------+------------------+------------------------------------+
                | is_supported         | $eq              | Determines whether the resource    |
                |                      |                  | pool can be used as a restore      |
                |                      |                  | destination. If true, the resource |
                |                      |                  | pool can be used as a restore      |
                |                      |                  | destination and backups can be     |
                |                      |                  | restored to the resource pool. For |
                |                      |                  | example, filter={"is_supported":{" |
                |                      |                  | $eq":true}}                        |
                +----------------------+------------------+------------------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                parent.id
                datacenter.id
                compute_resource.id

        Returns:
            ListResourcePoolsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/resource-pools'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_resource_pools.', errors
            )
        return list_resource_pools_response.ListResourcePoolsResponse.from_dictionary(resp)

    def read_vmware_vcenter_resource_pool(
        self, vcenter_id: str, resource_pool_id: str
    ) -> read_resource_pool_response.ReadResourcePoolResponse:
        """Returns a representation of the specified resource pool.

        Args:
            vcenter_id:
                Performs the operation on a resource pool within the specified vCenter server.
            resource_pool_id:
                Performs the operation on the resource pool with the specified ID.
        Returns:
            ReadResourcePoolResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/resource-pools/{resource_pool_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'resource_pool_id': resource_pool_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_resource_pool.', errors
            )
        return read_resource_pool_response.ReadResourcePoolResponse.from_dictionary(resp)
