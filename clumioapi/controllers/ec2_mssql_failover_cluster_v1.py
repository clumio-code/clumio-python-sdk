#
# Copyright 2021. Clumio, Inc.
#

import json

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
        self, failover_cluster_id: str
    ) -> read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse:
        """Returns a representation of the specified failover cluster.

        Args:
            failover_cluster_id:
                Performs the operation on the fci with the specified ID.
        Returns:
            read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-mssql/failover-clusters/{failover_cluster_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'failover_cluster_id': failover_cluster_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_ec2_mssql_failover_cluster.', errors
            )

        return read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse.from_dictionary(resp)
