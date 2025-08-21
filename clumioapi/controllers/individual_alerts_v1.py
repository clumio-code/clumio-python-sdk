#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_alerts_response
from clumioapi.models import read_alert_response
from clumioapi.models import update_alert_response
from clumioapi.models import update_individual_alert_v1_request
import requests


class IndividualAlertsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for individual-alerts resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.individual-alerts=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_individual_alerts(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: str | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> Union[
        list_alerts_response.ListAlertsResponse,
        tuple[requests.Response, Optional[list_alerts_response.ListAlertsResponse]],
    ]:
        """Returns a list of individual alerts.

        Each alert is associated with a cause, which represents the issue that generated
        the alert,
        and each cause belongs to a general alert type. Some alert types may be
        associated with multiple causes.

        The following table lists the Clumio alert types:


        +--------------------------+---------------------------------------------------+
        |        Alert Type        |                    Description                    |
        +==========================+===================================================+
        | policy_violated          | An entity's scheduled backup failed.              |
        +--------------------------+---------------------------------------------------+
        | restore_failed           | An entity restore failed.                         |
        +--------------------------+---------------------------------------------------+
        | file_restore_failed      | A file restore failed.                            |
        +--------------------------+---------------------------------------------------+
        | tag_conflict             | An EBS volume has multiple associated tags        |
        |                          | with different protection policies applied at the |
        |                          | tag level.                                        |
        +--------------------------+---------------------------------------------------+
        | aws_account_disconnected | The connection                                    |
        |                          | between Clumio Cloud Connector and the user's AWS |
        |                          | account failed.                                   |
        +--------------------------+---------------------------------------------------+
        | enc_key_inaccessible     | An issue is blocking encryption key access.       |
        +--------------------------+---------------------------------------------------+

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            sort:
                Returns the list of individual alerts in the order specified. Set `sort` to the
                name of the sort field by which to sort in ascending order.
                To sort the list in reverse order, prefix the field name with a minus sign
                (`-`).
                Only one field may be sorted at a time.

                The following table lists the supported sort fields for this resource and the
                operations that can be performed on the field:

                +-------------------+----------------------------------------------------------+
                |    Sort Field     |                       Description                        |
                +===================+==========================================================+
                | raised_timestamp  | Sorts the individual alerts in chronological ascending   |
                |                   | (oldest first) order by when the alert was raised. For   |
                |                   | example, sort=raised_timestamp                           |
                +-------------------+----------------------------------------------------------+
                | updated_timestamp | Sorts the individual alerts in chronological ascending   |
                |                   | (oldest first) order by when the alert was last updated. |
                |                   | For example, sort=updated_timestamp                      |
                +-------------------+----------------------------------------------------------+
                | cleared_timestamp | Sorts the individual alerts in chronological ascending   |
                |                   | (oldest first) order by when the alert was cleared,      |
                |                   | either automatically by Clumio or manually by a Clumio   |
                |                   | user. For example, sort=cleared_timestamp                |
                +-------------------+----------------------------------------------------------+

                If a sort order is not specified, the individual alerts are sorted by
                "raised_timestamp" in chronological descending (newest first) order.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | type                        | $in              | The general alert category. |
                |                             |                  | Alert types are listed in   |
                |                             |                  | the Alert Type table. For   |
                |                             |                  | example, filter={"type":{"$ |
                |                             |                  | in":["policy_violated"]}}   |
                +-----------------------------+------------------+-----------------------------+
                | status                      | $in              | The individual alert        |
                |                             |                  | status. Set to "active" to  |
                |                             |                  | display only                |
                |                             |                  | the individual alerts that  |
                |                             |                  | are in the active status.   |
                |                             |                  | Set to "cleared" to display |
                |                             |                  | only the individual alerts  |
                |                             |                  | that have been cleared,     |
                |                             |                  | either automatically by     |
                |                             |                  | Clumio or manually by a     |
                |                             |                  | Clumio user. For example, f |
                |                             |                  | ilter={"status":{"$in":["cl |
                |                             |                  | eared"]}}                   |
                +-----------------------------+------------------+-----------------------------+
                | severity                    | $in              | The alert severity level.   |
                |                             |                  | Values include "error".     |
                +-----------------------------+------------------+-----------------------------+
                | raised_timestamp            | $lte, $gte       | The timestamp value of when |
                |                             |                  | the alert was raised.       |
                |                             |                  | Represented in RFC-3339     |
                |                             |                  | format. For example, filter |
                |                             |                  | ={"raised_timestamp":{"$lte |
                |                             |                  | ":"1985-04-12T23:20:50Z"}}  |
                +-----------------------------+------------------+-----------------------------+
                | updated_timestamp           | $lte, $gte       | The timestamp value of when |
                |                             |                  | the alert was last updated. |
                |                             |                  | Represented in RFC-3339     |
                |                             |                  | format.                     |
                |                             |                  | The alert is updated        |
                |                             |                  | whenever there is a new     |
                |                             |                  | occurrence of the same      |
                |                             |                  | alert within the same       |
                |                             |                  | entity. For example, filter |
                |                             |                  | ={"updated_timestamp":{"$lt |
                |                             |                  | e":"1985-04-12T23:20:50Z"}} |
                +-----------------------------+------------------+-----------------------------+
                | cleared_timestamp           | $lte, $gte       | The timestamp value of when |
                |                             |                  | the alert was cleared,      |
                |                             |                  | either automatically by     |
                |                             |                  | Clumio or manually by a     |
                |                             |                  | Clumio user. Represented in |
                |                             |                  | RFC-3339 format. For        |
                |                             |                  | example, filter={"cleared_t |
                |                             |                  | imestamp":{"$lte":"1985-04- |
                |                             |                  | 12T23:20:50Z"}}             |
                +-----------------------------+------------------+-----------------------------+
                | consolidated_alert_id       | $eq              | The Clumio-assigned ID of   |
                |                             |                  | the consolidated alert      |
                |                             |                  | associated with the         |
                |                             |                  | individual alert. For       |
                |                             |                  | example, filter={"consolida |
                |                             |                  | ted_alert_id":{"$eq":"d78cd |
                |                             |                  | 819-ab15-48e2-acea-         |
                |                             |                  | 3f94d3a9f2fb"}}             |
                +-----------------------------+------------------+-----------------------------+
                | primary_entity.id           | $eq              | The system-generated ID of  |
                |                             |                  | the primary entity affected |
                |                             |                  | by the alert. For example,  |
                |                             |                  | filter={"primary_entity.id" |
                |                             |                  | :{"eq":"503765b4-62af-536d- |
                |                             |                  | c7ab-c5850a123194"}}        |
                +-----------------------------+------------------+-----------------------------+
                | primary_entity.type         | $eq              | The type of primary entity  |
                |                             |                  | affected by the alert.      |
                |                             |                  | Examples of primary entity  |
                |                             |                  | types include               |
                |                             |                  | "aws_ebs_volume",           |
                |                             |                  | "aws_environment". For      |
                |                             |                  | example, filter={"primary_e |
                |                             |                  | ntity.type":{"$eq":"aws_ebs |
                |                             |                  | _volume"}}                  |
                +-----------------------------+------------------+-----------------------------+
                | primary_entity.value        | $contains        | The value or name           |
                |                             |                  | associated with the primary |
                |                             |                  | entity affected by the      |
                |                             |                  | alert. For example, filter= |
                |                             |                  | {"primary_entity.value":{"$ |
                |                             |                  | contains":"prod"}}          |
                +-----------------------------+------------------+-----------------------------+
                | parent_entity.id and        | $eq              |                             |
                | parent_entity.type          |                  | The system-generated ID and |
                |                             |                  | type of the parent entity   |
                |                             |                  | that is associated with the |
                |                             |                  | primary entity affected by  |
                |                             |                  | the alert. Both filters     |
                |                             |                  | must be used together. For  |
                |                             |                  | example, filter={"parent_en |
                |                             |                  | tity.id":{"$eq":"9c2934fc-f |
                |                             |                  | f4d-11e9-8e11-              |
                |                             |                  | 76706df7fe01"},"parent_enti |
                |                             |                  | ty.type":{"$eq":"aws_enviro |
                |                             |                  | nment"}}                    |
                +-----------------------------+------------------+-----------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-------------------------+----------------------------------------------------+
                |     Embeddable Link     |                    Description                     |
                +=========================+====================================================+
                | read-consolidated-alert | Embeds the associated consolidated alert in the    |
                |                         | response. For example, embed=read-consolidated-    |
                |                         | alert                                              |
                +-------------------------+----------------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_alerts_response.ListAlertsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/alerts/individual'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter,
            'embed': embed,
        }

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_individual_alerts', error=http_error
            )

        obj = list_alerts_response.ListAlertsResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_individual_alert(
        self, individual_alert_id: str | None = None, embed: str | None = None, **kwargs
    ) -> Union[
        read_alert_response.ReadAlertResponse,
        tuple[requests.Response, Optional[read_alert_response.ReadAlertResponse]],
    ]:
        """Returns a representation of the specified individual alert.

        Args:
            individual_alert_id:
                Performs the operation on the individual alert with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-------------------------+----------------------------------------------------+
                |     Embeddable Link     |                    Description                     |
                +=========================+====================================================+
                | read-consolidated-alert | Embeds the associated consolidated alert in the    |
                |                         | response. For example, embed=read-consolidated-    |
                |                         | alert                                              |
                +-------------------------+----------------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_alert_response.ReadAlertResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/alerts/individual/{individual_alert_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'individual_alert_id': individual_alert_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_individual_alert', error=http_error
            )

        obj = read_alert_response.ReadAlertResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def update_individual_alert(
        self,
        individual_alert_id: str | None = None,
        embed: str | None = None,
        body: update_individual_alert_v1_request.UpdateIndividualAlertV1Request | None = None,
        **kwargs,
    ) -> Union[
        update_alert_response.UpdateAlertResponse,
        tuple[requests.Response, Optional[update_alert_response.UpdateAlertResponse]],
    ]:
        """Manages an existing individual alert. Managing an individual alert includes
        clearing the alert and adding notes to the specified alert.

        Args:
            individual_alert_id:
                Performs the operation on the individual alert with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-------------------------+----------------------------------------------------+
                |     Embeddable Link     |                    Description                     |
                +=========================+====================================================+
                | read-consolidated-alert | Embeds the associated consolidated alert in the    |
                |                         | response. For example, embed=read-consolidated-    |
                |                         | alert                                              |
                +-------------------------+----------------------------------------------------+

            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_alert_response.UpdateAlertResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/alerts/individual/{individual_alert_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'individual_alert_id': individual_alert_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_individual_alert', error=http_error
            )

        obj = update_alert_response.UpdateAlertResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
