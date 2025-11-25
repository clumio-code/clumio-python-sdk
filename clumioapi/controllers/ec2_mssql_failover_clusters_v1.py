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
from clumioapi.controllers.types import ec2_mssql_failover_clusters_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_mssqlfc_is_response
import requests
import retrying


class Ec2MssqlFailoverClustersV1Controller:
    """A Controller to access Endpoints for ec2-mssql-failover-clusters resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-failover-clusters=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_ec2_mssql_failover_clusters(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            ec2_mssql_failover_clusters_types.ListEc2MssqlFailoverClustersV1FilterT | None
        ) = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse:
        """Returns a list of failover clusters.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                | get-ec2-mssql-stats-backup-status     | Embeds the backup statistics for     |
                |                                       | each resource into the response. For |
                |                                       | example, embed=get-ec2-mssql-stats-  |
                |                                       | backup-status                        |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/failover-clusters'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse
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
                f'list_ec2_mssql_failover_clusters for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class Ec2MssqlFailoverClustersV1ControllerPaginator:
    """A Controller to access Endpoints for ec2-mssql-failover-clusters resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_ec2_mssql_failover_clusters(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            ec2_mssql_failover_clusters_types.ListEc2MssqlFailoverClustersV1FilterT | None
        ) = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_mssqlfc_is_response.ListEC2MSSQLFCIsResponse]:
        """Returns a list of failover clusters.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                | get-ec2-mssql-stats-backup-status     | Embeds the backup statistics for     |
                |                                       | each resource into the response. For |
                |                                       | example, embed=get-ec2-mssql-stats-  |
                |                                       | backup-status                        |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = Ec2MssqlFailoverClustersV1Controller(self.controller)
        while True:
            response = controller.list_ec2_mssql_failover_clusters(
                limit=limit,
                start=start,
                filter=filter,
                embed=embed,
                lookback_days=lookback_days,
                **kwargs,
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
