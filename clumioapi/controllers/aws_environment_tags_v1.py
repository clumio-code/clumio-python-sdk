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
from clumioapi.controllers.types import aws_environment_tags_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_tags_response
from clumioapi.models import read_aws_tag_response
import requests
import retrying


class AwsEnvironmentTagsV1Controller:
    """A Controller to access Endpoints for aws-environment-tags resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-environment-tags=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_aws_environment_tags(
        self,
        environment_id: str | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        total_count: int | None = None,
        total_pages_count: int | None = None,
        start: str | None = None,
        filter: aws_environment_tags_types.ListAwsEnvironmentTagsV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_aws_tags_response.ListAwsTagsResponse:
        """Returns a list of AWS tags in the specified environment.

        Args:
            environment_id:
                Performs the operation on the AWS environment with the specified ID.
            current_count:
                The number of items listed on the current page.
            limit:
                Limits the size of the items returned in the response.
            total_count:
                The total number of items, summed across all pages.
            total_pages_count:
                The total number of pages of results.
            start:
                The page number used to get this response.
                Pages are indexed starting from 1 (i.e., `"start": "1"`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | key_id                    | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS tag key associated with   |
                |                           |                  | the tag. For example, filter= |
                |                           |                  | {"key_id":{"$eq":"d23cd819-   |
                |                           |                  | ab15-48e2-acea-               |
                |                           |                  | 3f94d3a9f2fb"}}               |
                +---------------------------+------------------+-------------------------------+
                | value                     | $contains        | The AWS-assigned value of the |
                |                           |                  | tag. For example, filter={"va |
                |                           |                  | lue":{"$contains":"vol"}}     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | The protection status of the  |
                |                           |                  | tag. Set to "protected" to    |
                |                           |                  | return only protected tags.   |
                |                           |                  | For example, filter={"protect |
                |                           |                  | ion_status":{"$eq":"protected |
                |                           |                  | "}}                           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of a   |
                |                           |                  | Clumio policy applied to the  |
                |                           |                  | tag. For example, filter={"pr |
                |                           |                  | otection_info.policy_id":{"$e |
                |                           |                  | q":"e12cd819-ab15-48e2-acea-  |
                |                           |                  | 3f94d3a9f2fb"}}               |
                +---------------------------+------------------+-------------------------------+
                | id                        | $in              | The Clumio-assigned ID of the |
                |                           |                  | AWS tag. Multiple tags can be |
                |                           |                  | specified. For example, filte |
                |                           |                  | r={"id":{"in":["f78cd123-     |
                |                           |                  | ab15-48e2-acea-               |
                |                           |                  | 3f94d3a9f2fb","abbcd819-ba15- |
                |                           |                  | 48e2-acea-3f94aba9f2fb"]}}    |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-tag-ebs-volumes- | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-ebs-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-             | Embeds protection stats about EC2    |
                | ec2-instances-protection-stats        | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-rds-volumes- | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-rds-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-dynamodb-    | Embeds protection stats about        |
                | tables-protection-stats               | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-protection-  | Embeds protection stats about        |
                | groups-protection-stats               | Protection Groups associated with    |
                |                                       | this tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-protection-groups-protection-    |
                |                                       | stats                                |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-backup-      | Embeds the backup statistics for     |
                | status-stats                          | each tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-backup-status-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag into the response. For |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_aws_tags_response.ListAwsTagsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/environments/{environment_id}/tags'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'current_count': current_count,
            'limit': limit,
            'total_count': total_count,
            'total_pages_count': total_pages_count,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_aws_tags_response.ListAwsTagsResponse
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
                f'list_aws_environment_tags for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_environment_tag(
        self,
        environment_id: str | None = None,
        tag_id: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> read_aws_tag_response.ReadAwsTagResponse:
        """Returns a representation of the specified AWS tag in the specified environment.

        Args:
            environment_id:
                Performs the operation on an AWS tag within the specified environment.
            tag_id:
                Performs the operation on the AWS tag with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-tag-ebs-volumes- | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-ebs-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-             | Embeds protection stats about EC2    |
                | ec2-instances-protection-stats        | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-rds-volumes- | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-rds-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-dynamodb-    | Embeds protection stats about        |
                | tables-protection-stats               | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-protection-  | Embeds protection stats about        |
                | groups-protection-stats               | Protection Groups associated with    |
                |                                       | this tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-protection-groups-protection-    |
                |                                       | stats                                |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-backup-      | Embeds the backup statistics for     |
                | status-stats                          | each tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-backup-status-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag into the response. For |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_aws_tag_response.ReadAwsTagResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/environments/{environment_id}/tags/{tag_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id, 'tag_id': tag_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: read_aws_tag_response.ReadAwsTagResponse
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
            error_str = f'read_aws_environment_tag for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsEnvironmentTagsV1ControllerPaginator:
    """A Controller to access Endpoints for aws-environment-tags resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_aws_environment_tags(
        self,
        environment_id: str | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        total_count: int | None = None,
        total_pages_count: int | None = None,
        start: str | None = None,
        filter: aws_environment_tags_types.ListAwsEnvironmentTagsV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_aws_tags_response.ListAwsTagsResponse]:
        """Returns a list of AWS tags in the specified environment.

        Args:
            environment_id:
                Performs the operation on the AWS environment with the specified ID.
            current_count:
                The number of items listed on the current page.
            limit:
                Limits the size of the items returned in the response.
            total_count:
                The total number of items, summed across all pages.
            total_pages_count:
                The total number of pages of results.
            start:
                The page number used to get this response.
                Pages are indexed starting from 1 (i.e., `"start": "1"`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | key_id                    | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS tag key associated with   |
                |                           |                  | the tag. For example, filter= |
                |                           |                  | {"key_id":{"$eq":"d23cd819-   |
                |                           |                  | ab15-48e2-acea-               |
                |                           |                  | 3f94d3a9f2fb"}}               |
                +---------------------------+------------------+-------------------------------+
                | value                     | $contains        | The AWS-assigned value of the |
                |                           |                  | tag. For example, filter={"va |
                |                           |                  | lue":{"$contains":"vol"}}     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | The protection status of the  |
                |                           |                  | tag. Set to "protected" to    |
                |                           |                  | return only protected tags.   |
                |                           |                  | For example, filter={"protect |
                |                           |                  | ion_status":{"$eq":"protected |
                |                           |                  | "}}                           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of a   |
                |                           |                  | Clumio policy applied to the  |
                |                           |                  | tag. For example, filter={"pr |
                |                           |                  | otection_info.policy_id":{"$e |
                |                           |                  | q":"e12cd819-ab15-48e2-acea-  |
                |                           |                  | 3f94d3a9f2fb"}}               |
                +---------------------------+------------------+-------------------------------+
                | id                        | $in              | The Clumio-assigned ID of the |
                |                           |                  | AWS tag. Multiple tags can be |
                |                           |                  | specified. For example, filte |
                |                           |                  | r={"id":{"in":["f78cd123-     |
                |                           |                  | ab15-48e2-acea-               |
                |                           |                  | 3f94d3a9f2fb","abbcd819-ba15- |
                |                           |                  | 48e2-acea-3f94aba9f2fb"]}}    |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-tag-ebs-volumes- | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-ebs-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-             | Embeds protection stats about EC2    |
                | ec2-instances-protection-stats        | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-rds-volumes- | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-rds-  |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-dynamodb-    | Embeds protection stats about        |
                | tables-protection-stats               | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-protection-  | Embeds protection stats about        |
                | groups-protection-stats               | Protection Groups associated with    |
                |                                       | this tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-protection-groups-protection-    |
                |                                       | stats                                |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-backup-      | Embeds the backup statistics for     |
                | status-stats                          | each tag into the response. For      |
                |                                       | example, embed=read-aws-environment- |
                |                                       | tag-backup-status-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag into the response. For |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = AwsEnvironmentTagsV1Controller(self.controller)
        while True:
            response = controller.list_aws_environment_tags(
                environment_id=environment_id,
                current_count=current_count,
                limit=limit,
                total_count=total_count,
                total_pages_count=total_pages_count,
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
