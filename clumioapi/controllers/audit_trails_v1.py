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
from clumioapi.controllers.types import audit_trails_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_audit_trails_response
import requests
import retrying


class AuditTrailsV1Controller:
    """A Controller to access Endpoints for audit-trails resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.audit-trails=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_audit_trails(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: audit_trails_types.ListAuditTrailsV1FilterT | None = None,
        **kwargs,
    ) -> list_audit_trails_response.ListAuditTrailsResponse:
        """Returns a list of audit trails.

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

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | start_timestamp        | $gte, $lt, $eq   | The start timestamp denotes the  |
                |                        |                  | time filter for audit events     |
                |                        |                  | (when the server received the    |
                |                        |                  | request)                         |
                |                        |                  | $gte and $lt accept RFC-3999     |
                |                        |                  | timestamps and $eq accepts a     |
                |                        |                  | unix timestamp                   |
                |                        |                  | denoting the offset from the     |
                |                        |                  | current time. $eq takes          |
                |                        |                  | precedence over both             |
                |                        |                  | $gte and $lt so if $eq is used,  |
                |                        |                  | the backend will use the         |
                |                        |                  | relative time filter             |
                |                        |                  | instead of absolute time         |
                |                        |                  | filters.For example,             |
                |                        |                  |                                  |
                |                        |                  | filter={"start_timestamp":{"$eq" |
                |                        |                  | :86400}}                         |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | category               | $in              | The category of the resource     |
                |                        |                  | affected by an audit event.      |
                |                        |                  | Possible values include          |
                |                        |                  | authentication, data_source,     |
                |                        |                  | policy, protection, restore,     |
                |                        |                  | tasks,                           |
                |                        |                  | backup, users, api_tokens,       |
                |                        |                  | kms_config,                      |
                |                        |                  | sso, mfa, reports, alerts,       |
                |                        |                  | cloud_connector,                 |
                |                        |                  | cloudformation_template,         |
                |                        |                  | bandwidth_config,                |
                |                        |                  | partner_ecosystem, and           |
                |                        |                  | ecosystem_changes.               |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"category":{"$in":["poli |
                |                        |                  | cy"]}}                           |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | action                 | $in              |  The action performed by the     |
                |                        |                  | audit event. Possible values     |
                |                        |                  | include                          |
                |                        |                  | create, update, delete,          |
                |                        |                  | enable, disable, browse, search, |
                |                        |                  | login, logout, register,         |
                |                        |                  | unregister,                      |
                |                        |                  | refresh, apply, deploy, remove,  |
                |                        |                  | invite, suspend, full_restore,   |
                |                        |                  | and granular_restore.            |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"action":{"$in":["login" |
                |                        |                  | ]}}                              |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | status                 | $in              |  Whether or not the action       |
                |                        |                  | succeeded. Possible values       |
                |                        |                  | include success,                 |
                |                        |                  | failure, and partial_success.    |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"status":{"$in":["succes |
                |                        |                  | s"]}}                            |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | user_email             | $in              |  The email address of the user   |
                |                        |                  | performing the action            |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"user_email":{"$in":["xy |
                |                        |                  | z@example.com"]}}                |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | ip_address             | $eq              |  The IP Address of the client    |
                |                        |                  | making the request. For example, |
                |                        |                  |                                  |
                |                        |                  | filter={"ip_address":{"$eq":"127 |
                |                        |                  | .0.0.1"}}                        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.id      | $in              | The system-generated IDs of the  |
                |                        |                  | primary entities affected by the |
                |                        |                  | activity.                        |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.id":{"$i |
                |                        |                  | n":["9c2934fc-                   |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"]}}  |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.type    | $eq              |  The type(s) of primary entities |
                |                        |                  | to filter on.                    |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.type":{" |
                |                        |                  | $in":["aws_ebs_volume"]}}        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.value   | $in              | The value(s) or name(s) to       |
                |                        |                  | filter on. For example, the      |
                |                        |                  | primary entity                   |
                |                        |                  | value associated with primary    |
                |                        |                  | entity type "aws_ebs_volume" is  |
                |                        |                  | "vol-0a5f2e52d6decd664"          |
                |                        |                  | representing the name of the EBS |
                |                        |                  | volume.                          |
                |                        |                  | The filter supports substring    |
                |                        |                  | search for all elements in the   |
                |                        |                  | array For example,               |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.value":{ |
                |                        |                  | "$in":["vol-0a"]}}               |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.type     | $in              |  The type(s) of the parent       |
                |                        |                  | entities to filter on.           |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.type":{"$ |
                |                        |                  | in":["aws_environment"]}}        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.value    | $in              |                                  |
                |                        |                  | The value(s) or name(s)          |
                |                        |                  | associated with the parent       |
                |                        |                  | entities affected by             |
                |                        |                  | the event. For example, the      |
                |                        |                  | parent entity value associated   |
                |                        |                  | with                             |
                |                        |                  | primary entity type              |
                |                        |                  | "aws_ebs_volume" is              |
                |                        |                  | "891106093485/us-west-2"         |
                |                        |                  | representing                     |
                |                        |                  | the name of the AWS Account      |
                |                        |                  | Region. For example,             |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.value":{" |
                |                        |                  | $in":["891106093485/us-          |
                |                        |                  | west-2"]}}                       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.id       | $in              |                                  |
                |                        |                  | The system-generated IDs of the  |
                |                        |                  | parent entities which are        |
                |                        |                  | associated with the              |
                |                        |                  | primary entity affected by the   |
                |                        |                  | event. For example,              |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.id":{"$in |
                |                        |                  | ":["9c2934fc-                    |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"]}}  |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $eq              |                                  |
                |                        |                  | The system-generated ID of the   |
                |                        |                  | organizational unit whose audit  |
                |                        |                  | trails are desired.              |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"organizational_unit_id" |
                |                        |                  | :{"$eq":"9c2934fc-               |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"}}   |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_audit_trails_response.ListAuditTrailsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/audit-trails'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_audit_trails_response.ListAuditTrailsResponse
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
            error_str = f'list_audit_trails for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AuditTrailsV1ControllerPaginator:
    """A Controller to access Endpoints for audit-trails resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_audit_trails(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: audit_trails_types.ListAuditTrailsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_audit_trails_response.ListAuditTrailsResponse]:
        """Returns a list of audit trails.

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

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | start_timestamp        | $gte, $lt, $eq   | The start timestamp denotes the  |
                |                        |                  | time filter for audit events     |
                |                        |                  | (when the server received the    |
                |                        |                  | request)                         |
                |                        |                  | $gte and $lt accept RFC-3999     |
                |                        |                  | timestamps and $eq accepts a     |
                |                        |                  | unix timestamp                   |
                |                        |                  | denoting the offset from the     |
                |                        |                  | current time. $eq takes          |
                |                        |                  | precedence over both             |
                |                        |                  | $gte and $lt so if $eq is used,  |
                |                        |                  | the backend will use the         |
                |                        |                  | relative time filter             |
                |                        |                  | instead of absolute time         |
                |                        |                  | filters.For example,             |
                |                        |                  |                                  |
                |                        |                  | filter={"start_timestamp":{"$eq" |
                |                        |                  | :86400}}                         |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | category               | $in              | The category of the resource     |
                |                        |                  | affected by an audit event.      |
                |                        |                  | Possible values include          |
                |                        |                  | authentication, data_source,     |
                |                        |                  | policy, protection, restore,     |
                |                        |                  | tasks,                           |
                |                        |                  | backup, users, api_tokens,       |
                |                        |                  | kms_config,                      |
                |                        |                  | sso, mfa, reports, alerts,       |
                |                        |                  | cloud_connector,                 |
                |                        |                  | cloudformation_template,         |
                |                        |                  | bandwidth_config,                |
                |                        |                  | partner_ecosystem, and           |
                |                        |                  | ecosystem_changes.               |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"category":{"$in":["poli |
                |                        |                  | cy"]}}                           |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | action                 | $in              |  The action performed by the     |
                |                        |                  | audit event. Possible values     |
                |                        |                  | include                          |
                |                        |                  | create, update, delete,          |
                |                        |                  | enable, disable, browse, search, |
                |                        |                  | login, logout, register,         |
                |                        |                  | unregister,                      |
                |                        |                  | refresh, apply, deploy, remove,  |
                |                        |                  | invite, suspend, full_restore,   |
                |                        |                  | and granular_restore.            |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"action":{"$in":["login" |
                |                        |                  | ]}}                              |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | status                 | $in              |  Whether or not the action       |
                |                        |                  | succeeded. Possible values       |
                |                        |                  | include success,                 |
                |                        |                  | failure, and partial_success.    |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"status":{"$in":["succes |
                |                        |                  | s"]}}                            |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | user_email             | $in              |  The email address of the user   |
                |                        |                  | performing the action            |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"user_email":{"$in":["xy |
                |                        |                  | z@example.com"]}}                |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | ip_address             | $eq              |  The IP Address of the client    |
                |                        |                  | making the request. For example, |
                |                        |                  |                                  |
                |                        |                  | filter={"ip_address":{"$eq":"127 |
                |                        |                  | .0.0.1"}}                        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.id      | $in              | The system-generated IDs of the  |
                |                        |                  | primary entities affected by the |
                |                        |                  | activity.                        |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.id":{"$i |
                |                        |                  | n":["9c2934fc-                   |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"]}}  |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.type    | $eq              |  The type(s) of primary entities |
                |                        |                  | to filter on.                    |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.type":{" |
                |                        |                  | $in":["aws_ebs_volume"]}}        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | primary_entity.value   | $in              | The value(s) or name(s) to       |
                |                        |                  | filter on. For example, the      |
                |                        |                  | primary entity                   |
                |                        |                  | value associated with primary    |
                |                        |                  | entity type "aws_ebs_volume" is  |
                |                        |                  | "vol-0a5f2e52d6decd664"          |
                |                        |                  | representing the name of the EBS |
                |                        |                  | volume.                          |
                |                        |                  | The filter supports substring    |
                |                        |                  | search for all elements in the   |
                |                        |                  | array For example,               |
                |                        |                  |                                  |
                |                        |                  | filter={"primary_entity.value":{ |
                |                        |                  | "$in":["vol-0a"]}}               |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.type     | $in              |  The type(s) of the parent       |
                |                        |                  | entities to filter on.           |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.type":{"$ |
                |                        |                  | in":["aws_environment"]}}        |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.value    | $in              |                                  |
                |                        |                  | The value(s) or name(s)          |
                |                        |                  | associated with the parent       |
                |                        |                  | entities affected by             |
                |                        |                  | the event. For example, the      |
                |                        |                  | parent entity value associated   |
                |                        |                  | with                             |
                |                        |                  | primary entity type              |
                |                        |                  | "aws_ebs_volume" is              |
                |                        |                  | "891106093485/us-west-2"         |
                |                        |                  | representing                     |
                |                        |                  | the name of the AWS Account      |
                |                        |                  | Region. For example,             |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.value":{" |
                |                        |                  | $in":["891106093485/us-          |
                |                        |                  | west-2"]}}                       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | parent_entity.id       | $in              |                                  |
                |                        |                  | The system-generated IDs of the  |
                |                        |                  | parent entities which are        |
                |                        |                  | associated with the              |
                |                        |                  | primary entity affected by the   |
                |                        |                  | event. For example,              |
                |                        |                  |                                  |
                |                        |                  | filter={"parent_entity.id":{"$in |
                |                        |                  | ":["9c2934fc-                    |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"]}}  |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $eq              |                                  |
                |                        |                  | The system-generated ID of the   |
                |                        |                  | organizational unit whose audit  |
                |                        |                  | trails are desired.              |
                |                        |                  | For example,                     |
                |                        |                  |                                  |
                |                        |                  | filter={"organizational_unit_id" |
                |                        |                  | :{"$eq":"9c2934fc-               |
                |                        |                  | ff4d-11e9-8e11-76706df7fe01"}}   |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+

        """
        controller = AuditTrailsV1Controller(self.controller)
        while True:
            response = controller.list_audit_trails(
                limit=limit, start=start, filter=filter, **kwargs
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
