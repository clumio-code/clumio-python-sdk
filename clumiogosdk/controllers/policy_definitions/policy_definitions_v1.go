// Copyright (c) 2021 Clumio All Rights Reserved

// Package policydefinitions contains methods related to PolicyDefinitions
package policydefinitions

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// PolicyDefinitionsV1 represents a custom type struct
type PolicyDefinitionsV1 struct {
    config config.Config
}

// ListPolicyDefinitions Returns a list of policies and their configurations.
//  
//  The following table describes the supported policy operations.
//  
//  +----------------------------------+-------------------------------------------+
//  |            Operation             |                Description                |
//  +==================================+===========================================+
//  | vmware_vm_backup                 | VMware VM backup.                         |
//  +----------------------------------+-------------------------------------------+
//  | aws_ebs_volume_backup            | AWS EBS volume backup.                    |
//  +----------------------------------+-------------------------------------------+
//  | aws_ebs_volume_snapshot          | AWS EBS volume snapshot stored in         |
//  |                                  | customer's AWS account.                   |
//  +----------------------------------+-------------------------------------------+
//  | aws_ec2_instance_backup          | AWS EC2 instance backup.                  |
//  +----------------------------------+-------------------------------------------+
//  | aws_ec2_instance_snapshot        | AWS EC2 instance snapshot stored in       |
//  |                                  | customer's AWS account.                   |
//  +----------------------------------+-------------------------------------------+
//  | ec2_mssql_database_backup        | AWS EC2 MSSQL database backup.            |
//  +----------------------------------+-------------------------------------------+
//  | ec2_mssql_log_backup             | AWS EC2 MSSQL log backup.                 |
//  +----------------------------------+-------------------------------------------+
//  | aws_rds_resource_aws_snapshot    | AWS RDS snapshot stored in the customer's |
//  |                                  | AWS account.                              |
//  +----------------------------------+-------------------------------------------+
//  | aws_rds_resource_rolling_backup  | AWS RDS backup stored in Clumio.          |
//  +----------------------------------+-------------------------------------------+
//  | aws_rds_resource_granular_backup | AWS RDS granular backup stored in Clumio. |
//  +----------------------------------+-------------------------------------------+
//  | aws_dynamodb_table_snapshot      | AWS DynamoDB table snapshot stored in     |
//  |                                  | customer's AWS account.                   |
//  +----------------------------------+-------------------------------------------+
//  | aws_dynamodb_table_pitr          | AWS DynamoDB table point-in-time          |
//  |                                  | recovery.                                 |
//  +----------------------------------+-------------------------------------------+
//  | protection_group_backup          | AWS S3 Protection Group backup.           |
//  +----------------------------------+-------------------------------------------+
//  | microsoft365_mailbox_backup      | Microsoft365 mailbox backup.              |
//  +----------------------------------+-------------------------------------------+
//  | microsoft365_onedrive_backup     | Microsoft365 onedrive backup.             |
//  +----------------------------------+-------------------------------------------+
//  | microsoft365_share_point_backup  | Microsoft365 site backup.                 |
//  +----------------------------------+-------------------------------------------+
//  | mssql_database_backup            | VMC MSSQL database backup stored in       |
//  |                                  | Clumio.                                   |
//  +----------------------------------+-------------------------------------------+
//  | mssql_log_backup                 | VMC MSSQL log backup stored in Clumio.    |
//  +----------------------------------+-------------------------------------------+
//  
//  
//  The following table describes the supported policy activation statuses.
//  
//  +-------------------+----------------------------------------------------------+
//  | Activation Status |                       Description                        |
//  +===================+==========================================================+
//  | activated         | Backups will take place regularly according to the       |
//  |                   | policy SLA.                                              |
//  +-------------------+----------------------------------------------------------+
//  | deactivated       |                                                          |
//  |                   | Backups will not begin until the policy is reactivated.  |
//  |                   | The assets associated with the policy will have their    |
//  |                   | compliance status set to "deactivated".                  |
//  |                   |                                                          |
//  +-------------------+----------------------------------------------------------+
//  
func (p *PolicyDefinitionsV1) ListPolicyDefinitions(
    filter *string, 
    embed *string)(
    *models.ListPoliciesResponse, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/policies/definitions"

    
    header := "application/api.clumio.policy-definitions=v1+json"
    var result *models.ListPoliciesResponse
    defaultString := "" 
    
    if filter == nil {
        filter = &defaultString
    }
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "filter": *filter,
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreatePolicyDefinition Creates a new policy. Creating a new policy involves configuring the backup seed settings, backup service level agreement (SLA), and backup window.
func (p *PolicyDefinitionsV1) CreatePolicyDefinition(
    body *models.CreatePolicyDefinitionV1Request)(
    *models.CreatePolicyResponse, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/policies/definitions"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.policy-definitions=v1+json"
    var result *models.CreatePolicyResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadPolicyDefinition Returns a representation of the specified policy.
func (p *PolicyDefinitionsV1) ReadPolicyDefinition(
    policyId string, 
    embed *string)(
    *models.ReadPolicyResponse, *apiutils.APIError) {

    pathURL := "/policies/definitions/{policy_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "policy_id": policyId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    
    header := "application/api.clumio.policy-definitions=v1+json"
    var result *models.ReadPolicyResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdatePolicyDefinition Updates an existing policy by modifying its backup seed setting, backup service level agreement (SLA), and backup window. If a policy is updated while a backup is in progress, the policy changes will take effect after the backup completes.
func (p *PolicyDefinitionsV1) UpdatePolicyDefinition(
    policyId string, 
    embed *string, 
    body *models.UpdatePolicyDefinitionV1Request)(
    *models.UpdatePolicyResponse, *apiutils.APIError) {

    pathURL := "/policies/definitions/{policy_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "policy_id": policyId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.policy-definitions=v1+json"
    var result *models.UpdatePolicyResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}


// DeletePolicyDefinition Deletes the specified policy.
func (p *PolicyDefinitionsV1) DeletePolicyDefinition(
    policyId string)(
    *models.DeletePolicyResponse, *apiutils.APIError) {

    pathURL := "/policies/definitions/{policy_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "policy_id": policyId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    
    header := "application/api.clumio.policy-definitions=v1+json"
    var result *models.DeletePolicyResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}
