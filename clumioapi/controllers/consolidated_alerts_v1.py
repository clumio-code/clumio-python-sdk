#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import consolidated_alerts_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_consolidated_alerts_response
from clumioapi.models import read_consolidated_alert_response
from clumioapi.models import update_consolidated_alert_response
from clumioapi.models import update_consolidated_alert_v1_request
import requests


class ConsolidatedAlertsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for consolidated-alerts resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.consolidated-alerts=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_consolidated_alerts(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: consolidated_alerts_types.ListConsolidatedAlertsV1FilterT | None = None,
        **kwargs,
    ) -> list_consolidated_alerts_response.ListConsolidatedAlertsResponse:
        """Returns a list of consolidated alerts.

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

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | status                      | $in              | The consolidated alert      |
                |                             |                  | status.                     |
                |                             |                  | Set to "active" to display  |
                |                             |                  | only the consolidated       |
                |                             |                  | alerts that have one or     |
                |                             |                  | more of its associated      |
                |                             |                  | individual alerts in        |
                |                             |                  | "active" status.            |
                |                             |                  | Set to "cleared" to display |
                |                             |                  | only the consolidated       |
                |                             |                  | alerts that have all        |
                |                             |                  | individual alerts in        |
                |                             |                  | "cleared" status. For       |
                |                             |                  | example, filter={"status":{ |
                |                             |                  | "$in":["cleared"]}}         |
                +-----------------------------+------------------+-----------------------------+
                | raised_timestamp            | $lte, $gte       | The timestamp value of when |
                |                             |                  | the consolidated alert was  |
                |                             |                  | initially raised.           |
                |                             |                  | Represented in RFC-3339     |
                |                             |                  | format. For example, filter |
                |                             |                  | ={"raised_timestamp":{"$lte |
                |                             |                  | ":"1985-04-12T23:20:50Z"}}  |
                +-----------------------------+------------------+-----------------------------+
                | parent_entity.id and        | $eq              |                             |
                | parent_entity.type          |                  | The system-generated ID and |
                |                             |                  | value (name) of the parent  |
                |                             |                  | entity that is associated   |
                |                             |                  | with the primary entity     |
                |                             |                  | affected by the alert.      |
                |                             |                  | These two fields must be    |
                |                             |                  | set together. For example,  |
                |                             |                  | filter={"parent_entity.id": |
                |                             |                  | {"$eq":"9c2934fc-ff4d-11e9- |
                |                             |                  | 8e11-                       |
                |                             |                  | 76706df7fe01"},"parent_enti |
                |                             |                  | ty.type":{"$eq":"aws_enviro |
                |                             |                  | nment"}}                    |
                +-----------------------------+------------------+-----------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_consolidated_alerts_response.ListConsolidatedAlertsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/alerts/consolidated'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_consolidated_alerts_response.ListConsolidatedAlertsResponse
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
            error_str = f'list_consolidated_alerts for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_consolidated_alert(
        self, id: str | None = None, **kwargs
    ) -> read_consolidated_alert_response.ReadConsolidatedAlertResponse:
        """Returns a representation of the specified consolidated alert.

        Args:
            id:
                Performs the operation on the consolidated alert with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_consolidated_alert_response.ReadConsolidatedAlertResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/alerts/consolidated/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_consolidated_alert_response.ReadConsolidatedAlertResponse
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
            error_str = f'read_consolidated_alert for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_consolidated_alert(
        self,
        id: str | None = None,
        body: update_consolidated_alert_v1_request.UpdateConsolidatedAlertV1Request | None = None,
        **kwargs,
    ) -> update_consolidated_alert_response.UpdateConsolidatedAlertResponse:
        """Manages the specified consolidated alert. Managing a consolidated alert includes
        clearing the alert and adding notes to the specified consolidated alert.

        Args:
            id:
                Performs the operation on the consolidated alert with the specified ID.
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_consolidated_alert_response.UpdateConsolidatedAlertResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/alerts/consolidated/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters: dict[str, Any] = {}

        resp_instance: update_consolidated_alert_response.UpdateConsolidatedAlertResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'update_consolidated_alert for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class ConsolidatedAlertsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for consolidated-alerts resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = ConsolidatedAlertsV1Controller(config)

    def list_consolidated_alerts(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: consolidated_alerts_types.ListConsolidatedAlertsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_consolidated_alerts_response.ListConsolidatedAlertsResponse]:
        """Returns a list of consolidated alerts.

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

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | status                      | $in              | The consolidated alert      |
                |                             |                  | status.                     |
                |                             |                  | Set to "active" to display  |
                |                             |                  | only the consolidated       |
                |                             |                  | alerts that have one or     |
                |                             |                  | more of its associated      |
                |                             |                  | individual alerts in        |
                |                             |                  | "active" status.            |
                |                             |                  | Set to "cleared" to display |
                |                             |                  | only the consolidated       |
                |                             |                  | alerts that have all        |
                |                             |                  | individual alerts in        |
                |                             |                  | "cleared" status. For       |
                |                             |                  | example, filter={"status":{ |
                |                             |                  | "$in":["cleared"]}}         |
                +-----------------------------+------------------+-----------------------------+
                | raised_timestamp            | $lte, $gte       | The timestamp value of when |
                |                             |                  | the consolidated alert was  |
                |                             |                  | initially raised.           |
                |                             |                  | Represented in RFC-3339     |
                |                             |                  | format. For example, filter |
                |                             |                  | ={"raised_timestamp":{"$lte |
                |                             |                  | ":"1985-04-12T23:20:50Z"}}  |
                +-----------------------------+------------------+-----------------------------+
                | parent_entity.id and        | $eq              |                             |
                | parent_entity.type          |                  | The system-generated ID and |
                |                             |                  | value (name) of the parent  |
                |                             |                  | entity that is associated   |
                |                             |                  | with the primary entity     |
                |                             |                  | affected by the alert.      |
                |                             |                  | These two fields must be    |
                |                             |                  | set together. For example,  |
                |                             |                  | filter={"parent_entity.id": |
                |                             |                  | {"$eq":"9c2934fc-ff4d-11e9- |
                |                             |                  | 8e11-                       |
                |                             |                  | 76706df7fe01"},"parent_enti |
                |                             |                  | ty.type":{"$eq":"aws_enviro |
                |                             |                  | nment"}}                    |
                +-----------------------------+------------------+-----------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_consolidated_alerts(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
