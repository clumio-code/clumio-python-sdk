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
from clumioapi.models import read_ec2_mssqlfci_response
import requests
import retrying


class Ec2MssqlFailoverClusterV1Controller:
    """A Controller to access Endpoints for ec2-mssql-failover-cluster resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-failover-cluster=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def read_ec2_mssql_failover_cluster(
        self,
        failover_cluster_id: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse:
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
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/failover-clusters/{failover_cluster_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'failover_cluster_id': failover_cluster_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: read_ec2_mssqlfci_response.ReadEC2MSSQLFCIResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'read_ec2_mssql_failover_cluster for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class Ec2MssqlFailoverClusterV1ControllerPaginator:
    """A Controller to access Endpoints for ec2-mssql-failover-cluster resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
