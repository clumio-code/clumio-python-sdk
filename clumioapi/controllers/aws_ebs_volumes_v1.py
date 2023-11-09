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
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None, **kwargs
    ) -> Union[
        list_ebs_volumes_response.ListEbsVolumesResponse,
        tuple[requests.Response, Optional[list_ebs_volumes_response.ListEbsVolumesResponse]],
    ]:
        """Returns a list of EBS volumes.

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
                | compliance_status         | $eq, in          | The compliance status of the  |
                |                           |                  | EBS volume. This parameter    |
                |                           |                  | cannot be set if the          |
                |                           |                  | protection_status filter      |
                |                           |                  | parameter is set to           |
                |                           |                  | "unsupported" or              |
                |                           |                  | "unprotected". For example, f |
                |                           |                  | ilter={"compliance_status":{" |
                |                           |                  | $eq":"non_compliant"}} Refer  |
                |                           |                  | to the Compliance Status      |
                |                           |                  | table for a complete list of  |
                |                           |                  | compliance statuses.          |
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ebs_volumes_response.ListEbsVolumesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ebs-volumes'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

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
                'Error occurred while executing list_aws_ebs_volumes.', errors
            )

        if self.config.raw_response:
            return resp, list_ebs_volumes_response.ListEbsVolumesResponse.from_dictionary(
                resp.json()
            )
        return list_ebs_volumes_response.ListEbsVolumesResponse.from_dictionary(resp)

    def read_aws_ebs_volume(
        self, volume_id: str, embed: str = None, **kwargs
    ) -> Union[
        read_ebs_volume_response.ReadEbsVolumeResponse,
        tuple[requests.Response, Optional[read_ebs_volume_response.ReadEbsVolumeResponse]],
    ]:
        """Returns a representation of the specified EBS volume.

        Args:
            volume_id:
                Performs the operation on the EBS Volume with the specified ID.
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ebs_volume_response.ReadEbsVolumeResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ebs-volumes/{volume_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'volume_id': volume_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

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
                'Error occurred while executing read_aws_ebs_volume.', errors
            )

        if self.config.raw_response:
            return resp, read_ebs_volume_response.ReadEbsVolumeResponse.from_dictionary(resp.json())
        return read_ebs_volume_response.ReadEbsVolumeResponse.from_dictionary(resp)
