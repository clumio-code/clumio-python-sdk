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
from clumioapi.models import list_ec2_mssqlfc_is_response
import requests


class Ec2MssqlFailoverClustersV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for ec2-mssql-failover-clusters resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-failover-clusters=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_ec2_mssql_failover_clusters(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None, **kwargs
    ) -> Union[
        list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse,
        tuple[requests.Response, Optional[list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse]],
    ]:
        """Returns a list of failover clusters.

        Args:
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
                | name                      | $contains        | Filter fci based on the name  |
                |                           |                  | of the cluster.               |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | Filter fci based on the       |
                |                           |                  | environment ID.               |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter fci based on the       |
                |                           |                  | policy id                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter fci whose protection   |
                |                           |                  | status is equal to the given  |
                |                           |                  | string.                       |
                +---------------------------+------------------+-------------------------------+
                | account_ids               | $in              | Filter FCIs which belong to   |
                |                           |                  | any one or more of the        |
                |                           |                  | accounts in the list of       |
                |                           |                  | account_ids.                  |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-policy-definition                | Embeds the definition of the policy  |
                |                                       | associated with this resource.       |
                |                                       | Unprotected resources will not have  |
                |                                       | an associated policy. For example,   |
                |                                       | embed=read-policy-definition.        |
                +---------------------------------------+--------------------------------------+
                | get-ec2-mssql-failover-cluster-stats  | Embeds the stats information         |
                |                                       | associated with failover cluster.    |
                |                                       | For example, embed=get-ec2-mssql-    |
                |                                       | failover-cluster-stats.              |
                +---------------------------------------+--------------------------------------+
                | get-ec2-mssql-failover-cluster-hosts- | Embeds the stats information         |
                | info                                  | associated with Hosts part of        |
                |                                       | failover cluster. For example,       |
                |                                       | embed=get-ec2-mssql-failover-        |
                |                                       | cluster-hosts-info.                  |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-mssql/failover-clusters'

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
                'Error occurred while executing list_ec2_mssql_failover_clusters.', errors
            )

        if self.config.raw_response:
            return resp, list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse.from_dictionary(
                resp.json()
            )
        return list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse.from_dictionary(resp)
