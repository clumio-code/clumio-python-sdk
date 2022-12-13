// Copyright (c) 2021 Clumio All Rights Reserved

// Package models has the structs representing definitions
package models

// AWSConnection represents a custom type struct
type AWSConnection struct {
    // Embedded responses related to the resource.
    Embedded                 interface{}         `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                    *AWSConnectionLinks `json:"_links"`
    // The alias given to the account on AWS.
    AccountName              *string             `json:"account_name"`
    // The AWS-assigned ID of the account associated with the connection.
    AccountNativeId          *string             `json:"account_native_id"`
    // The AWS region associated with the connection. For example, `us-east-1`.
    AwsRegion                *string             `json:"aws_region"`
    // Clumio AWS AccountId
    ClumioAwsAccountId       *string             `json:"clumio_aws_account_id"`
    // Clumio AWS Region
    ClumioAwsRegion          *string             `json:"clumio_aws_region"`
    // The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud Discover products for this connection.
    // If this connection is deprecated to use unconsolidated configuration, then this field has a
    // value of `null`.
    Config                   *ConsolidatedConfig `json:"config"`
    // The status of the connection. Possible values include "connecting",
    // "connected", and "unlinked".
    ConnectionStatus         *string             `json:"connection_status"`
    // The timestamp of when the connection was created.
    CreatedTimestamp         *string             `json:"created_timestamp"`
    // An optional, user-provided description for this connection.
    Description              *string             `json:"description"`
    // The configuration of the Clumio Discover product for this connection.
    // If this connection is not configured for Clumio Discover, then this field has a
    // value of `null`.
    Discover                 *DiscoverConfig     `json:"discover"`
    // The Clumio-assigned ID of the connection.
    Id                       *string             `json:"id"`
    // K8S Namespace
    Namespace                *string             `json:"namespace"`
    // The Clumio-assigned ID of the organizational unit associated with the
    // AWS environment. If this parameter is not provided, then the value
    // defaults to the first organizational unit assigned to the requesting
    // user. For more information about organizational units, refer to the
    // Organizational-Units documentation.
    OrganizationalUnitId     *string             `json:"organizational_unit_id"`
    // The configuration of the Clumio Cloud Protect product for this connection.
    // If this connection is not configured for Clumio Cloud Protect, then this field has a
    // value of `null`.
    Protect                  *ProtectConfig      `json:"protect"`
    // The asset types enabled for protect. This is only populated if "protect"
    // is enabled. Valid values are any of ["EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3"].
    // EBS and RDS are mandatory datasources. (Deprecated)
    ProtectAssetTypesEnabled []*string           `json:"protect_asset_types_enabled"`
    // The services to be enabled for this configuration. Valid values are
    // ["discover"], ["discover", "protect"]. This is only set when the
    // registration is created, the enabled services are obtained directly from
    // the installed template after that. (Deprecated as all connections will have
    // both discover and protect enabled)
    ServicesEnabled          []*string           `json:"services_enabled"`
    // The Amazon Resource Name of the installed CloudFormation stack in this AWS account
    StackArn                 *string             `json:"stack_arn"`
    // The name given to the installed CloudFormation stack on AWS.
    StackName                *string             `json:"stack_name"`
    // The 36-character Clumio AWS integration ID token used to identify the
    // installation of the CloudFormation template on the account. This value
    // will be pasted into the ClumioToken field when creating the
    // CloudFormation stack.
    Token                    *string             `json:"token"`
}

// AWSConnectionLinks represents a custom type struct.
// URLs to pages related to the resource.
type AWSConnectionLinks struct {
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteConnectionAws    *HateoasLink     `json:"delete-connection-aws"`
    // A resource-specific HATEOAS link.
    ReadOrganizationalUnit *HateoasLink     `json:"read-organizational-unit"`
}

// AWSConnectionListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AWSConnectionListEmbedded struct {
    // TODO: Add struct field description
    Items []*AWSConnection `json:"items"`
}

// AWSConnectionListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AWSConnectionListLinks struct {
    // The HATEOAS link to the first page of results.
    First               *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next                *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self                *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateAwsConnection *HateoasLink      `json:"create-aws-connection"`
}

// AWSEnvironment represents a custom type struct
type AWSEnvironment struct {
    // Embedded responses related to the resource.
    Embedded             *AWSEnvironmentEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *AWSEnvironmentLinks    `json:"_links"`
    // The name given to the account.
    AccountName          *string                 `json:"account_name"`
    // The AWS-assigned ID of the account associated with the environment.
    AccountNativeId      *string                 `json:"account_native_id"`
    // The valid AWS availability zones for the environment. For example, `us_west-2a`.
    AwsAz                []*string               `json:"aws_az"`
    // The AWS region associated with the environment. For example, `us-west-2`.
    AwsRegion            *string                 `json:"aws_region"`
    // The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud Discover products for this connection.
    // If this connection is deprecated to use unconsolidated configuration, then this field has a
    // value of `null`.
    Config               *ConsolidatedConfig     `json:"config"`
    // The Clumio-assigned ID of the connection associated with the environment.
    ConnectionId         *string                 `json:"connection_id"`
    // The status of the connection to the environment, which is mediated by a CloudFormation stack.
    ConnectionStatus     *string                 `json:"connection_status"`
    // The user-provided account description.
    Description          *string                 `json:"description"`
    // The Clumio-assigned ID of the environment.
    Id                   *string                 `json:"id"`
    // The Clumio-assigned ID of the organizational unit associated with the environment.
    OrganizationalUnitId *string                 `json:"organizational_unit_id"`
    // The AWS services enabled for this environment. Possible values include "ebs", "rds" and "dynamodb".
    ServicesEnabled      []*string               `json:"services_enabled"`
    // The Clumio CloudFormation template version used to deploy the CloudFormation stack.
    TemplateVersion      *int64                  `json:"template_version"`
}

// AWSEnvironmentEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AWSEnvironmentEmbedded struct {
    // TODO: Add struct field description
    ReadAwsEnvironmentEbsVolumesComplianceStats interface{} `json:"read-aws-environment-ebs-volumes-compliance-stats"`
}

// AWSEnvironmentLinks represents a custom type struct.
// URLs to pages related to the resource.
type AWSEnvironmentLinks struct {
    // The HATEOAS link to this resource.
    Self                                        *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ProtectEntities                             *HateoasLink     `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadAwsEnvironmentEbsVolumesComplianceStats *HateoasLink     `json:"read-aws-environment-ebs-volumes-compliance-stats"`
    // A resource-specific HATEOAS link.
    ReadOrganizationalUnit                      *HateoasLink     `json:"read-organizational-unit"`
}

// AWSEnvironmentListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AWSEnvironmentListEmbedded struct {
    // TODO: Add struct field description
    Items []*AWSEnvironment `json:"items"`
}

// AWSEnvironmentListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AWSEnvironmentListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// Alert represents a custom type struct
type Alert struct {
    // Embedded responses related to the resource.
    Embedded            *AlertEmbedded          `json:"_embedded"`
    // URLs to pages related to the resource.
    Links               *AlertLinks             `json:"_links"`
    // The issue that generated the alert. Each cause belongs to an alert type.
    Cause               *string                 `json:"cause"`
    // The timestamp of when the alert was cleared, either automatically by Clumio or manually by a Clumio user.
    // Represented in RFC-3339 format. If this alert has not been cleared, then this field has a value of `null`.
    ClearedTimestamp    *string                 `json:"cleared_timestamp"`
    // The Clumio-assigned ID of the consolidated alert associated with this individual alert. Alerts are consolidated based on matching parent entity, alert type, and alert cause.
    ConsolidatedAlertId *string                 `json:"consolidated_alert_id"`
    // Additional information about the alert.
    Details             *IndividualAlertDetails `json:"details"`
    // The Clumio-assigned ID of the individual alert.
    Id                  *string                 `json:"id"`
    // A record of user-provided information about the alert.
    Notes               *string                 `json:"notes"`
    // The parent object of the primary entity associated with or affected by the alert. For example, "aws_environment" is the parent entity of primary entity "aws_ebs_volume".
    ParentEntity        *AlertParentEntity      `json:"parent_entity"`
    // The primary object associated with or affected by the alert. Examples of primary entities include "aws_connection", "aws_ebs_volume" and "vmware_vm".
    PrimaryEntity       *AlertPrimaryEntity     `json:"primary_entity"`
    // The number of times the alert has recurred for this primary entity.
    RaisedCount         *uint64                 `json:"raised_count"`
    // The timestamp of when the alert was raised. Represented in RFC-3339 format.
    RaisedTimestamp     *string                 `json:"raised_timestamp"`
    // The alert severity level. Values include "error" and "warning".
    Severity            *string                 `json:"severity"`
    // The individual alert status. An individual alert that is in "active" status is one that is still open and has yet to be addressed.
    // An individual alert that is in "cleared" status is one that has been cleared, either automatically by Clumio or manually by a Clumio user.
    Status              *string                 `json:"status"`
    // TODO: Add struct field description
    Tags                []*RestEntity           `json:"tags"`
    // The general alert category. Some alert types may be associated with multiple causes.
    // Refer to the Alert Type table for a complete list of alert types.
    ClumioType          *string                 `json:"type"`
    // The timestamp of when the alert was last updated. Represented in RFC-3339 format.
    // The alert is updated whenever there is a new occurrence of the same alert within the same entity.
    UpdatedTimestamp    *string                 `json:"updated_timestamp"`
}

// AlertEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AlertEmbedded struct {
    // Embeds the associated consolidated alert in the response.
    ReadConsolidatedAlert interface{} `json:"read-consolidated-alert"`
}

// AlertLinks represents a custom type struct.
// URLs to pages related to the resource.
type AlertLinks struct {
    // The HATEOAS link to this resource.
    Self                  *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ReadConsolidatedAlert *HateoasLink     `json:"read-consolidated-alert"`
    // A resource-specific HATEOAS link.
    UpdateIndividualAlert *HateoasLink     `json:"update-individual-alert"`
}

// AlertListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AlertListEmbedded struct {
    // TODO: Add struct field description
    Items []*Alert `json:"items"`
}

// AlertListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AlertListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// AlertParentEntity represents a custom type struct.
// The parent object of the primary entity associated with or affected by the alert. For example, "aws_environment" is the parent entity of primary entity "aws_ebs_volume".
type AlertParentEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// AlertPrimaryEntity represents a custom type struct.
// The primary object associated with or affected by the alert. Examples of primary entities include "aws_connection", "aws_ebs_volume" and "vmware_vm".
type AlertPrimaryEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// AncestorRefModel represents a custom type struct
type AncestorRefModel struct {
    // A VMware-assigned ID for this ancestor.
    Id         *string `json:"id"`
    // Determines whether this ancestor is a hidden root object. If `true`, this ancestor is a hidden root object.
    IsRoot     *bool   `json:"is_root"`
    // The name of the ancestor.
    Name       *string `json:"name"`
    // The type of vCenter object that this ancestor represents. For example, a data center can be an ancestor of a data center folder.
    ClumioType *string `json:"type"`
}

// AssignPolicyAction represents a custom type struct.
// Apply a policy to assets.
type AssignPolicyAction struct {
    // The policy to be applied to the assets.
    PolicyId *string `json:"policy_id"`
}

// AssignmentEntity represents a custom type struct
type AssignmentEntity struct {
    // A system-generated ID assigned of an entity being assigned or unassigned to a policy.
    Id         *string `json:"id"`
    // 
    // The type of an entity being associated or disassociated with a policy.
    // Valid primary entity types include the following:
    // 
    // +---------------------+---------------------+
    // | Primary Entity Type |       Details       |
    // +=====================+=====================+
    // | aws_ebs_volume      | AWS EBS volume.     |
    // +---------------------+---------------------+
    // | aws_ec2_instance    | AWS EC2 instance.   |
    // +---------------------+---------------------+
    // | aws_rds_cluster     | AWS RDS cluster.    |
    // +---------------------+---------------------+
    // | aws_rds_instance    | AWS RDS instance.   |
    // +---------------------+---------------------+
    // | aws_dynamodb_table  | AWS DynamoDB table. |
    // +---------------------+---------------------+
    // | protection_group    | Protection group.   |
    // +---------------------+---------------------+
    // 
    ClumioType *string `json:"type"`
}

// AssignmentInputModel represents a custom type struct.
// The portion of the policy assignment used for updates/creations
type AssignmentInputModel struct {
    // The action to be executed by this request.
    // Possible values include "assign" and "unassign".
    Action   *string           `json:"action"`
    // TODO: Add struct field description
    Entity   *AssignmentEntity `json:"entity"`
    // The Clumio-assigned ID of the policy to be applied to the requested entities.
    // If `action: assign`, then this parameter is required.
    // Otherwise, it must not be provided.
    PolicyId *string           `json:"policy_id"`
}

// AuditTrails represents a custom type struct
type AuditTrails struct {
    // The action performed by the user.
    // 
    // +------------------+-----------------------------------------------------------+
    // |      Action      |                          Details                          |
    // +==================+===========================================================+
    // | create           | Creating or adding new entities like new policy,          |
    // |                  | configuration, user, etc                                  |
    // +------------------+-----------------------------------------------------------+
    // | update           | Updating an existing entity like policy, settings,        |
    // |                  | passwords, etc                                            |
    // +------------------+-----------------------------------------------------------+
    // | delete           | Delete an existing entity like policy, settings, users,   |
    // |                  | etc                                                       |
    // +------------------+-----------------------------------------------------------+
    // | enable           | Enabling a feature like single sign on or multi factor    |
    // |                  | authentication settings                                   |
    // +------------------+-----------------------------------------------------------+
    // | disable          | Disabling features like single sign on or multi factor    |
    // |                  | authentication settings                                   |
    // +------------------+-----------------------------------------------------------+
    // | browse           | Browsing through entities in the system like mailboxes or |
    // |                  | backups, etc                                              |
    // +------------------+-----------------------------------------------------------+
    // | search           | Searching through entities in the system like mailboxes   |
    // |                  | or backups, etc                                           |
    // +------------------+-----------------------------------------------------------+
    // | login            | User logs in or tries to login                            |
    // +------------------+-----------------------------------------------------------+
    // | logout           | User explicitly logged out.                               |
    // +------------------+-----------------------------------------------------------+
    // | register         | When new registrations happen like new                    |
    // |                  | datasource registration or user registering for MFA       |
    // +------------------+-----------------------------------------------------------+
    // | unregister       | When unregistering like unregistering                     |
    // |                  | datasource or user unregistering MFA                      |
    // +------------------+-----------------------------------------------------------+
    // | apply            | Apply policy to protect entities, tags, etc               |
    // +------------------+-----------------------------------------------------------+
    // | remove           | Remove protection for entities, tags, etc                 |
    // +------------------+-----------------------------------------------------------+
    // | invite           | Inviting a user                                           |
    // +------------------+-----------------------------------------------------------+
    // | suspend          | Suspend an existing user                                  |
    // +------------------+-----------------------------------------------------------+
    // | full_restore     | Full restore of the VM, volume, mailbox, database or      |
    // |                  | other entities                                            |
    // +------------------+-----------------------------------------------------------+
    // | granular_restore | Restoring individual files, mails or records              |
    // +------------------+-----------------------------------------------------------+
    // 
    Action          *string             `json:"action"`
    // The category of the auditable action performed by the user.
    // 
    // +-------------------------+----------------------------------------------------+
    // |        Category         |                      Details                       |
    // +=========================+====================================================+
    // | authentication          | Activities related to Authentication               |
    // +-------------------------+----------------------------------------------------+
    // | data_source             | Data source changes                                |
    // +-------------------------+----------------------------------------------------+
    // | policy                  | Policy related actions                             |
    // +-------------------------+----------------------------------------------------+
    // | protection              | Applying and removing protection                   |
    // +-------------------------+----------------------------------------------------+
    // | restore                 | Restore related operations                         |
    // +-------------------------+----------------------------------------------------+
    // | tasks                   | Tasks                                              |
    // +-------------------------+----------------------------------------------------+
    // | backup                  | Backup related operations                          |
    // +-------------------------+----------------------------------------------------+
    // | users                   | User related operations                            |
    // +-------------------------+----------------------------------------------------+
    // | api_tokens              | API Token related operations like creating,        |
    // |                         | revoking or deleting tokens                        |
    // +-------------------------+----------------------------------------------------+
    // | kms_config              | Key Management Service(KMS) related operations     |
    // +-------------------------+----------------------------------------------------+
    // | sso                     | Single sign-on (SSO) related operations            |
    // +-------------------------+----------------------------------------------------+
    // | mfa                     | Multi Factor Authentication(MFA) related           |
    // |                         | operations                                         |
    // +-------------------------+----------------------------------------------------+
    // | reports                 | Reports related operations                         |
    // +-------------------------+----------------------------------------------------+
    // | alerts                  | Alerts related operations                          |
    // +-------------------------+----------------------------------------------------+
    // | cloud_connector         | Cloud connector related operations                 |
    // +-------------------------+----------------------------------------------------+
    // | cloudformation_template | Cloud Formation Template related operations        |
    // +-------------------------+----------------------------------------------------+
    // | bandwidth_config        | Bandwidth configuration related changes            |
    // +-------------------------+----------------------------------------------------+
    // | partner_ecosystem       | Changes to partner ecosystem                       |
    // +-------------------------+----------------------------------------------------+
    // | ecosystem_changes       | Changes in the ecosystem like adding or remvoings  |
    // |                         | VMs                                                |
    // +-------------------------+----------------------------------------------------+
    // 
    Category        *string             `json:"category"`
    // Additional details about the activity provided in JSON format.
    Details         *string             `json:"details"`
    // The Clumio-assigned ID of the audit event.
    Id              *string             `json:"id"`
    // The interface used to make the request i.e. 'UI','API'
    ClumioInterface *string             `json:"interface"`
    // The IP address from which the activity was requested.
    IpAddress       *string             `json:"ip_address"`
    // The parent object of the primary entity associated with or affected by the audit.
    // If the primary entity is not a vmware entity, this field will have a value of null
    // For example, "vmware_vcenter" is the parent entity of primary entity "vmware_vm".
    ParentEntity    *AuditParentEntity  `json:"parent_entity"`
    // The primary object associated with the audit event. Examples of primary entities
    // include "aws_connection", "aws_ebs_volume" and "vmware_vm". In some cases like
    // global settings, the primary entity may be null.
    PrimaryEntity   *AuditPrimaryEntity `json:"primary_entity"`
    // The status of the performed action. 'success', 'failure', 'partial_success'
    Status          *string             `json:"status"`
    // The Timestamp of when the activity began. Represented in RFC-3339 format.
    Timestamp       *string             `json:"timestamp"`
    // The email address of the logged in user making the request.
    UserEmail       *string             `json:"user_email"`
}

// AuditParentEntity represents a custom type struct.
// The parent object of the primary entity associated with or affected by the audit.
// If the primary entity is not a vmware entity, this field will have a value of null
// For example, "vmware_vcenter" is the parent entity of primary entity "vmware_vm".
type AuditParentEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// AuditPrimaryEntity represents a custom type struct.
// The primary object associated with the audit event. Examples of primary entities
// include "aws_connection", "aws_ebs_volume" and "vmware_vm". In some cases like
// global settings, the primary entity may be null.
type AuditPrimaryEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// AuditTrailListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AuditTrailListEmbedded struct {
    // TODO: Add struct field description
    Items []*AuditTrails `json:"items"`
}

// AuditTrailListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AuditTrailListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// AutoUserProvisioningRuleEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AutoUserProvisioningRuleEmbedded struct {
    // Embeds the associated organizational units for the OU UUIDs in the response
    // if requested using the `embed` query parameter.
    ReadOrganizationalUnit interface{} `json:"read-organizational-unit"`
    // Embeds the associated role for the role UUID in the response if requested using the `embed` query parameter.
    ReadRole               interface{} `json:"read-role"`
}

// AutoUserProvisioningRuleLinks represents a custom type struct.
// URLs to pages related to the resource.
type AutoUserProvisioningRuleLinks struct {
    // The HATEOAS link to this resource.
    Self                           *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteAutoUserProvisioningRule *HateoasLink     `json:"delete-auto-user-provisioning-rule"`
    // A resource-specific HATEOAS link.
    UpdateAutoUserProvisioningRule *HateoasLink     `json:"update-auto-user-provisioning-rule"`
}

// AutoUserProvisioningRuleListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AutoUserProvisioningRuleListEmbedded struct {
    // AutoUserProvisioningRuleWithETag to support etag string to be calculated
    Items []*AutoUserProvisioningRuleWithETag `json:"items"`
}

// AutoUserProvisioningRuleListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AutoUserProvisioningRuleListLinks struct {
    // The HATEOAS link to the first page of results.
    First                          *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next                           *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self                           *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateAutoUserProvisioningRule *HateoasLink      `json:"create-auto-user-provisioning-rule"`
}

// AutoUserProvisioningRuleWithETag represents a custom type struct.
// AutoUserProvisioningRuleWithETag to support etag string to be calculated
type AutoUserProvisioningRuleWithETag struct {
    // Embedded responses related to the resource.
    Embedded  *AutoUserProvisioningRuleEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links     *AutoUserProvisioningRuleLinks    `json:"_links"`
    // The following table describes the possible conditions for a rule.
    // 
    // +--------------------------+-------------------------+-------------------------+
    // |     Group Selection      |     Rule Condition      |       Description       |
    // +==========================+=========================+=========================+
    // | This group               |                         | User must belong to the |
    // |                          |                         | specified group.        |
    // |                          | {"user.groups":{"$eq":" |                         |
    // |                          | Admin"}}                |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // | ANY of these groups      |                         | User must belong to at  |
    // |                          |                         | least one of the        |
    // |                          | {"user.groups":{"$in":[ | specified groups.       |
    // |                          | "Admin", "Eng",         |                         |
    // |                          | "Sales"]}}              |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // | ALL of these groups      |                         | User must belong to all |
    // |                          |                         | the specified groups.   |
    // |                          | {"user.groups":{"$all": |                         |
    // |                          | ["Admin", "Eng",        |                         |
    // |                          | "Sales"]}}              |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // | Group CONTAINS this      |                         | User's group must       |
    // | keyword                  |                         | contain the specified   |
    // |                          | {"user.groups":{"$conta | keyword.                |
    // |                          | ins":{"$in":["Admin"]}} |                         |
    // |                          | }                       |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // | Group CONTAINS ANY of    |                         | User's group must       |
    // | these keywords           |                         | contain at least one of |
    // |                          | {"user.groups":{"$conta | the specified keywords. |
    // |                          | ins":{"$in":["Admin",   |                         |
    // |                          | "Eng", "Sales"]}}}      |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // | Group CONTAINS ALL of    |                         | User's group must       |
    // | these keywords           |                         | contain all the         |
    // |                          | {"user.groups":{"$conta | specified keywords.     |
    // |                          | ins":{"$all":["Admin",  |                         |
    // |                          | "Eng", "Sales"]}}}      |                         |
    // |                          |                         |                         |
    // |                          |                         |                         |
    // +--------------------------+-------------------------+-------------------------+
    // 
    Condition *string                           `json:"condition"`
    // Unique name assigned to the rule.
    Name      *string                           `json:"name"`
    // Specifies the role and the organizational units to be assigned to the user subject to the rule criteria.
    Provision *RuleProvision                    `json:"provision"`
    // The Clumio-assigned ID of the rule.
    RuleId    *string                           `json:"rule_id"`
}

// AutoUserProvisioningSettingLinks represents a custom type struct.
// URLs to pages related to the resource.
type AutoUserProvisioningSettingLinks struct {
    // The HATEOAS link to this resource.
    Self                              *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    UpdateAutoUserProvisioningSetting *HateoasLink     `json:"update-auto-user-provisioning-setting"`
}

// AwsDsGroupingCriteria represents a custom type struct.
// The entity type used to group organizational units for AWS resources.
type AwsDsGroupingCriteria struct {
    // Determines whether or not this data group is editable. If false, then an
    // organizational unit uses this data group.
    // To edit this data group, all organizational units using it must be deleted.
    IsEditable *bool   `json:"is_editable"`
    // 
    // +-----------------+-------------------------+
    // |   Entity Type   |         Details         |
    // +=================+=========================+
    // | aws_environment | AWS account and region. |
    // +-----------------+-------------------------+
    // 
    ClumioType *string `json:"type"`
}

// AwsTag represents a custom type struct
type AwsTag struct {
    // Embedded responses related to the resource.
    Embedded             *AwsTagEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *AwsTagLinks    `json:"_links"`
    // The Clumio-assigned ID of the AWS tag.
    Id                   *string         `json:"id"`
    // The AWS-assigned tag key.
    Key                  *string         `json:"key"`
    // The Clumio-assigned ID of the AWS key.
    KeyId                *string         `json:"key_id"`
    // The Clumio-assigned ID of the organizational unit associated with the tag.
    OrganizationalUnitId *string         `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo       *ProtectionInfo `json:"protection_info"`
    // The protection status of the EBS volume. Possible values include "protected" and "unprotected".
    ProtectionStatus     *string         `json:"protection_status"`
    // The AWS-assigned tag value.
    Value                *string         `json:"value"`
}

// AwsTagCommonModel represents a custom type struct.
// A tag created through AWS Console which can be applied to EBS volumes.
type AwsTagCommonModel struct {
    // The AWS-assigned tag key.
    Key   *string `json:"key"`
    // The AWS-assigned tag value.
    Value *string `json:"value"`
}

// AwsTagEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AwsTagEmbedded struct {
    // TODO: Add struct field description
    ReadAwsEnvironmentTagEbsVolumesComplianceStats interface{} `json:"read-aws-environment-tag-ebs-volumes-compliance-stats"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition                           interface{} `json:"read-policy-definition"`
}

// AwsTagLinks represents a custom type struct.
// URLs to pages related to the resource.
type AwsTagLinks struct {
    // The HATEOAS link to this resource.
    Self                                           *HateoasSelfLink                 `json:"_self"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                                *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadAwsEnvironmentTagEbsVolumesComplianceStats *HateoasLink                     `json:"read-aws-environment-tag-ebs-volumes-compliance-stats"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition                           *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                              *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
}

// AwsTagListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type AwsTagListEmbedded struct {
    // TODO: Add struct field description
    Items []*AwsTag `json:"items"`
}

// AwsTagListLinks represents a custom type struct.
// URLs to pages related to the resource.
type AwsTagListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// AwsTagModel represents a custom type struct.
// A tag created through AWS console which can be applied to EBS volumes.
type AwsTagModel struct {
    // The Clumio-assigned ID of the AWS tag.
    Id    *string `json:"id"`
    // The AWS-assigned tag key.
    Key   *string `json:"key"`
    // The Clumio-assigned ID of the AWS key.
    KeyId *string `json:"key_id"`
    // The AWS-assigned tag value.
    Value *string `json:"value"`
}

// BackupSLA represents a custom type struct.
// backup_sla captures the SLA parameters
// backup_sla captures the SLA parameters
type BackupSLA struct {
    // The retention time for this SLA. For example, to retain the backup for 1 month, set `unit="months"` and `value=1`.
    RetentionDuration *RetentionBackupSLAParam `json:"retention_duration"`
    // The minimum frequency between backups for this SLA. Also known as the recovery point objective (RPO) interval.
    // For example, to configure the minimum frequency between backups to be every 2 days, set `unit="days"` and `value=2`.
    // To configure the SLA for on-demand backups, set `unit="on_demand"` and leave the `value` field empty.
    RpoFrequency      *RPOBackupSLAParam       `json:"rpo_frequency"`
}

// BackupWindow represents a custom type struct.
// The start and end times of the customized backup window. Use of `backup_window` is deprecated, use `backup_window_tz` instead.
type BackupWindow struct {
    // The time when the backup window closes. Specify the end time in the format `hh:mm`, where `hh` represents the hour of the day and `mm` represents the minute of the day, based on a 24 hour clock. Leave empty if you do not want to specify an end time. If the backup window closes while a backup is in progress, the entire backup process is aborted. Clumio will perform the next backup when the backup window re-opens.
    EndTime   *string `json:"end_time"`
    // The time when the backup window opens. Specify the start time in the format `hh:mm`, where `hh` represents the hour of the day and `mm` represents the minute of the day based on the 24 hour clock.
    StartTime *string `json:"start_time"`
}

// Bucket represents a custom type struct
type Bucket struct {
    // Embedded responses related to the resource.
    Embedded                 interface{}                                   `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                    *BucketLinks                                  `json:"_links"`
    // The AWS-assigned ID of the account associated with the S3 bucket.
    AccountNativeId          *string                                       `json:"account_native_id"`
    // The AWS region associated with the S3 bucket.
    AwsRegion                *string                                       `json:"aws_region"`
    // The total size breakdown of S3 buckets in bytes per storage class. This parameter aggregates relevant fields from cloudwatch_metrics > size_bytes_per_storage_class
    BucketSizeBytesBreakdown *S3BucketsInventorySummaryBucketSizeBreakdown `json:"bucket_size_bytes_breakdown"`
    // The Cloudwatch metrics of the bucket.
    CloudwatchMetrics        *S3CloudwatchMetrics                          `json:"cloudwatch_metrics"`
    // The timestamp of when the bucket was created. Represented in RFC-3339 format.
    CreationTimestamp        *string                                       `json:"creation_timestamp"`
    // The AWS encryption output of the bucket.
    EncryptionSetting        *S3EncryptionOutput                           `json:"encryption_setting"`
    // The Clumio-assigned ID of the AWS environment associated with the S3 bucket.
    EnvironmentId            *string                                       `json:"environment_id"`
    // The EventBridge enablement state for the S3 bucket.
    EventBridgeEnabled       *bool                                         `json:"event_bridge_enabled"`
    // The Clumio-assigned ID of the bucket.
    Id                       *string                                       `json:"id"`
    // The Encryption enablement state for the S3 bucket.
    IsEncryptionEnabled      *bool                                         `json:"is_encryption_enabled"`
    // The Replication enablement state for the S3 bucket.
    IsReplicationEnabled     *bool                                         `json:"is_replication_enabled"`
    // The Versioning enablement state for the S3 bucket.
    IsVersioningEnabled      *bool                                         `json:"is_versioning_enabled"`
    // The AWS-assigned name of the bucket.
    Name                     *string                                       `json:"name"`
    // Number of objects in bucket.
    ObjectCount              *int64                                        `json:"object_count"`
    // The Clumio-assigned ID of the organizational unit associated with the S3 bucket.
    OrganizationalUnitId     *string                                       `json:"organizational_unit_id"`
    // Protection group count reflects how many protection groups are linked to this
    // bucket.
    ProtectionGroupCount     *int64                                        `json:"protection_group_count"`
    // The AWS replication output of the bucket.
    ReplicationSetting       *S3ReplicationOutput                          `json:"replication_setting"`
    // Size of bucket in bytes.
    SizeBytes                *int64                                        `json:"size_bytes"`
    // A tag created through AWS console which can be applied to EBS volumes.
    Tags                     []*AwsTagModel                                `json:"tags"`
    // The AWS versioning output of the bucket.
    VersioningSetting        *S3VersioningOutput                           `json:"versioning_setting"`
}

// BucketLinks represents a custom type struct.
// URLs to pages related to the resource.
type BucketLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// BucketListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type BucketListEmbedded struct {
    // TODO: Add struct field description
    Items []*Bucket `json:"items"`
}

// BucketListLinks represents a custom type struct.
// URLs to pages related to the resource.
type BucketListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// CloudConnectorCountByStatus represents a custom type struct.
// The number of cloud connectors in this subgroup, aggregated by their status.
type CloudConnectorCountByStatus struct {
    // The number of degraded cloud connectors in this subgroup.
    Degraded *int64 `json:"degraded"`
    // The number of healthy cloud connectors in this subgroup.
    Healthy  *int64 `json:"healthy"`
}

// ComplianceStatsDeprecated represents a custom type struct.
// ComplianceStatsDeprecated denotes compliance metrics for all entities associated with a given type
type ComplianceStatsDeprecated struct {
    // Compliant count.
    Compliant      *uint32 `json:"COMPLIANT"`
    // Deactivated count.
    Deactivated    *uint32 `json:"DEACTIVATED"`
    // Non-Compliant count.
    NonCompliant   *uint32 `json:"NON_COMPLIANT"`
    // Seeding count.
    Seeding        *uint32 `json:"SEEDING"`
    // Wait-for-seeding count.
    WaitForSeeding *uint32 `json:"WAIT_FOR_SEEDING"`
}

// ComputeResourceEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ComputeResourceEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition                            interface{} `json:"read-policy-definition"`
    // Embeds the compliance statistics of VMs into each vCenter resource in the response, if requested using the `_embed` query parameter.
    ReadVmwareVcenterComputeResourceComplianceStats interface{} `json:"read-vmware-vcenter-compute-resource-compliance-stats"`
    // TODO: Add struct field description
    ReadVmwareVcenterComputeResourceConnectionStats interface{} `json:"read-vmware-vcenter-compute-resource-connection-stats"`
}

// ComputeResourceIDModel represents a custom type struct
type ComputeResourceIDModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    Id *string `json:"id"`
}

// ComputeResourceLinks represents a custom type struct.
// URLs to pages related to the resource.
type ComputeResourceLinks struct {
    // The HATEOAS link to this resource.
    Self                                            *HateoasSelfLink                             `json:"_self"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                                 *ProtectEntitiesHateoasLink                  `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition                            *ReadPolicyDefinitionHateoasLink             `json:"read-policy-definition"`
    // A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
    ReadVmwareVcenterComputeResourceComplianceStats *ReadVCenterObjectProtectionStatsHateoasLink `json:"read-vmware-vcenter-compute-resource-compliance-stats"`
    // A resource-specific HATEOAS link.
    ReadVmwareVcenterComputeResourceConnectionStats *HateoasLink                                 `json:"read-vmware-vcenter-compute-resource-connection-stats"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                               *UnprotectEntitiesHateoasLink                `json:"unprotect-entities"`
}

// ConnectionRegion represents a custom type struct
type ConnectionRegion struct {
    // The Clumio-assigned ID of the connection.
    Id                *string `json:"id"`
    // Boolean that notes which regions can be designated as targets
    IsDataPlaneRegion *bool   `json:"is_data_plane_region"`
    // Name is a user friendly name of the AWS region.
    Name              *string `json:"name"`
}

// ConnectionRegionListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ConnectionRegionListEmbedded struct {
    // TODO: Add struct field description
    Items []*ConnectionRegion `json:"items"`
}

// ConnectionRegionListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ConnectionRegionListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ConsolidatedAlert represents a custom type struct
type ConsolidatedAlert struct {
    // URLs to pages related to the resource.
    Links              *ConsolidatedAlertLinks        `json:"_links"`
    // The number of currently active individual alerts associated with the consolidated alert.
    ActiveEntityCount  *int64                         `json:"active_entity_count"`
    // The issue that generated the alert. Each alert cause is associated with an alert type.
    Cause              *string                        `json:"cause"`
    // The number of cleared individual alerts associated with the consolidated alert.
    ClearedEntityCount *int64                         `json:"cleared_entity_count"`
    // The timestamp of when the consolidated alert was cleared, if ever. Represented in RFC-3339 format. If this alert has not been cleared, this field will have a value of `null`.
    // A consolidated alert goes into "cleared" status when all of its associated individual alerts are in "cleared" status or when a Clumio user manually clears it.
    ClearedTimestamp   *string                        `json:"cleared_timestamp"`
    // Additional information about the consolidated alert.
    Details            *ConsolidatedAlertDetails      `json:"details"`
    // The Clumio-assigned ID of the consolidated alert.
    Id                 *string                        `json:"id"`
    // A record of user-provided information about the alert.
    Notes              *string                        `json:"notes"`
    // The entity associated with or affected by the alert.
    ParentEntity       *ConsolidatedAlertParentEntity `json:"parent_entity"`
    // The timestamp of when the consolidated alert was initially raised. Represented in RFC-3339 format.
    RaisedTimestamp    *string                        `json:"raised_timestamp"`
    // The alert severity level. Values include "error" and "warning".
    Severity           *string                        `json:"severity"`
    // The consolidated alert status. A consolidated alert is in "active" status if one or more of its associated individual alerts is in "active" status.
    // A consolidated alert goes into "cleared" status when all of its associated individual alerts are in "cleared" status or when a Clumio user manually clears it.
    Status             *string                        `json:"status"`
    // The general alert category. An alert type may be associated with multiple alert causes. Examples of alert types include "tag_conflict" and "policy_violated".
    // Refer to the Alert Type table for a complete list of alert types.
    ClumioType         *string                        `json:"type"`
    // The timestamp of when the consolidated alert was last updated. Represented in RFC-3339 format.
    // Raising a new individual alert will update its associated consolidated alert.
    UpdatedTimestamp   *string                        `json:"updated_timestamp"`
}

// ConsolidatedAlertDetails represents a custom type struct.
// Additional information about the consolidated alert.
type ConsolidatedAlertDetails struct {
    // A brief description of the condition that caused the alert. Examples include "Size Limit Exceeded" and "Insufficient Cloud Connector Capacity".
    Cause      *string `json:"cause"`
    // The general alert category. Examples include "Policy Violated" and "Restore Failed".
    ClumioType *string `json:"type"`
}

// ConsolidatedAlertLinks represents a custom type struct.
// URLs to pages related to the resource.
type ConsolidatedAlertLinks struct {
    // The HATEOAS link to this resource.
    Self                    *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    UpdateConsolidatedAlert *HateoasLink     `json:"update-consolidated-alert"`
}

// ConsolidatedAlertListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ConsolidatedAlertListEmbedded struct {
    // TODO: Add struct field description
    Items []*ConsolidatedAlert `json:"items"`
}

// ConsolidatedAlertListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ConsolidatedAlertListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ConsolidatedAlertParentEntity represents a custom type struct.
// The entity associated with or affected by the alert.
type ConsolidatedAlertParentEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// ConsolidatedConfig represents a custom type struct.
// The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud Discover products for this connection.
// If this connection is deprecated to use unconsolidated configuration, then this field has a
// value of `null`.
type ConsolidatedConfig struct {
    // The asset types supported on the current version of the feature
    AssetTypesEnabled        []*string     `json:"asset_types_enabled"`
    // TODO: Add struct field description
    Ebs                      *EbsAssetInfo `json:"ebs"`
    // The current version of the feature.
    InstalledTemplateVersion *string       `json:"installed_template_version"`
    // TODO: Add struct field description
    Rds                      *RdsAssetInfo `json:"rds"`
}

// CreateRdsDatabaseRestoreResponseLinks represents a custom type struct.
// URLs to pages related to the resource.
type CreateRdsDatabaseRestoreResponseLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// CreateRestoreRecordResponseLinks represents a custom type struct.
// URLs to pages related to the resource.
type CreateRestoreRecordResponseLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// DataAccessObject represents a custom type struct.
// Specifies information about the data-access method for accessing the restored
// file.
type DataAccessObject struct {
    // The details used to access the restored file if it was shared by direct download. If
    // the restored file was shared by email (and not by direct download), then this field
    // has a value of `null`.
    DirectDownload *DirectDownloadDataAccessObject `json:"direct_download"`
    // The details used to access the restored file, if it was shared by email. If the
    // restored file was shared by direct download (and not email), then this field has a
    // value of `null`.
    Email          *EmailDownloadDataAccessObject  `json:"email"`
}

// DatabaseLinks represents a custom type struct.
// URLs to pages related to the resource.
type DatabaseLinks struct {
    // The HATEOAS link to this resource.
    Self                      *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateBackupMssqlDatabase *HateoasLink     `json:"create-backup-mssql-database"`
    // A resource-specific HATEOAS link.
    ListBackupMssqlDatabases  *HateoasLink     `json:"list-backup-mssql-databases"`
    // A resource-specific HATEOAS link.
    ReadManagementGroup       *HateoasLink     `json:"read-management-group"`
    // A resource-specific HATEOAS link.
    ReadManagementSubgroup    *HateoasLink     `json:"read-management-subgroup"`
}

// DatacenterEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type DatacenterEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition                       interface{} `json:"read-policy-definition"`
    // Embeds the compliance statistics of VMs into each vCenter resource in the response, if requested using the `_embed` query parameter.
    ReadVmwareVcenterDatacenterComplianceStats interface{} `json:"read-vmware-vcenter-datacenter-compliance-stats"`
}

// DatacenterLinks represents a custom type struct.
// URLs to pages related to the resource.
type DatacenterLinks struct {
    // The HATEOAS link to this resource.
    Self                                       *HateoasSelfLink                             `json:"_self"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                            *ProtectEntitiesHateoasLink                  `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition                       *ReadPolicyDefinitionHateoasLink             `json:"read-policy-definition"`
    // A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
    ReadVmwareVcenterDatacenterComplianceStats *ReadVCenterObjectProtectionStatsHateoasLink `json:"read-vmware-vcenter-datacenter-compliance-stats"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                          *UnprotectEntitiesHateoasLink                `json:"unprotect-entities"`
}

// DatacenterListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type DatacenterListEmbedded struct {
    // DatacenterWithETag to support etag string to be calculated
    Items []*DatacenterWithETag `json:"items"`
}

// DatacenterListLinks represents a custom type struct.
// URLs to pages related to the resource.
type DatacenterListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// DatacenterWithETag represents a custom type struct.
// DatacenterWithETag to support etag string to be calculated
type DatacenterWithETag struct {
    // Embedded responses related to the resource.
    Embedded                  *DatacenterEmbedded                     `json:"_embedded"`
    // The ETag value.
    Etag                      *string                                 `json:"_etag"`
    // URLs to pages related to the resource.
    Links                     *DatacenterLinks                        `json:"_links"`
    // TODO: Add struct field description
    AncestorRefs              []*AncestorRefModel                     `json:"ancestor_refs"`
    // The data center folder in which the data center resides.
    DatacenterFolder          *VMwareDatacenterFolderIDModel          `json:"datacenter_folder"`
    // Determines whether compute resources exist directly under the hidden root compute resource folder. If `true`, then compute resources exist directly under the root compute resource folder.
    HasComputeResources       *bool                                   `json:"has_compute_resources"`
    // Determines whether VMs exist directly under the hidden root VM folder. If `true`, then VMs exist directly under the root VM folder.
    HasVmFolders              *bool                                   `json:"has_vm_folders"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id                        *string                                 `json:"id"`
    // The VMware-assigned name of this data center.
    Name                      *string                                 `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the datacenter.
    OrganizationalUnitId      *string                                 `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo            *ProtectionInfo                         `json:"protection_info"`
    // The protection status of this data center. Refer to the Protection Status table for a complete list of protection statuses.
    ProtectionStatus          *string                                 `json:"protection_status"`
    // The hidden root compute resource folder of the data center.
    RootComputeResourceFolder *VMwareRootComputeResourceFolderIDModel `json:"root_compute_resource_folder"`
    // The hidden root virtual machine folder of the data center.
    RootVmFolder              *VMwareRootVMFolderIDModel              `json:"root_vm_folder"`
}

// DirectDownloadDataAccessObject represents a custom type struct.
// The details used to access the restored file if it was shared by direct download. If
// the restored file was shared by email (and not by direct download), then this field
// has a value of `null`.
type DirectDownloadDataAccessObject struct {
    // The download link used to access the restored file through direct download.
    DownloadLink *string `json:"download_link"`
    // The email address of the user who initiated the file level restore.
    RetrievedBy  *string `json:"retrieved_by"`
}

// Directory represents a custom type struct
type Directory struct {
    // URLs to pages related to the resource.
    Links             *DirectoryLinks `json:"_links"`
    // The directory ID of the file. If the file is not a directory, then this field has
    // a value of `null`.
    DirectoryId       *string         `json:"directory_id"`
    // Determines whether or not this file is a directory. If true, then this file
    // is a directory.
    IsDirectory       *bool           `json:"is_directory"`
    // The timestamp of when this file was last modified.
    ModifiedTimestamp *string         `json:"modified_timestamp"`
    // Name of this file.
    Name              *string         `json:"name"`
    // Size of this file, in bytes.
    Size              *uint64         `json:"size"`
}

// DirectoryBrowseEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type DirectoryBrowseEmbedded struct {
    // TODO: Add struct field description
    Items []*Directory `json:"items"`
}

// DirectoryBrowseLinks represents a custom type struct.
// URLs to pages related to the resource.
type DirectoryBrowseLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// DirectoryLinks represents a custom type struct.
// URLs to pages related to the resource.
type DirectoryLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// DiscoverConfig represents a custom type struct.
// The configuration of the Clumio Discover product for this connection.
// If this connection is not configured for Clumio Discover, then this field has a
// value of `null`.
type DiscoverConfig struct {
    // The asset types supported on the current version of the feature
    AssetTypesEnabled        []*string `json:"asset_types_enabled"`
    // The current version of the feature.
    InstalledTemplateVersion *string   `json:"installed_template_version"`
}

// DiscoverTemplateInfo represents a custom type struct.
// The latest available CloudFormation template for Clumio Discover.
type DiscoverTemplateInfo struct {
    // The AWS asset types supported with the available version of the template.
    AssetTypesEnabled        []*string `json:"asset_types_enabled"`
    // The latest available URL for the template.
    AvailableTemplateUrl     *string   `json:"available_template_url"`
    // The latest available version for the template.
    AvailableTemplateVersion *string   `json:"available_template_version"`
}

// DiscoverTemplateInfoV2 represents a custom type struct
type DiscoverTemplateInfoV2 struct {
    // The AWS asset types supported with the available version of the template.
    AssetTypesEnabled        []*string `json:"asset_types_enabled"`
    // The latest available version for the template.
    AvailableTemplateVersion *string   `json:"available_template_version"`
}

// DownloadSharedFileLinks represents a custom type struct.
// URLs to pages related to the resource.
type DownloadSharedFileLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// DynamoDBGRRAttributeFilter represents a custom type struct
type DynamoDBGRRAttributeFilter struct {
    // Filter condition on the DynamoDB attribute.
    // 
    // +----------------------+-------------------------------------------------------+
    // |      Condition       |                         Usage                         |
    // +======================+=======================================================+
    // | EqualTo              | Compares the filter attribute to be equal to the      |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number, Binary and Boolean.              |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotEqualTo           | Compares the filter attribute to not be equal to the  |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number, Binary and Boolean.              |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | LessThanOrEqualTo    | Compares the filter attribute to be less than or      |
    // |                      | equal to the operand value.                           |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | LessThan             | Compares the filter attribute to be less than the     |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | GreaterThanOrEqualTo | Compares the filter attribute to be greater than or   |
    // |                      | equal to the operand value.                           |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | GreaterThan          | Compares the filter attribute to be greater than the  |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Between              | Compares the filter attribute to be between the       |
    // |                      | operand values.                                       |
    // |                      | It expects two operand values. Supported types are:   |
    // |                      | String, Number and Binary.                            |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Exists               | Checks the filter attribute to exist.                 |
    // |                      | It does not expect any operand value. Supported types |
    // |                      | are: String, Number, Binary, Boolean and Null.        |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotExists            | Checks the filter attribute to not exist.             |
    // |                      | It does not expect any operand value. Supported types |
    // |                      | are: String, Number, Binary, Boolean and Null.        |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Contains             | Checks the filter attribute to contain the operand    |
    // |                      | value.                                                |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotContains          | Checks the filter attribute to not contain the        |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | BeginsWith           | Checks the filter attribute to begin with the operand |
    // |                      | value.                                                |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // 
    Condition  *string   `json:"condition"`
    // DynamoDB attribute name.
    Name       *string   `json:"name"`
    // Data-type of the DynamoDB attribute.
    // 
    // +----------------+
    // | Allowed values |
    // +================+
    // | String         |
    // +----------------+
    // | Number         |
    // +----------------+
    // | Binary         |
    // +----------------+
    // | Boolean        |
    // +----------------+
    // | Null           |
    // +----------------+
    // 
    ClumioType *string   `json:"type"`
    // Values for the attribute filter.
    Values     []*string `json:"values"`
}

// DynamoDBGRRQueryFilter represents a custom type struct.
// Filters based on which DynamoDB backup records are filtered in the query.
type DynamoDBGRRQueryFilter struct {
    // TODO: Add struct field description
    AttributeFilters []*DynamoDBGRRAttributeFilter `json:"attribute_filters"`
    // Partition Key value of the DynamoDB table.
    PartitionKey     *string                       `json:"partition_key"`
    // Sort Key filter of the DynamoDB table.
    SortKeyFilter    *DynamoDBGRRSortKeyFilter     `json:"sort_key_filter"`
}

// DynamoDBGRRSortKeyFilter represents a custom type struct.
// Sort Key filter of the DynamoDB table.
type DynamoDBGRRSortKeyFilter struct {
    // Filter condition on the DynamoDB sort key.
    // 
    // +----------------------+-------------------------------------------------------+
    // |      Condition       |                         Usage                         |
    // +======================+=======================================================+
    // | EqualTo              | Compares the filter attribute to be equal to the      |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotEqualTo           | Compares the filter attribute to not be equal to the  |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | LessThanOrEqualTo    | Compares the filter attribute to be less than or      |
    // |                      | equal to the operand value.                           |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | LessThan             | Compares the filter attribute to be less than the     |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | GreaterThanOrEqualTo | Compares the filter attribute to be greater than or   |
    // |                      | equal to the operand value.                           |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | GreaterThan          | Compares the filter attribute to be greater than the  |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Between              | Compares the filter attribute to be between the       |
    // |                      | operand values.                                       |
    // |                      | It expects two operand values. Supported types are:   |
    // |                      | String, Number and Binary.                            |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Exists               | Checks the filter attribute to exist.                 |
    // |                      | It does not expect any operand value. Supported types |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotExists            | Checks the filter attribute to not exist.             |
    // |                      | It does not expect any operand value. Supported types |
    // |                      | are: String, Number and Binary.                       |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | Contains             | Checks the filter attribute to contain the operand    |
    // |                      | value.                                                |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | NotContains          | Checks the filter attribute to not contain the        |
    // |                      | operand value.                                        |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // | BeginsWith           | Checks the filter attribute to begin with the operand |
    // |                      | value.                                                |
    // |                      | It expects only one operand value. Supported types    |
    // |                      | are: String and Binary.                               |
    // |                      |                                                       |
    // +----------------------+-------------------------------------------------------+
    // 
    Condition *string   `json:"condition"`
    // Values for the attribute filter.
    Values    []*string `json:"values"`
}

// DynamoDBGrrSource represents a custom type struct.
// The parameters for initiating a DynamoDB table backup query from a backup.
type DynamoDBGrrSource struct {
    // Performs the operation on a DynamoDB table within the specified backup.
    // Use the [GET /backups/aws/dynamodb-tables](#operation/list-backup-aws-dynamodb-tables)
    // endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// DynamoDBGrrTarget represents a custom type struct.
// The destination information for the operation, representing the access option
// for the query results. Users can access the query results by direct download or by
// email. The direct download (`direct_download`) option allows users to directly download
// the restored file from the Clumio UI. The email (`email`) option allows users to access
// the restored file using a downloadable link they receive by email. If a target is not
// specified, then `target` defaults to `direct_download`.
type DynamoDBGrrTarget struct {
    // Specifies the Clumio UI as the restore target for direct download. Optionally set
    // `direct_download: {}`. If a target is not specified, then `target` defaults to
    // `direct_download`.
    DirectDownload interface{}                      `json:"direct_download"`
    // Specifies a download link (accessible via emails) as the restore target. If not
    // specified, `target` defaults to `direct_download`.
    Email          *EmailRecipientsDataAccessOption `json:"email"`
    // Determines whether the query is preview only. If `true`, a preview of the
    // query results will be provided in the response immediately.
    // If `false` or omitted, a task will be queued to make results
    // of the query available for asynchronous download.
    Preview        *bool                            `json:"preview"`
}

// DynamoDBQueryPreviewResult represents a custom type struct.
// If preview was not set to true in the request, then the result of the query will be
// available for download asynchronously and this field has a value of `null`.
type DynamoDBQueryPreviewResult struct {
    // The columns of the previewed query result.
    Attributes []*string   `json:"attributes"`
    // The rows of the previewed query result.
    Items      []*[]string `json:"items"`
}

// DynamoDBRestoreSourceBackupOptions represents a custom type struct.
// The parameters for initiating a DynamoDB table restore from a backup.
type DynamoDBRestoreSourceBackupOptions struct {
    // The Clumio-assigned ID of the DynamoDB table backup to be restored. Use the
    // [GET /backups/aws/dynamodb-tables](#operation/list-backup-aws-dynamodb-tables)
    // endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// DynamoDBRestoreSourcePitrOptions represents a custom type struct.
// The parameters for initiating a DynamoDB table point-in-time restore.
// Only one of `timestamp` or `use_latest_restorable_time` should be set.
type DynamoDBRestoreSourcePitrOptions struct {
    // The Clumio-assigned ID of the DynamoDB table to be restored.
    // Use the [GET /datasources/aws/dynamodb-tables](#operation/list-aws-dynamodb-tables)
    // endpoint to fetch valid values.
    TableId                 *string `json:"table_id"`
    // A point in time to be restored in RFC-3339 format.
    Timestamp               *string `json:"timestamp"`
    // Restore the table to the latest possible time.
    UseLatestRestorableTime *bool   `json:"use_latest_restorable_time"`
}

// DynamoDBTableBackupLinks represents a custom type struct.
// URLs to pages related to the resource.
type DynamoDBTableBackupLinks struct {
    // The HATEOAS link to this resource.
    Self                      *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    RestoreAwsDynamodbRecords *HateoasLink     `json:"restore-aws-dynamodb-records"`
    // A resource-specific HATEOAS link.
    RestoreAwsDynamodbTable   *HateoasLink     `json:"restore-aws-dynamodb-table"`
}

// DynamoDBTableBackupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type DynamoDBTableBackupListEmbedded struct {
    // TODO: Add struct field description
    Items []*DynamoDBTableBackupWithETag `json:"items"`
}

// DynamoDBTableBackupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type DynamoDBTableBackupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// DynamoDBTableBackupWithETag represents a custom type struct
type DynamoDBTableBackupWithETag struct {
    // The ETag value.
    Etag                   *string                   `json:"_etag"`
    // URLs to pages related to the resource.
    Links                  *DynamoDBTableBackupLinks `json:"_links"`
    // The AWS-assigned ID of the account associated with this database at the time of backup.
    AccountNativeId        *string                   `json:"account_native_id"`
    // The AWS region associated with this environment.
    AwsRegion              *string                   `json:"aws_region"`
    // The billing mode of the DynamoDB table. Possible values are PROVISIONED or PAY_PER_REQUEST.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    // configuration of source table if both 'billing_mode' and 'provisioned_throughput' are empty or `null`.
    BillingMode            *string                   `json:"billing_mode"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp    *string                   `json:"expiration_timestamp"`
    // Represents the properties of a global secondary index.
    GlobalSecondaryIndexes []*GlobalSecondaryIndex   `json:"global_secondary_indexes"`
    // Describes the version of global tables in use, if the table is replicated across AWS Regions. If the table
    // is not a global table, then this field has a value of `null`. Possible values are 2017.11.29 or 2019.11.21.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), the version is defaulted to 2019.11.21.
    GlobalTableVersion     *string                   `json:"global_table_version"`
    // The Clumio-assigned ID of the backup.
    Id                     *string                   `json:"id"`
    // The number of items in DynamoDB table backup.
    ItemCount              *int64                    `json:"item_count"`
    // Represents the properties of a local secondary index.
    LocalSecondaryIndexes  []*LocalSecondaryIndex    `json:"local_secondary_indexes"`
    // Represents the provisioned throughput settings for a DynamoDB table.
    ProvisionedThroughput  *ProvisionedThroughput    `json:"provisioned_throughput"`
    // Contains the details of the replica.
    Replicas               []*ReplicaDescription     `json:"replicas"`
    // The size of the DynamoDB table backup in bytes.
    Size                   *int64                    `json:"size"`
    // Represents the server-side encryption settings for a table.
    SseSpecification       *SSESpecification         `json:"sse_specification"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp         *string                   `json:"start_timestamp"`
    // The table class of the DynamoDB table. Possible values are STANDARD or STANDARD_INFREQUENT_ACCESS.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    // STANDARD storage class if empty.
    TableClass             *string                   `json:"table_class"`
    // The Clumio-assigned ID of the DynamoDB table.
    TableId                *string                   `json:"table_id"`
    // The name of the DynamoDB table.
    TableName              *string                   `json:"table_name"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                   []*AwsTagCommonModel      `json:"tags"`
    // The type of backup. Possible values include `clumio_backup` and `aws_snapshot`.
    ClumioType             *string                   `json:"type"`
}

// DynamoDBTableRestoreSource represents a custom type struct.
// The DynamoDB table restore backup or point-in-time restore options. Only one of these fields should be set.
type DynamoDBTableRestoreSource struct {
    // The parameters for initiating a DynamoDB table point-in-time restore.
    // Only one of `timestamp` or `use_latest_restorable_time` should be set.
    ContinuousBackup  *DynamoDBRestoreSourcePitrOptions   `json:"continuous_backup"`
    // The parameters for initiating a DynamoDB table restore from a backup.
    SecurevaultBackup *DynamoDBRestoreSourceBackupOptions `json:"securevault_backup"`
}

// DynamoDBTableRestoreTarget represents a custom type struct.
// The configuration of the restored DynamoDB table.
// For restore from snapshot, use the DynamoDB table configurations present at time of snapshot obtained from
// [GET /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-dynamodb-table) and for restoring point-in-time,
// use the current configuration of the table from [GET /datasources/aws/dynamodb-tables/{table_id}](#operation/read-aws-dynamodb-table).
// The table properties are set to empty or to their default values if they are specified as `null`.
type DynamoDBTableRestoreTarget struct {
    // The billing mode of the DynamoDB table. Possible values are PROVISIONED or PAY_PER_REQUEST.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    // configuration of source table if both 'billing_mode' and 'provisioned_throughput' are empty or `null`.
    BillingMode            *string                 `json:"billing_mode"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint
    // to fetch valid values.
    EnvironmentId          *string                 `json:"environment_id"`
    // Represents the properties of a global secondary index.
    GlobalSecondaryIndexes []*GlobalSecondaryIndex `json:"global_secondary_indexes"`
    // Describes the version of global tables in use, if the table is replicated across AWS Regions. If the table
    // is not a global table, then this field has a value of `null`. Possible values are 2017.11.29 or 2019.11.21.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), the version is defaulted to 2019.11.21.
    GlobalTableVersion     *string                 `json:"global_table_version"`
    // Represents the properties of a local secondary index.
    LocalSecondaryIndexes  []*LocalSecondaryIndex  `json:"local_secondary_indexes"`
    // Represents the provisioned throughput settings for a DynamoDB table.
    ProvisionedThroughput  *ProvisionedThroughput  `json:"provisioned_throughput"`
    // Contains the details of the replica.
    Replicas               []*ReplicaDescription   `json:"replicas"`
    // Represents the server-side encryption settings for a table.
    SseSpecification       *SSESpecification       `json:"sse_specification"`
    // The table class of the DynamoDB table. Possible values are STANDARD or STANDARD_INFREQUENT_ACCESS.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    // STANDARD storage class if empty.
    TableClass             *string                 `json:"table_class"`
    // The name of the new table to which the backup must be restored.
    TableName              *string                 `json:"table_name"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                   []*AwsTagCommonModel    `json:"tags"`
}

// EBS represents a custom type struct
type EBS struct {
    // Embedded responses related to the resource.
    Embedded                 *EbsVolumeEmbedded      `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                    *EbsVolumeLinks         `json:"_links"`
    // The AWS-assigned ID of the account associated with the EBS volume.
    AccountNativeId          *string                 `json:"account_native_id"`
    // The AWS availability zone in which the EBS volume resides. For example,
    // `us-west-2a`.
    AwsAz                    *string                 `json:"aws_az"`
    // The AWS region associated with the EBS volume.
    AwsRegion                *string                 `json:"aws_region"`
    // The compliance status of the protected EBS volume. Possible values include
    // "compliant" and "noncompliant". If the volume is not protected, then this field has
    // a value of `null`.
    ComplianceStatus         *string                 `json:"compliance_status"`
    // The timestamp of when the volume was deleted. Represented in RFC-3339 format. If
    // this volume has not been deleted, then this field has a value of `null`.
    DeletionTimestamp        *string                 `json:"deletion_timestamp"`
    // The Clumio-assigned ID of the policy directly assigned to the entity.
    DirectAssignmentPolicyId *string                 `json:"direct_assignment_policy_id"`
    // The Clumio-assigned ID of the AWS environment associated with the EBS volume.
    EnvironmentId            *string                 `json:"environment_id"`
    // Determines whether the table has a direct assignment.
    HasDirectAssignment      *bool                   `json:"has_direct_assignment"`
    // The Clumio-assigned ID of the EBS volume.
    Id                       *string                 `json:"id"`
    // Iops of the volume.
    Iops                     *int64                  `json:"iops"`
    // Determines whether the EBS volume has been deleted. If `true`, the volume has been
    // deleted.
    IsDeleted                *bool                   `json:"is_deleted"`
    // Determines whether the EBS volume is encrypted. If `true`, the volume is encrypted.
    IsEncrypted              *bool                   `json:"is_encrypted"`
    // Determines whether the EBS volume is supported for backups.
    IsSupported              *bool                   `json:"is_supported"`
    // The AWS-assigned ID of the KMS key encrypting the EBS volume. If the volume is
    // unencrypted, then this field has a value of `null`.
    KmsKeyNativeId           *string                 `json:"kms_key_native_id"`
    // The timestamp of the most recent backup of the EBS volume. Represented in RFC-3339
    // format. If the volume has never been backed up, then this field has a value of
    // `null`.
    LastBackupTimestamp      *string                 `json:"last_backup_timestamp"`
    // The timestamp of the most recent snapshot of the EBS volume taken as part of
    // Snapshot Manager. Represented in RFC-3339 format. If the volume has never been
    // snapshotted, then this field has a value of `null`.
    LastSnapshotTimestamp    *string                 `json:"last_snapshot_timestamp"`
    // The AWS-assigned name of the EBS volume.
    Name                     *string                 `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the EBS volume.
    OrganizationalUnitId     *string                 `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo           *ProtectionInfoWithRule `json:"protection_info"`
    // The protection status of the EBS volume. Possible values include "protected",
    // "unprotected", and "unsupported". If the EBS volume does not support backups, then
    // this field has a value of `unsupported`. If the volume has been deleted, then this
    // field has a value of `null`.
    ProtectionStatus         *string                 `json:"protection_status"`
    // The size of the EBS volume. Measured in bytes (B).
    Size                     *int64                  `json:"size"`
    // A tag created through AWS console which can be applied to EBS volumes.
    Tags                     []*AwsTagModel          `json:"tags"`
    // The type of EBS volume. Possible values include "gp2", "io1", "st1", "sc1", and
    // "standard".
    ClumioType               *string                 `json:"type"`
    // The reason why protection is not available. If the volume is supported, then this
    // field has a value of `null`.
    UnsupportedReason        *string                 `json:"unsupported_reason"`
    // The AWS-assigned ID of the EBS volume.
    VolumeNativeId           *string                 `json:"volume_native_id"`
}

// EBSBackupAdvancedSetting represents a custom type struct.
// Backup tier to store the backup in. Valid values are: (empty) equivalent to standard, `standard`, and `lite`.
type EBSBackupAdvancedSetting struct {
    // TODO: Add struct field description
    BackupTier *string `json:"backup_tier"`
}

// EBSBackupLinksV1 represents a custom type struct.
// URLs to pages related to the resource.
type EBSBackupLinksV1 struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// EBSBackupListEmbeddedV1 represents a custom type struct.
// Embedded responses related to the resource.
type EBSBackupListEmbeddedV1 struct {
    // TODO: Add struct field description
    Items []*EBSBackupV1 `json:"items"`
}

// EBSBackupListLinksV1 represents a custom type struct.
// URLs to pages related to the resource.
type EBSBackupListLinksV1 struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// EBSBackupV1 represents a custom type struct
type EBSBackupV1 struct {
    // URLs to pages related to the resource.
    Links                *EBSBackupLinksV1    `json:"_links"`
    // The AWS-assigned ID of the account associated with the backup.
    AccountNativeId      *string              `json:"account_native_id"`
    // The availability zone associated with the volume backup. For example, `us-west-2a`.
    AwsAz                *string              `json:"aws_az"`
    // The AWS region in which the volume backup resides. For example, `us-west-2`.
    AwsRegion            *string              `json:"aws_region"`
    // The reason that browsing is unavailable for the backup. Possible values include "file_limit_exceeded" and
    // "browsing_unavailable". If browse indexing is successful, then this field has a value of `null`.
    BrowsingFailedReason *string              `json:"browsing_failed_reason"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp  *string              `json:"expiration_timestamp"`
    // The Clumio-assigned ID of the volume backup.
    Id                   *string              `json:"id"`
    // Determines whether browsing is available for the backup. If `true`, then browsing is available for the backup.
    IsBrowsable          *bool                `json:"is_browsable"`
    // Determines whether the EBS volume backup is encrypted. If `true`, the volume backup is encrypted.
    IsEncrypted          *bool                `json:"is_encrypted"`
    // The AWS-assigned ID of the KMS key encrypting this EBS volume backup. If the volume is not encrypted, this field has a value of `null`.
    KmsKeyNativeId       *string              `json:"kms_key_native_id"`
    // The size of the volume backup. Measured in gigabytes (GB).
    Size                 *int64               `json:"size"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp       *string              `json:"start_timestamp"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                 []*AwsTagCommonModel `json:"tags"`
    // The volume type of the original EBS volume before backup. Possible values include `gp2`, `io1`, `st1`, `sc1`, `standard`.
    ClumioType           *string              `json:"type"`
    // The Clumio-assigned ID of the EBS volume associated with the volume backup.
    VolumeId             *string              `json:"volume_id"`
    // The AWS-assigned ID of the EBS volume associated with the volume backup.
    VolumeNativeId       *string              `json:"volume_native_id"`
}

// EBSRestoreSource represents a custom type struct.
// The EBS volume backup to be restored.
type EBSRestoreSource struct {
    // The Clumio-assigned ID of the EBS volume backup to be restored. Use the [GET /backups/aws/ebs-volumes](#operation/list-aws-ebs-volumes) endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// EBSRestoreSourceV1 represents a custom type struct.
// The EBS volume backup to be restored.
type EBSRestoreSourceV1 struct {
    // The Clumio-assigned ID of the EBS volume backup to be restored. Use the [GET /backups/aws/ebs-volumes](#operation/list-aws-ebs-volumes) endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// EBSRestoreTarget represents a custom type struct.
// The configuration of the EBS volume to be restored.
type EBSRestoreTarget struct {
    // The availability zone into which the EBS volume is restored. For example, `us-west-2a`.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.
    AwsAz          *string              `json:"aws_az"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination. Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.
    EnvironmentId  *string              `json:"environment_id"`
    // Iops of the volume to be restored.
    // Iops field is only applicable if volume_type is gp3, io1, io2.
    Iops           *int64               `json:"iops"`
    // The KMS encryption key ID used to encrypt the EBS volume data. The KMS encryption key ID is stored in the AWS cloud as part of your AWS account.
    KmsKeyNativeId *string              `json:"kms_key_native_id"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags           []*AwsTagCommonModel `json:"tags"`
    // Type of the volume to restore as.
    // Allowed Values: gp2, gp3, io1, io2, sc1, st1, standard.
    ClumioType     *string              `json:"type"`
}

// EBSRestoreTargetV1 represents a custom type struct.
// The configuration of the EBS volume to be restored.
type EBSRestoreTargetV1 struct {
    // The availability zone into which the EBS volume is restored. For example, `us-west-2a`.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.
    AwsAz          *string              `json:"aws_az"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination. Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.
    EnvironmentId  *string              `json:"environment_id"`
    // The KMS encryption key ID used to encrypt the EBS volume data. The KMS encryption key ID is stored in the AWS cloud as part of your AWS account.
    KmsKeyNativeId *string              `json:"kms_key_native_id"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags           []*AwsTagCommonModel `json:"tags"`
}

// EC2AMIRestoreTarget represents a custom type struct.
// The configuration for the restore to AMI.
type EC2AMIRestoreTarget struct {
    // The description for the AMI.
    Description            *string                            `json:"description"`
    // TODO: Add struct field description
    EbsBlockDeviceMappings []*EC2RestoreEbsBlockDeviceMapping `json:"ebs_block_device_mappings"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint
    // to fetch valid values.
    EnvironmentId          *string                            `json:"environment_id"`
    // The name for the AMI.
    Name                   *string                            `json:"name"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                   []*AwsTagCommonModel               `json:"tags"`
}

// EC2BackupAdvancedSetting represents a custom type struct.
// Backup tier to store the backup in. Valid values are: (empty) equivalent to standard, `standard`, and `lite`.
type EC2BackupAdvancedSetting struct {
    // TODO: Add struct field description
    BackupTier *string `json:"backup_tier"`
}

// EC2InstanceRestoreTarget represents a custom type struct.
// The configuration of an EC2 instance to be restored.
type EC2InstanceRestoreTarget struct {
    // The AWS-assigned ID of the Amazon Machine Image (AMI) used to launch the EC2 instance.
    AmiNativeId            *string                            `json:"ami_native_id"`
    // The availability zone for the instance. This is determined by the subnet chosen to
    // restore the EC2 instance into.
    AwsAz                  *string                            `json:"aws_az"`
    // TODO: Add struct field description
    EbsBlockDeviceMappings []*EC2RestoreEbsBlockDeviceMapping `json:"ebs_block_device_mappings"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint
    // to fetch valid values.
    EnvironmentId          *string                            `json:"environment_id"`
    // The name of IAM instance profile to launch the instance with.
    IamInstanceProfileName *string                            `json:"iam_instance_profile_name"`
    // The name of SSH KeyPair to be used.
    KeyPairName            *string                            `json:"key_pair_name"`
    // TODO: Add struct field description
    NetworkInterfaces      []*EC2RestoreNetworkInterface      `json:"network_interfaces"`
    // Whether or not to power the instance on at the end of restore. If this is set
    // to true, the instance state will be 'running.' If it is set to false, the state
    // will be 'stopped.'
    ShouldPowerOn          *bool                              `json:"should_power_on"`
    // The AWS-assigned ID of the subnet to launch the instance into.
    SubnetNativeId         *string                            `json:"subnet_native_id"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                   []*AwsTagCommonModel               `json:"tags"`
    // The AWS-assigned ID of the vpc to launch the instance into.
    VpcNativeId            *string                            `json:"vpc_native_id"`
}

// EC2RestoreEbsBlockDeviceMapping represents a custom type struct
type EC2RestoreEbsBlockDeviceMapping struct {
    // The AWS-assigned ID for a customer managed KMS key under which the
    // EBS volume is encrypted.
    KmsKeyNativeId *string              `json:"kms_key_native_id"`
    // The device name where the EBS volume is attached to the instance, needed by
    // instance_restore_target and ami_restore_target restore type and by volumes_restore_target
    // when target_instance_native_id is provided.
    Name           *string              `json:"name"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags           []*AwsTagCommonModel `json:"tags"`
    // The AWS-assigned ID of the backed-up volume.
    VolumeNativeId *string              `json:"volume_native_id"`
}

// EC2RestoreNetworkInterface represents a custom type struct
type EC2RestoreNetworkInterface struct {
    // The position of the network interface in the attachment order. A primary
    // network interface has a device index of 0.
    DeviceIndex              *int64    `json:"device_index"`
    // The AWS-assigned ID of the existing network interface to attach to the
    // restored instance. If one wishes to restore this network interface from the backup,
    // then this field should be set to `null`.
    NetworkInterfaceNativeId *string   `json:"network_interface_native_id"`
    // Whether or not a default network interface should be restored. It will not have any of
    // the same configurations as the backup network interface.
    RestoreDefault           *bool     `json:"restore_default"`
    // Whether or not the network interface should be restored the backup network interface.
    // It will be configured with the same configurations as the backup network interface.
    RestoreFromBackup        *bool     `json:"restore_from_backup"`
    // The AWS-assigned IDs for the security groups to associate with this network interface.
    // If one wishes to attach an existing network interface, then this field should be
    // set to `null`.
    SecurityGroupNativeIds   []*string `json:"security_group_native_ids"`
    // The AWS-assigned ID of the subnet associated with the network interface.
    // If one wishes to attach an existing network interface, then this field should be
    // set to `null`.
    SubnetNativeId           *string   `json:"subnet_native_id"`
}

// EC2RestoreSource represents a custom type struct.
// The EC2 instance backup to be restored.
type EC2RestoreSource struct {
    // The Clumio-assigned ID of the EC2 instance backup to be restored. Use the
    // [GET /backups/aws/ec2-instances](#operation/list-aws-ec2-instances)
    // endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// EC2RestoreTarget represents a custom type struct.
// The target configuration per EC2 restore type. Only one of these fields should be set.
type EC2RestoreTarget struct {
    // The configuration for the restore to AMI.
    AmiRestoreTarget      *EC2AMIRestoreTarget      `json:"ami_restore_target"`
    // The configuration of an EC2 instance to be restored.
    InstanceRestoreTarget *EC2InstanceRestoreTarget `json:"instance_restore_target"`
    // The target configuration for the volumes to be restored.
    VolumesRestoreTarget  *EC2VolumesRestoreTarget  `json:"volumes_restore_target"`
}

// EC2VolumesRestoreTarget represents a custom type struct.
// The target configuration for the volumes to be restored.
type EC2VolumesRestoreTarget struct {
    // The availability zone for restoring the volumes unattached. Either this or
    // target_instance_native_id needs to be specified.
    AwsAz                  *string                            `json:"aws_az"`
    // TODO: Add struct field description
    EbsBlockDeviceMappings []*EC2RestoreEbsBlockDeviceMapping `json:"ebs_block_device_mappings"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint
    // to fetch valid values.
    EnvironmentId          *string                            `json:"environment_id"`
    // The aws native ID of the EC2 instance to be used to attach the restored volumes.
    // If not present, then aws_az need to be specified.
    TargetInstanceNativeId *string                            `json:"target_instance_native_id"`
}

// EbsAssetInfo represents a custom type struct
type EbsAssetInfo struct {
    // The current version of the feature.
    InstalledTemplateVersion *string `json:"installed_template_version"`
}

// EbsTemplateInfo represents a custom type struct
type EbsTemplateInfo struct {
    // The latest available feature version for the asset.
    AvailableTemplateVersion *string `json:"available_template_version"`
}

// EbsVolumeEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type EbsVolumeEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition interface{} `json:"read-policy-definition"`
}

// EbsVolumeLinks represents a custom type struct.
// URLs to pages related to the resource.
type EbsVolumeLinks struct {
    // The HATEOAS link to this resource.
    Self                     *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateBackupAwsEbsVolume *HateoasLink                     `json:"create-backup-aws-ebs-volume"`
    // A resource-specific HATEOAS link.
    ListBackupAwsEbsVolumes  *HateoasLink                     `json:"list-backup-aws-ebs-volumes"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition     *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
}

// EbsVolumeListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type EbsVolumeListEmbedded struct {
    // TODO: Add struct field description
    Items []*EBS `json:"items"`
}

// EbsVolumeListLinks represents a custom type struct.
// URLs to pages related to the resource.
type EbsVolumeListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// EmailDownloadDataAccessObject represents a custom type struct.
// The details used to access the restored file, if it was shared by email. If the
// restored file was shared by direct download (and not email), then this field has a
// value of `null`.
type EmailDownloadDataAccessObject struct {
    // The optional message that was sent as part of the email.
    EmailMessage *string `json:"email_message"`
    // The email address of the user who initiated the file level restore.
    RetrievedBy  *string `json:"retrieved_by"`
    // The email address of the user who the file was retrieved for.
    RetrievedFor *string `json:"retrieved_for"`
}

// EmailDownloadDataAccessOption represents a custom type struct.
// Specifies a download link (accessible via email) as the restore target. If not
// specified, `target` defaults to `direct_download`. If you specify `email`, also
// send the user the passcode that gets generated from this request (see `passcode` in
// the response). After the user clicks the download link, they must enter the
// passcode to access the files.
type EmailDownloadDataAccessOption struct {
    // The email address of the user who will receive the download link to the restored
    // file.
    EmailAddress *string `json:"email_address"`
    // The optional message sent as part of the email.
    Message      *string `json:"message"`
}

// EmailRecipientsDataAccessOption represents a custom type struct.
// Specifies a download link (accessible via emails) as the restore target. If not
// specified, `target` defaults to `direct_download`.
type EmailRecipientsDataAccessOption struct {
    // The optional message sent as part of the email.
    Message         *string   `json:"message"`
    // The recipient email addresses who will receive the download link to the restored records.
    RecipientEmails []*string `json:"recipient_emails"`
}

// EntityGroupAssignmetUpdates represents a custom type struct.
// Updates to the organizational unit assignments.
type EntityGroupAssignmetUpdates struct {
    // The Clumio-assigned IDs of the organizational units to be assigned to the user.
    Add    []*string `json:"add"`
    // The Clumio-assigned IDs of the organizational units to be unassigned to the user.
    Remove []*string `json:"remove"`
}

// EntityGroupEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type EntityGroupEmbedded struct {
    // Embeds the associated task of a resource in the response if requested using the `embed` query parameter.
    ReadTask interface{} `json:"read-task"`
}

// EntityModel represents a custom type struct.
// entityModel denotes the entityModel
type EntityModel struct {
    // The parent object of the primary entity associated with the organizational unit. For example, "vmware_vcenter" is the parent entity of primary entity "vmware_vm_folder".
    // The parent object is necessary for VMware entities and can be omitted for other data sources.
    ParentEntity  *OrganizationalUnitParentEntity  `json:"parent_entity"`
    // The primary object associated with the organizational unit. Examples of primary entities include "aws_environment" and "vmware_vm".
    PrimaryEntity *OrganizationalUnitPrimaryEntity `json:"primary_entity"`
}

// ErrorModel represents a custom type struct
type ErrorModel struct {
    // ErrorCode is a short string describing the error, if any.
    ErrorCode    *string `json:"error_code"`
    // ErrorMessage is a longer description explaining the error, if any, and how to
    // fix it.
    ErrorMessage *string `json:"error_message"`
}

// FileDescriptor represents a custom type struct.
// Specifies a file/directory by providing path and file system.
type FileDescriptor struct {
    // The Clumio-assigned ID of the filesystem within which to restore the file. Use
    // [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-versions)
    // to fetch the value.
    FilesystemId *string `json:"filesystem_id"`
    // The path of the file to be restored. Use
    // [GET /backups/files/search](#operation/list-files) to fetch the value.
    Path         *string `json:"path"`
}

// FileRestoreSource represents a custom type struct.
// The files to be restored and from which backup they are to be restored from.
type FileRestoreSource struct {
    // The Clumio-assigned ID of the backup containing the files you want to restore. Use
    // [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-versions)
    // to fetch the value.
    BackupId *string           `json:"backup_id"`
    // Specifies a file/directory by providing path and file system.
    Files    []*FileDescriptor `json:"files"`
}

// FileRestoreTarget represents a custom type struct.
// The destination information for the file level restore, representing the access option
// for the restored file. Users can access the restored file by direct download or by
// email. The direct download (`direct_download`) option allows users to directly download
// the restored file from the Clumio UI. The email (`email`) option allows users to access
// the restored file using a downloadable link they receive by email. If a target is not
// specified, then `target` defaults to `direct_download`.
type FileRestoreTarget struct {
    // Specifies the Clumio UI as the restore target for direct download. Optionally set
    // `direct_download: {}`. If a target is not specified, then `target` defaults to
    // `direct_download`.
    DirectDownload interface{}                    `json:"direct_download"`
    // Specifies a download link (accessible via email) as the restore target. If not
    // specified, `target` defaults to `direct_download`. If you specify `email`, also
    // send the user the passcode that gets generated from this request (see `passcode` in
    // the response). After the user clicks the download link, they must enter the
    // passcode to access the files.
    Email          *EmailDownloadDataAccessOption `json:"email"`
}

// FileSearchListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type FileSearchListEmbedded struct {
    // TODO: Add struct field description
    Items []*FileSearchResult `json:"items"`
}

// FileSearchListLinks represents a custom type struct.
// URLs to pages related to the resource.
type FileSearchListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// FileSearchResult represents a custom type struct
type FileSearchResult struct {
    // URLs to pages related to the resource.
    Links          *ListFileVersionsHateoasLinks `json:"_links"`
    // The full file path.
    Path           *string                       `json:"path"`
    // The Clumio-assigned ID representing a collection of one or more versions of the same
    // file backed up at different times. This ID cannot be used to restore the
    // file. To restore the file, use the
    // [GET /backups/files/search/{search_result_id}/versions](#operation/list-file-versions)
    // endpoint to retrieve particular versions of this file that can be restored.
    // Then, use the backup ID, filesystem ID, and file path as parameters for the
    // [POST /restores/files](#operation/restore-files) endpoint.
    SearchResultId *string                       `json:"search_result_id"`
}

// FileSystem represents a custom type struct
type FileSystem struct {
    // TODO: Add struct field description
    Links                *HateoasCommonLinks `json:"_links"`
    // The amount of available memory on the filesystem in bytes. Does not include
    // reserved memory.
    Available            *uint64             `json:"available"`
    // The filesystem UUID produced by the `lsblk` linux command. If this filesystem
    // was not given a UUID in the host environment, then this field has a value of
    // `null`.
    FilesystemNativeId   *string             `json:"filesystem_native_id"`
    // The Clumio-assigned ID of the filesystem.
    Id                   *string             `json:"id"`
    // The reason why file indexing failed. If file indexing succeeded, then this field
    // has a value of `null`. Possible values include "unsupported" and "encrypted".
    IndexingFailedReason *string             `json:"indexing_failed_reason"`
    // Determines whether the file system was encrypted.
    IsEncrypted          *bool               `json:"is_encrypted"`
    // Determines whether the file system has been indexed.
    // If `true`, file indexing completed successfully.
    IsIndexed            *bool               `json:"is_indexed"`
    // The location of this filesystem in the host environment. Only identifies mount
    // points that correspond to Windows drive letters. All other mount points are
    // identified by a '/'.
    MountPath            *string             `json:"mount_path"`
    // The number of files (including directories) indexed in the file system.
    NumFilesIndexed      *int64              `json:"num_files_indexed"`
    // The total amount of memory available to the filesystem in bytes.
    Size                 *uint64             `json:"size"`
    // The type of the filesystem. This field is populated with values returned from
    // the lsblk command. Possible values include `ntfs`, `xfs`, and `ext3`.
    ClumioType           *string             `json:"type"`
    // The amount of memory used by the filesystem in bytes.
    Used                 *uint64             `json:"used"`
}

// FileSystemListEmbedded represents a custom type struct.
// _embedded contains the list of items of a file_system list query
type FileSystemListEmbedded struct {
    // TODO: Add struct field description
    Items []*FileSystem `json:"items"`
}

// FileSystemListLinks represents a custom type struct.
// _links provides URLs to related navigable pages of a file_system list query
type FileSystemListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// FileVersion represents a custom type struct
type FileVersion struct {
    // URLs to pages related to the resource.
    Links             *FileVersionHateoas `json:"_links"`
    // The Clumio-assigned ID of the backup.
    BackupId          *string             `json:"backup_id"`
    // The Clumio-assigned ID of the filesystem within which to restore the file. Use
    // [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-versions)
    // to fetch the value.
    FilesystemId      *string             `json:"filesystem_id"`
    // The timestamp of the last time the file was modified. Represented in RFC-3339 format.
    ModifiedTimestamp *string             `json:"modified_timestamp"`
    // The path of the file to be restored. Use
    // [GET /backups/files/search](#operation/list-files) to fetch the value.
    Path              *string             `json:"path"`
    // The size of the file in bytes.
    Size              *int64              `json:"size"`
    // The timestamp of when the backup associated with this file started. Represented in RFC-3339 format.
    StartTimestamp    *string             `json:"start_timestamp"`
}

// FileVersionHateoas represents a custom type struct.
// URLs to pages related to the resource.
type FileVersionHateoas struct {
    // A resource-specific HATEOAS link.
    RestoreFiles *HateoasLink `json:"restore-files"`
}

// FileVersionsListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type FileVersionsListEmbedded struct {
    // TODO: Add struct field description
    Items []*FileVersion `json:"items"`
}

// FileVersionsListLinks represents a custom type struct.
// URLs to pages related to the resource.
type FileVersionsListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// FolderEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type FolderEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition                   interface{} `json:"read-policy-definition"`
    // Embeds the compliance statistics of VMs into each vCenter resource in the response, if requested using the `_embed` query parameter.
    ReadVmwareVcenterFolderComplianceStats interface{} `json:"read-vmware-vcenter-folder-compliance-stats"`
}

// FolderLinks represents a custom type struct.
// URLs to pages related to the resource.
type FolderLinks struct {
    // The HATEOAS link to this resource.
    Self                                   *HateoasSelfLink                             `json:"_self"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                        *ProtectEntitiesHateoasLink                  `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition                   *ReadPolicyDefinitionHateoasLink             `json:"read-policy-definition"`
    // A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
    ReadVmwareVcenterFolderComplianceStats *ReadVCenterObjectProtectionStatsHateoasLink `json:"read-vmware-vcenter-folder-compliance-stats"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                      *UnprotectEntitiesHateoasLink                `json:"unprotect-entities"`
}

// FolderListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type FolderListEmbedded struct {
    // FolderWithETag to support etag string to be calculated
    Items []*FolderWithETag `json:"items"`
}

// FolderListLinks represents a custom type struct.
// URLs to pages related to the resource.
type FolderListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// FolderWithETag represents a custom type struct.
// FolderWithETag to support etag string to be calculated
type FolderWithETag struct {
    // Embedded responses related to the resource.
    Embedded              *FolderEmbedded                     `json:"_embedded"`
    // The ETag value.
    Etag                  *string                             `json:"_etag"`
    // URLs to pages related to the resource.
    Links                 *FolderLinks                        `json:"_links"`
    // The data center associated with this folder.
    Datacenter            *VMwareVCenterFolderDatacenterModel `json:"datacenter"`
    // Count of all descendant folders inside this folder
    DescendantFolderCount *int64                              `json:"descendant_folder_count"`
    // Determines whether the folder has direct child folders.
    HasChildFolders       *bool                               `json:"has_child_folders"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id                    *string                             `json:"id"`
    // Determines whether the folder is a hidden root folder. If `true`, the folder is a hidden root folder.
    IsRoot                *bool                               `json:"is_root"`
    // Determines whether the folder can be used as a restore destination. If `true`, the folder can be used as a restore destination, and backups can be restored to the folder.
    IsSupported           *bool                               `json:"is_supported"`
    // The VMware-assigned name of the folder.
    Name                  *string                             `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the folder.
    OrganizationalUnitId  *string                             `json:"organizational_unit_id"`
    // The parent folder under which this folder resides.
    ParentFolder          *VMwareVCenterParentFolderModel     `json:"parent_folder"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo        *ProtectionInfo                     `json:"protection_info"`
    // The protection status of this folder. Refer to the Protection Status table for a complete list of protection statuses.
    ProtectionStatus      *string                             `json:"protection_status"`
    // The folder type. Examples of folder types include "datacenter_folder" and "vm_folder". Refer to the Folder Type table for a complete list of folder types.
    ClumioType            *string                             `json:"type"`
}

// GeneralSettingsLinks represents a custom type struct.
// URLs to pages related to the resource.
type GeneralSettingsLinks struct {
    // The HATEOAS link to this resource.
    Self                  *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    UpdateGeneralSettings *HateoasLink     `json:"update-general-settings"`
}

// GenerateRestoredFilePasscodeLinks represents a custom type struct.
// URLs to pages related to the resource.
type GenerateRestoredFilePasscodeLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// GlobalSecondaryIndex represents a custom type struct.
// Represents the properties of a global secondary index.
type GlobalSecondaryIndex struct {
    // The name of the global secondary index.
    IndexName             *string                `json:"index_name"`
    // Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key
    // of a table, or the key attributes of an index.
    KeySchema             []*KeySchemaElement    `json:"key_schema"`
    // Represents attributes that are copied (projected) from the table into an index. These are in addition to the
    // primary key attributes and index key attributes, which are automatically projected.
    Projection            *Projection            `json:"projection"`
    // Represents the provisioned throughput settings for a DynamoDB table.
    ProvisionedThroughput *ProvisionedThroughput `json:"provisioned_throughput"`
}

// GrrSource represents a custom type struct.
// The RDS database backup to be queried.
type GrrSource struct {
    // Performs the operation on a database within the specified backup.
    // Use the [GET /backups/aws/rds-resources](#operation/list-backup-aws-rds-resources)
    // endpoint to fetch valid values.
    BackupId     *string `json:"backup_id"`
    // Performs the operation on the database with the specified name.
    // Use the [GET /backups/aws/rds-resources](#operation/list-backup-aws-rds-resource-databases)
    // endpoint to fetch valid values.
    DatabaseName *string `json:"database_name"`
}

// GrrTarget represents a custom type struct.
// The query to perform on the source RDS database.
type GrrTarget struct {
    // Determines whether the query is preview only. If `true`, a preview of the
    // query results will be provided in the response immediately.
    // If `false` or omitted, a task will be queued to make the result
    // of the query available for asynchronous download.
    Preview        *bool   `json:"preview"`
    // The SQL statement that is to be executed on the target database.
    // For example, "SELECT * FROM employee WHERE id > 100"
    QueryStatement *string `json:"query_statement"`
}

// HateoasCommonLinks represents a custom type struct
type HateoasCommonLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// HateoasFirstLink represents a custom type struct.
// The HATEOAS link to the first page of results.
type HateoasFirstLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// HateoasLastLink represents a custom type struct.
// The HATEOAS link to the last page of results.
type HateoasLastLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// HateoasLink represents a custom type struct.
// A resource-specific HATEOAS link.
type HateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// HateoasNextLink represents a custom type struct.
// The HATEOAS link to the next page of results.
type HateoasNextLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// HateoasPrevLink represents a custom type struct.
// The HATEOAS link to the previous page of results.
type HateoasPrevLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// HateoasSelfLink represents a custom type struct.
// The HATEOAS link to this resource.
type HateoasSelfLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// Host represents a custom type struct
type Host struct {
    // URLs to pages related to the resource.
    Links                  *HostLinks `json:"_links"`
    // The endpoints discovered post the host connection of the host.
    DiscoveredEndpoints    []*string  `json:"discovered_endpoints"`
    // The Current MSI version of the edge connector installed in the host.
    EdgeConnectorVersion   *string    `json:"edge_connector_version"`
    // The user-provided endpoint used to connect the host.
    Endpoint               *string    `json:"endpoint"`
    // The Clumio-assigned ID of the management group associated with the host.
    GroupId                *string    `json:"group_id"`
    // The Clumio-assigned ID of the Host.
    Id                     *string    `json:"id"`
    // The timestamp of the last successful heartbeat of this host. Represented in RFC-3339 format.
    LastHeartbeatTimestamp *string    `json:"last_heartbeat_timestamp"`
    // Name of the Host.
    Name                   *string    `json:"name"`
    // The operational status of the Host. Possible values include `upgrade_in_progress`, `upgrade_success`, `upgrade_failed`, `delete_in_progress`, `delete_failed`, `move_in_progress`, `move_succeeded` and `move_failed`.
    OperationalStatus      *string    `json:"operational_status"`
    // The connection status of the Host. Possible values include `connected`, `disconnected`, `connection_pending`, and `invalid_token`.
    Status                 *string    `json:"status"`
    // The Clumio-assigned ID of the subgroup associated with the host.
    SubgroupId             *string    `json:"subgroup_id"`
    // The Clumio-assigned UUID of the host. This UUID is used for filtering hosts during list operations.
    Uuid                   *string    `json:"uuid"`
}

// HostIDModel represents a custom type struct
type HostIDModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the host.
    Id *string `json:"id"`
}

// HostLinks represents a custom type struct.
// URLs to pages related to the resource.
type HostLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// HostListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type HostListEmbedded struct {
    // HostWithETag to support etag string to be calculated
    Items []*HostWithETag `json:"items"`
}

// HostListLinks represents a custom type struct.
// URLs to pages related to the resource.
type HostListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// HostWithETag represents a custom type struct.
// HostWithETag to support etag string to be calculated
type HostWithETag struct {
    // The ETag value.
    Etag                *string                                `json:"_etag"`
    // URLs to pages related to the resource.
    Links               *HostLinks                             `json:"_links"`
    // The VMware compute resource representing the host.
    ComputeResource     *VMwareVCenterHostComputeResourceModel `json:"compute_resource"`
    // The connection state of the host as seen through the vCenter server. Examples include "connected", "disconnected", and "not_responding".
    ConnectionState     *string                                `json:"connection_state"`
    // The data center in which the host resides.
    Datacenter          *VMwareVCenterHostDatacenterModel      `json:"datacenter"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the host.
    Id                  *string                                `json:"id"`
    // Determines whether the host has been placed in maintenance mode as seen through the vCenter server. If `true`, the host is in maintenance mode.
    IsInMaintenanceMode *bool                                  `json:"is_in_maintenance_mode"`
    // Determines whether the host has been placed in quarantine mode as seen through the vCenter server. If `true`, the host is in quarantine mode.
    IsInQuarantineMode  *bool                                  `json:"is_in_quarantine_mode"`
    // Determines whether the host is a standalone host. If `true`, the host is a standalone host.
    IsStandalone        *bool                                  `json:"is_standalone"`
    // Determines whether the host can be used as a restore destination. If `true`, the host can be used as a restore destination and backups can be restored to the host.
    IsSupported         *bool                                  `json:"is_supported"`
    // The VMware-assigned name of the host.
    Name                *string                                `json:"name"`
    // The power state of the host as seen through the vCenter server. Examples include "powered_off", "powered_on", and "standby".
    PowerState          *string                                `json:"power_state"`
}

// IndividualAlertDetails represents a custom type struct.
// Additional information about the alert.
type IndividualAlertDetails struct {
    // A brief description of the condition that caused the alert. Examples include "Size Limit Exceeded" and "Insufficient Cloud Connector Capacity".
    Cause       *string            `json:"cause"`
    // A detailed description of the alert, including the reason why the alert occurred
    // and the steps you must take to resolve the issue.
    Description *string            `json:"description"`
    // The general alert category. Examples include "Policy Violated" and "Restore Failed".
    ClumioType  *string            `json:"type"`
    // Data specific to the alert generated. If the alert has no variables, then this
    // field has a value of `null`.
    Variables   map[string]*string `json:"variables"`
}

// InheritedFrom represents a custom type struct
type InheritedFrom struct {
    // The Clumio-assigned ID of the item.
    Id         *string `json:"id"`
    // Name of the folder.
    Name       *string `json:"name"`
    // VCenterObjectType denotes the VCenter object type
    Objecttype *string `json:"objectType"`
}

// KeySchemaElement represents a custom type struct.
// Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key
// of a table, or the key attributes of an index.
type KeySchemaElement struct {
    // The name of a key attribute.
    AttributeName *string `json:"attribute_name"`
    // The role that this key attribute will assume.
    // Possible values include: `HASH` - partition key and `RANGE` - sort key.
    KeyType       *string `json:"key_type"`
}

// ListFileVersionsHateoasLink represents a custom type struct.
// A HATEOAS link to the file versions associated with this resource.
type ListFileVersionsHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// ListFileVersionsHateoasLinks represents a custom type struct.
// URLs to pages related to the resource.
type ListFileVersionsHateoasLinks struct {
    // A HATEOAS link to the file versions associated with this resource.
    ListFileVersions *ListFileVersionsHateoasLink `json:"list-file-versions"`
}

// LocalSecondaryIndex represents a custom type struct.
// Represents the properties of a local secondary index.
type LocalSecondaryIndex struct {
    // The name of the local secondary index
    IndexName  *string             `json:"index_name"`
    // Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key
    // of a table, or the key attributes of an index.
    KeySchema  []*KeySchemaElement `json:"key_schema"`
    // Represents attributes that are copied (projected) from the table into an index. These are in addition to the
    // primary key attributes and index key attributes, which are automatically projected.
    Projection *Projection         `json:"projection"`
}

// M365GroupingCriteria represents a custom type struct.
// The entity type used to group organizational units for Microsoft 365 resources.
type M365GroupingCriteria struct {
    // Determines whether or not this data group is editable. If false, then an
    // organizational unit uses this data group.
    // To edit this data group, all organizational units using it must be deleted.
    IsEditable *bool   `json:"is_editable"`
    // 
    // +---------------------+------------------------+
    // |     Entity Type     |        Details         |
    // +=====================+========================+
    // | microsoft365_domain | Microsoft 365 account. |
    // +---------------------+------------------------+
    // | microsoft365_group  | Microsoft 365 group.   |
    // +---------------------+------------------------+
    // 
    ClumioType *string `json:"type"`
}

// MSSQLDatabaseBackupAdvancedSetting represents a custom type struct.
// Additional policy configuration settings for the `mssql_database_backup` operation. If this operation is not of type `mssql_database_backup`, then this field is omitted from the response.
type MSSQLDatabaseBackupAdvancedSetting struct {
    // The alternative replica for MSSQL database backups. This setting only applies to Availability Group databases. Possible values include `"primary"`, `"sync_secondary"`, and `"stop"`. If `"stop"` is provided, then backups will not attempt to switch to a different replica when the preferred replica is unavailable. Otherwise, recurring backups will attempt to use either the primary replica or the secondary replica accordingly.
    AlternativeReplica *string `json:"alternative_replica"`
    // The primary preferred replica for MSSQL database backups. This setting only applies to Availability Group databases. Possible values include `"primary"` and `"sync_secondary"`. Recurring backup will first attempt to use either the primary replica or the secondary replica accordingly.
    PreferredReplica   *string `json:"preferred_replica"`
}

// MSSQLLogBackupAdvancedSetting represents a custom type struct.
// Additional policy configuration settings for the `mssql_log_backup` operation. If this operation is not of type `mssql_log_backup`, then this field is omitted from the response.
type MSSQLLogBackupAdvancedSetting struct {
    // The alternative replica for MSSQL log backups. This setting only applies to Availability Group databases. Possible values include `"primary"`, `"sync_secondary"`, and `"stop"`. If `"stop"` is provided, then backups will not attempt to switch to a different replica when the preferred replica is unavailable. Otherwise, recurring backups will attempt to use either the primary replica or the secondary replica accordingly.
    AlternativeReplica *string `json:"alternative_replica"`
    // The primary preferred replica for MSSQL log backups. This setting only applies to Availability Group databases. Possible values include `"primary"` and `"sync_secondary"`. Recurring backup will first attempt to use either the primary replica or the secondary replica accordingly.
    PreferredReplica   *string `json:"preferred_replica"`
}

// ManagementGroup represents a custom type struct
type ManagementGroup struct {
    // URLs to pages related to the resource.
    Links      *ManagementGroupLinks `json:"_links"`
    // The Clumio-assigned ID of the management group.
    Id         *string               `json:"id"`
    // The name of the management group.
    Name       *string               `json:"name"`
    // The type of the management group. Possible values include `on_prem`.
    ClumioType *string               `json:"type"`
    // The Clumio-assigned ID of the vCenter server associated with the management group.
    // All management groups are associated with a vCenter server.
    VcenterId  *string               `json:"vcenter_id"`
}

// ManagementGroupLinks represents a custom type struct.
// URLs to pages related to the resource.
type ManagementGroupLinks struct {
    // The HATEOAS link to this resource.
    Self                    *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ListManagementSubgroups *HateoasLink     `json:"list-management-subgroups"`
    // A resource-specific HATEOAS link.
    UpdateManagementGroup   *HateoasLink     `json:"update-management-group"`
}

// ManagementGroupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ManagementGroupListEmbedded struct {
    // TODO: Add struct field description
    Items []*ManagementGroup `json:"items"`
}

// ManagementGroupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ManagementGroupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// MoveHostsLinks represents a custom type struct.
// URLs to pages related to the resource.
type MoveHostsLinks struct {
    // URLs to pages related to the resource.
    Links *ReadTaskHateoasLinks `json:"_links"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink      `json:"_self"`
}

// MoveHostsSource represents a custom type struct.
// The hosts to be moved to a different management subgroup.
type MoveHostsSource struct {
    // Endpoints of hosts to be deleted
    Endpoints  []*string `json:"endpoints"`
    // Performs the operation on a host within the specified group id.
    GroupId    *string   `json:"group_id"`
    // Performs the operation on a host within the specified subgroup id.
    SubgroupId *string   `json:"subgroup_id"`
}

// MoveHostsTarget represents a custom type struct.
// The target configuration of the hosts to be moved.
type MoveHostsTarget struct {
    // Performs the operation on a host within the specified group id.
    GroupId    *string `json:"group_id"`
    // Performs the operation on a host within the specified subgroup id.
    SubgroupId *string `json:"subgroup_id"`
}

// MssqlAG represents a custom type struct
type MssqlAG struct {
    // MssqlAGEmbedded is embed of MSSQL Availability Groups
    // Embedded responses related to the resource.
    Embedded             *MssqlAGEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *MssqlAGLinks    `json:"_links"`
    // The Clumio-assigned ID of the availability group.
    Id                   *string          `json:"id"`
    // The Microsoft SQL-assigned name of the availability group.
    Name                 *string          `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the availability group.
    OrganizationalUnitId *string          `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo       *ProtectionInfo  `json:"protection_info"`
    // The status of the availability group, Possible values include 'active' and 'inactive'.
    Status               *string          `json:"status"`
}

// MssqlAGEmbedded represents a custom type struct.
// MssqlAGEmbedded is embed of MSSQL Availability Groups
// Embedded responses related to the resource.
type MssqlAGEmbedded struct {
    // availability group level stats contains compliant database stats
    GetMssqlAvailabilityGroupStats interface{} `json:"get-mssql-availability-group-stats"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition           interface{} `json:"read-policy-definition"`
}

// MssqlAGLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlAGLinks struct {
    // The HATEOAS link to this resource.
    Self                           *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    GetMssqlAvailabilityGroupStats *HateoasLink                     `json:"get-mssql-availability-group-stats"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition           *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities              *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
}

// MssqlAGListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlAGListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlAG `json:"items"`
}

// MssqlAGListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlAGListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// MssqlDatabase represents a custom type struct
type MssqlDatabase struct {
    // Embedded responses related to the resource.
    Embedded                                *MssqlDatabaseEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                                   *DatabaseLinks         `json:"_links"`
    // The Clumio-assigned ID of the availability group. It is null in case of a standalone database.
    AvailabilityGroupId                     *string                `json:"availability_group_id"`
    // The Microsoft SQL assigned name of the availability group. It is null in case of a standalone database.
    AvailabilityGroupName                   *string                `json:"availability_group_name"`
    // The policy compliance status of the resource. If the database is not protected,
    // then this field has a value of `null`. Refer to
    // 
    // the Compliance Status table
    // 
    // for a complete list of compliance statuses.
    ComplianceStatus                        *string                `json:"compliance_status"`
    // The Clumio-assigned ID of the failover cluster.
    FailoverClusterId                       *string                `json:"failover_cluster_id"`
    // The Microsoft SQL assigned name of the Failover Cluster
    FailoverClusterName                     *string                `json:"failover_cluster_name"`
    // The Clumio-assigned ID of the group to which the standalone database belongs, in case of an
    // availability group database it will be empty.
    GroupId                                 *string                `json:"group_id"`
    // The user-provided endpoint of the host containing the given database.
    HostEndpoint                            *string                `json:"host_endpoint"`
    // The Clumio-assigned ID of the host containing the given database.
    HostId                                  *string                `json:"host_id"`
    // The Clumio-assigned ID of the Database.
    Id                                      *string                `json:"id"`
    // The Clumio-assigned ID of the instance containing the given database.
    InstanceId                              *string                `json:"instance_id"`
    // The name of the Microsoft SQL instance containing the given database.
    InstanceName                            *string                `json:"instance_name"`
    // is_supported is true if Clumio supports backup of the database.
    IsSupported                             *bool                  `json:"is_supported"`
    // The timestamp of the last time this database was full backed up.
    // Represented in RFC-3339 format. If this database has never been backed up,
    // this field has a value of `null`.
    LastBackupTimestamp                     *string                `json:"last_backup_timestamp"`
    // The timestamp of the last time this database was log backed up in Bulk Recovery Model.
    // Represented in RFC-3339 format. If this database has never been backed up,
    // this field has a value of `null`.
    LastBulkRecoveryModelLogBackupTimestamp *string                `json:"last_bulk_recovery_model_log_backup_timestamp"`
    // The timestamp of the last time this database was log backed up in Full Recovery Model.
    // Represented in RFC-3339 format. If this database has never been backed up,
    // this field has a value of `null`.
    LastFullRecoveryModelLogBackupTimestamp *string                `json:"last_full_recovery_model_log_backup_timestamp"`
    // The name of the Database.
    Name                                    *string                `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the database.
    OrganizationalUnitId                    *string                `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo                          *ProtectionInfo        `json:"protection_info"`
    // recovery_model is the recovery model of the database. Possible values include 'simple_recovery_model',
    // 'bulk_recovery_model', and 'full_recovery_model'.
    RecoveryModel                           *string                `json:"recovery_model"`
    // The size of the Database.
    Size                                    *float64               `json:"size"`
    // The status of the database, Possible values include 'active' and 'inactive'.
    Status                                  *string                `json:"status"`
    // subgroup id is the id of the Subgroup where this database belongs, in case of AG database
    // it will be empty.
    SubgroupId                              *string                `json:"subgroup_id"`
    // The type of the database. Possible values include 'availability_group_database' and 'standalone_database'.
    ClumioType                              *string                `json:"type"`
    // unsupported_reason is the reason why Clumio doesn't support backup of such database,
    // possible values include 'filestream_enabled_database'.
    UnsupportedReason                       *string                `json:"unsupported_reason"`
}

// MssqlDatabaseBackup represents a custom type struct
type MssqlDatabaseBackup struct {
    // Embedded responses related to the resource.
    Embedded            *MssqlDatabaseBackupEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links               *MssqlDatabaseBackupLinks    `json:"_links"`
    // TODO: Add struct field description
    DatabaseFiles       []*MssqlDatabaseFile         `json:"database_files"`
    // The Clumio-assigned ID of the database associated with this backup.
    DatabaseId          *string                      `json:"database_id"`
    // The Microsoft SQL database engine at the time of backup.
    Engine              *string                      `json:"engine"`
    // The Microsoft SQL database engine version at the time of backup.
    EngineVersion       *string                      `json:"engine_version"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp *string                      `json:"expiration_timestamp"`
    // The Clumio-assigned ID of the management group associated with the database at the time of backup.
    GroupId             *string                      `json:"group_id"`
    // The user-provided endpoint of the host containing the given database at the time of backup.
    HostEndpoint        *string                      `json:"host_endpoint"`
    // The Clumio-assigned ID of the host associated with the database at the time of backup.
    HostId              *string                      `json:"host_id"`
    // The Clumio-assigned ID of the backup.
    Id                  *string                      `json:"id"`
    // The Clumio-assigned instance id at the time of backup.
    InstanceId          *string                      `json:"instance_id"`
    // The instance name at the time of backup.
    InstanceName        *string                      `json:"instance_name"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp      *string                      `json:"start_timestamp"`
    // The Clumio-assigned ID of the management subgroup associated with the database at the time of backup.
    SubgroupId          *string                      `json:"subgroup_id"`
    // The type of backup. Possible values include `mssql_database_backup`, `mssql_log_backup_full_recovery_model` and `mssql_log_backup_bulk_logged_model`.
    ClumioType          *string                      `json:"type"`
}

// MssqlDatabaseBackupEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlDatabaseBackupEmbedded struct {
    // Embeds details about the management group if requested using the `embed` query.
    ReadManagementGroup    interface{} `json:"read-management-group"`
    // Embeds details about the management subgroup if requested using the `embed` query.
    ReadManagementSubgroup interface{} `json:"read-management-subgroup"`
}

// MssqlDatabaseBackupLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlDatabaseBackupLinks struct {
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ReadManagementGroup    *HateoasLink     `json:"read-management-group"`
    // A resource-specific HATEOAS link.
    ReadManagementSubgroup *HateoasLink     `json:"read-management-subgroup"`
    // A resource-specific HATEOAS link.
    RestoreMssqlDatabase   *HateoasLink     `json:"restore-mssql-database"`
}

// MssqlDatabaseBackupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlDatabaseBackupListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlDatabaseBackup `json:"items"`
}

// MssqlDatabaseBackupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlDatabaseBackupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// MssqlDatabaseEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlDatabaseEmbedded struct {
    // Embeds details about the management group if requested using the `embed` query.
    ReadManagementGroup    interface{} `json:"read-management-group"`
    // Embeds details about the management subgroup if requested using the `embed` query.
    ReadManagementSubgroup interface{} `json:"read-management-subgroup"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition   interface{} `json:"read-policy-definition"`
}

// MssqlDatabaseFile represents a custom type struct
type MssqlDatabaseFile struct {
    // The name of the database file.
    Name       *string `json:"name"`
    // The type of the database file. Possible values include sql_row_file and sql_log_file.
    ClumioType *string `json:"type"`
}

// MssqlDatabaseListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlDatabaseListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlDatabase `json:"items"`
}

// MssqlDatabaseListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlDatabaseListLinks struct {
    // The HATEOAS link to the first page of results.
    First                      *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last                       *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next                       *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev                       *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self                       *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateMssqlHostConnections *HateoasLink      `json:"create-mssql-host-connections"`
}

// MssqlDatabasePitrInterval represents a custom type struct
type MssqlDatabasePitrInterval struct {
    // End timestamp of the interval. Represented in RFC-3339 format.
    EndTimestamp   *string `json:"end_timestamp"`
    // Start timestamp of the interval. Represented in RFC-3339 format.
    StartTimestamp *string `json:"start_timestamp"`
}

// MssqlDatabasePitrIntervalListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlDatabasePitrIntervalListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlDatabasePitrInterval `json:"items"`
}

// MssqlDatabasePitrIntervalListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlDatabasePitrIntervalListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// MssqlHost represents a custom type struct
type MssqlHost struct {
    // Embedded responses related to the resource.
    Embedded                       *MssqlHostEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                          *MssqlHostLinks    `json:"_links"`
    // The user-provided endpoint of the host containing the given database.
    Endpoint                       *string            `json:"endpoint"`
    // The Clumio-assigned ID of the management group to which the host belongs.
    GroupId                        *string            `json:"group_id"`
    // Determines whether or not an availability group is present in the host.
    HasAssociatedAvailabilityGroup *bool              `json:"has_associated_availability_group"`
    // The Clumio-assigned ID of the Host.
    Id                             *string            `json:"id"`
    // The number of instances present in the host.
    InstanceCount                  *int64             `json:"instance_count"`
    // IsPartOfFCI is a boolean field representing if the Host is part of Failover Cluster
    IsPartOfFci                    *bool              `json:"is_part_of_fci"`
    // The Clumio-assigned ID of the organizational unit associated with the host.
    OrganizationalUnitId           *string            `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo                 *ProtectionInfo    `json:"protection_info"`
    // The status of the Host, Possible values include 'active' and 'inactive'.
    Status                         *string            `json:"status"`
    // The Clumio-assigned ID of the management subgroup to which the host belongs.
    SubgroupId                     *string            `json:"subgroup_id"`
}

// MssqlHostEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlHostEmbedded struct {
    // host level stats
    GetMssqlHostStats      interface{} `json:"get-mssql-host-stats"`
    // Embeds details about the management group if requested using the `embed` query.
    ReadManagementGroup    interface{} `json:"read-management-group"`
    // Embeds details about the management subgroup if requested using the `embed` query.
    ReadManagementSubgroup interface{} `json:"read-management-subgroup"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition   interface{} `json:"read-policy-definition"`
}

// MssqlHostLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlHostLinks struct {
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    GetMssqlHostStats      *HateoasLink                     `json:"get-mssql-host-stats"`
    // A HATEOAS link to protect the entities.
    ProtectEntities        *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadManagementGroup    *HateoasLink                     `json:"read-management-group"`
    // A resource-specific HATEOAS link.
    ReadManagementSubgroup *HateoasLink                     `json:"read-management-subgroup"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition   *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities      *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
}

// MssqlHostListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlHostListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlHost `json:"items"`
}

// MssqlHostListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlHostListLinks struct {
    // The HATEOAS link to the first page of results.
    First                      *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last                       *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next                       *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev                       *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self                       *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateMssqlHostConnections *HateoasLink      `json:"create-mssql-host-connections"`
}

// MssqlInstance represents a custom type struct
type MssqlInstance struct {
    // Embedded responses related to the resource.
    Embedded                       *MssqlInstanceEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                          *MssqlInstanceLinks    `json:"_links"`
    // The Clumio-assigned ID of the management group to which the host belongs.
    GroupId                        *string                `json:"group_id"`
    // The boolean value represents if availability group is present in the instance.
    HasAssociatedAvailabilityGroup *bool                  `json:"has_associated_availability_group"`
    // The user-provided endpoint of the host containing the given database.
    HostEndpoint                   *string                `json:"host_endpoint"`
    // The Clumio-assigned ID of the host, containing the instance.
    HostId                         *string                `json:"host_id"`
    // The Clumio-assigned ID of the Instance.
    Id                             *string                `json:"id"`
    // The Microsoft SQL assigned name of the instance.
    Name                           *string                `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the instance.
    OrganizationalUnitId           *string                `json:"organizational_unit_id"`
    // Product Version of the instance.
    ProductVersion                 *string                `json:"product_version"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo                 *ProtectionInfo        `json:"protection_info"`
    // The Microsoft SQL assigned server name of the instance.
    ServerName                     *string                `json:"server_name"`
    // The status of the Instance, Possible values include 'active' and 'inactive'.
    Status                         *string                `json:"status"`
    // The Clumio-assigned ID of the management subgroup to which the host belongs.
    SubgroupId                     *string                `json:"subgroup_id"`
}

// MssqlInstanceEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlInstanceEmbedded struct {
    // TODO: Add struct field description
    GetMssqlInstanceStats  interface{} `json:"get-mssql-instance-stats"`
    // Embeds details about the management group if requested using the `embed` query.
    ReadManagementGroup    interface{} `json:"read-management-group"`
    // Embeds details about the management subgroup if requested using the `embed` query.
    ReadManagementSubgroup interface{} `json:"read-management-subgroup"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition   interface{} `json:"read-policy-definition"`
}

// MssqlInstanceLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlInstanceLinks struct {
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    GetMssqlInstanceStats  *HateoasLink                     `json:"get-mssql-instance-stats"`
    // A HATEOAS link to protect the entities.
    ProtectEntities        *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadManagementGroup    *HateoasLink                     `json:"read-management-group"`
    // A resource-specific HATEOAS link.
    ReadManagementSubgroup *HateoasLink                     `json:"read-management-subgroup"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition   *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities      *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
}

// MssqlInstanceListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type MssqlInstanceListEmbedded struct {
    // TODO: Add struct field description
    Items []*MssqlInstance `json:"items"`
}

// MssqlInstanceListLinks represents a custom type struct.
// URLs to pages related to the resource.
type MssqlInstanceListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// MssqlPITROptions represents a custom type struct.
// A database and a point-in-time to be restored. Only one of `backup` or
// `pitr` should be specified.
type MssqlPITROptions struct {
    // The Clumio-assigned ID of the MSSQL database to be restored.
    // Use the [GET /datasources/mssql/databases](#operation/list-mssql-databases)
    // endpoint to fetch valid values.
    DatabaseId *string `json:"database_id"`
    // The point in time to be restored in RFC-3339 format.
    Timestamp  *string `json:"timestamp"`
}

// MssqlRestoreFromBackupOptions represents a custom type struct.
// The MSSQL database backup to be restored. Only one of `backup` or `pitr`
// should be specified.
type MssqlRestoreFromBackupOptions struct {
    // The Clumio-assigned ID of the backup to be restored.
    // Use the [GET /backups/mssql/databases](#operation/list-backup-mssql-databases)
    // endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// MssqlRestoreSource represents a custom type struct.
// The MSSQL database backup to be restored. Only one of `backup` or `pitr`
// should be set.
type MssqlRestoreSource struct {
    // The MSSQL database backup to be restored. Only one of `backup` or `pitr`
    // should be specified.
    Backup *MssqlRestoreFromBackupOptions `json:"backup"`
    // A database and a point-in-time to be restored. Only one of `backup` or
    // `pitr` should be specified.
    Pitr   *MssqlPITROptions              `json:"pitr"`
}

// MssqlRestoreTarget represents a custom type struct.
// The configuration of the MSSQL database to which the data has to be restored.
type MssqlRestoreTarget struct {
    // The target location within the instance to restore data files. For example,
    // `C:\\Programe Files\clumio\restored-data-files\`. If this field is empty, we
    // will restore data files into the same location as the source database.
    DataFilesPath *string `json:"data_files_path"`
    // The user-assigned name of the database.
    DatabaseName  *string `json:"database_name"`
    // The Clumio-assigned ID of the instance to restore the database into.
    // Use the [GET /datasources/mssql/instances](#operation/list-mssql-instances) to fetch valid values.
    InstanceId    *string `json:"instance_id"`
    // The target location within the instance to restore log files. For example,
    // `C:\\Programe Files\clumio\restored-log-files\`. If this field is empty, we
    // will restore log files into the same location as the source database.
    LogFilesPath  *string `json:"log_files_path"`
}

// OUGroupingCriteria represents a custom type struct.
// The grouping criteria for each datasource type.
// These can only be edited for datasource types which do not have any
// organizational units configured.
type OUGroupingCriteria struct {
    // The entity type used to group organizational units for AWS resources.
    Aws          *AwsDsGroupingCriteria    `json:"aws"`
    // The entity type used to group organizational units for Microsoft 365 resources.
    Microsoft365 *M365GroupingCriteria     `json:"microsoft365"`
    // The entity type used to group organizational units for VMware resources.
    Vmware       *VMwareDsGroupingCriteria `json:"vmware"`
}

// ObjectFilter represents a custom type struct.
// ObjectFilter
// defines which objects will be backed up.
type ObjectFilter struct {
    // Whether to back up only the latest object version.
    LatestVersionOnly *bool           `json:"latest_version_only"`
    // PrefixFilter
    PrefixFilters     []*PrefixFilter `json:"prefix_filters"`
    // Storage class to include in the backup. If not specified, then all objects across all storage
    // classes will be backed up. Valid values are: `S3 Standard`, `S3 Standard-IA`,
    // `S3 Intelligent-Tiering`, and `S3 One Zone-IA`.
    StorageClasses    []*string       `json:"storage_classes"`
}

// OnDemandDynamoDBBackupLinks represents a custom type struct.
// URLs to pages related to the resource.
type OnDemandDynamoDBBackupLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// OnDemandSetting represents a custom type struct.
// Settings for requesting on-demand backup directly.
type OnDemandSetting struct {
    // Additional operation-specific policy settings. For operation types which do not support additional settings, this field is `null`.
    AdvancedSettings  *PolicyAdvancedSettings  `json:"advanced_settings"`
    // Specifies the destination vault for AWS backups.
    BackupAwsRegion   *string                  `json:"backup_aws_region"`
    // The retention time for this SLA. For example, to retain the backup for 1 month, set `unit="months"` and `value=1`.
    RetentionDuration *RetentionBackupSLAParam `json:"retention_duration"`
}

// OrganizationalUnitLinks represents a custom type struct.
// URLs to pages related to the resource.
type OrganizationalUnitLinks struct {
    // The HATEOAS link to this resource.
    Self                     *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteOrganizationalUnit *HateoasLink     `json:"delete-organizational-unit"`
    // A resource-specific HATEOAS link.
    PatchOrganizationalUnit  *HateoasLink     `json:"patch-organizational-unit"`
    // A resource-specific HATEOAS link.
    ReadTask                 *HateoasLink     `json:"read-task"`
}

// OrganizationalUnitListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type OrganizationalUnitListEmbedded struct {
    // OrganizationalUnitWithETag to support etag string to be calculated
    Items []*OrganizationalUnitWithETag `json:"items"`
}

// OrganizationalUnitListLinks represents a custom type struct.
// URLs to pages related to the resource.
type OrganizationalUnitListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// OrganizationalUnitParentEntity represents a custom type struct.
// The parent object of the primary entity associated with the organizational unit. For example, "vmware_vcenter" is the parent entity of primary entity "vmware_vm_folder".
// The parent object is necessary for VMware entities and can be omitted for other data sources.
type OrganizationalUnitParentEntity struct {
    // The Clumio assigned ID of the entity.
    Id         *string `json:"id"`
    // The entity type.
    ClumioType *string `json:"type"`
}

// OrganizationalUnitPrimaryEntity represents a custom type struct.
// The primary object associated with the organizational unit. Examples of primary entities include "aws_environment" and "vmware_vm".
type OrganizationalUnitPrimaryEntity struct {
    // The Clumio assigned ID of the entity.
    Id         *string `json:"id"`
    // The entity type.
    ClumioType *string `json:"type"`
}

// OrganizationalUnitWithETag represents a custom type struct.
// OrganizationalUnitWithETag to support etag string to be calculated
type OrganizationalUnitWithETag struct {
    // Embedded responses related to the resource.
    Embedded                  *EntityGroupEmbedded     `json:"_embedded"`
    // ETag value
    Etag                      *string                  `json:"_etag"`
    // URLs to pages related to the resource.
    Links                     *OrganizationalUnitLinks `json:"_links"`
    // Number of immediate children of the organizational unit.
    ChildrenCount             *int64                   `json:"children_count"`
    // Datasource types configured in this organizational unit. Possible values include `aws`, `microsoft365`, `vmware`, or `mssql`.
    ConfiguredDatasourceTypes []*string                `json:"configured_datasource_types"`
    // List of all recursive descendant organizational units of this OU.
    DescendantIds             []*string                `json:"descendant_ids"`
    // A description of the organizational unit.
    Description               *string                  `json:"description"`
    // The Clumio assigned ID of the organizational unit.
    Id                        *string                  `json:"id"`
    // Unique name assigned to the organizational unit.
    Name                      *string                  `json:"name"`
    // The Clumio assigned ID of the parent organizational unit.
    // The parent organizational unit contains the entities in this organizational unit and can update this organizational unit.
    // If this organizational unit is the global organizational unit, then this field has a value of `null`.
    ParentId                  *string                  `json:"parent_id"`
    // Number of users to whom this organizational unit or any of its descendants have been assigned.
    UserCount                 *int64                   `json:"user_count"`
    // Users IDs to whom the organizational unit has been assigned.
    // This attribute will be available when reading a single OU and not when listing OUs.
    Users                     []*string                `json:"users"`
}

// PermissionModel represents a custom type struct
type PermissionModel struct {
    // Description of the permission.
    Description *string `json:"description"`
    // The Clumio-assigned ID of the permission.
    Id          *string `json:"id"`
    // Name of the permission.
    // The following table lists the supported permissions for a role:
    // 
    // +----------------------------------------------------+-------------------------+
    // |                  Permission Name                   | Full/Partial Applicable |
    // +====================================================+=========================+
    // | Policy Management                                  | Yes                     |
    // +----------------------------------------------------+-------------------------+
    // | Data Source Management                             | Yes                     |
    // +----------------------------------------------------+-------------------------+
    // | Perform Backup (Scheduled or On-demand)            | Yes                     |
    // +----------------------------------------------------+-------------------------+
    // | Regular Restore                                    | No                      |
    // +----------------------------------------------------+-------------------------+
    // | Redirected Granular Restore (things like GRR &     | Yes                     |
    // | content download)                                  |                         |
    // +----------------------------------------------------+-------------------------+
    // | Dashboards & Reports                               | Yes                     |
    // +----------------------------------------------------+-------------------------+
    // | Some Admin Functions (User mgmt, SSO/MFA, IP       | No                      |
    // | Allow, Password expiry, OU, KMS)                   |                         |
    // +----------------------------------------------------+-------------------------+
    // | Other Admin Functions (API Tokens, Tasks, Alerts   | Yes                     |
    // | and Audit Logs)                                    |                         |
    // +----------------------------------------------------+-------------------------+
    // 
    Name        *string `json:"name"`
}

// Policy represents a custom type struct
type Policy struct {
    // If the `embed` query parameter is set, displays the responses of the related resource,
    // as defined by the embeddable link specified.
    Embedded             *PolicyEmbedded    `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *PolicyLinks       `json:"_links"`
    // The status of the policy.
    // Refer to the Policy Activation Status table for a complete list of policy statuses.
    ActivationStatus     *string            `json:"activation_status"`
    // The created time of the policy in unix time.
    CreatedTime          *int64             `json:"created_time"`
    // The Clumio-assigned ID of the policy.
    Id                   *string            `json:"id"`
    // The following table describes the possible lock statuses of a policy.
    // 
    // +----------+-------------------------------------------------------------------+
    // |  Status  |                            Description                            |
    // +==========+===================================================================+
    // | unlocked | Policies are unlocked until an update or deletion task is queued. |
    // +----------+-------------------------------------------------------------------+
    // | updating | During a policy edit, concurrent edits or deletion requests will  |
    // |          | be rejected.                                                      |
    // +----------+-------------------------------------------------------------------+
    // | deleting | During policy deletion, concurrent edits or deletion requests     |
    // |          | will be rejected.                                                 |
    // +----------+-------------------------------------------------------------------+
    // 
    LockStatus           *string            `json:"lock_status"`
    // The user-provided name of the policy.
    Name                 *string            `json:"name"`
    // TODO: Add struct field description
    Operations           []*PolicyOperation `json:"operations"`
    // The Clumio-assigned ID of the organizational unit associated with the policy.
    OrganizationalUnitId *string            `json:"organizational_unit_id"`
    // The timezone for the policy.
    Timezone             *string            `json:"timezone"`
    // The updated time of the policy in unix time.
    UpdatedTime          *int64             `json:"updated_time"`
}

// PolicyAdvancedSettings represents a custom type struct.
// Additional operation-specific policy settings. For operation types which do not support additional settings, this field is `null`.
type PolicyAdvancedSettings struct {
    // Backup tier to store the backup in. Valid values are: (empty) equivalent to standard, `standard`, and `lite`.
    AwsEbsVolumeBackup     *EBSBackupAdvancedSetting             `json:"aws_ebs_volume_backup"`
    // Backup tier to store the backup in. Valid values are: (empty) equivalent to standard, `standard`, and `lite`.
    AwsEc2InstanceBackup   *EC2BackupAdvancedSetting             `json:"aws_ec2_instance_backup"`
    // Additional policy configuration settings for the `mssql_database_backup` operation. If this operation is not of type `mssql_database_backup`, then this field is omitted from the response.
    Ec2MssqlDatabaseBackup *MSSQLDatabaseBackupAdvancedSetting   `json:"ec2_mssql_database_backup"`
    // Additional policy configuration settings for the `mssql_log_backup` operation. If this operation is not of type `mssql_log_backup`, then this field is omitted from the response.
    Ec2MssqlLogBackup      *MSSQLLogBackupAdvancedSetting        `json:"ec2_mssql_log_backup"`
    // Additional policy configuration settings for the `mssql_database_backup` operation. If this operation is not of type `mssql_database_backup`, then this field is omitted from the response.
    MssqlDatabaseBackup    *MSSQLDatabaseBackupAdvancedSetting   `json:"mssql_database_backup"`
    // Additional policy configuration settings for the `mssql_log_backup` operation. If this operation is not of type `mssql_log_backup`, then this field is omitted from the response.
    MssqlLogBackup         *MSSQLLogBackupAdvancedSetting        `json:"mssql_log_backup"`
    // Additional policy configuration settings for the `protection_group_backup` operation. If this operation is not of type `protection_group_backup`, then this field is omitted from the response.
    ProtectionGroupBackup  *ProtectionGroupBackupAdvancedSetting `json:"protection_group_backup"`
}

// PolicyEmbedded represents a custom type struct.
// If the `embed` query parameter is set, displays the responses of the related resource,
// as defined by the embeddable link specified.
type PolicyEmbedded struct {
    // Embeds the EBS compliance statistics into the response.
    ReadPolicyAwsEbsVolumesComplianceStats interface{} `json:"read-policy-aws-ebs-volumes-compliance-stats"`
    // Embeds the VM compliance statisticss into the response.
    ReadPolicyVmwareVmsComplianceStats     interface{} `json:"read-policy-vmware-vms-compliance-stats"`
}

// PolicyLinks represents a custom type struct.
// URLs to pages related to the resource.
type PolicyLinks struct {
    // The HATEOAS link to this resource.
    Self                                   *HateoasSelfLink            `json:"_self"`
    // A resource-specific HATEOAS link.
    DeletePolicyDefinition                 *HateoasLink                `json:"delete-policy-definition"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                        *ProtectEntitiesHateoasLink `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadPolicyAwsEbsVolumesComplianceStats *HateoasLink                `json:"read-policy-aws-ebs-volumes-compliance-stats"`
    // A resource-specific HATEOAS link.
    ReadPolicyVmwareVmsComplianceStats     *HateoasLink                `json:"read-policy-vmware-vms-compliance-stats"`
    // A resource-specific HATEOAS link.
    UpdatePolicyDefinition                 *HateoasLink                `json:"update-policy-definition"`
}

// PolicyListEmbedded represents a custom type struct.
// An array of embedded resources related to this resource.
type PolicyListEmbedded struct {
    // TODO: Add struct field description
    Items []*Policy `json:"items"`
}

// PolicyListLinks represents a custom type struct.
// URLs to pages related to the resource.
type PolicyListLinks struct {
    // The HATEOAS link to the first page of results.
    First                  *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next                   *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreatePolicyDefinition *HateoasLink      `json:"create-policy-definition"`
}

// PolicyOperation represents a custom type struct
type PolicyOperation struct {
    // Determines whether the protection policy should take action now or during the specified backup window.
    // If set to `immediate`, Clumio starts the backup process right away. If set to `window`, Clumio starts the backup process when the backup window (`backup_window`) opens.
    // If set to `window` and `operation in ("aws_rds_resource_aws_snapshot", "mssql_log_backup", "ec2_mssql_log_backup")`,
    // the backup window will not be determined by Clumio's backup window.
    ActionSetting     *string                 `json:"action_setting"`
    // Additional operation-specific policy settings. For operation types which do not support additional settings, this field is `null`.
    AdvancedSettings  *PolicyAdvancedSettings `json:"advanced_settings"`
    // The start and end times of the customized backup window. Use of `backup_window` is deprecated, use `backup_window_tz` instead.
    BackupWindow      *BackupWindow           `json:"backup_window"`
    // The start and end times of the customized backup window. Use of `backup_window` is deprecated, use `backup_window_tz` instead.
    BackupWindowTz    *BackupWindow           `json:"backup_window_tz"`
    // The next start time of this operation in unix time.
    NextStartTime     *int64                  `json:"next_start_time"`
    // The previous start time of this operation in unix time.
    PreviousStartTime *int64                  `json:"previous_start_time"`
    // backup_sla captures the SLA parameters
    // backup_sla captures the SLA parameters
    Slas              []*BackupSLA            `json:"slas"`
    // The operation to be performed for this SLA set. Each SLA set corresponds to one and only one operation.
    // Refer to the Policy Operation table for a complete list of policy operations.
    ClumioType        *string                 `json:"type"`
}

// PolicyOperationInput represents a custom type struct
type PolicyOperationInput struct {
    // Determines whether the protection policy should take action now or during the specified backup window.
    // If set to `immediate`, Clumio starts the backup process right away. If set to `window`, Clumio starts the backup process when the backup window (`backup_window`) opens.
    // If set to `window` and `operation in ("aws_rds_resource_aws_snapshot", "mssql_log_backup", "ec2_mssql_log_backup")`,
    // the backup window will not be determined by Clumio's backup window.
    ActionSetting    *string                 `json:"action_setting"`
    // Additional operation-specific policy settings. For operation types which do not support additional settings, this field is `null`.
    AdvancedSettings *PolicyAdvancedSettings `json:"advanced_settings"`
    // The start and end times of the customized backup window. Use of `backup_window` is deprecated, use `backup_window_tz` instead.
    BackupWindow     *BackupWindow           `json:"backup_window"`
    // The start and end times of the customized backup window. Use of `backup_window` is deprecated, use `backup_window_tz` instead.
    BackupWindowTz   *BackupWindow           `json:"backup_window_tz"`
    // backup_sla captures the SLA parameters
    // backup_sla captures the SLA parameters
    Slas             []*BackupSLA            `json:"slas"`
    // The operation to be performed for this SLA set. Each SLA set corresponds to one and only one operation.
    // Refer to the Policy Operation table for a complete list of policy operations.
    ClumioType       *string                 `json:"type"`
}

// PrefixFilter represents a custom type struct.
// PrefixFilter
type PrefixFilter struct {
    // List of subprefixes to exclude from the prefix.
    ExcludedSubPrefixes []*string `json:"excluded_sub_prefixes"`
    // Prefix to include.
    Prefix              *string   `json:"prefix"`
}

// Projection represents a custom type struct.
// Represents attributes that are copied (projected) from the table into an index. These are in addition to the
// primary key attributes and index key attributes, which are automatically projected.
type Projection struct {
    // Represents the non-key attribute names which will be projected into the index.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this must be empty if
    // 'projection_type' is ALL or KEYS_ONLY, and non-empty if 'projection_type' is INCLUDE.
    NonKeyAttributes []*string `json:"non_key_attributes"`
    // The set of attributes that are projected into the index. Valid Values: ALL, KEYS_ONLY, INCLUDE.
    ProjectionType   *string   `json:"projection_type"`
}

// ProtectConfig represents a custom type struct.
// The configuration of the Clumio Cloud Protect product for this connection.
// If this connection is not configured for Clumio Cloud Protect, then this field has a
// value of `null`.
type ProtectConfig struct {
    // The asset types supported on the current version of the feature
    AssetTypesEnabled        []*string     `json:"asset_types_enabled"`
    // TODO: Add struct field description
    Ebs                      *EbsAssetInfo `json:"ebs"`
    // The current version of the feature.
    InstalledTemplateVersion *string       `json:"installed_template_version"`
    // TODO: Add struct field description
    Rds                      *RdsAssetInfo `json:"rds"`
}

// ProtectEntitiesHateoasLink represents a custom type struct.
// A HATEOAS link to protect the entities.
type ProtectEntitiesHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// ProtectTemplateConfig represents a custom type struct
type ProtectTemplateConfig struct {
    // The asset types for which the template is to be generated. Possible
    // asset types are ["EBS", "RDS", "DynamoDB", "EC2MSSQL"].
    AssetTypesEnabled []*string `json:"asset_types_enabled"`
}

// ProtectTemplateInfo represents a custom type struct.
// The latest available CloudFormation template for Clumio Cloud Protect.
type ProtectTemplateInfo struct {
    // The AWS asset types supported with the available version of the template.
    AssetTypesEnabled        []*string        `json:"asset_types_enabled"`
    // The latest available URL for the template.
    AvailableTemplateUrl     *string          `json:"available_template_url"`
    // The latest available version for the template.
    AvailableTemplateVersion *string          `json:"available_template_version"`
    // TODO: Add struct field description
    Ebs                      *EbsTemplateInfo `json:"ebs"`
    // TODO: Add struct field description
    Rds                      *RdsTemplateInfo `json:"rds"`
}

// ProtectTemplateInfoV2 represents a custom type struct
type ProtectTemplateInfoV2 struct {
    // The AWS asset types supported with the available version of the template.
    AssetTypesEnabled        []*string        `json:"asset_types_enabled"`
    // The latest available version for the template.
    AvailableTemplateVersion *string          `json:"available_template_version"`
    // TODO: Add struct field description
    Ebs                      *EbsTemplateInfo `json:"ebs"`
    // TODO: Add struct field description
    Rds                      *RdsTemplateInfo `json:"rds"`
}

// ProtectedStatsDeprecated represents a custom type struct.
// ProtectedStatsDeprecated contains the compliance stats for policies which are protected along with
// the unprotected policies count
type ProtectedStatsDeprecated struct {
    // ComplianceStatsDeprecated denotes compliance metrics for all entities associated with a given type
    Protected   *ComplianceStatsDeprecated `json:"protected"`
    // Unprotected count.
    Unprotected *uint32                    `json:"unprotected"`
}

// ProtectionComplianceStatsWithSeeding represents a custom type struct.
// The compliance statistics of workloads associated with this entity.
type ProtectionComplianceStatsWithSeeding struct {
    // The total number of compliant entities.
    CompliantCount     *int64 `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64 `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool  `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64 `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64 `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64 `json:"unprotected_count"`
}

// ProtectionGroup represents a custom type struct
type ProtectionGroup struct {
    // Embedded responses related to the resource.
    Embedded                      *ProtectionGroupEmbedded              `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                         *ProtectionGroupLinks                 `json:"_links"`
    // Number of buckets
    BucketCount                   *int64                                `json:"bucket_count"`
    // The following table describes the possible conditions for a bucket to be
    // automatically added to a protection group.
    // 
    // +---------+----------------+---------------------------------------------------+
    // |  Field  | Rule Condition |                    Description                    |
    // +=========+================+===================================================+
    // | aws_tag | $eq            | Denotes the AWS tag(s) to conditionalize on       |
    // |         |                |                                                   |
    // |         |                | {"aws_tag":{"$eq":{"key":"Environment",           |
    // |         |                | "value":"Prod"}}}                                 |
    // |         |                |                                                   |
    // |         |                |                                                   |
    // +---------+----------------+---------------------------------------------------+
    // 
    BucketRule                    *string                               `json:"bucket_rule"`
    // The compliance statistics of workloads associated with this entity.
    ComplianceStats               *ProtectionComplianceStatsWithSeeding `json:"compliance_stats"`
    // The compliance status of the protected protection group. Possible values include
    // "compliant" and "noncompliant". If the table is not protected, then this field has
    // a value of `null`.
    ComplianceStatus              *string                               `json:"compliance_status"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string                               `json:"created_timestamp"`
    // The user-assigned description of the protection group.
    Description                   *string                               `json:"description"`
    // The Clumio-assigned ID of the protection group.
    Id                            *string                               `json:"id"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string                               `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string                               `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string                               `json:"last_discover_sync_timestamp"`
    // Modified time of the protection group in RFC-3339 format.
    ModifiedTimestamp             *string                               `json:"modified_timestamp"`
    // The user-assigned name of the protection group.
    Name                          *string                               `json:"name"`
    // ObjectFilter
    // defines which objects will be backed up.
    ObjectFilter                  *ObjectFilter                         `json:"object_filter"`
    // The Clumio-assigned ID of the organizational unit associated with the Protection Group.
    OrganizationalUnitId          *string                               `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo                *ProtectionInfoWithRule               `json:"protection_info"`
    // The protection status of the protection group. Possible values include "protected",
    // "unprotected", and "unsupported". If the protection group does not support backups, then
    // this field has a value of `unsupported`.
    ProtectionStatus              *string                               `json:"protection_status"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64                                `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64                                `json:"total_backed_up_size_bytes"`
    // Version of the protection group. The version number is incremented every time
    // a change is made to the protection group.
    Version                       *int64                                `json:"version"`
}

// ProtectionGroupBackup represents a custom type struct
type ProtectionGroupBackup struct {
    // URLs to pages related to the resource.
    Links                  *ProtectionGroupBackupLinks `json:"_links"`
    // The number of objects in the protection group that were successfully backed up.
    BackedUpObjectCount    *int64                      `json:"backed_up_object_count"`
    // The total size in bytes of objects in the protection group that were
    // successfully backed up.
    BackedUpSizeBytes      *int64                      `json:"backed_up_size_bytes"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp    *string                     `json:"expiration_timestamp"`
    // The number of objects in the protection group that failed to be backed up.
    FailedObjectCount      *int64                      `json:"failed_object_count"`
    // The total size in bytes of objects in the protection group that failed
    // to be backed up.
    FailedSizeBytes        *int64                      `json:"failed_size_bytes"`
    // The Clumio-assigned ID of the protection group backup.
    Id                     *string                     `json:"id"`
    // The Clumio-assigned ID of the protection group.
    ProtectionGroupId      *string                     `json:"protection_group_id"`
    // The user-assigned name of the protection group.
    ProtectionGroupName    *string                     `json:"protection_group_name"`
    // The version of the protection group at the time the backup was taken.
    ProtectionGroupVersion *int64                      `json:"protection_group_version"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp         *string                     `json:"start_timestamp"`
    // The type of backup. Possible values include `protection_group_backup`.
    ClumioType             *string                     `json:"type"`
}

// ProtectionGroupBackupAdvancedSetting represents a custom type struct.
// Additional policy configuration settings for the `protection_group_backup` operation. If this operation is not of type `protection_group_backup`, then this field is omitted from the response.
type ProtectionGroupBackupAdvancedSetting struct {
    // Backup tier to store the backup in. Valid values are: `cold`, `frozen`
    BackupTier *string `json:"backup_tier"`
}

// ProtectionGroupBackupLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupBackupLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ProtectionGroupBackupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ProtectionGroupBackupListEmbedded struct {
    // TODO: Add struct field description
    Items []*ProtectionGroupBackup `json:"items"`
}

// ProtectionGroupBackupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupBackupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ProtectionGroupBucket represents a custom type struct
type ProtectionGroupBucket struct {
    // TODO: Add struct field description
    Embedded                      *ProtectionGroupBucketEmbedded `json:"_embedded"`
    // TODO: Add struct field description
    Links                         *ProtectionGroupBucketLinks    `json:"_links"`
    // The AWS-assigned ID of the account associated with the DynamoDB table.
    AccountNativeId               *string                        `json:"account_native_id"`
    // Whether this bucket was added to this protection group by the bucket rule
    AddedByBucketRule             *bool                          `json:"added_by_bucket_rule"`
    // Whether this bucket was added to this protection group by the user
    AddedByUser                   *bool                          `json:"added_by_user"`
    // The AWS region associated with the DynamoDB table.
    AwsRegion                     *string                        `json:"aws_region"`
    // The Clumio-assigned ID of the bucket
    BucketId                      *string                        `json:"bucket_id"`
    // The name of the bucket
    BucketName                    *string                        `json:"bucket_name"`
    // The compliance status of the protected protection group. Possible values include
    // "compliant" and "noncompliant". If the table is not protected, then this field has
    // a value of `null`.
    ComplianceStatus              *string                        `json:"compliance_status"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string                        `json:"created_timestamp"`
    // The Clumio-assigned ID of the AWS environment associated with the protection group.
    EnvironmentId                 *string                        `json:"environment_id"`
    // The Clumio-assigned ID of the protection group
    GroupId                       *string                        `json:"group_id"`
    // The name of the protection group
    GroupName                     *string                        `json:"group_name"`
    // The Clumio-assigned ID that represents the bucket within the protection group.
    Id                            *string                        `json:"id"`
    // Determines whether the protection group bucket has been deleted
    IsDeleted                     *bool                          `json:"is_deleted"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string                        `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string                        `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string                        `json:"last_discover_sync_timestamp"`
    // The Clumio-assigned ID of the organizational unit associated with the protection group.
    OrganizationalUnitId          *string                        `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo                *ProtectionInfoWithRule        `json:"protection_info"`
    // The protection status of the protection group. Possible values include "protected",
    // "unprotected", and "unsupported". If the protection group does not support backups, then
    // this field has a value of `unsupported`.
    ProtectionStatus              *string                        `json:"protection_status"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64                         `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64                         `json:"total_backed_up_size_bytes"`
}

// ProtectionGroupBucketEmbedded represents a custom type struct
type ProtectionGroupBucketEmbedded struct {
    // This embed is for internal use only since an embed results in additional HTTP
    // calls. "embeds" can affect the performance of "list" API calls as an embed is
    // processed once per item in the result list.
    ReadOrganizationalUnit interface{} `json:"read-organizational-unit"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition   interface{} `json:"read-policy-definition"`
}

// ProtectionGroupBucketLinks represents a custom type struct
type ProtectionGroupBucketLinks struct {
    // The HATEOAS link to this resource.
    Self                        *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteBucketProtectionGroup *HateoasLink                     `json:"delete-bucket-protection-group"`
    // A resource-specific HATEOAS link.
    ReadOrganizationalUnit      *HateoasLink                     `json:"read-organizational-unit"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition        *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
}

// ProtectionGroupBucketListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ProtectionGroupBucketListEmbedded struct {
    // TODO: Add struct field description
    Items []*ProtectionGroupBucket `json:"items"`
}

// ProtectionGroupBucketListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupBucketListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ProtectionGroupEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ProtectionGroupEmbedded struct {
    // This embed is for internal use only since an embed results in additional HTTP
    // calls. "embeds" can affect the performance of "list" API calls as an embed is
    // processed once per item in the result list.
    ReadOrganizationalUnit interface{} `json:"read-organizational-unit"`
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition   interface{} `json:"read-policy-definition"`
}

// ProtectionGroupLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupLinks struct {
    // The HATEOAS link to this resource.
    Self                        *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    AddBucketProtectionGroup    *HateoasLink                     `json:"add-bucket-protection-group"`
    // A resource-specific HATEOAS link.
    DeleteBucketProtectionGroup *HateoasLink                     `json:"delete-bucket-protection-group"`
    // A HATEOAS link to protect the entities.
    ProtectEntities             *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A resource-specific HATEOAS link.
    ReadOrganizationalUnit      *HateoasLink                     `json:"read-organizational-unit"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition        *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities           *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
    // A resource-specific HATEOAS link.
    UpdateProtectionGroup       *HateoasLink                     `json:"update-protection-group"`
}

// ProtectionGroupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ProtectionGroupListEmbedded struct {
    // TODO: Add struct field description
    Items []*ProtectionGroup `json:"items"`
}

// ProtectionGroupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ProtectionGroupRestoreSource represents a custom type struct.
// The parameters for initiating a protection group restore from a backup.
type ProtectionGroupRestoreSource struct {
    // The Clumio-assigned ID of the protection group backup to be restored. Use the
    // [GET /backups/protection-groups](#operation/list-backup-protection-groups)
    // endpoint to fetch valid values. 
    BackupId                  *string              `json:"backup_id"`
    // Search for or restore only objects that pass the source object filter.
    ObjectFilters             *SourceObjectFilters `json:"object_filters"`
    // A list of Clumio-assigned IDs of protection group S3 assets, representing the
    // buckets within the protection group to restore from. Use the
    // [GET /datasources/protection-groups/s3-assets](#operation/list-protection-group-s3-assets)
    // endpoint to fetch valid values.
    ProtectionGroupS3AssetIds []*string            `json:"protection_group_s3_asset_ids"`
}

// ProtectionGroupRestoreTarget represents a custom type struct.
// The destination where the protection group will be restored.
type ProtectionGroupRestoreTarget struct {
    // The Clumio-assigned ID of the bucket to which the backup must be restored.
    // Use the [GET /datasources/aws/s3-buckets](#operation/list-aws-s3-buckets) endpoint
    // to fetch valid values.
    BucketId                    *string              `json:"bucket_id"`
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/s3-buckets/{bucket_id}](#operation/read-aws-s3-bucket) endpoint
    // to fetch the environment ID for a bucket.
    EnvironmentId               *string              `json:"environment_id"`
    // If overwrite is set to true, we will overwrite an object if it exists. If it's set to false,
    // then we will fail the restore if an object already exists.
    Overwrite                   *bool                `json:"overwrite"`
    // Prefix to restore the objects under. If more than one bucket is restored, the
    // bucket name will be appended to the prefix.
    Prefix                      *string              `json:"prefix"`
    // Whether to restore objects with their original storage class or not. 
    // If it is `true`, `storage_class` must be empty.
    // Otherwise, `storage_class` must be given.
    RestoreOriginalStorageClass *bool                `json:"restore_original_storage_class"`
    // Storage class for restored objects. Valid values are: `S3 Standard`, `S3 Standard-IA`,
    // `S3 Intelligent-Tiering` and `S3 One Zone-IA`. 
    // Note that this must be given unless `restore_original_storage_class` is `true`.
    StorageClass                *string              `json:"storage_class"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                        []*AwsTagCommonModel `json:"tags"`
}

// ProtectionGroupS3AssetBackup represents a custom type struct
type ProtectionGroupS3AssetBackup struct {
    // URLs to pages related to the resource.
    Links                    *ProtectionGroupS3AssetBackupLinks `json:"_links"`
    // The number of objects in the protection group S3 asset that were successfully backed up.
    BackedUpObjectCount      *uint64                            `json:"backed_up_object_count"`
    // The total size in bytes of objects in the protection group S3 asset that were
    // successfully backed up.
    BackedUpSizeBytes        *uint64                            `json:"backed_up_size_bytes"`
    // The Clumio-assigned ID of the bucket.
    BucketId                 *string                            `json:"bucket_id"`
    // The name of the bucket.
    BucketName               *string                            `json:"bucket_name"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp      *string                            `json:"expiration_timestamp"`
    // The number of objects in the protection group S3 asset that failed to be backed up.
    FailedObjectCount        *uint64                            `json:"failed_object_count"`
    // The total size in bytes of objects in the protection group S3 asset that failed
    // to be backed up.
    FailedSizeBytes          *uint64                            `json:"failed_size_bytes"`
    // The Clumio-assigned ID of the protection group S3 asset backup.
    Id                       *string                            `json:"id"`
    // The Clumio-assigned ID of the protection group.
    ProtectionGroupId        *string                            `json:"protection_group_id"`
    // The Clumio-assigned ID of the protection group S3 asset.
    ProtectionGroupS3AssetId *string                            `json:"protection_group_s3_asset_id"`
    // The version of the protection group at the time the backup was taken.
    ProtectionGroupVersion   *int64                             `json:"protection_group_version"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp           *string                            `json:"start_timestamp"`
    // The type of backup. Possible values include `protection_group_s3_asset_backup`.
    ClumioType               *string                            `json:"type"`
}

// ProtectionGroupS3AssetBackupLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupS3AssetBackupLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ProtectionGroupS3AssetBackupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ProtectionGroupS3AssetBackupListEmbedded struct {
    // TODO: Add struct field description
    Items []*ProtectionGroupS3AssetBackup `json:"items"`
}

// ProtectionGroupS3AssetBackupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupS3AssetBackupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ProtectionGroupS3AssetRestoreSource represents a custom type struct.
// The parameters for initiating a protection group S3 asset restore from a backup.
type ProtectionGroupS3AssetRestoreSource struct {
    // The Clumio-assigned ID of the protection group S3 asset backup to be restored. Use the
    // [GET /backups/protection-groups/s3-assets](#operation/list-backup-protection-group-s3-assets)
    // endpoint to fetch valid values. 
    BackupId      *string              `json:"backup_id"`
    // Search for or restore only objects that pass the source object filter.
    ObjectFilters *SourceObjectFilters `json:"object_filters"`
}

// ProtectionGroupVersionLinks represents a custom type struct.
// URLs to pages related to the resource.
type ProtectionGroupVersionLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ProtectionInfo represents a custom type struct.
// The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
type ProtectionInfo struct {
    // The ID of the entity from which protection was inherited.
    // If protection was not inherited, then this field has a value of `null`.
    InheritingEntityId   *string `json:"inheriting_entity_id"`
    // The type of entity from which protection was inherited.
    // If protection was not inherited, then this field has a value of `null`.
    // Entities from which protection can be inherited include the following:
    // 
    // +--------------------------------+---------------------------------+
    // |     Inheriting Entity Type     |             Details             |
    // +================================+=================================+
    // | aws_tag                        | AWS tag.                        |
    // +--------------------------------+---------------------------------+
    // | vmware_vm_folder               | VMware VM folder.               |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter              | VMware data center.             |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter_folder       | VMware data center folder.      |
    // +--------------------------------+---------------------------------+
    // | vmware_tag                     | VMware tag.                     |
    // +--------------------------------+---------------------------------+
    // | vmware_category                | VMware tag category.            |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource        | VMware compute resource.        |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource_folder | VMware compute resource folder. |
    // +--------------------------------+---------------------------------+
    // 
    InheritingEntityType *string `json:"inheriting_entity_type"`
    // A system-generated ID assigned to the policy protecting this resource.
    PolicyId             *string `json:"policy_id"`
}

// ProtectionInfoDeprecated represents a custom type struct
type ProtectionInfoDeprecated struct {
    // TODO: Add struct field description
    Inheritedfrom *InheritedFrom `json:"inheritedFrom"`
    // PolicyID for the policy.
    Policyid      *string        `json:"policyId"`
}

// ProtectionInfoWithRule represents a custom type struct.
// The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
type ProtectionInfoWithRule struct {
    // The ID of the entity from which protection was inherited.
    // If protection was not inherited, then this field has a value of `null`.
    InheritingEntityId   *string `json:"inheriting_entity_id"`
    // The type of entity from which protection was inherited.
    // If protection was not inherited, then this field has a value of `null`.
    // Entities from which protection can be inherited include the following:
    // 
    // +--------------------------------+---------------------------------+
    // |     Inheriting Entity Type     |             Details             |
    // +================================+=================================+
    // | aws_tag                        | AWS tag.                        |
    // +--------------------------------+---------------------------------+
    // | vmware_vm_folder               | VMware VM folder.               |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter              | VMware data center.             |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter_folder       | VMware data center folder.      |
    // +--------------------------------+---------------------------------+
    // | vmware_tag                     | VMware tag.                     |
    // +--------------------------------+---------------------------------+
    // | vmware_category                | VMware tag category.            |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource        | VMware compute resource.        |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource_folder | VMware compute resource folder. |
    // +--------------------------------+---------------------------------+
    // 
    InheritingEntityType *string `json:"inheriting_entity_type"`
    // A system-generated ID assigned to the policy protecting this resource.
    PolicyId             *string `json:"policy_id"`
}

// ProvisionedThroughput represents a custom type struct.
// Represents the provisioned throughput settings for a DynamoDB table.
type ProvisionedThroughput struct {
    // The maximum number of strongly consistent reads consumed per second.
    ReadCapacityUnits  *int64 `json:"read_capacity_units"`
    // The maximum number of writes consumed per second.
    WriteCapacityUnits *int64 `json:"write_capacity_units"`
}

// ProvisionedThroughputOverride represents a custom type struct.
// Replica-specific provisioned throughput settings. If not specified, uses the source table's provisioned throughput settings.
type ProvisionedThroughputOverride struct {
    // The maximum number of strongly consistent reads consumed per second.
    ReadCapacityUnits *int64 `json:"read_capacity_units"`
}

// RDSDatabaseTableColumn represents a custom type struct.
// RDSDatabaseTableColumn denotes the model for rds database column
type RDSDatabaseTableColumn struct {
    // The name of the column.
    Name       *string `json:"name"`
    // The Hive data type of the column. Possible values include `int`, `bigint`, `string`, and `boolean`.
    ClumioType *string `json:"type"`
}

// RDSLogicalPreviewQueryResult represents a custom type struct.
// The preview of the query result, if `preview:true` in the request.
// If preview was not set to true in the request, then the result of the query will be
// available for download asynchronously.
type RDSLogicalPreviewQueryResult struct {
    // RDSDatabaseTableColumn denotes the model for rds database column
    Columns []*RDSDatabaseTableColumn `json:"columns"`
    // The rows of the previewed query result.
    Rows    []*[]string               `json:"rows"`
}

// RPOBackupSLAParam represents a custom type struct.
// The minimum frequency between backups for this SLA. Also known as the recovery point objective (RPO) interval.
// For example, to configure the minimum frequency between backups to be every 2 days, set `unit="days"` and `value=2`.
// To configure the SLA for on-demand backups, set `unit="on_demand"` and leave the `value` field empty.
type RPOBackupSLAParam struct {
    // The measurement unit of the SLA parameter. Values include `hours`, `days`, `months`, and `years`.
    Unit  *string `json:"unit"`
    // The measurement value of the SLA parameter.
    Value *int64  `json:"value"`
}

// RdsAssetInfo represents a custom type struct
type RdsAssetInfo struct {
    // The current version of the feature.
    InstalledTemplateVersion *string `json:"installed_template_version"`
}

// RdsResourceRestoreSource represents a custom type struct.
// The RDS resource backup or snapshot to be restored.  Only one of these fields should be set.
type RdsResourceRestoreSource struct {
    // The parameters for initiating an RDS restore from a backup.
    Backup   *RdsResourceRestoreSourceAirGapOptions `json:"backup"`
    // The parameters for initiating an RDS restore from a snapshot.
    Snapshot *RdsResourceRestoreSourcePitrOptions   `json:"snapshot"`
}

// RdsResourceRestoreSourceAirGapOptions represents a custom type struct.
// The parameters for initiating an RDS restore from a backup.
type RdsResourceRestoreSourceAirGapOptions struct {
    // The Clumio-assigned ID of the RDS backup to be restored.
    // Use the [GET /backups/aws/rds-resources](#operation/list-backup-aws-rds-resources)
    // endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// RdsResourceRestoreSourcePitrOptions represents a custom type struct.
// The parameters for initiating an RDS restore from a snapshot.
type RdsResourceRestoreSourcePitrOptions struct {
    // The Clumio-assigned ID of the RDS resource to be restored.
    // Use the [GET /datasources/aws/rds-resources](#operation/list-aws-rds-resources)
    // endpoint to fetch valid values.
    ResourceId *string `json:"resource_id"`
    // A point in time to be restored in RFC-3339 format.
    Timestamp  *string `json:"timestamp"`
}

// RdsResourceRestoreTarget represents a custom type struct.
// The configuration of the RDS resource to be restored.
type RdsResourceRestoreTarget struct {
    // The Clumio-assigned ID of the AWS environment to be used as the restore destination.
    // Use the [GET /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.
    EnvironmentId          *string              `json:"environment_id"`
    // The instance class of the RDS resources to be created. Possible values include `db.r5.2xlarge` and `db.t2.small`.
    InstanceClass          *string              `json:"instance_class"`
    // Designates whether the restored RDS resource also has a public IP address in addition to the private IP address.
    IsPubliclyAccessible   *bool                `json:"is_publicly_accessible"`
    // The AWS-assigned ID of the KMS encryption key used to encrypt data in this RDS resource.
    KmsKeyNativeId         *string              `json:"kms_key_native_id"`
    // The name given to the restored RDS resource.
    // The name must follow AWS RDS naming conventions:
    // https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints
    Name                   *string              `json:"name"`
    // Option group name to be added to the restored RDS resource
    OptionGroupName        *string              `json:"option_group_name"`
    // The AWS-assigned IDs of the security groups to be associated with the restored RDS resource.
    SecurityGroupNativeIds []*string            `json:"security_group_native_ids"`
    // The AWS-assigned name of the subnet group to be associated with the restored RDS resource.
    SubnetGroupName        *string              `json:"subnet_group_name"`
    // A tag created through AWS Console which can be applied to EBS volumes.
    Tags                   []*AwsTagCommonModel `json:"tags"`
}

// RdsTemplateInfo represents a custom type struct
type RdsTemplateInfo struct {
    // The latest available feature version for the asset.
    AvailableTemplateVersion *string `json:"available_template_version"`
}

// ReadPolicyDefinitionHateoasLink represents a custom type struct.
// A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
type ReadPolicyDefinitionHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// ReadTaskHateoasLink represents a custom type struct.
// A HATEOAS link to the task associated with this resource.
type ReadTaskHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// ReadTaskHateoasLinks represents a custom type struct.
// URLs to pages related to the resource.
type ReadTaskHateoasLinks struct {
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// ReadTaskHateoasOuterEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ReadTaskHateoasOuterEmbedded struct {
    // Embeds the associated task of a resource in the response if requested using the `embed` query parameter.
    ReadTask interface{} `json:"read-task"`
}

// ReadVCenterObjectProtectionStatsHateoasLink represents a custom type struct.
// A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
type ReadVCenterObjectProtectionStatsHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// ReadVMwareVCenterProtectionStatsLinks represents a custom type struct.
// URLs to pages related to the resource.
type ReadVMwareVCenterProtectionStatsLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ReplicaDescription represents a custom type struct.
// Contains the details of the replica.
type ReplicaDescription struct {
    // Represents the properties of a replica global secondary index.
    GlobalSecondaryIndexes        []*ReplicaGlobalSecondaryIndexDescription `json:"global_secondary_indexes"`
    // The AWS KMS key of the replica that will be used for AWS KMS encryption.
    KmsMasterKeyId                *string                                   `json:"kms_master_key_id"`
    // Replica-specific provisioned throughput settings. If not specified, uses the source table's provisioned throughput settings.
    ProvisionedThroughputOverride *ProvisionedThroughputOverride            `json:"provisioned_throughput_override"`
    // The name of the Region.
    RegionName                    *string                                   `json:"region_name"`
}

// ReplicaGlobalSecondaryIndexDescription represents a custom type struct.
// Represents the properties of a replica global secondary index.
type ReplicaGlobalSecondaryIndexDescription struct {
    // The name of the global secondary index.
    IndexName                     *string                        `json:"index_name"`
    // Replica-specific provisioned throughput settings. If not specified, uses the source table's provisioned throughput settings.
    ProvisionedThroughputOverride *ProvisionedThroughputOverride `json:"provisioned_throughput_override"`
}

// ReportDownload represents a custom type struct
type ReportDownload struct {
    // The link to the actual CSV report.
    DownloadLink        *string `json:"download_link"`
    // The time when the request was completed.
    EndTimestamp        *string `json:"end_timestamp"`
    // The time when this report CSV will expire and not be available for download.
    ExpirationTimestamp *string `json:"expiration_timestamp"`
    // The name of CSV file.
    FileName            *string `json:"file_name"`
    // The filters applied to the report when download was initiated.
    Filters             *string `json:"filters"`
    // TODO: Add struct field description
    Id                  *string `json:"id"`
    // The time when the request was made.
    StartTimestamp      *string `json:"start_timestamp"`
    // The Clumio-assigned ID of the task which generated the restored file.
    TaskId              *string `json:"task_id"`
    // The type of report this CSV Download is associated with.
    // The possible values include "activity" and "compliance".
    ClumioType          *string `json:"type"`
}

// ReportDownloadListEmbedded represents a custom type struct.
// _embedded contains the list of items of a list report CSV download query
type ReportDownloadListEmbedded struct {
    // TODO: Add struct field description
    Items []*ReportDownload `json:"items"`
}

// ReportDownloadListLinks represents a custom type struct.
// _links provides URLs to related navigable pages of a list report CSV download query
type ReportDownloadListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ResourcePoolDatacenterModel represents a custom type struct.
// The data center in which the resource pool resides.
type ResourcePoolDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id *string `json:"id"`
}

// ResourcePoolLinks represents a custom type struct.
// URLs to pages related to the resource.
type ResourcePoolLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ResourcePoolListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type ResourcePoolListEmbedded struct {
    // ResourcePoolWithETag to support etag string to be calculated
    Items []*ResourcePoolWithETag `json:"items"`
}

// ResourcePoolListLinks represents a custom type struct.
// URLs to pages related to the resource.
type ResourcePoolListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// ResourcePoolWithETag represents a custom type struct.
// ResourcePoolWithETag to support etag string to be calculated
type ResourcePoolWithETag struct {
    // The ETag value.
    Etag            *string                                 `json:"_etag"`
    // URLs to pages related to the resource.
    Links           *ResourcePoolLinks                      `json:"_links"`
    // The compute resource that the resource pool comprises.
    ComputeResource *VMwareResourcePoolComputeResourceModel `json:"compute_resource"`
    // The data center in which the resource pool resides.
    Datacenter      *ResourcePoolDatacenterModel            `json:"datacenter"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool.
    Id              *string                                 `json:"id"`
    // Determines whether the resource pool is the default, hidden resource pool.
    IsRoot          *bool                                   `json:"is_root"`
    // Determines whether the resource pool can be used as a restore destination. If `true`, the resource pool can be used as a restore destination and backups can be restored to the resource pool.
    IsSupported     *bool                                   `json:"is_supported"`
    // The VMware-assigned name of the resource pool.
    Name            *string                                 `json:"name"`
    // The vCenter object that is the parent of the resource pool.
    Parent          *VMwareResourcePoolParentModel          `json:"parent"`
}

// RestEntity represents a custom type struct
type RestEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// RestoreDynamoDBTableLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoreDynamoDBTableLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreEBSLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoreEBSLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreEC2Links represents a custom type struct.
// URLs to pages related to the resource.
type RestoreEC2Links struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreFileLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoreFileLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreProtectionGroupLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoreProtectionGroupLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreProtectionGroupS3AssetLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoreProtectionGroupS3AssetLinks struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreRecordsLinksAsync represents a custom type struct.
// URLs to pages related to the resource.
type RestoreRecordsLinksAsync struct {
    // The HATEOAS link to this resource.
    Self     *HateoasSelfLink     `json:"_self"`
    // A HATEOAS link to the task associated with this resource.
    ReadTask *ReadTaskHateoasLink `json:"read-task"`
}

// RestoreRecordsLinksSync represents a custom type struct.
// URLs to pages related to the resource.
type RestoreRecordsLinksSync struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// RestoredFileInfo represents a custom type struct
type RestoredFileInfo struct {
    // Specifies information about the data-access method for accessing the restored
    // file.
    AccessMethods       []*DataAccessObject `json:"access_methods"`
    // The Clumio-assigned ID of the backup associated with this restored file.
    BackupId            *string             `json:"backup_id"`
    // The timestamp of the when the backup associated with this file started.
    // Represented in RFC-3339 format.
    BackupTimestamp     *string             `json:"backup_timestamp"`
    // The timestamp of when the restored file will expire. Represented in RFC-3339
    // format.
    ExpirationTimestamp *string             `json:"expiration_timestamp"`
    // The Clumio-assigned ID of the restored file.
    Id                  *string             `json:"id"`
    // The Clumio-assigned name of the restored file.
    Name                *string             `json:"name"`
    // The size of the restored file. Measured in bytes (B).
    Size                *int64              `json:"size"`
    // The Clumio-assigned ID of the task which generated the restored file.
    TaskId              *string             `json:"task_id"`
}

// RestoredFilesListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type RestoredFilesListEmbedded struct {
    // TODO: Add struct field description
    Items []*RestoredFileInfo `json:"items"`
}

// RestoredFilesListLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoredFilesListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// RestoredRecord represents a custom type struct
type RestoredRecord struct {
    // URLs to pages related to the resource.
    Links               *RestoredRecordLinks `json:"_links"`
    // The AWS-assigned ID of the account with this record.
    AccountNativeId     *string              `json:"account_native_id"`
    // The AWS region associated with this record. For example, `us-west-2`.
    AwsRegion           *string              `json:"aws_region"`
    // The Clumio-assigned ID of the backup associated with this record.
    BackupId            *string              `json:"backup_id"`
    // The AWS-assigned name of the database associated with this record.
    DatabaseName        *string              `json:"database_name"`
    // The download link of the query result.
    DownloadLink        *string              `json:"download_link"`
    // The timestamp of when the record will expire. Represented in RFC-3339 format.
    ExpirationTimestamp *string              `json:"expiration_timestamp"`
    // The Clumio-assigned ID of the restored record.
    Id                  *string              `json:"id"`
    // The SQL query statement which produced this record.
    QueryStatement      *string              `json:"query_statement"`
    // The Clumio-assigned ID of the RDS resource associated with this record.
    ResourceId          *string              `json:"resource_id"`
    // The number of rows produced by the query.
    RowCount            *int64               `json:"row_count"`
    // The timestamp of when the query was executed. Represented in RFC-3339 format.
    StartTimestamp      *string              `json:"start_timestamp"`
    // The Clumio-assigned ID of the task which generated the restored record.
    TaskId              *string              `json:"task_id"`
}

// RestoredRecordLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoredRecordLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// RestoredRecordListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type RestoredRecordListEmbedded struct {
    // TODO: Add struct field description
    Items []*RestoredRecord `json:"items"`
}

// RestoredRecordListLinks represents a custom type struct.
// URLs to pages related to the resource.
type RestoredRecordListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// RetentionBackupSLAParam represents a custom type struct.
// The retention time for this SLA. For example, to retain the backup for 1 month, set `unit="months"` and `value=1`.
type RetentionBackupSLAParam struct {
    // The measurement unit of the SLA parameter. Values include `hours`, `days`, `months`, and `years`.
    Unit  *string `json:"unit"`
    // The measurement value of the SLA parameter.
    Value *int64  `json:"value"`
}

// RoleLinks represents a custom type struct.
// URLs to pages related to the resource.
type RoleLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// RoleListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type RoleListEmbedded struct {
    // RoleWithETag to support etag string to be calculated
    Items []*RoleWithETag `json:"items"`
}

// RoleListLinks represents a custom type struct.
// URLs to pages related to the resource.
type RoleListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// RoleWithETag represents a custom type struct.
// RoleWithETag to support etag string to be calculated
type RoleWithETag struct {
    // ETag value
    Etag        *string            `json:"_etag"`
    // URLs to pages related to the resource.
    Links       *RoleLinks         `json:"_links"`
    // A description of the role.
    Description *string            `json:"description"`
    // The Clumio-assigned ID of the role.
    Id          *string            `json:"id"`
    // Unique name assigned to the role.
    Name        *string            `json:"name"`
    // TODO: Add struct field description
    Permissions []*PermissionModel `json:"permissions"`
    // Number of users to whom the role has been assigned.
    UserCount   *int64             `json:"user_count"`
}

// Rule represents a custom type struct.
// A rule applies an action subject to a condition criteria.
type Rule struct {
    // Embedded responses related to the resource.
    Embedded             *RuleEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *RuleLinks    `json:"_links"`
    // An action to be applied subject to the rule criteria.
    Action               *RuleAction   `json:"action"`
    // The following table describes the possible conditions for a rule.
    // 
    // +-----------------------+---------------------------+--------------------------+
    // |         Field         |      Rule Condition       |       Description        |
    // +=======================+===========================+==========================+
    // | aws_account_native_id | $eq, $in                  | Denotes the AWS account  |
    // |                       |                           | to conditionalize on     |
    // |                       |                           |                          |
    // |                       |                           | {"aws_account_native_id" |
    // |                       |                           | :{"$eq":"111111111111"}} |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"aws_account_native_id" |
    // |                       |                           | :{"$in":["111111111111", |
    // |                       |                           | "222222222222"]}}        |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // +-----------------------+---------------------------+--------------------------+
    // | aws_region            | $eq, $in                  | Denotes the AWS region   |
    // |                       |                           | to conditionalize on     |
    // |                       |                           |                          |
    // |                       |                           | {"aws_region":{"$eq":"us |
    // |                       |                           | -west-2"}}               |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"aws_region":{"$in":["u |
    // |                       |                           | s-west-2", "us-          |
    // |                       |                           | east-1"]}}               |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // +-----------------------+---------------------------+--------------------------+
    // | aws_tag               | $eq, $in, $all, $contains | Denotes the AWS tag(s)   |
    // |                       |                           | to conditionalize on.    |
    // |                       |                           | Max 100 tags allowed in  |
    // |                       |                           | each rule                |
    // |                       |                           | and tag key can be upto  |
    // |                       |                           | 128 characters and value |
    // |                       |                           | can be upto 256          |
    // |                       |                           | characters long.         |
    // |                       |                           |                          |
    // |                       |                           | {"aws_tag":{"$eq":{"key" |
    // |                       |                           | :"Environment",          |
    // |                       |                           | "value":"Prod"}}}        |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"aws_tag":{"$in":[{"key |
    // |                       |                           | ":"Environment",         |
    // |                       |                           | "value":"Prod"},         |
    // |                       |                           | {"key":"Hello",          |
    // |                       |                           | "value":"World"}]}}      |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"aws_tag":{"$all":[{"ke |
    // |                       |                           | y":"Environment",        |
    // |                       |                           | "value":"Prod"},         |
    // |                       |                           | {"key":"Hello",          |
    // |                       |                           | "value":"World"}]}}      |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"aws_tag":{"$contains": |
    // |                       |                           | {"key":"Environment",    |
    // |                       |                           | "value":"Prod"}}}        |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // +-----------------------+---------------------------+--------------------------+
    // | entity_type           | $eq, $in                  | Denotes the AWS entity   |
    // |                       |                           | type to conditionalize   |
    // |                       |                           | on. (Required)           |
    // |                       |                           |                          |
    // |                       |                           | {"entity_type":{"$eq":"a |
    // |                       |                           | ws_rds_instance"}}       |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // |                       |                           | {"entity_type":{"$in":[" |
    // |                       |                           | aws_rds_instance",       |
    // |                       |                           | "aws_ebs_volume", "aws_e |
    // |                       |                           | c2_instance","aws_dynamo |
    // |                       |                           | db_table",               |
    // |                       |                           | "aws_rds_cluster"]}}     |
    // |                       |                           |                          |
    // |                       |                           |                          |
    // +-----------------------+---------------------------+--------------------------+
    // 
    Condition            *string       `json:"condition"`
    // The Clumio-assigned ID of the policy rule.
    Id                   *string       `json:"id"`
    // Name of the rule. Max 100 characters.
    Name                 *string       `json:"name"`
    // The Clumio-assigned ID of the organizational unit (OU) to which the policy rule belongs.
    OrganizationalUnitId *string       `json:"organizational_unit_id"`
    // A priority relative to other rules.
    Priority             *RulePriority `json:"priority"`
}

// RuleAction represents a custom type struct.
// An action to be applied subject to the rule criteria.
type RuleAction struct {
    // Apply a policy to assets.
    AssignPolicy *AssignPolicyAction `json:"assign_policy"`
}

// RuleEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type RuleEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition interface{} `json:"read-policy-definition"`
}

// RuleLinks represents a custom type struct.
// URLs to pages related to the resource.
type RuleLinks struct {
    // The HATEOAS link to this resource.
    Self                 *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    DeletePolicyRule     *HateoasLink                     `json:"delete-policy-rule"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A resource-specific HATEOAS link.
    UpdatePolicyRule     *HateoasLink                     `json:"update-policy-rule"`
}

// RuleListEmbedded represents a custom type struct.
// An array of embedded resources related to this resource.
type RuleListEmbedded struct {
    // A rule applies an action subject to a condition criteria.
    Items []*Rule `json:"items"`
}

// RuleListLinks represents a custom type struct.
// URLs to pages related to the resource.
type RuleListLinks struct {
    // The HATEOAS link to the first page of results.
    First            *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next             *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self             *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreatePolicyRule *HateoasLink      `json:"create-policy-rule"`
}

// RulePriority represents a custom type struct.
// A priority relative to other rules.
type RulePriority struct {
    // The rule ID before which this rule should be inserted.
    BeforeRuleId *string `json:"before_rule_id"`
}

// RuleProvision represents a custom type struct.
// Specifies the role and the organizational units to be assigned to the user subject to the rule criteria.
type RuleProvision struct {
    // The Clumio-assigned IDs of the organizational units to be assigned to the user.
    // Use the [GET /organizational-units](#operation/list-organizational-units) endpoint to fetch valid values.
    OrganizationalUnitIds []*string `json:"organizational_unit_ids"`
    // The Clumio-assigned ID of the role to be assigned to the user.
    // Use the [GET /roles](#operation/list-roles) endpoint to fetch valid values.
    RoleId                *string   `json:"role_id"`
}

// S3AccessControlTranslation represents a custom type struct.
// A container for information about access control for replicas.
type S3AccessControlTranslation struct {
    // Specifies the replica ownership.
    Owner *string `json:"owner"`
}

// S3BucketSizeRes represents a custom type struct.
// The size breakdown in bytes with timestamps of a bucket per storage class.
type S3BucketSizeRes struct {
    // Size of Deep Archive Object Overhead in bytes.
    DeepArchiveObjectOverhead                   *int64  `json:"deep_archive_object_overhead"`
    // Timestamp when CloudWatch reported the Deep Archive Object Overhead size.
    DeepArchiveObjectOverheadRetrievedTime      *string `json:"deep_archive_object_overhead_retrieved_time"`
    // Size of Deep Archive S3 Object Overhead in bytes.
    DeepArchiveS3ObjectOverhead                 *int64  `json:"deep_archive_s3_object_overhead"`
    // Timestamp when CloudWatch reported the Deep Archive S3 Object Overhead size.
    DeepArchiveS3ObjectOverheadRetrievedTime    *string `json:"deep_archive_s3_object_overhead_retrieved_time"`
    // Size of Deep Archive Staging Storage objects in bytes.
    DeepArchiveStagingStorage                   *int64  `json:"deep_archive_staging_storage"`
    // Timestamp when CloudWatch reported the Deep Archive Staging Storage objects size.
    DeepArchiveStagingStorageRetrievedTime      *string `json:"deep_archive_staging_storage_retrieved_time"`
    // Size of Deep Archive Storage objects in bytes.
    DeepArchiveStorage                          *int64  `json:"deep_archive_storage"`
    // Timestamp when CloudWatch reported the Deep Archive Storage objects size.
    DeepArchiveStorageRetrievedTime             *string `json:"deep_archive_storage_retrieved_time"`
    // Size of Glacier Instant Retrieval Storage objects in bytes.
    GlacierInstantRetrievalStorage              *int64  `json:"glacier_instant_retrieval_storage"`
    // Timestamp when CloudWatch reported the Glacier Instant Retrieval Storage objects size.
    GlacierInstantRetrievalStorageRetrievedTime *string `json:"glacier_instant_retrieval_storage_retrieved_time"`
    // Size of Glacier Object Overhead in bytes.
    GlacierObjectOverhead                       *int64  `json:"glacier_object_overhead"`
    // Timestamp when CloudWatch reported the Glacier Object Overhead size.
    GlacierObjectOverheadRetrievedTime          *string `json:"glacier_object_overhead_retrieved_time"`
    // Size of Glacier S3 Object Overhead in bytes.
    GlacierS3ObjectOverhead                     *int64  `json:"glacier_s3_object_overhead"`
    // Timestamp when CloudWatch reported the Glacier S3 Object Overhead size.
    GlacierS3ObjectOverheadRetrievedTime        *string `json:"glacier_s3_object_overhead_retrieved_time"`
    // Size of Glacier Staging Storage objects in bytes.
    GlacierStagingStorage                       *int64  `json:"glacier_staging_storage"`
    // Timestamp when CloudWatch reported the Glacier Staging Storage objects size.
    GlacierStagingStorageRetrievedTime          *string `json:"glacier_staging_storage_retrieved_time"`
    // Size of Glacier Storage objects in bytes.
    GlacierStorage                              *int64  `json:"glacier_storage"`
    // Timestamp when CloudWatch reported the Glacier Storage objects size.
    GlacierStorageRetrievedTime                 *string `json:"glacier_storage_retrieved_time"`
    // Size of Intelligent-Tiering AA Storage objects in bytes.
    IntelligentTieringAaStorage                 *int64  `json:"intelligent_tiering_aa_storage"`
    // Timestamp when CloudWatch reported the Intelligent-Tiering AA Storage objects size.
    IntelligentTieringAaStorageRetrievedTime    *string `json:"intelligent_tiering_aa_storage_retrieved_time"`
    // Size of Intelligent-Tiering AIA Storage objects in bytes.
    IntelligentTieringAiaStorage                *int64  `json:"intelligent_tiering_aia_storage"`
    // Timestamp when CloudWatch reported the Intelligent-Tiering AIA Storage objects size.
    IntelligentTieringAiaStorageRetrievedTime   *string `json:"intelligent_tiering_aia_storage_retrieved_time"`
    // Size of Intelligent-Tiering DAA Storage objects in bytes.
    IntelligentTieringDaaStorage                *int64  `json:"intelligent_tiering_daa_storage"`
    // Timestamp when CloudWatch reported the Intelligent-Tiering DAA Storage objects size.
    IntelligentTieringDaaStorageRetrievedTime   *string `json:"intelligent_tiering_daa_storage_retrieved_time"`
    // Size of Intelligent-Tiering FA Storage objects in bytes.
    IntelligentTieringFaStorage                 *int64  `json:"intelligent_tiering_fa_storage"`
    // Timestamp when CloudWatch reported the Intelligent-Tiering FA Storage objects size.
    IntelligentTieringFaStorageRetrievedTime    *string `json:"intelligent_tiering_fa_storage_retrieved_time"`
    // Size of Intelligent-Tiering IA Storage objects in bytes.
    IntelligentTieringIaStorage                 *int64  `json:"intelligent_tiering_ia_storage"`
    // Timestamp when CloudWatch reported the Intelligent-Tiering IA Storage objects size.
    IntelligentTieringIaStorageRetrievedTime    *string `json:"intelligent_tiering_ia_storage_retrieved_time"`
    // Size of OneZone IA Overhead in bytes.
    OneZoneIaSizeOverhead                       *int64  `json:"one_zone_ia_size_overhead"`
    // Timestamp when CloudWatch reported the OneZone IA Overhead size.
    OneZoneIaSizeOverheadRetrievedTime          *string `json:"one_zone_ia_size_overhead_retrieved_time"`
    // Size of OneZone IA Storage objects in bytes.
    OneZoneIaStorage                            *int64  `json:"one_zone_ia_storage"`
    // Timestamp when CloudWatch reported the OneZone IA Storage objects size.
    OneZoneIaStorageRetrievedTime               *string `json:"one_zone_ia_storage_retrieved_time"`
    // Size of Reduced Redundancy Storage objects in bytes.
    ReducedRedundancyStorage                    *int64  `json:"reduced_redundancy_storage"`
    // Timestamp when CloudWatch reported the Reduced Redundancy Storage objects size.
    ReducedRedundancyStorageRetrievedTime       *string `json:"reduced_redundancy_storage_retrieved_time"`
    // Size of Standard IA Object Overhead in bytes.
    StandardIaObjectOverhead                    *int64  `json:"standard_ia_object_overhead"`
    // Timestamp when CloudWatch reported the Standard IA Object Overhead size.
    StandardIaObjectOverheadRetrievedTime       *string `json:"standard_ia_object_overhead_retrieved_time"`
    // Size of Standard IA Overhead in bytes.
    StandardIaSizeOverhead                      *int64  `json:"standard_ia_size_overhead"`
    // Timestamp when CloudWatch reported the Standard IA Overhead size.
    StandardIaSizeOverheadRetrievedTime         *string `json:"standard_ia_size_overhead_retrieved_time"`
    // Size of Standard IA Storage objects in bytes.
    StandardIaStorage                           *int64  `json:"standard_ia_storage"`
    // Timestamp when CloudWatch reported the Standard IA Storage objects size.
    StandardIaStorageRetrievedTime              *string `json:"standard_ia_storage_retrieved_time"`
    // Size of Standard Storage objects in bytes.
    StandardStorage                             *int64  `json:"standard_storage"`
    // Timestamp when CloudWatch reported the Standard Storage objects size.
    StandardStorageRetrievedTime                *string `json:"standard_storage_retrieved_time"`
}

// S3BucketsInventorySummaryBucketSizeBreakdown represents a custom type struct.
// The total size breakdown of S3 buckets in bytes per storage class. This parameter aggregates relevant fields from cloudwatch_metrics > size_bytes_per_storage_class
type S3BucketsInventorySummaryBucketSizeBreakdown struct {
    // Size of Glacier Deep Archive Storage in bytes.
    GlacierDeepArchiveStorageBytes       *int64 `json:"glacier_deep_archive_storage_bytes"`
    // Size of Glacier Flexible Retrieval Storage in bytes.
    GlacierFlexibleRetrievalStorageBytes *int64 `json:"glacier_flexible_retrieval_storage_bytes"`
    // Size of Glacier Instant Retrieval Storage in bytes.
    GlacierInstantRetrievalStorageBytes  *int64 `json:"glacier_instant_retrieval_storage_bytes"`
    // Size of Intelligent-Tiering Storage objects in bytes.
    IntelligentTieringStorageBytes       *int64 `json:"intelligent_tiering_storage_bytes"`
    // Size of OneZone-IA Storage in bytes.
    OneZoneIaStorageBytes                *int64 `json:"one_zone_ia_storage_bytes"`
    // Size of Reduced Redundancy Storage in bytes.
    ReducedRedundancyStorageBytes        *int64 `json:"reduced_redundancy_storage_bytes"`
    // Size of Standard-IA Storage in bytes.
    StandardIaStorageBytes               *int64 `json:"standard_ia_storage_bytes"`
    // Size of Standard Storage in bytes.
    StandardStorageBytes                 *int64 `json:"standard_storage_bytes"`
}

// S3CloudwatchMetrics represents a custom type struct.
// The Cloudwatch metrics of the bucket.
type S3CloudwatchMetrics struct {
    // The average size of object in bucket.
    AverageObjectSizeBytes     *float64         `json:"average_object_size_bytes"`
    // Timestamp when average size of the bucket is calculated.
    AverageObjectSizeBytesTime *string          `json:"average_object_size_bytes_time"`
    // Number of objects in bucket.
    ObjectCount                *int64           `json:"object_count"`
    // Timestamp when CloudWatch reported the bucket object count.
    ObjectCountRetrievedTime   *string          `json:"object_count_retrieved_time"`
    // Size of bucket in bytes.
    SizeBytes                  *int64           `json:"size_bytes"`
    // The size breakdown in bytes with timestamps of a bucket per storage class.
    SizeBytesPerStorageClass   *S3BucketSizeRes `json:"size_bytes_per_storage_class"`
    // Timestamp when CloudWatch reported the bucket size.
    SizeBytesRetrievedTime     *string          `json:"size_bytes_retrieved_time"`
}

// S3DeleteMarkerReplication represents a custom type struct.
// Specifies whether Amazon S3 replicates delete markers.
type S3DeleteMarkerReplication struct {
    // Indicates whether to replicate delete markers.
    Status *string `json:"status"`
}

// S3Destination represents a custom type struct.
// Specifies information about where to publish analysis or configuration results.
type S3Destination struct {
    // A container for information about access control for replicas.
    AccessControlTranslation *S3AccessControlTranslation `json:"access_control_translation"`
    // Destination bucket owner account ID.
    Account                  *string                     `json:"account"`
    // The Amazon Resource Name (ARN) of the bucket where
    // you want Amazon S3 to store the results.
    Bucket                   *string                     `json:"bucket"`
    // Specifies encryption-related information for an Amazon S3 bucket
    // that is a destination for replicated objects.
    EncryptionConfiguration  *S3EncryptionConfiguration  `json:"encryption_configuration"`
    // A container specifying replication metrics-related settings
    // enabling replication metrics and events.
    Metrics                  *S3Metrics                  `json:"metrics"`
    // A container specifying S3 Replication Time Control (S3 RTC)
    // related information.
    ReplicationTime          *S3ReplicationTime          `json:"replication_time"`
    // The storage class to use when replicating objects.
    StorageClass             *string                     `json:"storage_class"`
}

// S3EncryptionConfiguration represents a custom type struct.
// Specifies encryption-related information for an Amazon S3 bucket
// that is a destination for replicated objects.
type S3EncryptionConfiguration struct {
    // Specifies the ID (Key ARN or Alias ARN) of the customer managed
    // AWS KMS key stored in AWS Key Management Service (KMS) for the
    // destination bucket.
    ReplicaKmsKeyId *string `json:"replica_kms_key_id"`
}

// S3EncryptionOutput represents a custom type struct.
// The AWS encryption output of the bucket.
type S3EncryptionOutput struct {
    // Specifies the default server-side-encryption configuration.
    ServerSideEncryptionConfiguration *S3ServerSideEncryptionConfiguration `json:"server_side_encryption_configuration"`
}

// S3ExistingObjectReplication represents a custom type struct.
// Configuration to replicate existing source bucket objects.
type S3ExistingObjectReplication struct {
    // Specifies whether the existing object replication is enabled.
    Status *string `json:"status"`
}

// S3Metrics represents a custom type struct.
// A container specifying replication metrics-related settings
// enabling replication metrics and events.
type S3Metrics struct {
    // A container specifying the time value for S3 Replication Time
    // Control (S3 RTC) and replication metrics EventThreshold.
    EventThreshold *S3ReplicationTimeValue `json:"event_threshold"`
    // Specifies whether the replication metrics are enabled.
    Status         *string                 `json:"status"`
}

// S3ReplicaModifications represents a custom type struct.
// A filter that you can specify for selection for modifications on replicas.
type S3ReplicaModifications struct {
    // Specifies whether Amazon S3 replicates modifications on replicas.
    Status *string `json:"status"`
}

// S3ReplicationConfiguration represents a custom type struct.
// A container for replication rules with a maximum size
// of 2MB and a maximum of 1,000 rules.
type S3ReplicationConfiguration struct {
    // The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM)
    // role that Amazon S3 assumes when replicating objects.
    Role  *string              `json:"role"`
    // Specifies which Amazon S3 objects to replicate and where to store the replicas.
    Rules []*S3ReplicationRule `json:"rules"`
}

// S3ReplicationOutput represents a custom type struct.
// The AWS replication output of the bucket.
type S3ReplicationOutput struct {
    // A container for replication rules with a maximum size
    // of 2MB and a maximum of 1,000 rules.
    ReplicationConfiguration *S3ReplicationConfiguration `json:"replication_configuration"`
}

// S3ReplicationRule represents a custom type struct.
// Specifies which Amazon S3 objects to replicate and where to store the replicas.
type S3ReplicationRule struct {
    // Specifies whether Amazon S3 replicates delete markers.
    DeleteMarkerReplication   *S3DeleteMarkerReplication   `json:"delete_marker_replication"`
    // Specifies information about where to publish analysis or configuration results.
    Destination               *S3Destination               `json:"destination"`
    // Configuration to replicate existing source bucket objects.
    ExistingObjectReplication *S3ExistingObjectReplication `json:"existing_object_replication"`
    // A filter that identifies the subset of objects
    // to which the replication rule applies.
    Filter                    *S3ReplicationRuleFilter     `json:"filter"`
    // A unique identifier for the rule (max 255 characters).
    Id                        *string                      `json:"id"`
    // The priority indicates which rule has precedence whenever
    // two or more replication rules conflict.
    Priority                  *int64                       `json:"priority"`
    // A container that describes additional filters for identifying
    // the source objects that you want to replicate.
    SourceSelectionCriteria   *S3SourceSelectionCriteria   `json:"source_selection_criteria"`
    // Specifies whether the rule is enabled.
    Status                    *string                      `json:"status"`
}

// S3ReplicationRuleAndOperator represents a custom type struct.
// A container for specifying rule filters. The filters
// determine the subset of objects to which the rule applies.
type S3ReplicationRuleAndOperator struct {
    // An object key name prefix that identifies
    // the subset of objects to which the rule applies.
    Prefix *string  `json:"prefix"`
    // A container of a key value name pair.
    Tags   []*S3Tag `json:"tags"`
}

// S3ReplicationRuleFilter represents a custom type struct.
// A filter that identifies the subset of objects
// to which the replication rule applies.
type S3ReplicationRuleFilter struct {
    // A container for specifying rule filters. The filters
    // determine the subset of objects to which the rule applies.
    And    *S3ReplicationRuleAndOperator `json:"and"`
    // An object key name prefix that identifies the
    // subset of objects to which the rule applies.
    Prefix *string                       `json:"prefix"`
    // A container of a key value name pair.
    Tag    *S3Tag                        `json:"tag"`
}

// S3ReplicationTime represents a custom type struct.
// A container specifying S3 Replication Time Control (S3 RTC)
// related information.
type S3ReplicationTime struct {
    // Specifies whether the replication time is enabled.
    Status *string                 `json:"status"`
    // A container specifying the time value for S3 Replication Time
    // Control (S3 RTC) and replication metrics EventThreshold.
    Time   *S3ReplicationTimeValue `json:"time"`
}

// S3ReplicationTimeValue represents a custom type struct.
// A container specifying the time value for S3 Replication Time
// Control (S3 RTC) and replication metrics EventThreshold.
type S3ReplicationTimeValue struct {
    // Contains an integer specifying time in minutes.
    Minutes *int64 `json:"minutes"`
}

// S3ServerSideEncryptionByDefault represents a custom type struct.
// Describes the default server-side encryption to apply to new objects in the bucket.
type S3ServerSideEncryptionByDefault struct {
    // AWS Key Management Service (KMS) customer AWS KMS key ID to use for the default encryption.
    KmsMasterKeyId *string `json:"kms_master_key_id"`
    // Server-side encryption algorithm to use for the default encryption.
    SseAlgorithm   *string `json:"sse_algorithm"`
}

// S3ServerSideEncryptionConfiguration represents a custom type struct.
// Specifies the default server-side-encryption configuration.
type S3ServerSideEncryptionConfiguration struct {
    // Specifies the default server-side encryption configuration.
    Rules []*S3ServerSideEncryptionRule `json:"rules"`
}

// S3ServerSideEncryptionRule represents a custom type struct.
// Specifies the default server-side encryption configuration.
type S3ServerSideEncryptionRule struct {
    // Describes the default server-side encryption to apply to new objects in the bucket.
    ApplyServerSideEncryptionByDefault *S3ServerSideEncryptionByDefault `json:"apply_server_side_encryption_by_default"`
    // Specifies whether Amazon S3 should use an S3 Bucket Key with server-side
    // encryption using KMS (SSE-KMS) for new objects in the bucket.
    BucketKeyEnabled                   *bool                            `json:"bucket_key_enabled"`
}

// S3SourceSelectionCriteria represents a custom type struct.
// A container that describes additional filters for identifying
// the source objects that you want to replicate.
type S3SourceSelectionCriteria struct {
    // A filter that you can specify for selection for modifications on replicas.
    ReplicaModifications   *S3ReplicaModifications   `json:"replica_modifications"`
    // A container for filter information for the selection of
    // S3 objects encrypted with AWS KMS.
    SseKmsEncryptedObjects *S3SseKmsEncryptedObjects `json:"sse_kms_encrypted_objects"`
}

// S3SseKmsEncryptedObjects represents a custom type struct.
// A container for filter information for the selection of
// S3 objects encrypted with AWS KMS.
type S3SseKmsEncryptedObjects struct {
    // Specifies whether Amazon S3 replicates objects created with server-side
    // encryption using an AWS KMS key stored in AWS Key Management Service.
    Status *string `json:"status"`
}

// S3Tag represents a custom type struct.
// A container of a key value name pair.
type S3Tag struct {
    // Name of the object key.
    Key   *string `json:"key"`
    // Value of the tag.
    Value *string `json:"value"`
}

// S3VersioningOutput represents a custom type struct.
// The AWS versioning output of the bucket.
type S3VersioningOutput struct {
    // Specifies whether MFA delete is enabled in the bucket versioning configuration.
    MfaDelete *string `json:"mfa_delete"`
    // The versioning state of the bucket.
    Status    *string `json:"status"`
}

// SSESpecification represents a custom type struct.
// Represents the server-side encryption settings for a table.
type SSESpecification struct {
    // The server-side encryption KMS key type.
    // This field will only be populated for [GET /datasources/aws/dynamodb-tables/{table_id}](#operation/read-aws-dynamodb-table)
    // and [GET /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-dynamodb-table).
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), `kms_master_key_id` must be specified
    // in case of CUSTOMER_MANAGED. Possible values include: DEFAULT, AWS_MANAGED, CUSTOMER_MANAGED.
    KmsKeyType     *string `json:"kms_key_type"`
    // The AWS KMS customer master key (CMK) ARN that is used to encrypt the table.
    // If this field is `null`, server-side encryption is the default encryption (AWS owned CMK).
    // Otherwise, an AWS-managed or customer-managed CMK exists having these values.
    // For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), use key ID, Amazon Resource
    // Name (ARN), alias name or alias ARN to specify a key to be used for encrypting the restored table.
    // In case of default encryption (AWS owned CMK), specify this as `null`.
    KmsMasterKeyId *string `json:"kms_master_key_id"`
}

// SetBucketPropertiesResponseLinks represents a custom type struct
type SetBucketPropertiesResponseLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// ShareFileRestoreEmailLinks represents a custom type struct.
// URLs to pages related to the resource.
type ShareFileRestoreEmailLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// SingleErrorResponse represents a custom type struct
type SingleErrorResponse struct {
    // TODO: Add struct field description
    ErrorCode    *uint32 `json:"error_code"`
    // The reason for the error.
    ErrorMessage *string `json:"error_message"`
}

// SourceObjectFilters represents a custom type struct.
// Search for or restore only objects that pass the source object filter.
type SourceObjectFilters struct {
    // Filter for objects with this etag.
    Etag               *string   `json:"etag"`
    // If set to true, filter for latest versions only. Otherwise, all versions will
    // be returned.
    LatestVersionOnly  *bool     `json:"latest_version_only"`
    // Filter for objects with at most this size in bytes.
    MaxObjectSizeBytes *int64    `json:"max_object_size_bytes"`
    // Filter for objects with at least this size in bytes.
    MinObjectSizeBytes *int64    `json:"min_object_size_bytes"`
    // Filter for objects whose key contains this string.
    ObjectKeyContains  *string   `json:"object_key_contains"`
    // Filter for objects whose key matches this string.
    ObjectKeyMatches   *string   `json:"object_key_matches"`
    // Filter for objects that start with this key prefix.
    ObjectKeyPrefix    *string   `json:"object_key_prefix"`
    // Filter for objects that end with this key suffix.
    ObjectKeySuffix    *string   `json:"object_key_suffix"`
    // Storage class to include in the restore. If not specified, then all objects across all storage
    // classes will be restored. Valid values are: `S3 Standard`, `S3 Standard-IA`, `S3 Intelligent-Tiering`
    // and `S3 One Zone-IA`.
    StorageClasses     []*string `json:"storage_classes"`
    // Filter for objects with this version ID.
    VersionId          *string   `json:"version_id"`
}

// Subgroup represents a custom type struct
type Subgroup struct {
    // URLs to pages related to the resource.
    Links                       *SubgroupLinks               `json:"_links"`
    // The number of cloud connectors in this subgroup, aggregated by their status.
    CloudConnectorCountByStatus *CloudConnectorCountByStatus `json:"cloud_connector_count_by_status"`
    // The overall health of cloud connectors in this subgroup. Possible values include: 'healthy', indicating
    // that all cloud connectors in the subgroup are connected; 'degraded' indicating that one or more cloud
    // connectors in the subgroup have connection issues; `none`, indicating that no cloud connectors are in the subgroup.
    CloudConnectorStatus        *string                      `json:"cloud_connector_status"`
    // The Clumio-assigned ID of the management group associated with this subgroup.
    GroupId                     *string                      `json:"group_id"`
    // The Clumio-assigned ID of the management subgroup.
    Id                          *string                      `json:"id"`
    // The name of the management subgroup.
    Name                        *string                      `json:"name"`
}

// SubgroupLinks represents a custom type struct.
// URLs to pages related to the resource.
type SubgroupLinks struct {
    // The HATEOAS link to this resource.
    Self                     *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ListMssqlHostConnections *HateoasLink     `json:"list-mssql-host-connections"`
}

// SubgroupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type SubgroupListEmbedded struct {
    // TODO: Add struct field description
    Items []*Subgroup `json:"items"`
}

// SubgroupListLinks represents a custom type struct.
// URLs to pages related to the resource.
type SubgroupListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// Tag2 represents a custom type struct
type Tag2 struct {
    // Embedded responses related to the resource.
    Embedded             *Tag2Embedded           `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                *Tag2Links              `json:"_links"`
    // The tag category associated with the tag.
    Category             *TagParentCategoryModel `json:"category"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
    Id                   *string                 `json:"id"`
    // The VMware-assigned name of the tag.
    Name                 *string                 `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the tag.
    OrganizationalUnitId *string                 `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo       *ProtectionInfo         `json:"protection_info"`
    // The protection status of this tag. Refer to the Protection Status table for a complete list of protection statuses.
    ProtectionStatus     *string                 `json:"protection_status"`
}

// Tag2Embedded represents a custom type struct.
// Embedded responses related to the resource.
type Tag2Embedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition                interface{} `json:"read-policy-definition"`
    // Embeds the compliance statistics of VMs into each vCenter resource in the response, if requested using the `_embed` query parameter.
    ReadVmwareVcenterTagComplianceStats interface{} `json:"read-vmware-vcenter-tag-compliance-stats"`
}

// Tag2Links represents a custom type struct.
// URLs to pages related to the resource.
type Tag2Links struct {
    // The HATEOAS link to this resource.
    Self                                *HateoasSelfLink                             `json:"_self"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                     *ProtectEntitiesHateoasLink                  `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition                *ReadPolicyDefinitionHateoasLink             `json:"read-policy-definition"`
    // A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
    ReadVmwareVcenterTagComplianceStats *ReadVCenterObjectProtectionStatsHateoasLink `json:"read-vmware-vcenter-tag-compliance-stats"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                   *UnprotectEntitiesHateoasLink                `json:"unprotect-entities"`
}

// Tag2ListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type Tag2ListEmbedded struct {
    // TODO: Add struct field description
    Items []*Tag2 `json:"items"`
}

// Tag2ListLinks represents a custom type struct.
// URLs to pages related to the resource.
type Tag2ListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// TagCategory2Links represents a custom type struct.
// URLs to pages related to the resource
type TagCategory2Links struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// TagCategory2ListEmbedded represents a custom type struct.
// Embedded responses related to the resource
type TagCategory2ListEmbedded struct {
    // TagCategory2WithETag to support etag string to be calculated
    Items []*TagCategory2WithETag `json:"items"`
}

// TagCategory2ListLinks represents a custom type struct.
// URLs to pages related to the resource
type TagCategory2ListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// TagCategory2WithETag represents a custom type struct.
// TagCategory2WithETag to support etag string to be calculated
type TagCategory2WithETag struct {
    // The ETag value.
    Etag                 *string            `json:"_etag"`
    // URLs to pages related to the resource
    Links                *TagCategory2Links `json:"_links"`
    // A description of the tag category.
    Description          *string            `json:"description"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
    Id                   *string            `json:"id"`
    // The VMware-assigned name of the tag category.
    Name                 *string            `json:"name"`
    // The number of tags in the tag category.
    NumberOfTags         *int32             `json:"number_of_tags"`
    // The Clumio-assigned ID of the organizational unit associated with the tag category.
    OrganizationalUnitId *string            `json:"organizational_unit_id"`
}

// TagParentCategoryModel represents a custom type struct.
// The tag category associated with the tag.
type TagParentCategoryModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
    Id                   *string `json:"id"`
    // The VMware-assigned name of the tag category.
    Name                 *string `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the tag category.
    OrganizationalUnitId *string `json:"organizational_unit_id"`
}

// Task represents a custom type struct
type Task struct {
    // URLs to pages related to the resource.
    Links              *TaskLinks         `json:"_links"`
    // The task category. Examples of task types include "backup", "restore", "snapshot", and "system".
    // 
    // +-------------------+----------------------------------------------------------+
    // |     Category      |                       Description                        |
    // +===================+==========================================================+
    // | backup            | Encompasses all modes of backups. This does not include  |
    // |                   | in-account snapshots.                                    |
    // +-------------------+----------------------------------------------------------+
    // | restore           | Encompasses all modes of restores. This does not include |
    // |                   | restores of in-account snapshots.                        |
    // +-------------------+----------------------------------------------------------+
    // | snapshot          | Encompasses all modes of in-account snapshots.           |
    // +-------------------+----------------------------------------------------------+
    // | snapshot_restore  | Encompasses all modes of snapshot restores.              |
    // +-------------------+----------------------------------------------------------+
    // | system            | Encompasses a variety of system-initiated tasks, such as |
    // |                   | aws_rds_backup_target_setup and                          |
    // |                   | aws_ec2_instance_backup_indexing.                        |
    // +-------------------+----------------------------------------------------------+
    // | report_generation | Encompasses task types which generate reports, such as   |
    // |                   | activity_report_file_download.                           |
    // +-------------------+----------------------------------------------------------+
    // | management        | Encompasses user-initiated tasks which manage Clumio     |
    // |                   | resources, such as organizational_unit_update and        |
    // |                   | policy_update.                                           |
    // +-------------------+----------------------------------------------------------+
    // 
    Category           *string            `json:"category"`
    // The timestamp of when the task was created. Represented in RFC-3339 format.
    CreatedTimestamp   *string            `json:"created_timestamp"`
    // The timestamp of when the task ended. If this task has not yet ended,
    // then this field has a value of `null`. Represented in RFC-3339 format.
    EndTimestamp       *string            `json:"end_timestamp"`
    // The task genre. A genre is a high-level collection of task categories.
    // 
    // +----------------+-------------------------------------------------------------+
    // |     Genre      |                         Description                         |
    // +================+=============================================================+
    // | operational    | Encompasses all backup, restore, snapshot, and              |
    // |                | snapshot_restore tasks.                                     |
    // +----------------+-------------------------------------------------------------+
    // | administrative | Encompasses management, system, and report_generation       |
    // |                | tasks.                                                      |
    // +----------------+-------------------------------------------------------------+
    // 
    Genre              *string            `json:"genre"`
    // The Clumio-assigned ID of the task.
    Id                 *string            `json:"id"`
    // Determines whether or not this task can be aborted.
    // A task can be aborted if its status is either "queued" or "in_progress".
    // Tasks of certain types including
    // "vmware_vm_backup_indexing" and "aws_ebs_volume_backup_indexing" cannot be aborted.
    IsAbortable        *bool              `json:"is_abortable"`
    // The parent entity associated with the task.
    ParentEntity       *TaskParentEntity  `json:"parent_entity"`
    // The primary entity associated with the task.
    PrimaryEntity      *TaskPrimaryEntity `json:"primary_entity"`
    // The percentage progress of task completion. Measured as an integer value between 0 and 100.
    ProgressPercentage *int64             `json:"progress_percentage"`
    // The timestamp of when the task started. If this task has not started yet,
    // then this field has a value of `null`. Represented in RFC-3339 format.
    StartTimestamp     *string            `json:"start_timestamp"`
    // The task status. Examples of task statuses include, "queued", "in_progress", and "completed".
    // Refer to the Task Status table for a complete list of task statuses.
    Status             *string            `json:"status"`
    // The task type. Examples of task types include "vm_backup_seeding", "ebs_indexing", and "file_restore".
    // Refer to the Task Type table for a complete list of task types.
    ClumioType         *string            `json:"type"`
}

// TaskLinks represents a custom type struct.
// URLs to pages related to the resource.
type TaskLinks struct {
    // The HATEOAS link to this resource.
    Self                   *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    ReadOrganizationalUnit *HateoasLink     `json:"read-organizational-unit"`
    // A resource-specific HATEOAS link.
    UpdateTask             *HateoasLink     `json:"update-task"`
}

// TaskListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type TaskListEmbedded struct {
    // TODO: Add struct field description
    Items []*Task `json:"items"`
}

// TaskListLinks represents a custom type struct.
// URLs to pages related to the resource.
type TaskListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// TaskParentEntity represents a custom type struct.
// The parent entity associated with the task.
type TaskParentEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// TaskPrimaryEntity represents a custom type struct.
// The primary entity associated with the task.
type TaskPrimaryEntity struct {
    // A system-generated ID assigned to this entity.
    Id         *string `json:"id"`
    // 
    // Entity Type
    // Details
    // 
    // 
    // vmware_vcenter
    // VMware vCenter.
    // 
    // 
    // vmware_vm
    // VMware virtual machine.
    // 
    // 
    // vmware_vm_folder
    // VMware VM folder.
    // 
    // 
    // vmware_datacenter
    // VMware data center.
    // 
    // 
    // vmware_datacenter_folder
    // VMware data center folder.
    // 
    // 
    // vmware_tag
    // VMware tag.
    // 
    // 
    // vmware_category
    // VMware tag category.
    // 
    // 
    // vmware_compute_resource
    // VMware compute resource.
    // 
    // 
    // vmware_compute_resource_folder
    // VMware compute resource folder.
    // 
    // 
    // aws_ebs_volume
    // AWS EBS volume.
    // 
    // 
    // aws_connection
    // AWS connection mediated by a CloudFormation stack.
    // 
    // 
    // aws_environment
    // AWS environment specified by an account/region pair.
    // 
    // 
    // aws_tag
    // AWS tag.
    // 
    // 
    // aws_cmk
    // AWS Customer Master Key used to encrypt data.
    // 
    // 
    ClumioType *string `json:"type"`
    // A system-generated value assigned to the entity. For example, if the primary entity type is "vmware_vm" for a virtual machine, then the value is the name of the VM.
    Value      *string `json:"value"`
}

// TemplateConfiguration represents a custom type struct
type TemplateConfiguration struct {
    // TODO: Add struct field description
    Discover *DiscoverTemplateInfoV2 `json:"discover"`
    // TODO: Add struct field description
    Protect  *ProtectTemplateInfoV2  `json:"protect"`
}

// TemplateConfigurationV2 represents a custom type struct
type TemplateConfigurationV2 struct {
    // The AWS asset types supported with the available version of the template.
    AssetTypesEnabled        []*string        `json:"asset_types_enabled"`
    // The latest available version for the template.
    AvailableTemplateVersion *string          `json:"available_template_version"`
    // TODO: Add struct field description
    Ebs                      *EbsTemplateInfo `json:"ebs"`
    // TODO: Add struct field description
    Rds                      *RdsTemplateInfo `json:"rds"`
}

// UnprotectEntitiesHateoasLink represents a custom type struct.
// A HATEOAS link to unprotect the entities.
type UnprotectEntitiesHateoasLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// UpdateEntities represents a custom type struct.
// Updates to the entities in the organizational unit.
type UpdateEntities struct {
    // entityModel denotes the entityModel
    Add    []*EntityModel `json:"add"`
    // entityModel denotes the entityModel
    Remove []*EntityModel `json:"remove"`
}

// UpdateUserAssignments represents a custom type struct.
// Updates to the user assignments.
type UpdateUserAssignments struct {
    // List of user ids to assign this organizational unit.
    Add    []*string `json:"add"`
    // List of user ids to un-assign this organizational unit.
    Remove []*string `json:"remove"`
}

// UserEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type UserEmbedded struct {
    // A description of the role.
    Description *string `json:"description"`
    // Unique name assigned to the role.
    Name        *string `json:"name"`
}

// UserHateoas represents a custom type struct
type UserHateoas struct {
    // Embedded responses related to the resource.
    Embedded                      *UserEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                         *UserLinks    `json:"_links"`
    // The list of organizational unit IDs assigned to the user.
    // This attribute will be available when reading a single user and not when listing users.
    AssignedOrganizationalUnitIds []*string     `json:"assigned_organizational_unit_ids"`
    // Assigned Role for the user.
    AssignedRole                  *string       `json:"assigned_role"`
    // The email address of the Clumio user.
    Email                         *string       `json:"email"`
    // The first and last name of the Clumio user. The name appears in the User Management screen and is used to identify the user.
    FullName                      *string       `json:"full_name"`
    // The Clumio-assigned ID of the Clumio user.
    Id                            *string       `json:"id"`
    // The ID number of the user who sent the email invitation.
    Inviter                       *string       `json:"inviter"`
    // Determines whether the user has activated their Clumio account.
    // If `true`, the user has activated the account.
    IsConfirmed                   *bool         `json:"is_confirmed"`
    // Determines whether the user is enabled (in "Activated" or "Invited" status) in Clumio.
    // If `true`, the user is in "Activated" or "Invited" status in Clumio.
    // Users in "Activated" status can log in to Clumio.
    // Users in "Invited" status have been invited to log in to Clumio via an email invitation and the invitation
    // is pending acceptance from the user.
    // If `false`, the user has been manually suspended and cannot log in to Clumio
    // until another Clumio user reactivates the account.
    IsEnabled                     *bool         `json:"is_enabled"`
    // The timestamp of when when the user was last active in the Clumio system. Represented in RFC-3339 format.
    LastActivityTimestamp         *string       `json:"last_activity_timestamp"`
    // The number of organizational units accessible to the user.
    OrganizationalUnitCount       *int64        `json:"organizational_unit_count"`
}

// UserLinks represents a custom type struct.
// URLs to pages related to the resource.
type UserLinks struct {
    // The HATEOAS link to this resource.
    Self       *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteUser *HateoasLink     `json:"delete-user"`
    // A resource-specific HATEOAS link.
    UpdateUser *HateoasLink     `json:"update-user"`
}

// UserListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type UserListEmbedded struct {
    // TODO: Add struct field description
    Items []*UserHateoas `json:"items"`
}

// UserListHateoasLinks represents a custom type struct.
// URLs to pages related to the resource.
type UserListHateoasLinks struct {
    // The HATEOAS link to the first page of results.
    First      *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last       *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next       *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev       *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self       *HateoasSelfLink  `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateUser *HateoasLink      `json:"create-user"`
}

// VCenterComputeResource represents a custom type struct
type VCenterComputeResource struct {
    // URLs to pages related to the resource.
    Links                *VCenterComputeResourceLinks `json:"_links"`
    // The Clumio-assigned ID of the item.
    Id                   *string                      `json:"id"`
    // IsCluster denotes whether the compute resource is a cluster.
    Iscluster            *bool                        `json:"isCluster"`
    // IsDrsEnabled denotes whether the compute resource has DRS enabled.
    // NOTE: This is only applicable if "IsCluster" is true.
    Isdrsenabled         *bool                        `json:"isDrsEnabled"`
    // The name of the compute resource.
    Name                 *string                      `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the compute resource.
    OrganizationalUnitId *string                      `json:"organizational_unit_id"`
    // TODO: Add struct field description
    Protectioninfo       *ProtectionInfoDeprecated    `json:"protectionInfo"`
    // ProtectedStatsDeprecated contains the compliance stats for policies which are protected along with
    // the unprotected policies count
    Vmstats              *ProtectedStatsDeprecated    `json:"vmStats"`
}

// VCenterComputeResourceLinks represents a custom type struct.
// URLs to pages related to the resource.
type VCenterComputeResourceLinks struct {
    // A HATEOAS link to protect the entities.
    ProtectEntities   *ProtectEntitiesHateoasLink   `json:"protect-entities"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities *UnprotectEntitiesHateoasLink `json:"unprotect-entities"`
}

// VCenterFolder represents a custom type struct
type VCenterFolder struct {
    // URLs to pages related to the resource.
    Links                *VCenterFolderLinks       `json:"_links"`
    // HasChildGroups denotes whether direct child folders exist.
    Haschildgroups       *bool                     `json:"hasChildGroups"`
    // The Clumio-assigned ID of the item.
    Id                   *string                   `json:"id"`
    // IsRoot denotes whether this folder is a root (hidden) folder.
    Isroot               *bool                     `json:"isRoot"`
    // Name of the folder.
    Name                 *string                   `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the folder.
    OrganizationalUnitId *string                   `json:"organizational_unit_id"`
    // TODO: Add struct field description
    Protectioninfo       *ProtectionInfoDeprecated `json:"protectionInfo"`
    // ProtectedStatsDeprecated contains the compliance stats for policies which are protected along with
    // the unprotected policies count
    Vmstats              *ProtectedStatsDeprecated `json:"vmStats"`
}

// VCenterFolderLinks represents a custom type struct.
// URLs to pages related to the resource.
type VCenterFolderLinks struct {
    // A HATEOAS link to protect the entities.
    ProtectEntities   *ProtectEntitiesHateoasLink   `json:"protect-entities"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities *UnprotectEntitiesHateoasLink `json:"unprotect-entities"`
}

// VMBackupHateoas represents a custom type struct
type VMBackupHateoas struct {
    // URLs to pages related to the resource.
    Links                *VMBackupHateoasLinks     `json:"_links"`
    // The reason that browsing is unavailable for the backup. Possible values include "file_limit_exceeded" and
    // "browsing_unavailable". If browse indexing is successful, then this field has a value of `null`.
    BrowsingFailedReason *string                   `json:"browsing_failed_reason"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center
    // associated with this backup.
    DatacenterId         *string                   `json:"datacenter_id"`
    // The timestamp of when this backup expires. Represented in RFC-3339 format.
    ExpirationTimestamp  *string                   `json:"expiration_timestamp"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the
    // host associated with this backup.
    HostId               *string                   `json:"host_id"`
    // The Clumio-assigned ID of the backup.
    Id                   *string                   `json:"id"`
    // Determines whether browsing is available for the backup. If `true`, then browsing is available for the backup.
    IsBrowsable          *bool                     `json:"is_browsable"`
    // TODO: Add struct field description
    Nics                 []*VMNicBackupModel       `json:"nics"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool
    // associated with this backup.
    ResourcePoolId       *string                   `json:"resource_pool_id"`
    // The timestamp of when this backup started. Represented in RFC-3339 format.
    StartTimestamp       *string                   `json:"start_timestamp"`
    // VMTagWithCategoryModel
    // A tag associated with the VM.
    Tags                 []*VMTagWithCategoryModel `json:"tags"`
    // The IP address or FQDN of the vCenter server associated with this backup.
    // If a backup was initiated before 2020-06-30, when this field was introduced,
    // then this field has a value of `null`.
    VcenterEndpoint      *string                   `json:"vcenter_endpoint"`
    // The Clumio-assigned ID of the vCenter associated with this backup.
    VcenterId            *string                   `json:"vcenter_id"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the
    // VM folder associated with this backup.
    VmFolderId           *string                   `json:"vm_folder_id"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the
    // VM associated with this backup.
    VmId                 *string                   `json:"vm_id"`
    // The name of the virtual machine associated with this backup.
    VmName               *string                   `json:"vm_name"`
}

// VMBackupHateoasLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMBackupHateoasLinks struct {
    // The HATEOAS link to this resource.
    Self            *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    RestoreVmwareVm *HateoasLink     `json:"restore-vmware-vm"`
}

// VMBackupListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VMBackupListEmbedded struct {
    // TODO: Add struct field description
    Items []*VMBackupHateoas `json:"items"`
}

// VMBackupListHateoasLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMBackupListHateoasLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// VMComputeResourceFolderModel represents a custom type struct.
// The compute resource folder associated with this VM. If the VM is deleted, then this field has a value of `null`.
type VMComputeResourceFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMComputeResourceModel represents a custom type struct.
// The compute resource from which the VM draws. If the VM is deleted, then `compute_resource.id` has a value of `null`.
type VMComputeResourceModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    Id   *string `json:"id"`
    // The VMware-assigned name of the compute resource.
    Name *string `json:"name"`
}

// VMDatacenterFolderModel represents a custom type struct.
// The data center folder associated with this VM. If the VM is deleted, then this field has a value of `null`.
type VMDatacenterFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMDatacenterModel represents a custom type struct.
// The data center in which the VM resides. If the VM is deleted, then `datacenter.id` has a value of `null`.
type VMDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id   *string `json:"id"`
    // The VMware-assigned name of this data center.
    Name *string `json:"name"`
}

// VMFolderModel represents a custom type struct.
// The VM folder containing the VM. If the VM is deleted, then `vm_folder.id` has a value of `null`.
type VMFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id   *string `json:"id"`
    // The VMware-assigned name of the folder.
    Name *string `json:"name"`
}

// VMHostModel represents a custom type struct.
// The host on which the VM resides. If the VM is deleted, then `host.id` and `host.is_standalone` have values of `null`. The `host.name` field may also have a value of `null`.
type VMHostModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the host.
    Id           *string `json:"id"`
    // Determines whether the host is a standalone host. If `true`, the host is a standalone host.
    IsStandalone *bool   `json:"is_standalone"`
    // The VMware-assigned name of the host.
    Name         *string `json:"name"`
}

// VMNicBackupModel represents a custom type struct
type VMNicBackupModel struct {
    // Determines whether the NIC was connected to the network at the time of backup. If `true`, the NIC was connected to the network at the time of backup.
    IsConnected *bool   `json:"is_connected"`
    // The media access control (MAC) address assigned to the NIC. The MAC address is assigned through the vSphere client.
    MacAddress  *string `json:"mac_address"`
    // The network to which the NIC was attached.
    NetworkId   *string `json:"network_id"`
}

// VMNicModel represents a custom type struct.
// The network interface card (NIC) attached to the VM.
type VMNicModel struct {
    // The MAC address of the NIC.
    MacAddress *string            `json:"mac_address"`
    // The network associated with this NIC.
    Network    *VMNicNetworkModel `json:"network"`
}

// VMNicNetworkModel represents a custom type struct.
// The network associated with this NIC.
type VMNicNetworkModel struct {
    // The VMware-assigned ID of this network.
    Id *string `json:"id"`
}

// VMNicRestore represents a custom type struct
type VMNicRestore struct {
    // The unique media access control (MAC) address assigned to the network interface card (NIC). The MAC address is assigned through the vSphere client.
    MacAddress    *string `json:"mac_address"`
    // The network connection for the virtual NIC. The NIC is configured in the vSphere client. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/networks](#operation/list-vmware-vcenter-networks) endpoint to fetch valid values.
    NetworkId     *string `json:"network_id"`
    // Determines whether the restored VM should automatically connect to the specified network after a restore.
    // If `true`, the restored VM will automatically connect to the specified network after a restore.
    ShouldConnect *bool   `json:"should_connect"`
}

// VMResourcePoolModel represents a custom type struct.
// The resource pool from which the VM draws. If the VM is deleted, then `resource_pool.id` and `resource_pool.is_root` have values of `null`.
type VMResourcePoolModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool.
    Id     *string `json:"id"`
    // Determines whether the resource pool is the default, hidden resource pool.
    IsRoot *bool   `json:"is_root"`
    // The VMware-assigned name of the resource pool.
    Name   *string `json:"name"`
}

// VMRestoreOptions represents a custom type struct.
// Additional VM restore options.
type VMRestoreOptions struct {
    // Determines whether a VM rapid recovery should be attempted or not.
    // As a part of the rapid recovery, by default the Clumio backup service
    // attempts the following Reverse Change Block Tracking (RCBT) operation. It
    // retrieves the blocks changed since the backup was taken and applies them
    // into a clone of the original VM to rollback the VM to the previous point
    // in time. As a result typically it is much faster to restore a VM using
    // rapid recovery RCBT. However if the clone operation is not desired to be
    // performed for some reason, then rapid recovery RCBT can be turned off
    // using this field.
    // It is applicable to both in-place restore and restore to a new VM.
    // If it is not set, then the behavior is same as setting it to true.
    // If true or unset, rapid recovery is attempted first. If rapid recovery
    // fails, then a full VM restore is performed.
    // If false, rapid recovery is not attempted.
    AttemptRapidRecovery *bool   `json:"attempt_rapid_recovery"`
    // Determines whether to preserve the original data by cloning the existing
    // VM before performing an in-place restore.
    // If `"restore_in_place":false`, then this parameter is ignored.
    // If true, the original data is preserved by creating a clone of the VM.
    // If false, a clone is not created. The original data in the source VM may
    // get over-written by the restored data.
    CloneSourceVm        *bool   `json:"clone_source_vm"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the VMFS
    // datastore to be used as the destination for the cloned VM.
    // Use the [GET /datasources/vmware/vcenters/{vcenter_id}/datastores](#operation/list-vmware-vcenter-datastores) endpoint to fetch valid values.
    // This field is required only if `"clone_source_vm":true`.
    ClonedVmDatastoreId  *string `json:"cloned_vm_datastore_id"`
    // The name given to the cloned VM (see clone_source_vm parameter).
    // The VM name cannot exceed 80 characters in length and must follow VMware
    // VM naming conventions.
    // This field is required only if `"clone_source_vm":true`.
    ClonedVmName         *string `json:"cloned_vm_name"`
    // Determines whether the restore should overwrite the existing VM i.e.
    // perform an in-place restore or create a new VM for restore.
    // If true, the existing VM is used for the restore. In this case if the VM
    // is already deleted, the restore will fail.
    // If false, a new VM is created for the restore. In this case if the VM
    // is already deleted, the restore will still proceed.
    RestoreInPlace       *bool   `json:"restore_in_place"`
}

// VMRestoreSource represents a custom type struct.
// The VM backup to be restored.
type VMRestoreSource struct {
    // The Clumio-assigned ID of the backup to be restored. Use the [GET /backups/vmware/vms](#operation/list-backup-vmware-vms) endpoint to fetch valid values.
    BackupId *string `json:"backup_id"`
}

// VMRestoreTag represents a custom type struct
type VMRestoreTag struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
    TagId *string `json:"tag_id"`
}

// VMRestoreTarget represents a custom type struct.
// The configuration of the VM to be restored.
type VMRestoreTarget struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center to be used as the restore destination. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/datacenters](#operation/list-vmware-vcenter-datacenters) endpoint to fetch valid values.
    DatacenterId     *string         `json:"datacenter_id"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the VMFS datastore to be used as the restore destination. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/datastores](#operation/list-vmware-vcenter-datastores) endpoint to fetch valid values.
    // While performing an in-place restore, this parameter is optional.
    // If `"options.restore_in_place":false`, then this parameter is required.
    DatastoreId      *string         `json:"datastore_id"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the vSphere host to be used as the restore destination. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/hosts](#operation/list-vmware-vcenter-hosts) endpoint to fetch valid values.
    // If provided, the specified host (`host_id`) must belong to a compute resource that is the parent of the specified resource pool (`resource_pool_id`).
    // If not provided, the VMware Distributed Resource Scheduler (DRS) will automatically select a host that belongs to a compute resource that is the parent of the specified resource pool (`resource_pool_id`).
    HostId           *string         `json:"host_id"`
    // TODO: Add struct field description
    NetworkOptions   []*VMNicRestore `json:"network_options"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the VM folder to be used as the restore destination. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/folders](#operation/list-vmware-vcenter-folders) endpoint to fetch valid values.
    ParentVmFolderId *string         `json:"parent_vm_folder_id"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool to be used as the restore destination. Use the [GET /datasources/vmware/vcenters/{vcenter_id}/resource-pools](#operation/list-vmware-vcenter-resource-pools) endpoint to fetch valid values.
    ResourcePoolId   *string         `json:"resource_pool_id"`
    // Determines whether the VM should remain powered on after the restore. If `true`, the VM will remain powered on after the restore. Users may choose to power off a VM to change the network configurations.
    ShouldPowerOn    *bool           `json:"should_power_on"`
    // TODO: Add struct field description
    Tags             []*VMRestoreTag `json:"tags"`
    // The Clumio-assigned ID of the vCenter to be used as the restore destination.
    VcenterId        *string         `json:"vcenter_id"`
    // The name given to the restored VM. The VM name cannot exceed 80 characters in length and must follow VMware VM naming conventions.
    VmName           *string         `json:"vm_name"`
}

// VMTagWithCategoryModel represents a custom type struct.
// VMTagWithCategoryModel
// A tag associated with the VM.
type VMTagWithCategoryModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
    CategoryId           *string `json:"category_id"`
    // The VMware-assigned name of the tag category.
    CategoryName         *string `json:"category_name"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
    Id                   *string `json:"id"`
    // The VMware-assigned name of the tag.
    Name                 *string `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the tag.
    OrganizationalUnitId *string `json:"organizational_unit_id"`
}

// VMwareComputeResourceComplianceStatsLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareComputeResourceComplianceStatsLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareDatacenterFolderIDModel represents a custom type struct.
// The data center folder in which the data center resides.
type VMwareDatacenterFolderIDModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareDatacenterStatsLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareDatacenterStatsLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareDatastoreLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareDatastoreLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareDatastoreListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VMwareDatastoreListEmbedded struct {
    // VMwareDatastoreWithETag to support etag string to be calculated
    Items []*VMwareDatastoreWithETag `json:"items"`
}

// VMwareDatastoreListLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareDatastoreListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// VMwareDatastoreWithETag represents a custom type struct.
// VMwareDatastoreWithETag to support etag string to be calculated
type VMwareDatastoreWithETag struct {
    // The ETag value.
    Etag             *string                                `json:"_etag"`
    // URLs to pages related to the resource.
    Links            *VMwareDatastoreLinks                  `json:"_links"`
    // TODO: Add struct field description
    ComputeResources []*ComputeResourceIDModel              `json:"compute_resources"`
    // The data center in which this datastore resides.
    Datacenter       *VMwareVCenterDatastoreDatacenterModel `json:"datacenter"`
    // VMwareVCenterDatastoreFolderModel
    // The datastore folder in which this datastore resides.
    DatastoreFolder  *VMwareVCenterDatastoreFolderModel     `json:"datastore_folder"`
    // The file system format used for the datastore. Refer to the Supported Datastore Types section for a complete list of datastore types.
    DatastoreType    *string                                `json:"datastore_type"`
    // TODO: Add struct field description
    Hosts            []*HostIDModel                         `json:"hosts"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the datastore.
    Id               *string                                `json:"id"`
    // Determines whether the datastore is shared across multiple hosts. If `true`, the datastore is a multi-host datastore.
    IsMultiHost      *bool                                  `json:"is_multi_host"`
    // Determines whether the datastore can be used as a restore destination. If `true`, the datastore can be used as a restore destination and backups can be restored to the datastore.
    IsSupported      *bool                                  `json:"is_supported"`
    // The VMware-assigned name of this datastore.
    Name             *string                                `json:"name"`
}

// VMwareDsGroupingCriteria represents a custom type struct.
// The entity type used to group organizational units for VMware resources.
type VMwareDsGroupingCriteria struct {
    // Determines whether or not this data group is editable. If false, then an
    // organizational unit uses this data group.
    // To edit this data group, all organizational units using it must be deleted.
    IsEditable *bool   `json:"is_editable"`
    // 
    // +--------------------------------+---------------------------------+
    // |         vmware_vcenter         |         VMware vCenter.         |
    // +================================+=================================+
    // | vmware_vm_folder               | VMware VM folder.               |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter_folder       | VMware datacenter folder.       |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource_folder | VMware compute resource folder. |
    // +--------------------------------+---------------------------------+
    // | vmware_datacenter              | VMware datacenter.              |
    // +--------------------------------+---------------------------------+
    // | vmware_compute_resource        | VMware compute resource.        |
    // +--------------------------------+---------------------------------+
    // | vmware_vm                      | VMware VM.                      |
    // +--------------------------------+---------------------------------+
    // | vmware_tag                     | VMware tag.                     |
    // +--------------------------------+---------------------------------+
    // 
    ClumioType *string `json:"type"`
}

// VMwareFolderStatsLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareFolderStatsLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareResourcePoolComputeResourceModel represents a custom type struct.
// The compute resource that the resource pool comprises.
type VMwareResourcePoolComputeResourceModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    Id *string `json:"id"`
}

// VMwareResourcePoolParentModel represents a custom type struct.
// The vCenter object that is the parent of the resource pool.
type VMwareResourcePoolParentModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the vCenter object.
    Id *string `json:"id"`
}

// VMwareRootComputeResourceFolderIDModel represents a custom type struct.
// The hidden root compute resource folder of the data center.
type VMwareRootComputeResourceFolderIDModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareRootVMFolderIDModel represents a custom type struct.
// The hidden root virtual machine folder of the data center.
type VMwareRootVMFolderIDModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareTagStatsLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareTagStatsLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareVCenterComputeResourceDatacenterModel represents a custom type struct.
// The data center associated with this compute resource.
type VMwareVCenterComputeResourceDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id   *string `json:"id"`
    // The VMware-assigned name of this data center.
    Name *string `json:"name"`
}

// VMwareVCenterComputeResourceFolderModel represents a custom type struct.
// The compute resource folder in which the compute resource resides.
type VMwareVCenterComputeResourceFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareVCenterDatastoreDatacenterModel represents a custom type struct.
// The data center in which this datastore resides.
type VMwareVCenterDatastoreDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id *string `json:"id"`
}

// VMwareVCenterDatastoreFolderModel represents a custom type struct.
// VMwareVCenterDatastoreFolderModel
// The datastore folder in which this datastore resides.
type VMwareVCenterDatastoreFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareVCenterFolderDatacenterModel represents a custom type struct.
// The data center associated with this folder.
type VMwareVCenterFolderDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id *string `json:"id"`
}

// VMwareVCenterHostComputeResourceModel represents a custom type struct.
// The VMware compute resource representing the host.
type VMwareVCenterHostComputeResourceModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    Id *string `json:"id"`
}

// VMwareVCenterHostDatacenterModel represents a custom type struct.
// The data center in which the host resides.
type VMwareVCenterHostDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id *string `json:"id"`
}

// VMwareVCenterNetworkDatacenterModel represents a custom type struct.
// The data center associated with this network.
type VMwareVCenterNetworkDatacenterModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
    Id *string `json:"id"`
}

// VMwareVCenterNetworkFolderModel represents a custom type struct.
// The network folder associated with this network.
type VMwareVCenterNetworkFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// VMwareVCenterNetworkLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareVCenterNetworkLinks struct {
    // The HATEOAS link to this resource.
    Self *HateoasSelfLink `json:"_self"`
}

// VMwareVCenterNetworkListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VMwareVCenterNetworkListEmbedded struct {
    // VMwareVCenterNetworkWithETag to support etag string to be calculated.
    Items []*VMwareVCenterNetworkWithETag `json:"items"`
}

// VMwareVCenterNetworkListLinks represents a custom type struct.
// URLs to pages related to the resource.
type VMwareVCenterNetworkListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// VMwareVCenterNetworkWithETag represents a custom type struct.
// VMwareVCenterNetworkWithETag to support etag string to be calculated.
type VMwareVCenterNetworkWithETag struct {
    // The ETag value.
    Etag          *string                              `json:"_etag"`
    // URLs to pages related to the resource.
    Links         *VMwareVCenterNetworkLinks           `json:"_links"`
    // The data center associated with this network.
    Datacenter    *VMwareVCenterNetworkDatacenterModel `json:"datacenter"`
    // The VMware-assigned ID of this network.
    Id            *string                              `json:"id"`
    // Determines whether VMs can be connected to the network. If `true`, VMs can be connected to the network.
    IsSupported   *bool                                `json:"is_supported"`
    // The name of this network.
    Name          *string                              `json:"name"`
    // The network folder associated with this network.
    NetworkFolder *VMwareVCenterNetworkFolderModel     `json:"network_folder"`
}

// VMwareVCenterParentFolderModel represents a custom type struct.
// The parent folder under which this folder resides.
type VMwareVCenterParentFolderModel struct {
    // The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
    Id *string `json:"id"`
}

// Vcenter represents a custom type struct
type Vcenter struct {
    // Embedded responses related to the resource.
    Embedded                  *VcenterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                     *VcenterLinks    `json:"_links"`
    // The region to which data is backed-up to for the vCenter server. If the vCenter server's back up region is unavailable, this field has a value of `unavailable`. Refer to the Back up Regions table for a complete list of back up regions.
    BackupRegion              *string          `json:"backup_region"`
    // The URL at which the Clumio Cloud Connector for this vCenter server can be downloaded.
    CloudConnectorDownloadUrl *string          `json:"cloud_connector_download_url"`
    // The IP address or FQDN of the vCenter server.
    Endpoint                  *string          `json:"endpoint"`
    // The Clumio-assigned ID of the vCenter server.
    Id                        *string          `json:"id"`
    // The IP address or FQDN of the vCenter server.
    // This field has been replaced by the `endpoint` field
    // and is being retained for backward compatibility reasons.
    IpAddress                 *string          `json:"ip_address"`
    // The Clumio-assigned ID of the organizational unit associated with the vCenter.
    OrganizationalUnitId      *string          `json:"organizational_unit_id"`
    // The connection status of the Clumio Cloud Connector. Examples include "pending", "connected", "disconnected", "invalid_credentials", "partial", and "unavailable".
    Status                    *string          `json:"status"`
    // The type of vCenter server. If the vCenter server's type is unavailable, this field has a value of `unavailable`. Refer to the vCenter Types table for a complete list of vCenter types.
    ClumioType                *string          `json:"type"`
    // The token given to the Clumio Cloud Connectors to identify the vCenter server.
    VcenterToken              *string          `json:"vcenter_token"`
}

// VcenterEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VcenterEmbedded struct {
    // Embeds the compliance statistics of VMs into each vCenter resource in the response, if requested using the `_embed` query parameter.
    ReadVmwareVcenterComplianceStats interface{} `json:"read-vmware-vcenter-compliance-stats"`
}

// VcenterLinks represents a custom type struct.
// URLs to pages related to the resource.
type VcenterLinks struct {
    // The HATEOAS link to this resource.
    Self                             *HateoasSelfLink                             `json:"_self"`
    // A HATEOAS link to the compliance statistics of VMs in the folders and subfolders of this vCenter resource.
    ReadVmwareVcenterComplianceStats *ReadVCenterObjectProtectionStatsHateoasLink `json:"read-vmware-vcenter-compliance-stats"`
}

// VcenterListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VcenterListEmbedded struct {
    // TODO: Add struct field description
    Items []*Vcenter `json:"items"`
}

// VcenterListLinks represents a custom type struct.
// URLs to pages related to the resource.
type VcenterListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// Vm represents a custom type struct
type Vm struct {
    // Embedded responses related to the resource.
    Embedded              *VmEmbedded                   `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                 *VmLinks                      `json:"_links"`
    // The policy compliance status of the resource. If the VM is deleted or unprotected, then this field has a value of `null`. Refer to the Compliance Status table for a complete list of compliance statuses.
    ComplianceStatus      *string                       `json:"compliance_status"`
    // The compute resource from which the VM draws. If the VM is deleted, then `compute_resource.id` has a value of `null`.
    ComputeResource       *VMComputeResourceModel       `json:"compute_resource"`
    // The compute resource folder associated with this VM. If the VM is deleted, then this field has a value of `null`.
    ComputeResourceFolder *VMComputeResourceFolderModel `json:"compute_resource_folder"`
    // The data center in which the VM resides. If the VM is deleted, then `datacenter.id` has a value of `null`.
    Datacenter            *VMDatacenterModel            `json:"datacenter"`
    // The data center folder associated with this VM. If the VM is deleted, then this field has a value of `null`.
    DatacenterFolder      *VMDatacenterFolderModel      `json:"datacenter_folder"`
    // The host on which the VM resides. If the VM is deleted, then `host.id` and `host.is_standalone` have values of `null`. The `host.name` field may also have a value of `null`.
    Host                  *VMHostModel                  `json:"host"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the VM.
    // VMs from different vCenters may have the same VMware-assigned ID.
    Id                    *string                       `json:"id"`
    // Determines whether the VM is deleted. If `true`, the VM is deleted.
    IsDeleted             *bool                         `json:"is_deleted"`
    // Determines whether the VM is supported for backups. If `true`, the VM is supported for backups.
    IsSupported           *bool                         `json:"is_supported"`
    // The timestamp of when the VM was last
    // backed up. If this VM has not been backed up, then this field has a value of `null`.
    LastBackupTimestamp   *string                       `json:"last_backup_timestamp"`
    // The name of the virtual machine.
    Name                  *string                       `json:"name"`
    // The network interface card (NIC) attached to the VM.
    Nics                  []*VMNicModel                 `json:"nics"`
    // The Clumio-assigned ID of the organizational unit associated with the VM.
    OrganizationalUnitId  *string                       `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo        *ProtectionInfo               `json:"protection_info"`
    // The protection status of the resource. If the VM has been deleted, then this field has a value of `null`. Refer to the Protection Status table for a complete list of protection statuses.
    ProtectionStatus      *string                       `json:"protection_status"`
    // The resource pool from which the VM draws. If the VM is deleted, then `resource_pool.id` and `resource_pool.is_root` have values of `null`.
    ResourcePool          *VMResourcePoolModel          `json:"resource_pool"`
    // VMTagWithCategoryModel
    // A tag associated with the VM.
    Tags                  []*VMTagWithCategoryModel     `json:"tags"`
    // The reason why the VM cannot be supported. If the VM is supported, then this field has a value of `null`.
    UnsupportedReason     *string                       `json:"unsupported_reason"`
    // The Clumio-assigned ID of the VM.
    // Use this parameter in the [GET /backups/files/search](#operation/list-files) endpoint
    // to search for files in backups of this VM.
    Uuid                  *string                       `json:"uuid"`
    // The VM folder containing the VM. If the VM is deleted, then `vm_folder.id` has a value of `null`.
    VmFolder              *VMFolderModel                `json:"vm_folder"`
}

// VmComputeResourceLink represents a custom type struct.
// A HATEOAS link to the compute resource from which this VM draws from. Will be omitted for deleted VMs.
type VmComputeResourceLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// VmDatacenterLink represents a custom type struct.
// A HATEOAS link to the data center in which this VM resides. Will be omitted for deleted VMs.
type VmDatacenterLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// VmEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VmEmbedded struct {
    // Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. Unprotected resources will not have an associated policy.
    ReadPolicyDefinition interface{} `json:"read-policy-definition"`
}

// VmFolderLink represents a custom type struct.
// A HATEOAS link to the VM folder in which this VM resides. Will be omitted for deleted VMs.
type VmFolderLink struct {
    // The URI for the referenced operation.
    Href       *string `json:"href"`
    // Determines whether the "href" link is a URI template. If set to `true`, the "href" link is a URI template.
    Templated  *bool   `json:"templated"`
    // The HTTP method to be used with the "href" link for the referenced operation.
    ClumioType *string `json:"type"`
}

// VmLinks represents a custom type struct.
// URLs to pages related to the resource.
type VmLinks struct {
    // The HATEOAS link to this resource.
    Self                             *HateoasSelfLink                 `json:"_self"`
    // A resource-specific HATEOAS link.
    CreateBackupVmwareVm             *HateoasLink                     `json:"create-backup-vmware-vm"`
    // A resource-specific HATEOAS link.
    ListBackupVmwareVms              *HateoasLink                     `json:"list-backup-vmware-vms"`
    // A resource-specific HATEOAS link.
    ListRestoredFiles                *HateoasLink                     `json:"list-restored-files"`
    // A HATEOAS link to protect the entities.
    ProtectEntities                  *ProtectEntitiesHateoasLink      `json:"protect-entities"`
    // A HATEOAS link to the policy protecting this resource. Will be omitted for unprotected entities.
    ReadPolicyDefinition             *ReadPolicyDefinitionHateoasLink `json:"read-policy-definition"`
    // A HATEOAS link to the compute resource from which this VM draws from. Will be omitted for deleted VMs.
    ReadVmwareVcenterComputeResource *VmComputeResourceLink           `json:"read-vmware-vcenter-compute-resource"`
    // A HATEOAS link to the data center in which this VM resides. Will be omitted for deleted VMs.
    ReadVmwareVcenterDatacenter      *VmDatacenterLink                `json:"read-vmware-vcenter-datacenter"`
    // A HATEOAS link to the VM folder in which this VM resides. Will be omitted for deleted VMs.
    ReadVmwareVcenterFolder          *VmFolderLink                    `json:"read-vmware-vcenter-folder"`
    // A HATEOAS link to unprotect the entities.
    UnprotectEntities                *UnprotectEntitiesHateoasLink    `json:"unprotect-entities"`
}

// VmListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type VmListEmbedded struct {
    // TODO: Add struct field description
    Items []*Vm `json:"items"`
}

// VmListLinks represents a custom type struct.
// URLs to pages related to the resource.
type VmListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}

// Wallet represents a custom type struct
type Wallet struct {
    // Embedded responses related to the resource.
    Embedded           interface{}            `json:"_embedded"`
    // URLs to pages related to the resource.
    Links              *WalletLinks           `json:"_links"`
    // AWS Account ID associated with the wallet.
    AccountNativeId    *string                `json:"account_native_id"`
    // Version of the template available
    AvailableVersion   *int64                 `json:"available_version"`
    // Clumio AWS Account ID.
    ClumioAwsAccountId *string                `json:"clumio_aws_account_id"`
    // DeploymentURL is an (external) link to an AWS console page for quick-creation
    // of the stack.
    DeploymentUrl      *string                `json:"deployment_url"`
    // ErrorCode is a short string describing the error, if any.
    ErrorCode          *string                `json:"error_code"`
    // ErrorMessage is a longer description explaining the error, if any, and how to
    // fix it.
    ErrorMessage       *string                `json:"error_message"`
    // The Clumio-assigned ID of the wallet.
    Id                 *string                `json:"id"`
    // The regions where the wallet is installed.
    InstalledRegions   []*string              `json:"installed_regions"`
    // TODO: Add struct field description
    KeyErrors          map[string]*ErrorModel `json:"key_errors"`
    // RoleArn is the AWS Resource Name of the IAM Role created by the stack.
    RoleArn            *string                `json:"role_arn"`
    // The version of the stack used or being used.
    StackVersion       *int64                 `json:"stack_version"`
    // State describes the state of the wallet. Valid states are:
    // Waiting: The wallet has been created, but a stack hasn't been created. The
    // wallet can't be used in this state.
    // Enabled: The wallet has been created and a stack has been created for the
    // wallet. This is the normal expected state of a wallet in use.
    // Error:   The wallet is inaccessible. See ErrorCode and ErrorMessage fields for
    // additional details.
    State              *string                `json:"state"`
    // The supported regions for the wallet.
    SupportedRegions   []*string              `json:"supported_regions"`
    // TemplateURL is the URL to the CloudFormation template to be used to create the
    // CloudFormation stack.
    TemplateUrl        *string                `json:"template_url"`
    // Token is used to identify and authenticate the CloudFormation stack creation.
    Token              *string                `json:"token"`
}

// WalletLinks represents a custom type struct.
// URLs to pages related to the resource.
type WalletLinks struct {
    // The HATEOAS link to this resource.
    Self           *HateoasSelfLink `json:"_self"`
    // A resource-specific HATEOAS link.
    DeleteWallet   *HateoasLink     `json:"delete-wallet"`
    // A resource-specific HATEOAS link.
    ListWalletKeys *HateoasLink     `json:"list-wallet-keys"`
    // A resource-specific HATEOAS link.
    RefreshWallet  *HateoasLink     `json:"refresh-wallet"`
}

// WalletListEmbedded represents a custom type struct.
// Embedded responses related to the resource.
type WalletListEmbedded struct {
    // TODO: Add struct field description
    Items []*Wallet `json:"items"`
}

// WalletListLinks represents a custom type struct.
// URLs to pages related to the resource.
type WalletListLinks struct {
    // The HATEOAS link to the first page of results.
    First *HateoasFirstLink `json:"_first"`
    // The HATEOAS link to the last page of results.
    Last  *HateoasLastLink  `json:"_last"`
    // The HATEOAS link to the next page of results.
    Next  *HateoasNextLink  `json:"_next"`
    // The HATEOAS link to the previous page of results.
    Prev  *HateoasPrevLink  `json:"_prev"`
    // The HATEOAS link to this resource.
    Self  *HateoasSelfLink  `json:"_self"`
}
