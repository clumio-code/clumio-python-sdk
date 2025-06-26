#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_ec2_mssqlfci_response
import requests


class Ec2MssqlFailoverClusterV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for ec2-mssql-failover-cluster resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-failover-cluster=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_ec2_mssql_failover_cluster(
        self, failover_cluster_id: str, embed: str = None, lookback_days: int = None, **kwargs
    ) -> Union[
        read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse,
        tuple[requests.Response, Optional[read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse]],
    ]:
        """Returns a representation of the specified failover cluster.

        Args:
            failover_cluster_id:
                Performs the operation on the fci with the specified ID.
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
                | get-ec2-mssql-stats-backup-status     | Embeds the backup statistics for     |
                |                                       | each resource into the response. For |
                |                                       | example, embed=get-ec2-mssql-stats-  |
                |                                       | backup-status                        |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/failover-clusters/{failover_cluster_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'failover_cluster_id': failover_cluster_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed, 'lookback_days': lookback_days}

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
                'Error occurred while executing read_ec2_mssql_failover_cluster.', errors
            )

        if self.config.raw_response:
            return resp, read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse.from_dictionary(
                resp.json()
            )
        return read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse.from_dictionary(resp)
