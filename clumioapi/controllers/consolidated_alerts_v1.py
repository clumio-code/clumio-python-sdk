#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
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
        }

    def list_consolidated_alerts(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_consolidated_alerts_response.ListConsolidatedAlertsResponse:
        """Returns a list of consolidated alerts.

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

        Returns:
            ListConsolidatedAlertsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/alerts/consolidated'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_consolidated_alerts.', errors
            )
        return list_consolidated_alerts_response.ListConsolidatedAlertsResponse.from_dictionary(
            resp
        )

    def read_consolidated_alert(
        self, id: str
    ) -> read_consolidated_alert_response.ReadConsolidatedAlertResponse:
        """Returns a representation of the specified consolidated alert.

        Args:
            id:
                Performs the operation on the consolidated alert with the specified ID.
        Returns:
            ReadConsolidatedAlertResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/alerts/consolidated/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_consolidated_alert.', errors
            )
        return read_consolidated_alert_response.ReadConsolidatedAlertResponse.from_dictionary(resp)

    def update_consolidated_alert(
        self,
        id: str,
        body: update_consolidated_alert_v1_request.UpdateConsolidatedAlertV1Request = None,
    ) -> update_consolidated_alert_response.UpdateConsolidatedAlertResponse:
        """Manages the specified consolidated alert. Managing a consolidated alert includes
        clearing the alert and adding notes to the specified consolidated alert.

        Args:
            id:
                Performs the operation on the consolidated alert with the specified ID.
            body:

        Returns:
            UpdateConsolidatedAlertResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/alerts/consolidated/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_consolidated_alert.', errors
            )
        return update_consolidated_alert_response.UpdateConsolidatedAlertResponse.from_dictionary(
            resp
        )
