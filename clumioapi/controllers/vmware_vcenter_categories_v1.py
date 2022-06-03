#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_tag_categories2_response
from clumioapi.models import read_tag_category2_response
import requests


class VmwareVcenterCategoriesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-categories resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-categories=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }

    def list_vmware_vcenter_categories(
        self, vcenter_id: str, limit: int = None, start: str = None, filter: str = None
    ) -> list_tag_categories2_response.ListTagCategories2Response:
        """Returns a list of tag categories in the specified vCenter server.

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

                +-------+------------------+---------------------------------------------------+
                | Field | Filter Condition |                    Description                    |
                +=======+==================+===================================================+
                | name  | contains         | The name of the category. For example,            |
                |       |                  | filter={"name":{"$contains":"backup-category"}}   |
                +-------+------------------+---------------------------------------------------+

        Returns:
            ListTagCategories2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/categories'
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
                'Error occurred while executing list_vmware_vcenter_categories.', errors
            )
        return list_tag_categories2_response.ListTagCategories2Response.from_dictionary(resp)

    def read_vmware_vcenter_category(
        self, vcenter_id: str, category_id: str
    ) -> read_tag_category2_response.ReadTagCategory2Response:
        """Returns a representation of the specified tag category.

        Args:
            vcenter_id:
                Performs the operation on a tag category within the specified vCenter server.
            category_id:
                Performs the operation on the tag category with the specified ID.
        Returns:
            ReadTagCategory2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/categories/{category_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'category_id': category_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_category.', errors
            )
        return read_tag_category2_response.ReadTagCategory2Response.from_dictionary(resp)
