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
from clumioapi.models import list_tags_response
from clumioapi.models import read_tag_response
import requests


class VmwareVcenterTagsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-tags resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-tags=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_vmware_vcenter_tags(
        self,
        vcenter_id: str,
        limit: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
        **kwargs,
    ) -> Union[
        list_tags_response.ListTagsResponse,
        tuple[requests.Response, Optional[list_tags_response.ListTagsResponse]],
    ]:
        """Returns a list of tags in the specified vCenter server.

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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | name                      | contains         | The name of the tag. For      |
                |                           |                  | example, filter={"name":{"$co |
                |                           |                  | ntains":"backup-tag"}}        |
                +---------------------------+------------------+-------------------------------+
                | category.id               | eq               | The Clumio-assigned ID of the |
                |                           |                  | category in which to search   |
                |                           |                  | for tags. For example, filter |
                |                           |                  | ={"category.id":{"$eq":"d78cd |
                |                           |                  | 819-ab15-48e2-acea-           |
                |                           |                  | 3f94d3a9f2fb"}}               |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | eq               | The Clumio-assigned ID of the |
                |                           |                  | policy protecting the tag.    |
                |                           |                  | For example, filter={"protect |
                |                           |                  | ion_info.policy_id":{"$eq":"9 |
                |                           |                  | c2934fc-ff4d-11e9-8e11-       |
                |                           |                  | 76706df7fe01"}}               |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | in               | The protection status of the  |
                |                           |                  | tag. Refer to the Protection  |
                |                           |                  | Status table for a complete   |
                |                           |                  | list of protection statuses.  |
                |                           |                  | For example, filter={"protect |
                |                           |                  | ion_status":{"$in":["unprotec |
                |                           |                  | ted", "protected"]}}          |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-tag-compliance-   | Embeds the compliance statistics of  |
                | stats                                 | VMs with the specified tag applied   |
                |                                       | into the response. For example,      |
                |                                       | embed=read-vmware-vcenter-tag-       |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag in the response. Has   |
                |                                       | no effect on unprotected tags. For   |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_tags_response.ListTagsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/vmware/vcenters/{vcenter_id}/tags'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

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
                'Error occurred while executing list_vmware_vcenter_tags.', errors
            )

        if self.config.raw_response:
            return resp, list_tags_response.ListTagsResponse.from_dictionary(resp.json())
        return list_tags_response.ListTagsResponse.from_dictionary(resp)

    def read_vmware_vcenter_tag(
        self, vcenter_id: str, tag_id: str, embed: str = None, **kwargs
    ) -> Union[
        read_tag_response.ReadTagResponse,
        tuple[requests.Response, Optional[read_tag_response.ReadTagResponse]],
    ]:
        """Returns a representation of the specified tag.

        Args:
            vcenter_id:
                Performs the operation on a tag within the specified vCenter server.
            tag_id:
                Performs the operation on the tag with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-tag-compliance-   | Embeds the compliance statistics of  |
                | stats                                 | VMs with the specified tag applied   |
                |                                       | into the response. For example,      |
                |                                       | embed=read-vmware-vcenter-tag-       |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag in the response. Has   |
                |                                       | no effect on unprotected tags. For   |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_tag_response.ReadTagResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/datasources/vmware/vcenters/{vcenter_id}/tags/{tag_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'tag_id': tag_id}
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
                'Error occurred while executing read_vmware_vcenter_tag.', errors
            )

        if self.config.raw_response:
            return resp, read_tag_response.ReadTagResponse.from_dictionary(resp.json())
        return read_tag_response.ReadTagResponse.from_dictionary(resp)
