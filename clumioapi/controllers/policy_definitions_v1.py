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

    def list_policy_definitions(self, filter: str = None, embed: str = None, **kwargs) -> Union[
        list_policies_response.ListPoliciesResponse,
        tuple[requests.Response, Optional[list_policies_response.ListPoliciesResponse]],
    ]:
        """Returns a list of policies and their configurations.

        The following table describes the supported policy operations.

        +----------------------------------+-------------------------------------------+
        |            Operation             |                Description                |
        +==================================+===========================================+
        | vmware_vm_backup                 | VMware VM backup.                         |
        +----------------------------------+-------------------------------------------+
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
        | mssql_database_backup            | VMC MSSQL database backup stored in       |
        |                                  | Clumio.                                   |
        +----------------------------------+-------------------------------------------+
        | mssql_log_backup                 | VMC MSSQL log backup stored in Clumio.    |
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
        |                   | compliance status set to "deactivated".                  |
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
                |                   |                   | e":{"$in":["vmware_vm_backup","aws_e |
                |                   |                   | bs_volume_backup"]}}                 |
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
                | [DEPRECATED] read-policy-aws-ebs-     | Embeds compliance statistics about   |
                | volumes-compliance-stats              | EBS volumes into the _embedded field |
                |                                       | of each policy in the response. For  |
                |                                       | example, embed=read-policy-aws-ebs-  |
                |                                       | volumes-compliance-stats             |
                +---------------------------------------+--------------------------------------+
                | [DEPRECATED] read-policy-vmware-vms-  | Embeds compliance statistics about   |
                | compliance-stats                      | VMs into the _embedded field of each |
                |                                       | policy in the response. For example, |
                |                                       | embed=read-policy-vmware-vms-        |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | [DEPRECATED] read-policy-aws-         | Embeds compliance statistics about   |
                | dynamodb-tables-compliance-stats      | DynamoDB tables into the _embedded   |
                |                                       | field of each policy in the          |
                |                                       | response. For example, embed=read-   |
                |                                       | policy-aws-dynamodb-tables-          |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | [DEPRECATED] read-policy-protection-  | Embeds compliance statistics about   |
                | groups-compliance-stats               | protection groups into the _embedded |
                |                                       | field of each policy in the          |
                |                                       | response. For example, embed=read-   |
                |                                       | policy-protection-groups-compliance- |
                |                                       | stats                                |
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

        _query_parameters = {}
        _query_parameters = {'filter': filter, 'embed': embed}

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
                'Error occurred while executing list_policy_definitions.', errors
            )

        if self.config.raw_response:
            return resp, list_policies_response.ListPoliciesResponse.from_dictionary(resp.json())
        return list_policies_response.ListPoliciesResponse.from_dictionary(resp)

    def create_policy_definition(
        self,
        body: create_policy_definition_v1_request.CreatePolicyDefinitionV1Request = None,
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

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_policy_definition.', errors
            )

        if self.config.raw_response:
            return resp, create_policy_response.CreatePolicyResponse.from_dictionary(resp.json())
        return create_policy_response.CreatePolicyResponse.from_dictionary(resp)

    def read_policy_definition(self, policy_id: str, embed: str = None, **kwargs) -> Union[
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
                | [DEPRECATED] read-policy-aws-ebs-     | Embeds compliance statistics about   |
                | volumes-compliance-stats              | EBS volumes into the _embedded field |
                |                                       | of the response. For example,        |
                |                                       | embed=read-policy-aws-ebs-volumes-   |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | [DEPRECATED] read-policy-vmware-vms-  | Embeds compliance statistics about   |
                | compliance-stats                      | VMs into the _embedded field of the  |
                |                                       | response. For example, embed=read-   |
                |                                       | policy-vmware-vms-compliance-stats   |
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
                'Error occurred while executing read_policy_definition.', errors
            )

        if self.config.raw_response:
            return resp, read_policy_response.ReadPolicyResponse.from_dictionary(resp.json())
        return read_policy_response.ReadPolicyResponse.from_dictionary(resp)

    def update_policy_definition(
        self,
        policy_id: str,
        embed: str = None,
        body: update_policy_definition_v1_request.UpdatePolicyDefinitionV1Request = None,
        **kwargs,
    ) -> Union[
        update_policy_response.UpdatePolicyResponse,
        tuple[requests.Response, Optional[update_policy_response.UpdatePolicyResponse]],
    ]:
        """Updates an existing policy by modifying its backup seed setting, backup service
        level agreement (SLA), and backup window. If a policy is updated while a backup
        is in progress, the policy changes will take effect after the backup completes.

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
                | [DEPRECATED] read-policy-aws-ebs-     | Embeds compliance statistics about   |
                | volumes-compliance-stats              | EBS volumes into the _embedded field |
                |                                       | of the response. For example,        |
                |                                       | embed=read-policy-aws-ebs-volumes-   |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+
                | [DEPRECATED] read-policy-vmware-vms-  | Embeds compliance statistics about   |
                | compliance-stats                      | VMs into the _embedded field of the  |
                |                                       | response. For example, embed=read-   |
                |                                       | policy-vmware-vms-compliance-stats   |
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
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_policy_definition.', errors
            )

        if self.config.raw_response:
            return resp, update_policy_response.UpdatePolicyResponse.from_dictionary(resp.json())
        return update_policy_response.UpdatePolicyResponse.from_dictionary(resp)

    def delete_policy_definition(self, policy_id: str, **kwargs) -> Union[
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
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(
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
                'Error occurred while executing delete_policy_definition.', errors
            )

        if self.config.raw_response:
            return resp, delete_policy_response.DeletePolicyResponse.from_dictionary(resp.json())
        return delete_policy_response.DeletePolicyResponse.from_dictionary(resp)
