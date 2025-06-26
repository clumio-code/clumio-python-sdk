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
from clumioapi.models import list_rds_resources_response
from clumioapi.models import read_rds_resource_response
import requests


class AwsRdsResourcesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-rds-resources resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-rds-resources=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_rds_resources(
        self,
        limit: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
        lookback_days: int = None,
        **kwargs,
    ) -> Union[
        list_rds_resources_response.ListRdsResourcesResponse,
        tuple[requests.Response, Optional[list_rds_resources_response.ListRdsResourcesResponse]],
    ]:
        """Retrieve a list of RDS resources.

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
                | resource_native_id        | $eq              | The AWS-assigned ID of this   |
                |                           |                  | resource. For example, filter |
                |                           |                  | ={"resource_native_id":{"$eq" |
                |                           |                  | :"db-                         |
                |                           |                  | CRYU5ABKC4Y2IO3NZISYPIZNBA"}} |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains        | The AWS-assigned name of this |
                |                           |                  | resource. For example, filter |
                |                           |                  | ={"name":{"$contains":"dev"}} |
                |                           |                  | retrieves all RDS resources   |
                |                           |                  | with "dev" in their name.     |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example, filter={"account_nat |
                |                           |                  | ive_id":{"$eq":"789901323485" |
                |                           |                  | }} retrieves RDS resources    |
                |                           |                  | across all regions in account |
                |                           |                  | 789901323485.                 |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | engine                    | $eq              | The database engine of this   |
                |                           |                  | resource. Possible values     |
                |                           |                  | include postgres and mysql.   |
                |                           |                  | For a full list of possible   |
                |                           |                  | values, please refer to the   |
                |                           |                  | AWS documentation.            |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The Clumio-assigned ID(s) of  |
                |                           |                  | AWS tag(s) applied to this    |
                |                           |                  | resource. For example, filter |
                |                           |                  | ={"tags.id":{"$all":["c764b15 |
                |                           |                  | 2-5819-11ea-bb9f-             |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                |                           |                  | retrieves all RDS resources   |
                |                           |                  | that are associated with the  |
                |                           |                  | 2 AWS tags identified by      |
                |                           |                  | these IDs. If multiple tags   |
                |                           |                  | are specified, all of them    |
                |                           |                  | must be applied to the same   |
                |                           |                  | RDS resource.                 |
                +---------------------------+------------------+-------------------------------+
                | type                      | $in              | The type of this resource.    |
                |                           |                  | Possible values include       |
                |                           |                  | aws_rds_cluster and           |
                |                           |                  | aws_rds_instance. For         |
                |                           |                  | example, filter={"type":{"$in |
                |                           |                  | ":["aws_rds_cluster"]}}       |
                |                           |                  | retrieves all RDS resources   |
                |                           |                  | that are Aurora clusters.     |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include protected,            |
                |                           |                  | unprotected, and unsupported. |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active RDS     |
                |                           |                  | resources. filter={"is_delete |
                |                           |                  | d":{"$in":["true","false"]}}  |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources will not have  |
                |                        | an associated policy. For example, embed=read-      |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rds_resources_response.ListRdsResourcesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/rds-resources'

        _query_parameters = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter,
            'embed': embed,
            'lookback_days': lookback_days,
        }

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
                'Error occurred while executing list_aws_rds_resources.', errors
            )

        if self.config.raw_response:
            return resp, list_rds_resources_response.ListRdsResourcesResponse.from_dictionary(
                resp.json()
            )
        return list_rds_resources_response.ListRdsResourcesResponse.from_dictionary(resp)

    def read_aws_rds_resource(
        self, resource_id: str, lookback_days: int = None, embed: str = None, **kwargs
    ) -> Union[
        read_rds_resource_response.ReadRdsResourceResponse,
        tuple[requests.Response, Optional[read_rds_resource_response.ReadRdsResourceResponse]],
    ]:
        """Returns a representation of the specified RDS resource.

        Args:
            resource_id:
                The Clumio-assigned ID of the resource.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | the resource (if any).                              |
                +------------------------+-----------------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_rds_resource_response.ReadRdsResourceResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/rds-resources/{resource_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'resource_id': resource_id}
        )
        _query_parameters = {}
        _query_parameters = {'lookback_days': lookback_days, 'embed': embed}

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
                'Error occurred while executing read_aws_rds_resource.', errors
            )

        if self.config.raw_response:
            return resp, read_rds_resource_response.ReadRdsResourceResponse.from_dictionary(
                resp.json()
            )
        return read_rds_resource_response.ReadRdsResourceResponse.from_dictionary(resp)
