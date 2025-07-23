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
from clumioapi.models import create_policy_definition_v1_request
from clumioapi.models import create_policy_response
from clumioapi.models import delete_policy_response
from clumioapi.models import list_policies_response
from clumioapi.models import read_policy_response
from clumioapi.models import update_policy_definition_v1_request
from clumioapi.models import update_policy_response
import requests


class PolicyDefinitionsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for policy-definitions resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.policy-definitions=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_policy_definitions(
        self, filter: str | None = None, embed: str | None = None, **kwargs
    ) -> Union[
        list_policies_response.ListPoliciesResponse,
        tuple[requests.Response, Optional[list_policies_response.ListPoliciesResponse]],
    ]:
        """Returns a list of policies and their configurations.

        The following table describes the supported policy operations.

        +----------------------------------+-------------------------------------------+
        |            Operation             |                Description                |
        +==================================+===========================================+
        | aws_ebs_volume_backup            | AWS EBS volume backup.                    |
        +----------------------------------+-------------------------------------------+
        | aws_ebs_volume_snapshot          | AWS EBS volume snapshot stored in         |
        |                                  | customer's AWS account.                   |
        +----------------------------------+-------------------------------------------+
        | aws_ec2_instance_backup          | AWS EC2 instance backup.                  |
        +----------------------------------+-------------------------------------------+
        | aws_ec2_instance_snapshot        | AWS EC2 instance snapshot stored in       |
        |                                  | customer's AWS account.                   |
        +----------------------------------+-------------------------------------------+
        | ec2_mssql_database_backup        | AWS EC2 MSSQL database backup.            |
        +----------------------------------+-------------------------------------------+
        | ec2_mssql_log_backup             | AWS EC2 MSSQL log backup.                 |
        +----------------------------------+-------------------------------------------+
        | aws_rds_resource_aws_snapshot    | AWS RDS snapshot stored in the customer's |
        |                                  | AWS account.                              |
        +----------------------------------+-------------------------------------------+
        | aws_rds_resource_rolling_backup  | AWS RDS backup stored in Clumio.          |
        +----------------------------------+-------------------------------------------+
        | aws_rds_resource_granular_backup | AWS RDS granular backup stored in Clumio. |
        +----------------------------------+-------------------------------------------+
        | aws_dynamodb_table_snapshot      | AWS DynamoDB table snapshot stored in     |
        |                                  | customer's AWS account.                   |
        +----------------------------------+-------------------------------------------+
        | aws_dynamodb_table_pitr          | AWS DynamoDB table point-in-time          |
        |                                  | recovery.                                 |
        +----------------------------------+-------------------------------------------+
        | protection_group_backup          | AWS S3 Protection Group backup.           |
        +----------------------------------+-------------------------------------------+
        | microsoft365_mailbox_backup      | Microsoft365 mailbox backup.              |
        +----------------------------------+-------------------------------------------+
        | microsoft365_onedrive_backup     | Microsoft365 onedrive backup.             |
        +----------------------------------+-------------------------------------------+
        | microsoft365_share_point_backup  | Microsoft365 site backup.                 |
        +----------------------------------+-------------------------------------------+
        | microsoft365_teams_backup        | Microsoft365 team backup.                 |
        +----------------------------------+-------------------------------------------+


        The following table describes the supported policy activation statuses.

        +-------------------+----------------------------------------------------------+
        | Activation Status |                       Description                        |
        +===================+==========================================================+
        | activated         | Backups will take place regularly according to the       |
        |                   | policy SLA.                                              |
        +-------------------+----------------------------------------------------------+
        | deactivated       |                                                          |
        |                   | Backups will not begin until the policy is reactivated.  |
        |                   | The assets associated with the policy will have their    |
        |                   | protection status set to "deactivated".                  |
        |                   |                                                          |
        +-------------------+----------------------------------------------------------+

        Args:
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                filter conditions that can be applied on those fields:

                +-------------------+-------------------+--------------------------------------+
                |       Field       | Filter Condition  |             Description              |
                +===================+===================+======================================+
                | name              | $eq, $begins_with | The unique name of the policy. For   |
                |                   |                   | example,                             |
                |                   |                   | filter={"name":{"$eq":"Silver"}}     |
                +-------------------+-------------------+--------------------------------------+
                | operations.type   | $in               | Set to the desired operations to     |
                |                   |                   | limit the results to policies who    |
                |                   |                   | support the specified operations.    |
                |                   |                   | For example, filter={"operations.typ |
                |                   |                   | e":{"$in":["aws_ec2_instance_backup" |
                |                   |                   | ,"aws_ebs_volume_backup"]}}          |
                +-------------------+-------------------+--------------------------------------+
                | activation_status | $eq               | The activation status of the policy. |
                |                   |                   | For example, filter={"activation_sta |
                |                   |                   | tus":{"$eq":"activated"}}            |
                +-------------------+-------------------+--------------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-policy-aws-ebs-volumes-          | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ebs-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-ec2-instances-        | Embeds protection stats about EC2    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ec2-instances- |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-rds-volumes-          | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-rds-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-dynamodb-tables-      | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-dynamodb-      |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-iceberg-tables-       | Embeds protection stats about        |
                | protection-stats                      | Iceberg tables associated with this  |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-iceberg-       |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-backup-status-stats       | Embeds backup statistics for each    |
                |                                       | AWS environment into the response.   |
                |                                       | For example, embed=read-policy-      |
                |                                       | backup-status-stats                  |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_policies_response.ListPoliciesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/definitions'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'filter': filter, 'embed': embed}

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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_policy_definitions.', errors
            )

        obj = list_policies_response.ListPoliciesResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def create_policy_definition(
        self,
        body: create_policy_definition_v1_request.CreatePolicyDefinitionV1Request | None = None,
        **kwargs,
    ) -> Union[
        create_policy_response.CreatePolicyResponse,
        tuple[requests.Response, Optional[create_policy_response.CreatePolicyResponse]],
    ]:
        """Creates a new policy. Creating a new policy involves configuring the backup seed
        settings, backup service level agreement (SLA), and backup window.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_policy_response.CreatePolicyResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/definitions'

        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_policy_definition.', errors
            )

        obj = create_policy_response.CreatePolicyResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_policy_definition(
        self, policy_id: str | None = None, embed: str | None = None, **kwargs
    ) -> Union[
        read_policy_response.ReadPolicyResponse,
        tuple[requests.Response, Optional[read_policy_response.ReadPolicyResponse]],
    ]:
        """Returns a representation of the specified policy.

        Args:
            policy_id:
                Performs the operation on the policy with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-policy-aws-ebs-volumes-          | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ebs-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-ec2-instances-        | Embeds protection stats about EC2    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ec2-instances- |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-rds-volumes-          | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-rds-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-dynamodb-tables-      | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-dynamodb-      |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-iceberg-tables-       | Embeds protection stats about        |
                | protection-stats                      | Iceberg tables associated with this  |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-iceberg-       |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-backup-status-stats       | Embeds backup statistics for each    |
                |                                       | AWS environment into the response.   |
                |                                       | For example, embed=read-policy-      |
                |                                       | backup-status-stats                  |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_policy_response.ReadPolicyResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/definitions/{policy_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'policy_id': policy_id}
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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_policy_definition.', errors
            )

        obj = read_policy_response.ReadPolicyResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def update_policy_definition(
        self,
        policy_id: str | None = None,
        embed: str | None = None,
        body: update_policy_definition_v1_request.UpdatePolicyDefinitionV1Request | None = None,
        **kwargs,
    ) -> Union[
        update_policy_response.UpdatePolicyResponse,
        tuple[requests.Response, Optional[update_policy_response.UpdatePolicyResponse]],
    ]:
        """Updates an existing policy by modifying its backup seed setting, backup service
        level agreement (SLA), and backup window. The policy is updated asynchronously,
        and the response will include the existing policy. If a policy is updated while
        a backup is in progress, the policy changes will take effect after the backup is
        completed.

        Args:
            policy_id:
                Performs the operation on the policy with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-policy-aws-ebs-volumes-          | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes associated with this tag     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ebs-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-ec2-instances-        | Embeds protection stats about EC2    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-ec2-instances- |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-rds-volumes-          | Embeds protection stats about RDS    |
                | protection-stats                      | Instance associated with this tag    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-policy-aws-rds-volumes-   |
                |                                       | protection-stats                     |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-dynamodb-tables-      | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables associated with this |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-dynamodb-      |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-aws-iceberg-tables-       | Embeds protection stats about        |
                | protection-stats                      | Iceberg tables associated with this  |
                |                                       | tag into the response. For example,  |
                |                                       | embed=read-policy-aws-iceberg-       |
                |                                       | tables-protection-stats              |
                +---------------------------------------+--------------------------------------+
                | read-policy-backup-status-stats       | Embeds backup statistics for each    |
                |                                       | AWS environment into the response.   |
                |                                       | For example, embed=read-policy-      |
                |                                       | backup-status-stats                  |
                +---------------------------------------+--------------------------------------+

            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_policy_response.UpdatePolicyResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/definitions/{policy_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'policy_id': policy_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.put(
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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_policy_definition.', errors
            )

        obj = update_policy_response.UpdatePolicyResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def delete_policy_definition(self, policy_id: str | None = None, **kwargs) -> Union[
        delete_policy_response.DeletePolicyResponse,
        tuple[requests.Response, Optional[delete_policy_response.DeletePolicyResponse]],
    ]:
        """Deletes the specified policy.

        Args:
            policy_id:
                Performs the operation on the policy with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            delete_policy_response.DeletePolicyResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/definitions/{policy_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'policy_id': policy_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_policy_definition.', errors
            )

        obj = delete_policy_response.DeletePolicyResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
