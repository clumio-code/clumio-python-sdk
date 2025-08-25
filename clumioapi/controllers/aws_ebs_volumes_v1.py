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
from clumioapi.controllers.types import aws_ebs_volumes_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ebs_volumes_response
from clumioapi.models import read_ebs_volume_response
import requests


class AwsEbsVolumesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-ebs-volumes resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-ebs-volumes=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_ebs_volumes(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_ebs_volumes_types.ListAwsEbsVolumesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_ebs_volumes_response.ListEbsVolumesResponse:
        """Returns a list of EBS volumes.

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
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains, $eq   | The AWS-assigned name of this |
                |                           |                  | resource to conditionalize    |
                |                           |                  | on. For example, filter={"nam |
                |                           |                  | e":{"$contains":"dev"}}       |
                |                           |                  | retrieves all EBS volumes     |
                |                           |                  | with "dev" in their name.     |
                |                           |                  | filter={"name":{"$eq":"dev"}} |
                |                           |                  | retrieves only EBS volumes    |
                |                           |                  | with names that exactly match |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | volume_native_id          | $eq, $contains   | The AWS-assigned ID of the    |
                |                           |                  | EBS volume.                   |
                |                           |                  | For example, filter={"volume_ |
                |                           |                  | native_id":{"$eq":"vol-       |
                |                           |                  | 06aa02a849fe376d9"}} or filte |
                |                           |                  | r={"volume_native_id":{"$cont |
                |                           |                  | ains":"02a849"}}              |
                |                           |                  | Both filter operations cannot |
                |                           |                  | be used simultaneously.       |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example, fil |
                |                           |                  | ter={"account_native_id":{"$e |
                |                           |                  | q":"789901323485"}}           |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq, $in         | The protection status of the  |
                |                           |                  | EBS volume. For example, filt |
                |                           |                  | er={"protection_status":{"$eq |
                |                           |                  | ":"protected"}} or filter={"p |
                |                           |                  | rotection_status":{"$in":["pr |
                |                           |                  | otected"]}}.  Refer to the    |
                |                           |                  | Protection Status table for a |
                |                           |                  | complete list of protection   |
                |                           |                  | statuses.                     |
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
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource. filter={"protection |
                |                           |                  | _info.policy_id":{"$eq":"c764 |
                |                           |                  | abb6-5819-16ea-               |
                |                           |                  | bb9f-b2e1c9a040ad"}}          |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The ID of the AWS tag applied |
                |                           |                  | to the EBS volume. For        |
                |                           |                  | example, filter={"tags.id":{" |
                |                           |                  | $all":["c764b152-5819-11ea-bb |
                |                           |                  | 9f-b2e1c9a040ad","c764abb6-   |
                |                           |                  | 5819-11ea-                    |
                |                           |                  | bb9f-b2e1c9a040ad"]}}. If     |
                |                           |                  | multiple tags are specified,  |
                |                           |                  | all of them must be applied   |
                |                           |                  | to the same EBS volume.       |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of the    |
                |                           |                  | EBS volume. Set to "true" to  |
                |                           |                  | retrieve deleted EBS volumes. |
                |                           |                  | For example, filter={"is_dele |
                |                           |                  | ted":{"$eq":true}} filter={"i |
                |                           |                  | s_deleted":{"$in":["true","fa |
                |                           |                  | lse"]}}                       |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with each
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EBS     |
                |                        | volume into the response. For example, embed=read-  |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_ebs_volumes_response.ListEbsVolumesResponse.from_response(response)

        # Prepare query URL
        _url_path = '/datasources/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_ebs_volumes_response.ListEbsVolumesResponse
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
            error_str = f'list_aws_ebs_volumes for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_ebs_volume(
        self,
        volume_id: str | None = None,
        lookback_days: int | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> read_ebs_volume_response.ReadEbsVolumeResponse:
        """Returns a representation of the specified EBS volume.

        Args:
            volume_id:
                Performs the operation on the EBS Volume with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EBS     |
                |                        | volume into the response. For example, embed=read-  |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_ebs_volume_response.ReadEbsVolumeResponse.from_response(response)

        # Prepare query URL
        _url_path = '/datasources/aws/ebs-volumes/{volume_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'volume_id': volume_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'lookback_days': lookback_days, 'embed': embed}

        resp_instance: read_ebs_volume_response.ReadEbsVolumeResponse
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
            error_str = f'read_aws_ebs_volume for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsEbsVolumesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for aws-ebs-volumes resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AwsEbsVolumesV1Controller(config)

    def list_aws_ebs_volumes(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_ebs_volumes_types.ListAwsEbsVolumesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_ebs_volumes_response.ListEbsVolumesResponse]:
        """Returns a list of EBS volumes.

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
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains, $eq   | The AWS-assigned name of this |
                |                           |                  | resource to conditionalize    |
                |                           |                  | on. For example, filter={"nam |
                |                           |                  | e":{"$contains":"dev"}}       |
                |                           |                  | retrieves all EBS volumes     |
                |                           |                  | with "dev" in their name.     |
                |                           |                  | filter={"name":{"$eq":"dev"}} |
                |                           |                  | retrieves only EBS volumes    |
                |                           |                  | with names that exactly match |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | volume_native_id          | $eq, $contains   | The AWS-assigned ID of the    |
                |                           |                  | EBS volume.                   |
                |                           |                  | For example, filter={"volume_ |
                |                           |                  | native_id":{"$eq":"vol-       |
                |                           |                  | 06aa02a849fe376d9"}} or filte |
                |                           |                  | r={"volume_native_id":{"$cont |
                |                           |                  | ains":"02a849"}}              |
                |                           |                  | Both filter operations cannot |
                |                           |                  | be used simultaneously.       |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example, fil |
                |                           |                  | ter={"account_native_id":{"$e |
                |                           |                  | q":"789901323485"}}           |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq, $in         | The protection status of the  |
                |                           |                  | EBS volume. For example, filt |
                |                           |                  | er={"protection_status":{"$eq |
                |                           |                  | ":"protected"}} or filter={"p |
                |                           |                  | rotection_status":{"$in":["pr |
                |                           |                  | otected"]}}.  Refer to the    |
                |                           |                  | Protection Status table for a |
                |                           |                  | complete list of protection   |
                |                           |                  | statuses.                     |
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
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource. filter={"protection |
                |                           |                  | _info.policy_id":{"$eq":"c764 |
                |                           |                  | abb6-5819-16ea-               |
                |                           |                  | bb9f-b2e1c9a040ad"}}          |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The ID of the AWS tag applied |
                |                           |                  | to the EBS volume. For        |
                |                           |                  | example, filter={"tags.id":{" |
                |                           |                  | $all":["c764b152-5819-11ea-bb |
                |                           |                  | 9f-b2e1c9a040ad","c764abb6-   |
                |                           |                  | 5819-11ea-                    |
                |                           |                  | bb9f-b2e1c9a040ad"]}}. If     |
                |                           |                  | multiple tags are specified,  |
                |                           |                  | all of them must be applied   |
                |                           |                  | to the same EBS volume.       |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of the    |
                |                           |                  | EBS volume. Set to "true" to  |
                |                           |                  | retrieve deleted EBS volumes. |
                |                           |                  | For example, filter={"is_dele |
                |                           |                  | ted":{"$eq":true}} filter={"i |
                |                           |                  | s_deleted":{"$in":["true","fa |
                |                           |                  | lse"]}}                       |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with each
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EBS     |
                |                        | volume into the response. For example, embed=read-  |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        start = start or '1'
        while True:
            response = self.controller.list_aws_ebs_volumes(
                limit=limit,
                start=start,
                filter=filter,
                embed=embed,
                lookback_days=lookback_days,
                **kwargs,
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
