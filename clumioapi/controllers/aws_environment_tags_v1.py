#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_tags_response
from clumioapi.models import read_aws_tag_response
from clumioapi.models import read_ebs_tag_compliance_stats_response
import requests


class AwsEnvironmentTagsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-environment-tags resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_aws_environment_tags(
        self,
        environment_id: str,
        current_count: int = None,
        limit: int = None,
        total_count: int = None,
        total_pages_count: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
    ) -> list_aws_tags_response.ListAwsTagsResponse:
        """Returns a list of AWS tags in the specified environment.

        Args:
            environment_id:
                Performs the operation on the AWS environment with the specified ID.
            current_count:
                The number of items listed on the current page.
            limit:
                The maximum number of items displayed per page in the response.
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
                | read-aws-environment-tag-ebs-volumes- | Embeds compliance statistics about   |
                | compliance-stats                      | EBS volumes for each tag into the    |
                |                                       | response. For example, embed=read-   |
                |                                       | aws-environment-tag-ebs-volumes-     |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-dynamodb-    | Embeds compliance statistics about   |
                | tables-compliance-stats               | DynamoDB tables for each tag into    |
                |                                       | the response. For example,           |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | dynamodb-tables-compliance-stats     |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag into the response. For |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

        Returns:
            ListAwsTagsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/environments/{environment_id}/tags'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id}
        )
        _query_parameters = {}
        _query_parameters = {
            'current_count': current_count,
            'limit': limit,
            'total_count': total_count,
            'total_pages_count': total_pages_count,
            'start': start,
            'filter': filter,
            'embed': embed,
        }

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.aws-environment-tags=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_environment_tags.', errors
            )
        return list_aws_tags_response.ListAwsTagsResponse.from_dictionary(resp)

    def read_aws_environment_tag(
        self, environment_id: str, tag_id: str, embed: str = None
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
                | read-aws-environment-tag-ebs-volumes- | Embeds compliance stats about EBS    |
                | compliance-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-tag-ebs-  |
                |                                       | volumes-compliance-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-tag-dynamodb-    | Embeds compliance stats about        |
                | tables-compliance-stats               | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-aws-environment-tag-      |
                |                                       | dynamodb-tables-compliance-stats     |
                +---------------------------------------+--------------------------------------+
                | read-policy-definition                | Embeds the associated policy of a    |
                |                                       | protected tag into the response. For |
                |                                       | example, embed=read-policy-          |
                |                                       | definition                           |
                +---------------------------------------+--------------------------------------+

        Returns:
            ReadAwsTagResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/aws/environments/{environment_id}/tags/{tag_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id, 'tag_id': tag_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.aws-environment-tags=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_environment_tag.', errors
            )
        return read_aws_tag_response.ReadAwsTagResponse.from_dictionary(resp)

    def read_aws_environment_tag_ebs_volumes_compliance_stats(
        self, environment_id: str, tag_id: str
    ) -> read_ebs_tag_compliance_stats_response.ReadEbsTagComplianceStatsResponse:
        """Returns the specified AWS tag's EBS compliance statistics.

        Args:
            environment_id:
                Performs the operation on an AWS tag within the specified environment.
            tag_id:
                Performs the operation on the AWS tag with the specified ID.
        Returns:
            ReadEbsTagComplianceStatsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/environments/{environment_id}/tags/{tag_id}/stats/compliance/ebs-volumes'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id, 'tag_id': tag_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.aws-environment-tags=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_environment_tag_ebs_volumes_compliance_stats.',
                errors,
            )
        return read_ebs_tag_compliance_stats_response.ReadEbsTagComplianceStatsResponse.from_dictionary(
            resp
        )
