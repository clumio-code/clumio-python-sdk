// Copyright (c) 2021 Clumio All Rights Reserved

package policydefinitions

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// PolicyDefinitionsV1Client represents a custom type interface
type PolicyDefinitionsV1Client interface {
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
    ListPolicyDefinitions(
        filter *string, 
        embed *string)(
        *models.ListPoliciesResponse,  *apiutils.APIError)
    
    // CreatePolicyDefinition Creates a new policy. Creating a new policy involves configuring the backup seed settings, backup service level agreement (SLA), and backup window.
    CreatePolicyDefinition(
        body *models.CreatePolicyDefinitionV1Request)(
        *models.CreatePolicyResponse,  *apiutils.APIError)
    
    // ReadPolicyDefinition Returns a representation of the specified policy.
    ReadPolicyDefinition(
        policyId string, 
        embed *string)(
        *models.ReadPolicyResponse,  *apiutils.APIError)
    
    // UpdatePolicyDefinition Updates an existing policy by modifying its backup seed setting, backup service level agreement (SLA), and backup window. If a policy is updated while a backup is in progress, the policy changes will take effect after the backup completes.
    UpdatePolicyDefinition(
        policyId string, 
        embed *string, 
        body *models.UpdatePolicyDefinitionV1Request)(
        *models.UpdatePolicyResponse,  *apiutils.APIError)
    
    // DeletePolicyDefinition Deletes the specified policy.
    DeletePolicyDefinition(
        policyId string)(
        *models.DeletePolicyResponse,  *apiutils.APIError)
    
}

// NewPolicyDefinitionsV1 returns PolicyDefinitionsV1Client
func NewPolicyDefinitionsV1(config config.Config) PolicyDefinitionsV1Client {
    client := new(PolicyDefinitionsV1)
    client.config = config
    return client
}
