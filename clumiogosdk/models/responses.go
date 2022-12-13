// Copyright (c) 2021 Clumio All Rights Reserved

// Package models has the structs representing responses
package models

// AddBucketToProtectionGroupResponse represents a custom type struct for Success
type AddBucketToProtectionGroupResponse struct {
    // The AWS-assigned ID of the account associated with the DynamoDB table.
    AccountNativeId               *string `json:"account_native_id"`
    // Whether this bucket was added to this protection group by the bucket rule
    AddedByBucketRule             *bool   `json:"added_by_bucket_rule"`
    // Whether this bucket was added to this protection group by the user
    AddedByUser                   *bool   `json:"added_by_user"`
    // The AWS region associated with the DynamoDB table.
    AwsRegion                     *string `json:"aws_region"`
    // The Clumio-assigned ID of the bucket
    BucketId                      *string `json:"bucket_id"`
    // The name of the bucket
    BucketName                    *string `json:"bucket_name"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string `json:"created_timestamp"`
    // The Clumio-assigned ID of the AWS environment associated with the protection group.
    EnvironmentId                 *string `json:"environment_id"`
    // The Clumio-assigned ID of the protection group
    GroupId                       *string `json:"group_id"`
    // The name of the protection group
    GroupName                     *string `json:"group_name"`
    // The Clumio-assigned ID that represents the bucket within the protection group.
    Id                            *string `json:"id"`
    // Determines whether the protection group bucket has been deleted
    IsDeleted                     *bool   `json:"is_deleted"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string `json:"last_discover_sync_timestamp"`
    // The Clumio-assigned ID of the organizational unit associated with the protection group.
    OrganizationalUnitId          *string `json:"organizational_unit_id"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64  `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64  `json:"total_backed_up_size_bytes"`
}

// CreateAWSConnectionResponse represents a custom type struct for Success
type CreateAWSConnectionResponse struct {
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

// CreateAWSTemplateResponse represents a custom type struct for Success
type CreateAWSTemplateResponse struct {
    // The latest available URL for the template.
    AvailableTemplateUrl *string                `json:"available_template_url"`
    // TODO: Add struct field description
    Config               *TemplateConfiguration `json:"config"`
}

// CreateAWSTemplateV2Response represents a custom type struct for Success
type CreateAWSTemplateV2Response struct {
    // The latest available URL for the template.
    CloudformationUrl *string                  `json:"cloudformation_url"`
    // TODO: Add struct field description
    Config            *TemplateConfigurationV2 `json:"config"`
    // The latest available URL for the terraform template.
    TerraformUrl      *string                  `json:"terraform_url"`
}

// CreateAutoUserProvisioningRuleResponse represents a custom type struct for Success
type CreateAutoUserProvisioningRuleResponse struct {
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

// CreateHcmHostResponse represents a custom type struct for Success
type CreateHcmHostResponse struct {
    // TODO: Add struct field description
    Hosts []*Host `json:"hosts"`
}

// CreateHostECCredentialsResponse represents a custom type struct for Success
type CreateHostECCredentialsResponse struct {
    // URLs to pages related to the resource.
    Links                    *HostLinks `json:"_links"`
    // The edge connector credentials for the host. This token is required during the installation of the MSI.
    EdgeConnectorCredentials *string    `json:"edge_connector_credentials"`
    // The user-provided endpoint used to connect the host.
    Endpoint                 *string    `json:"endpoint"`
    // The Clumio-assigned ID of the management group associated with the host.
    GroupId                  *string    `json:"group_id"`
    // The Clumio-assigned ID of the Host.
    Id                       *string    `json:"id"`
    // The timestamp of the last successful heartbeat of this host. Represented in RFC-3339 format.
    LastHeartbeatTimestamp   *string    `json:"last_heartbeat_timestamp"`
    // Name of the Host.
    Name                     *string    `json:"name"`
    // The connection status of the Host. Possible values include `connected`, `disconnected`, `connection_pending`, and `invalid_token`.
    Status                   *string    `json:"status"`
    // The Clumio-assigned ID of the management subgroup associated with the host.
    SubgroupId               *string    `json:"subgroup_id"`
    // The Clumio-assigned UUID of the host. This UUID is used for filtering hosts during list operations.
    Uuid                     *string    `json:"uuid"`
}

// CreateMssqlDatabaseRestoreResponse represents a custom type struct for Success
type CreateMssqlDatabaseRestoreResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *ReadTaskHateoasLinks         `json:"_links"`
}

// CreateOrganizationalUnitResponse represents a custom type struct for Success
type CreateOrganizationalUnitResponse struct {
    // Embedded responses related to the resource.
    Embedded                  *EntityGroupEmbedded     `json:"_embedded"`
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

// CreatePolicyResponse represents a custom type struct for Success
type CreatePolicyResponse struct {
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

// CreateProtectionGroupResponse represents a custom type struct for Success
type CreateProtectionGroupResponse struct {
    // Embedded responses related to the resource.
    Embedded                      interface{}                  `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                         *ProtectionGroupVersionLinks `json:"_links"`
    // Number of buckets
    BucketCount                   *int64                       `json:"bucket_count"`
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
    BucketRule                    *string                      `json:"bucket_rule"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string                      `json:"created_timestamp"`
    // The user-assigned description of the protection group.
    Description                   *string                      `json:"description"`
    // The Clumio-assigned ID of the protection group.
    Id                            *string                      `json:"id"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string                      `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string                      `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string                      `json:"last_discover_sync_timestamp"`
    // Modified time of the protection group in RFC-3339 format.
    ModifiedTimestamp             *string                      `json:"modified_timestamp"`
    // The user-assigned name of the protection group.
    Name                          *string                      `json:"name"`
    // ObjectFilter
    // defines which objects will be backed up.
    ObjectFilter                  *ObjectFilter                `json:"object_filter"`
    // The Clumio-assigned ID of the organizational unit associated with the Protection Group.
    OrganizationalUnitId          *string                      `json:"organizational_unit_id"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64                       `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64                       `json:"total_backed_up_size_bytes"`
    // Version of the protection group. The version number is incremented every time
    // a change is made to the protection group.
    Version                       *int64                       `json:"version"`
}

// CreateRdsResourceRestoreResponse represents a custom type struct for Success
type CreateRdsResourceRestoreResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded          `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *CreateRdsDatabaseRestoreResponseLinks `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the `GET /tasks/{task_id}` endpoint.
    TaskId   *string                                `json:"task_id"`
}

// CreateReportDownloadResponse represents a custom type struct for Success
type CreateReportDownloadResponse struct {
    // The Clumio-assigned ID of the task created by the request.
    // The progress of the task can be monitored using the
    // [`GET /tasks/{task_id}`](#operation/list-tasks) endpoint.
    TaskId *string `json:"task_id"`
}

// CreateRuleResponse represents a custom type struct for Success
type CreateRuleResponse struct {
    // URLs to pages related to the resource.
    Links     *ReadTaskHateoasLinks `json:"_links"`
    // The Clumio-assigned ID of the preview generated by this request. Only valid if
    // `execution_type` is set to `dryrun`.
    PreviewId *string               `json:"preview_id"`
    // A rule applies an action subject to a condition criteria.
    Rule      *Rule                 `json:"rule"`
    // The Clumio-assigned ID of the task generated by this request.
    TaskId    *string               `json:"task_id"`
}

// CreateUserResponse represents a custom type struct for Success
type CreateUserResponse struct {
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

// CreateWalletResponse represents a custom type struct for Success
type CreateWalletResponse struct {
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

// DeleteBucketFromProtectionGroupResponse represents a custom type struct for Success
type DeleteBucketFromProtectionGroupResponse struct {
    // The AWS-assigned ID of the account associated with the DynamoDB table.
    AccountNativeId               *string `json:"account_native_id"`
    // Whether this bucket was added to this protection group by the bucket rule
    AddedByBucketRule             *bool   `json:"added_by_bucket_rule"`
    // Whether this bucket was added to this protection group by the user
    AddedByUser                   *bool   `json:"added_by_user"`
    // The AWS region associated with the DynamoDB table.
    AwsRegion                     *string `json:"aws_region"`
    // The Clumio-assigned ID of the bucket
    BucketId                      *string `json:"bucket_id"`
    // The name of the bucket
    BucketName                    *string `json:"bucket_name"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string `json:"created_timestamp"`
    // The Clumio-assigned ID of the AWS environment associated with the protection group.
    EnvironmentId                 *string `json:"environment_id"`
    // The Clumio-assigned ID of the protection group
    GroupId                       *string `json:"group_id"`
    // The name of the protection group
    GroupName                     *string `json:"group_name"`
    // The Clumio-assigned ID that represents the bucket within the protection group.
    Id                            *string `json:"id"`
    // Determines whether the protection group bucket has been deleted
    IsDeleted                     *bool   `json:"is_deleted"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string `json:"last_discover_sync_timestamp"`
    // The Clumio-assigned ID of the organizational unit associated with the protection group.
    OrganizationalUnitId          *string `json:"organizational_unit_id"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64  `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64  `json:"total_backed_up_size_bytes"`
}

// DeleteHcmHostResponse represents a custom type struct for Success
type DeleteHcmHostResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *ReadTaskHateoasLinks         `json:"_links"`
    // TaskID for DeleteHostsReq
    TaskId   *string                       `json:"task_id"`
}

// DeleteOrganizationalUnitResponse represents a custom type struct.
// Accepted
type DeleteOrganizationalUnitResponse struct {
    // Embedded responses related to the resource.
    Embedded *EntityGroupEmbedded  `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *ReadTaskHateoasLinks `json:"_links"`
}

// DeletePolicyResponse represents a custom type struct for Success
type DeletePolicyResponse struct {
    // The Clumio-assigned ID of the task generated by this request.
    TaskId *string `json:"task_id"`
}

// DeleteRuleResponse represents a custom type struct for Success
type DeleteRuleResponse struct {
    // URLs to pages related to the resource.
    Links     *ReadTaskHateoasLinks `json:"_links"`
    // The Clumio-assigned ID of the preview generated by this request. Only valid if
    // `execution_type` is set to `dryrun`.
    PreviewId *string               `json:"preview_id"`
    // The Clumio-assigned ID of the task generated by this request.
    TaskId    *string               `json:"task_id"`
}

// DownloadSharedFileResponse represents a custom type struct for Success
type DownloadSharedFileResponse struct {
    // URLs to pages related to the resource.
    Links       *DownloadSharedFileLinks `json:"_links"`
    // A download link that lets you directly download the file. The link expires
    // 24 hours after file restore.
    DownloadUrl *string                  `json:"download_url"`
}

// EditProfileResponse represents a custom type struct for Success
type EditProfileResponse struct {
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

// Error represents a custom type struct.
// Error
type Error struct {
    // TODO: Add struct field description
    Errors []*SingleErrorResponse `json:"errors"`
}

// FileListResponse represents a custom type struct for Success
type FileListResponse struct {
    // Embedded responses related to the resource.
    Embedded     *FileVersionsListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *FileVersionsListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                    `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                    `json:"limit"`
    // The page token used to get this response.
    Start        *string                   `json:"start"`
}

// FileSearchResponse represents a custom type struct for Success
type FileSearchResponse struct {
    // Embedded responses related to the resource.
    Embedded     *FileSearchListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *FileSearchListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                  `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                  `json:"limit"`
    // The page token used to get this response.
    Start        *string                 `json:"start"`
}

// GenerateRestoredFilePasscodeResponse represents a custom type struct for Success
type GenerateRestoredFilePasscodeResponse struct {
    // URLs to pages related to the resource.
    Links    *GenerateRestoredFilePasscodeLinks `json:"_links"`
    // The new passcode that has been generated for the restored file. Send the
    // passcode to the email recipient, who must use it to access the restored file.
    Passcode *string                            `json:"passcode"`
}

// ListAWSConnectionsResponse represents a custom type struct for Success
type ListAWSConnectionsResponse struct {
    // Embedded responses related to the resource.
    Embedded      *AWSConnectionListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links         *AWSConnectionListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount  *int64                     `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied *string                    `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit         *int64                     `json:"limit"`
    // The page token used to get this response.
    Start         *string                    `json:"start"`
}

// ListAWSEnvironmentsResponse represents a custom type struct for Success
type ListAWSEnvironmentsResponse struct {
    // Embedded responses related to the resource.
    Embedded     *AWSEnvironmentListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *AWSEnvironmentListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                      `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                      `json:"limit"`
    // The page token used to get this response.
    Start        *string                     `json:"start"`
}

// ListAWSRegionsResponse represents a custom type struct for Success
type ListAWSRegionsResponse struct {
    // Embedded responses related to the resource.
    Embedded     *ConnectionRegionListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *ConnectionRegionListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                        `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                        `json:"limit"`
    // The page token used to get this response.
    Start        *string                       `json:"start"`
}

// ListAlertsResponse represents a custom type struct for Success
type ListAlertsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *AlertListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *AlertListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64             `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string            `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64             `json:"limit"`
    // The sort order used in the request.
    SortApplied     *string            `json:"sort_applied"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string            `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64             `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64             `json:"total_pages_count"`
}

// ListAuditTrailsResponse represents a custom type struct for Success
type ListAuditTrailsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *AuditTrailListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *AuditTrailListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                  `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                 `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                  `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                 `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                  `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                  `json:"total_pages_count"`
}

// ListAutoUserProvisioningRulesResponse represents a custom type struct for Success
type ListAutoUserProvisioningRulesResponse struct {
    // Embedded responses related to the resource.
    Embedded     *AutoUserProvisioningRuleListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *AutoUserProvisioningRuleListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                                `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                                `json:"limit"`
    // The page token used to get this response.
    Start        *string                               `json:"start"`
}

// ListAwsTagsResponse represents a custom type struct for Success
type ListAwsTagsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *AwsTagListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *AwsTagListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64              `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string             `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64              `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string             `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64              `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64              `json:"total_pages_count"`
}

// ListBucketsResponse represents a custom type struct for Success
type ListBucketsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *BucketListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *BucketListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64              `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64              `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string             `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64              `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64              `json:"total_pages_count"`
}

// ListComputeResourcesResponse represents a custom type struct for Success
type ListComputeResourcesResponse struct {
    // TODO: Add struct field description
    Computeresourcefolders []*VCenterFolder          `json:"computeResourceFolders"`
    // TODO: Add struct field description
    Computeresources       []*VCenterComputeResource `json:"computeResources"`
}

// ListConsolidatedAlertsResponse represents a custom type struct for Success
type ListConsolidatedAlertsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ConsolidatedAlertListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ConsolidatedAlertListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                         `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                        `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                         `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                        `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                         `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                         `json:"total_pages_count"`
}

// ListDatacentersResponse represents a custom type struct for Success
type ListDatacentersResponse struct {
    // Embedded responses related to the resource.
    Embedded        *DatacenterListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *DatacenterListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                  `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                 `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                  `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                 `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                  `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                  `json:"total_pages_count"`
}

// ListDynamoDBTableBackupsResponse represents a custom type struct for Success
type ListDynamoDBTableBackupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *DynamoDBTableBackupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *DynamoDBTableBackupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                           `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                          `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                           `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                          `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                           `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                           `json:"total_pages_count"`
}

// ListEBSBackupsResponseV1 represents a custom type struct for Success
type ListEBSBackupsResponseV1 struct {
    // Embedded responses related to the resource.
    Embedded        *EBSBackupListEmbeddedV1 `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *EBSBackupListLinksV1    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                   `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                  `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                   `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                  `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                   `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                   `json:"total_pages_count"`
}

// ListEbsVolumesResponse represents a custom type struct for Success
type ListEbsVolumesResponse struct {
    // Embedded responses related to the resource.
    Embedded        *EbsVolumeListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *EbsVolumeListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                 `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                 `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                 `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                 `json:"total_pages_count"`
}

// ListFileSystemsResponse represents a custom type struct for Success
type ListFileSystemsResponse struct {
    // _embedded contains the list of items of a file_system list query
    Embedded        *FileSystemListEmbedded `json:"_embedded"`
    // _links provides URLs to related navigable pages of a file_system list query
    Links           *FileSystemListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                  `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                  `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                 `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                  `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                  `json:"total_pages_count"`
}

// ListFoldersResponse represents a custom type struct for Success
type ListFoldersResponse struct {
    // Embedded responses related to the resource.
    Embedded        *FolderListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *FolderListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64              `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string             `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64              `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string             `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64              `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64              `json:"total_pages_count"`
}

// ListHcmHostsResponse represents a custom type struct for Success
type ListHcmHostsResponse struct {
    // Embedded responses related to the resource.
    Embedded      *HostListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links         *HostListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount  *int64            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied *string           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit         *int64            `json:"limit"`
    // The page token used to get this response.
    Start         *string           `json:"start"`
}

// ListHostsResponse represents a custom type struct for Success
type ListHostsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *HostListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *HostListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64            `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string           `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64            `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64            `json:"total_pages_count"`
}

// ListManagementGroupsResponse represents a custom type struct for Success
type ListManagementGroupsResponse struct {
    // Embedded responses related to the resource.
    Embedded     *ManagementGroupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *ManagementGroupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                       `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                       `json:"limit"`
    // The total count of groups upto 10. Any number of groups beyond 10 will
    // still be returned as 10.
    MinCount     *int64                       `json:"min_count"`
    // The page token used to get this response.
    Start        *string                      `json:"start"`
}

// ListMssqlAGsResponse represents a custom type struct for Success
type ListMssqlAGsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *MssqlAGListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *MssqlAGListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64               `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string              `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64               `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string              `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64               `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64               `json:"total_pages_count"`
}

// ListMssqlDatabaseBackupsResponse represents a custom type struct for Success
type ListMssqlDatabaseBackupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *MssqlDatabaseBackupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *MssqlDatabaseBackupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                           `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                          `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                           `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                          `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                           `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                           `json:"total_pages_count"`
}

// ListMssqlDatabasePitrIntervalsResponse represents a custom type struct.
// ListMssqlDatabasePitrIntervalsResponse represents the success response
type ListMssqlDatabasePitrIntervalsResponse struct {
    // Embedded responses related to the resource.
    Embedded      *MssqlDatabasePitrIntervalListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links         *MssqlDatabasePitrIntervalListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount  *int64                                 `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied *string                                `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit         *int64                                 `json:"limit"`
    // The page token used to get this response.
    Start         *string                                `json:"start"`
}

// ListMssqlDatabasesResponse represents a custom type struct for Success
type ListMssqlDatabasesResponse struct {
    // Embedded responses related to the resource.
    Embedded        *MssqlDatabaseListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *MssqlDatabaseListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                     `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                    `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                     `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                    `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                     `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                     `json:"total_pages_count"`
}

// ListMssqlHostsResponse represents a custom type struct for Success
type ListMssqlHostsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *MssqlHostListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *MssqlHostListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                 `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                 `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                 `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                 `json:"total_pages_count"`
}

// ListMssqlInstancesResponse represents a custom type struct for Success
type ListMssqlInstancesResponse struct {
    // Embedded responses related to the resource.
    Embedded        *MssqlInstanceListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *MssqlInstanceListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                     `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                    `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                     `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                    `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                     `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                     `json:"total_pages_count"`
}

// ListOrganizationalUnitsResponse represents a custom type struct for Success
type ListOrganizationalUnitsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *OrganizationalUnitListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *OrganizationalUnitListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                          `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                         `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                          `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                         `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                          `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                          `json:"total_pages_count"`
}

// ListPoliciesResponse represents a custom type struct for Success
type ListPoliciesResponse struct {
    // An array of embedded resources related to this resource.
    Embedded      *PolicyListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links         *PolicyListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount  *int64              `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied *string             `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit         *int64              `json:"limit"`
    // The page token used to get this response.
    Start         *string             `json:"start"`
}

// ListProtectionGroupBackupsResponse represents a custom type struct for Success
type ListProtectionGroupBackupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ProtectionGroupBackupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ProtectionGroupBackupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                             `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                            `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                             `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                            `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                             `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                             `json:"total_pages_count"`
}

// ListProtectionGroupS3AssetBackupsResponse represents a custom type struct for Success
type ListProtectionGroupS3AssetBackupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ProtectionGroupS3AssetBackupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ProtectionGroupS3AssetBackupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                                    `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                                   `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                                    `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                                   `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                                    `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                                    `json:"total_pages_count"`
}

// ListProtectionGroupS3AssetsResponse represents a custom type struct for Success
type ListProtectionGroupS3AssetsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ProtectionGroupBucketListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ProtectionGroupBucketListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                             `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                             `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                            `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                             `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                             `json:"total_pages_count"`
}

// ListProtectionGroupsResponse represents a custom type struct for Success
type ListProtectionGroupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ProtectionGroupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ProtectionGroupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                       `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                       `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                      `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                       `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                       `json:"total_pages_count"`
}

// ListReportDownloadsResponse represents a custom type struct for Success
type ListReportDownloadsResponse struct {
    // _embedded contains the list of items of a list report CSV download query
    Embedded        *ReportDownloadListEmbedded `json:"_embedded"`
    // _links provides URLs to related navigable pages of a list report CSV download query
    Links           *ReportDownloadListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                      `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                     `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                      `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                     `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                      `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                      `json:"total_pages_count"`
}

// ListResourcePoolsResponse represents a custom type struct for Success
type ListResourcePoolsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *ResourcePoolListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *ResourcePoolListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                    `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                   `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                    `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                   `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                    `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                    `json:"total_pages_count"`
}

// ListRestoredRecordsResponse represents a custom type struct for Success
type ListRestoredRecordsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *RestoredRecordListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *RestoredRecordListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                      `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                      `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                     `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                      `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                      `json:"total_pages_count"`
}

// ListRolesResponse represents a custom type struct for Success
type ListRolesResponse struct {
    // Embedded responses related to the resource.
    Embedded        *RoleListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *RoleListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64            `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string           `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64            `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64            `json:"total_pages_count"`
}

// ListRulesResponse represents a custom type struct for Success
type ListRulesResponse struct {
    // An array of embedded resources related to this resource.
    Embedded     *RuleListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *RuleListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64            `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64            `json:"limit"`
    // The page token used to get this response.
    Start        *string           `json:"start"`
}

// ListSubgroupsResponse represents a custom type struct for Success
type ListSubgroupsResponse struct {
    // Embedded responses related to the resource.
    Embedded     *SubgroupListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *SubgroupListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                `json:"limit"`
    // The total count of subgroups upto 20. Any number of subgroups beyond 20
    // will still be returned as 20.
    MinCount     *int64                `json:"min_count"`
    // The page token used to get this response.
    Start        *string               `json:"start"`
}

// ListTagCategories2Response represents a custom type struct for Success
type ListTagCategories2Response struct {
    // Embedded responses related to the resource
    Embedded        *TagCategory2ListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource
    Links           *TagCategory2ListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                    `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                    `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                   `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                    `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                    `json:"total_pages_count"`
}

// ListTagsResponse represents a custom type struct for Success
type ListTagsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *Tag2ListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *Tag2ListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64            `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string           `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64            `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64            `json:"total_pages_count"`
}

// ListTasksResponse represents a custom type struct for Success
type ListTasksResponse struct {
    // Embedded responses related to the resource.
    Embedded        *TaskListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *TaskListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64            `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string           `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64            `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64            `json:"total_pages_count"`
}

// ListUsersResponse represents a custom type struct for Success
type ListUsersResponse struct {
    // Embedded responses related to the resource.
    Embedded        *UserListEmbedded     `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *UserListHateoasLinks `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string               `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string               `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                `json:"total_pages_count"`
}

// ListVMBackupsResponse represents a custom type struct for Success
type ListVMBackupsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *VMBackupListEmbedded     `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *VMBackupListHateoasLinks `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                    `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                   `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                    `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                   `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                    `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                    `json:"total_pages_count"`
}

// ListVMwareDatastoresResponse represents a custom type struct for Success
type ListVMwareDatastoresResponse struct {
    // Embedded responses related to the resource.
    Embedded        *VMwareDatastoreListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *VMwareDatastoreListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                       `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                      `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                       `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                      `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                       `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                       `json:"total_pages_count"`
}

// ListVMwareVCenterNetworksResponse represents a custom type struct for Success
type ListVMwareVCenterNetworksResponse struct {
    // Embedded responses related to the resource.
    Embedded        *VMwareVCenterNetworkListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *VMwareVCenterNetworkListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                            `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string                           `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                            `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                           `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                            `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                            `json:"total_pages_count"`
}

// ListVcentersResponse represents a custom type struct for Success
type ListVcentersResponse struct {
    // Embedded responses related to the resource.
    Embedded        *VcenterListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *VcenterListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64               `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64               `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string              `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64               `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64               `json:"total_pages_count"`
}

// ListVmsResponse represents a custom type struct for Success
type ListVmsResponse struct {
    // Embedded responses related to the resource.
    Embedded        *VmListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *VmListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64          `json:"current_count"`
    // The filter used in the request. The filter includes both manually-specified and system-generated filters.
    FilterApplied   *string         `json:"filter_applied"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64          `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string         `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64          `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64          `json:"total_pages_count"`
}

// ListWalletsResponse represents a custom type struct for Success
type ListWalletsResponse struct {
    // Embedded responses related to the resource.
    Embedded     *WalletListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *WalletListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64              `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64              `json:"limit"`
    // The page token used to get this response.
    Start        *string             `json:"start"`
}

// MoveHcmHostsResponse represents a custom type struct for Success
type MoveHcmHostsResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *MoveHostsLinks               `json:"_links"`
    // TaskID for MoveHostsReq
    TaskId   *string                       `json:"task_id"`
}

// OnDemandDynamoDBBackupResponse represents a custom type struct for Success
type OnDemandDynamoDBBackupResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *OnDemandDynamoDBBackupLinks  `json:"_links"`
    // The Clumio-assigned ID of the task created for DynamoDB backup.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// OnDemandMssqlBackupResponse represents a custom type struct for Success
type OnDemandMssqlBackupResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *ReadTaskHateoasLinks         `json:"_links"`
}

// PatchGeneralSettingsResponseV2 represents a custom type struct for Success
type PatchGeneralSettingsResponseV2 struct {
    // URLs to pages related to the resource.
    Links                        *GeneralSettingsLinks `json:"_links"`
    // The length of time before a user is logged out of the Clumio system due to inactivity. Measured in seconds.
    // The valid range is between `600` seconds (10 minutes) and `3600` seconds (60 minutes).
    // If not configured, the value defaults to `900` seconds (15 minutes).
    AutoLogoutDuration           *int64                `json:"auto_logout_duration"`
    // The designated range of IP addresses that are allowed to access the Clumio REST API.
    // API requests that originate from outside this list will be blocked.
    // The IP address of the server from which this request is being made must be in this list; otherwise, the request will fail.
    // Set the parameter to individual IP addresses and/or a range of IP addresses in CIDR notation.
    // For example, `["193.168.1.0/24", "193.172.1.1"]`.
    // If not configured, the value defaults to ["0.0.0.0/0"] meaning all addresses will be allowed.
    IpAllowlist                  []*string             `json:"ip_allowlist"`
    // The grouping criteria for each datasource type.
    // These can only be edited for datasource types which do not have any
    // organizational units configured.
    OrganizationalUnitDataGroups *OUGroupingCriteria   `json:"organizational_unit_data_groups"`
    // The length of time a user password is valid before it must be changed. Measured in seconds.
    // The valid range is between `2592000` seconds (30 days) and `15552000` seconds (180 days).
    // If not configured, the value defaults to `7776000` seconds (90 days).
    PasswordExpirationDuration   *int64                `json:"password_expiration_duration"`
}

// PatchOrganizationalUnitResponse represents a custom type struct.
// Accepted
type PatchOrganizationalUnitResponse struct {
    // Embedded responses related to the resource.
    Embedded                  *EntityGroupEmbedded     `json:"_embedded"`
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

// ReadAWSConnectionResponse represents a custom type struct for Success
type ReadAWSConnectionResponse struct {
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

// ReadAWSEnvironmentResponse represents a custom type struct for Success
type ReadAWSEnvironmentResponse struct {
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

// ReadAWSTemplatesResponse represents a custom type struct for Success
type ReadAWSTemplatesResponse struct {
    // The latest available CloudFormation template for Clumio Discover.
    Discover *DiscoverTemplateInfo `json:"discover"`
    // The latest available CloudFormation template for Clumio Cloud Protect.
    Protect  *ProtectTemplateInfo  `json:"protect"`
}

// ReadAWSTemplatesV2Response represents a custom type struct for Success
type ReadAWSTemplatesV2Response struct {
    // TODO: Add struct field description
    Config *TemplateConfigurationV2 `json:"config"`
}

// ReadAlertResponse represents a custom type struct for Success
type ReadAlertResponse struct {
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

// ReadAutoUserProvisioningRuleResponse represents a custom type struct for Success
type ReadAutoUserProvisioningRuleResponse struct {
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

// ReadAutoUserProvisioningSettingResponse represents a custom type struct for Success
type ReadAutoUserProvisioningSettingResponse struct {
    // URLs to pages related to the resource.
    Links     *AutoUserProvisioningSettingLinks `json:"_links"`
    // Whether auto user provisioning is enabled or not.
    IsEnabled *bool                             `json:"is_enabled"`
}

// ReadAwsTagResponse represents a custom type struct for Success
type ReadAwsTagResponse struct {
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

// ReadBucketResponse represents a custom type struct for Success
type ReadBucketResponse struct {
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

// ReadComputeResourceResponse represents a custom type struct for Success
type ReadComputeResourceResponse struct {
    // Embedded responses related to the resource.
    Embedded              *ComputeResourceEmbedded                     `json:"_embedded"`
    // The ETag value.
    Etag                  *string                                      `json:"_etag"`
    // URLs to pages related to the resource.
    Links                 *ComputeResourceLinks                        `json:"_links"`
    // The compute resource folder in which the compute resource resides.
    ComputeResourceFolder *VMwareVCenterComputeResourceFolderModel     `json:"compute_resource_folder"`
    // The data center associated with this compute resource.
    Datacenter            *VMwareVCenterComputeResourceDatacenterModel `json:"datacenter"`
    // The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    Id                    *string                                      `json:"id"`
    // Determines whether the compute resource is a cluster. If `true`, then the compute resource is a cluster.
    IsCluster             *bool                                        `json:"is_cluster"`
    // Determines whether the compute resource has Distributed Resource Scheduler (DRS) enabled. If this field and `"is_cluster":true`, then DRS is enabled in the compute resource cluster.
    IsDrsEnabled          *bool                                        `json:"is_drs_enabled"`
    // The VMware-assigned name of the compute resource.
    Name                  *string                                      `json:"name"`
    // The Clumio-assigned ID of the organizational unit associated with the compute resource.
    OrganizationalUnitId  *string                                      `json:"organizational_unit_id"`
    // The protection policy applied to this resource. If the resource is not protected, then this field has a value of `null`.
    ProtectionInfo        *ProtectionInfo                              `json:"protection_info"`
    // The protection status of this compute resource. Refer to the Protection Status table for a complete list of protection statuses.
    ProtectionStatus      *string                                      `json:"protection_status"`
}

// ReadConsolidatedAlertResponse represents a custom type struct for Success
type ReadConsolidatedAlertResponse struct {
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

// ReadDatacenterResponse represents a custom type struct for Success
type ReadDatacenterResponse struct {
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

// ReadDirectoryResponse represents a custom type struct for Success
type ReadDirectoryResponse struct {
    // Embedded responses related to the resource.
    Embedded     *DirectoryBrowseEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links        *DirectoryBrowseLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount *int64                   `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit        *int64                   `json:"limit"`
    // The page token used to get this response.
    Start        *string                  `json:"start"`
}

// ReadDynamoDBTableBackupResponse represents a custom type struct for Success
type ReadDynamoDBTableBackupResponse struct {
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

// ReadEBSBackupResponseV1 represents a custom type struct for Success
type ReadEBSBackupResponseV1 struct {
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

// ReadEbsTagComplianceStatsResponse represents a custom type struct for Success
type ReadEbsTagComplianceStatsResponse struct {
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

// ReadEbsVolumeResponse represents a custom type struct for Success
type ReadEbsVolumeResponse struct {
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

// ReadFileSystemResponse represents a custom type struct for Success
type ReadFileSystemResponse struct {
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

// ReadFolderResponse represents a custom type struct for Success
type ReadFolderResponse struct {
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

// ReadGeneralSettingsResponseV2 represents a custom type struct for Success
type ReadGeneralSettingsResponseV2 struct {
    // URLs to pages related to the resource.
    Links                        *GeneralSettingsLinks `json:"_links"`
    // The length of time before a user is logged out of the Clumio system due to inactivity. Measured in seconds.
    // The valid range is between `600` seconds (10 minutes) and `3600` seconds (60 minutes).
    // If not configured, the value defaults to `900` seconds (15 minutes).
    AutoLogoutDuration           *int64                `json:"auto_logout_duration"`
    // The designated range of IP addresses that are allowed to access the Clumio REST API.
    // API requests that originate from outside this list will be blocked.
    // The IP address of the server from which this request is being made must be in this list; otherwise, the request will fail.
    // Set the parameter to individual IP addresses and/or a range of IP addresses in CIDR notation.
    // For example, `["193.168.1.0/24", "193.172.1.1"]`.
    // If not configured, the value defaults to ["0.0.0.0/0"] meaning all addresses will be allowed.
    IpAllowlist                  []*string             `json:"ip_allowlist"`
    // The grouping criteria for each datasource type.
    // These can only be edited for datasource types which do not have any
    // organizational units configured.
    OrganizationalUnitDataGroups *OUGroupingCriteria   `json:"organizational_unit_data_groups"`
    // The length of time a user password is valid before it must be changed. Measured in seconds.
    // The valid range is between `2592000` seconds (30 days) and `15552000` seconds (180 days).
    // If not configured, the value defaults to `7776000` seconds (90 days).
    PasswordExpirationDuration   *int64                `json:"password_expiration_duration"`
}

// ReadHcmHostResponse represents a custom type struct for Success
type ReadHcmHostResponse struct {
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

// ReadHostResponse represents a custom type struct for Success
type ReadHostResponse struct {
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

// ReadManagementGroupResponse represents a custom type struct for Success
type ReadManagementGroupResponse struct {
    // URLs to pages related to the resource.
    Links                 *ManagementGroupLinks `json:"_links"`
    // Determines whether backups are allowed to occur across different subgroups or cloud connectors.
    BackupAcrossSubgroups *bool                 `json:"backup_across_subgroups"`
    // The Clumio-assigned ID of the management group.
    Id                    *string               `json:"id"`
    // The name of the management group.
    Name                  *string               `json:"name"`
    // The type of the management group. Possible values include `on_prem`.
    ClumioType            *string               `json:"type"`
    // The Clumio-assigned ID of the vCenter server associated with the management group.
    // All management groups are associated with a vCenter server.
    VcenterId             *string               `json:"vcenter_id"`
}

// ReadMssqlAGResponse represents a custom type struct for Success
type ReadMssqlAGResponse struct {
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

// ReadMssqlDatabaseBackupResponse represents a custom type struct for Success
type ReadMssqlDatabaseBackupResponse struct {
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

// ReadMssqlDatabaseResponse represents a custom type struct for Success
type ReadMssqlDatabaseResponse struct {
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

// ReadMssqlHostResponse represents a custom type struct for Success
type ReadMssqlHostResponse struct {
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

// ReadMssqlInstanceResponse represents a custom type struct for Success
type ReadMssqlInstanceResponse struct {
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

// ReadOrganizationalUnitResponse represents a custom type struct for Success
type ReadOrganizationalUnitResponse struct {
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

// ReadPolicyResponse represents a custom type struct for Success
type ReadPolicyResponse struct {
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

// ReadProtectionGroupBackupResponse represents a custom type struct for Success
type ReadProtectionGroupBackupResponse struct {
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

// ReadProtectionGroupResponse represents a custom type struct for Success
type ReadProtectionGroupResponse struct {
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
    // The list of AWS regions that this protection group is linked to
    Regions                       []*string                             `json:"regions"`
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

// ReadProtectionGroupS3AssetBackupResponse represents a custom type struct for Success
type ReadProtectionGroupS3AssetBackupResponse struct {
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

// ReadProtectionGroupS3AssetResponse represents a custom type struct for Success
type ReadProtectionGroupS3AssetResponse struct {
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

// ReadResourcePoolResponse represents a custom type struct for Success
type ReadResourcePoolResponse struct {
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

// ReadRoleResponse represents a custom type struct for Success
type ReadRoleResponse struct {
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

// ReadRuleResponse represents a custom type struct for Success
type ReadRuleResponse struct {
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

// ReadSubgroupResponse represents a custom type struct for Success
type ReadSubgroupResponse struct {
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

// ReadTagCategory2Response represents a custom type struct for Success
type ReadTagCategory2Response struct {
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

// ReadTagResponse represents a custom type struct for Success
type ReadTagResponse struct {
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

// ReadTaskResponse represents a custom type struct for Success
type ReadTaskResponse struct {
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

// ReadUserResponse represents a custom type struct for Success
type ReadUserResponse struct {
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

// ReadVMBackupResponse represents a custom type struct for Success
type ReadVMBackupResponse struct {
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

// ReadVMwareComputeResourceStatsResponse represents a custom type struct for Success
type ReadVMwareComputeResourceStatsResponse struct {
    // The ETag value.
    Etag               *string                                    `json:"_etag"`
    // URLs to pages related to the resource.
    Links              *VMwareComputeResourceComplianceStatsLinks `json:"_links"`
    // The total number of compliant entities.
    CompliantCount     *int64                                     `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64                                     `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool                                      `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64                                     `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64                                     `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64                                     `json:"unprotected_count"`
}

// ReadVMwareDatacenterStatsResponse represents a custom type struct for Success
type ReadVMwareDatacenterStatsResponse struct {
    // The ETag value.
    Etag               *string                     `json:"_etag"`
    // URLs to pages related to the resource.
    Links              *VMwareDatacenterStatsLinks `json:"_links"`
    // The total number of compliant entities.
    CompliantCount     *int64                      `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64                      `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool                       `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64                      `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64                      `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64                      `json:"unprotected_count"`
}

// ReadVMwareDatastoreResponse represents a custom type struct for Success
type ReadVMwareDatastoreResponse struct {
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

// ReadVMwareFolderStatsResponse represents a custom type struct for Success
type ReadVMwareFolderStatsResponse struct {
    // The ETag value.
    Etag               *string                 `json:"_etag"`
    // URLs to pages related to the resource.
    Links              *VMwareFolderStatsLinks `json:"_links"`
    // The total number of compliant entities.
    CompliantCount     *int64                  `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64                  `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool                   `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64                  `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64                  `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64                  `json:"unprotected_count"`
}

// ReadVMwareTagStatsResponse represents a custom type struct for Success
type ReadVMwareTagStatsResponse struct {
    // The ETag value.
    Etag               *string              `json:"_etag"`
    // URLs to pages related to the resource.
    Links              *VMwareTagStatsLinks `json:"_links"`
    // The total number of compliant entities.
    CompliantCount     *int64               `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64               `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool                `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64               `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64               `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64               `json:"unprotected_count"`
}

// ReadVMwareVCenterNetworkResponse represents a custom type struct for Success
type ReadVMwareVCenterNetworkResponse struct {
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

// ReadVMwareVCenterProtectionStatsResponse represents a custom type struct for Success
type ReadVMwareVCenterProtectionStatsResponse struct {
    // URLs to pages related to the resource.
    Links              *ReadVMwareVCenterProtectionStatsLinks `json:"_links"`
    // The total number of compliant entities.
    CompliantCount     *int64                                 `json:"compliant_count"`
    // The total number of entities associated with deactivated policies.
    DeactivatedCount   *int64                                 `json:"deactivated_count"`
    // Determines whether one or more entities is currently seeding or waiting for seeding.
    // If set to `true`, at least one entity is currently seeding or waiting for seeding.
    HasSeedingEntities *bool                                  `json:"has_seeding_entities"`
    // The total number of non-compliant entities.
    NonCompliantCount  *int64                                 `json:"non_compliant_count"`
    // The number of entities with protection applied.
    ProtectedCount     *int64                                 `json:"protected_count"`
    // The number of entities without protection applied.
    UnprotectedCount   *int64                                 `json:"unprotected_count"`
}

// ReadVcenterResponse represents a custom type struct for Success
type ReadVcenterResponse struct {
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

// ReadVmResponse represents a custom type struct for Success
type ReadVmResponse struct {
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

// ReadWalletResponse represents a custom type struct for Success
type ReadWalletResponse struct {
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

// RefreshWalletResponse represents a custom type struct for Success
type RefreshWalletResponse struct {
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

// RestoreDynamoDBTableResponse represents a custom type struct for Success
type RestoreDynamoDBTableResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreDynamoDBTableLinks    `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoreEBSResponse represents a custom type struct for Success
type RestoreEBSResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreEBSLinks              `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoreEC2Response represents a custom type struct for Success
type RestoreEC2Response struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreEC2Links              `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoreFileResponse represents a custom type struct for Success
type RestoreFileResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreFileLinks             `json:"_links"`
    // The Clumio-assigned ID of the restored file.
    Id       *string                       `json:"id"`
    // The passcode that the end-user must use to access the restored
    // file, in the case the restored file was emailed to the end-user as part
    // of transparent data access.
    Passcode *string                       `json:"passcode"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoreProtectionGroupResponse represents a custom type struct for Success
type RestoreProtectionGroupResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreProtectionGroupLinks  `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoreProtectionGroupS3AssetResponse represents a custom type struct for Success
type RestoreProtectionGroupS3AssetResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded       `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreProtectionGroupS3AssetLinks `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request.
    // The progress of the task can be monitored using the
    // `GET /tasks/{task_id}` endpoint.
    TaskId   *string                             `json:"task_id"`
}

// RestoreRecordPreviewResponse represents a custom type struct.
// Preview Success
type RestoreRecordPreviewResponse struct {
    // TODO: Add struct field description
    Links         *HateoasCommonLinks           `json:"_links"`
    // The preview of the query result, if `preview:true` in the request.
    // If preview was not set to true in the request, then the result of the query will be
    // available for download asynchronously.
    PreviewResult *RDSLogicalPreviewQueryResult `json:"preview_result"`
}

// RestoreRecordResponse represents a custom type struct for Success
type RestoreRecordResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded     `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *CreateRestoreRecordResponseLinks `json:"_links"`
    // The Clumio-assigned ID of the task generated by this request.
    // The requested records will be available for asynchronous download when the Task completes.
    // Use the [GET /restores/aws/rds-resources/records](#operation/list-rds-restored-records)
    // endpoint to list the records available for download. 
    // If `"preview":true` was set in the request, then a preview of the result
    // will be given instead of a Task ID.
    TaskId   *string                           `json:"task_id"`
}

// RestoreRecordsResponseAsync represents a custom type struct.
// Records restore request accepted
type RestoreRecordsResponseAsync struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *RestoreRecordsLinksAsync     `json:"_links"`
    // passcode that the end-user must use to access the restored
    // file, in case when restored file was emailed to the end-user as part
    // of transparent data access.
    Passcode *string                       `json:"passcode"`
    // The Clumio-assigned ID of the task generated by this request.
    // The requested records will be available for asynchronous download when the Task completes.
    // Use the [GET /restores/aws/dynamodb-tables/records](#operation/list-restored-records-aws-dynamodb-table)
    // endpoint to list the records available for download. 
    // If `"preview":true` was set in the request, then a preview of the result
    // will be given instead of a Task ID, and this field will be omitted.
    TaskId   *string                       `json:"task_id"`
}

// RestoreRecordsResponseSync represents a custom type struct.
// Records preview success
type RestoreRecordsResponseSync struct {
    // URLs to pages related to the resource.
    Links         *RestoreRecordsLinksSync    `json:"_links"`
    // If preview was not set to true in the request, then the result of the query will be
    // available for download asynchronously and this field has a value of `null`.
    PreviewResult *DynamoDBQueryPreviewResult `json:"preview_result"`
}

// RestoreVMwareVMResponse represents a custom type struct for Success
type RestoreVMwareVMResponse struct {
    // Embedded responses related to the resource.
    Embedded *ReadTaskHateoasOuterEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links    *ReadTaskHateoasLinks         `json:"_links"`
    // The Clumio-assigned ID of the task created by this restore request. The progress of the task can be monitored using the `GET /tasks/{task_id}` endpoint.
    TaskId   *string                       `json:"task_id"`
}

// RestoredFilesResponse represents a custom type struct for Success
type RestoredFilesResponse struct {
    // Embedded responses related to the resource.
    Embedded        *RestoredFilesListEmbedded `json:"_embedded"`
    // URLs to pages related to the resource.
    Links           *RestoredFilesListLinks    `json:"_links"`
    // The number of items listed on the current page.
    CurrentCount    *int64                     `json:"current_count"`
    // The maximum number of items displayed per page in the response.
    Limit           *int64                     `json:"limit"`
    // The page number used to get this response.
    // Pages are indexed starting from 1 (i.e., `"start": "1"`).
    Start           *string                    `json:"start"`
    // The total number of items, summed across all pages.
    TotalCount      *int64                     `json:"total_count"`
    // The total number of pages of results.
    TotalPagesCount *int64                     `json:"total_pages_count"`
}

// SetAssignmentsResponse represents a custom type struct for Success
type SetAssignmentsResponse struct {
    // URLs to pages related to the resource.
    Links  *ReadTaskHateoasLinks `json:"_links"`
    // The Clumio-assigned ID of the task generated by this request.
    TaskId *string               `json:"task_id"`
}

// SetBucketPropertiesResponse represents a custom type struct.
// Accepted
type SetBucketPropertiesResponse struct {
    // TODO: Add struct field description
    Links *SetBucketPropertiesResponseLinks `json:"_links"`
}

// ShareFileRestoreEmailResponse represents a custom type struct for Success
type ShareFileRestoreEmailResponse struct {
    // URLs to pages related to the resource.
    Links *ShareFileRestoreEmailLinks `json:"_links"`
}

// UpdateAWSConnectionResponse represents a custom type struct for Success
type UpdateAWSConnectionResponse struct {
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

// UpdateAlertResponse represents a custom type struct for Success
type UpdateAlertResponse struct {
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

// UpdateAutoUserProvisioningRuleResponse represents a custom type struct for Success
type UpdateAutoUserProvisioningRuleResponse struct {
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

// UpdateAutoUserProvisioningSettingResponse represents a custom type struct for Success
type UpdateAutoUserProvisioningSettingResponse struct {
    // URLs to pages related to the resource.
    Links     *AutoUserProvisioningSettingLinks `json:"_links"`
    // Whether auto user provisioning is enabled or not.
    IsEnabled *bool                             `json:"is_enabled"`
}

// UpdateConsolidatedAlertResponse represents a custom type struct for Success
type UpdateConsolidatedAlertResponse struct {
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

// UpdateManagementGroupResponse represents a custom type struct for Success
type UpdateManagementGroupResponse struct {
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

// UpdatePolicyResponse represents a custom type struct for Success
type UpdatePolicyResponse struct {
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
    // The Clumio-assigned ID of the task generated by this request.
    TaskId               *string            `json:"task_id"`
    // The timezone for the policy.
    Timezone             *string            `json:"timezone"`
    // The updated time of the policy in unix time.
    UpdatedTime          *int64             `json:"updated_time"`
}

// UpdateProtectionGroupResponse represents a custom type struct for Success
type UpdateProtectionGroupResponse struct {
    // Embedded responses related to the resource.
    Embedded                      interface{}                  `json:"_embedded"`
    // URLs to pages related to the resource.
    Links                         *ProtectionGroupVersionLinks `json:"_links"`
    // Number of buckets
    BucketCount                   *int64                       `json:"bucket_count"`
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
    BucketRule                    *string                      `json:"bucket_rule"`
    // Creation time of the protection group in RFC-3339 format.
    CreatedTimestamp              *string                      `json:"created_timestamp"`
    // The user-assigned description of the protection group.
    Description                   *string                      `json:"description"`
    // The Clumio-assigned ID of the protection group.
    Id                            *string                      `json:"id"`
    // Time of the last backup in RFC-3339 format.
    LastBackupTimestamp           *string                      `json:"last_backup_timestamp"`
    // Time of the last successful continuous backup in RFC-3339 format.
    LastContinuousBackupTimestamp *string                      `json:"last_continuous_backup_timestamp"`
    // Time of the last discover sync in RFC-3339 format.
    LastDiscoverSyncTimestamp     *string                      `json:"last_discover_sync_timestamp"`
    // Modified time of the protection group in RFC-3339 format.
    ModifiedTimestamp             *string                      `json:"modified_timestamp"`
    // The user-assigned name of the protection group.
    Name                          *string                      `json:"name"`
    // ObjectFilter
    // defines which objects will be backed up.
    ObjectFilter                  *ObjectFilter                `json:"object_filter"`
    // The Clumio-assigned ID of the organizational unit associated with the Protection Group.
    OrganizationalUnitId          *string                      `json:"organizational_unit_id"`
    // Cumulative count of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpObjectCount      *int64                       `json:"total_backed_up_object_count"`
    // Cumulative size of all unexpired objects in each backup (any new or updated since
    // the last backup) that have been backed up as part of this protection group
    TotalBackedUpSizeBytes        *int64                       `json:"total_backed_up_size_bytes"`
    // Version of the protection group. The version number is incremented every time
    // a change is made to the protection group.
    Version                       *int64                       `json:"version"`
}

// UpdateRuleResponse represents a custom type struct for Success
type UpdateRuleResponse struct {
    // URLs to pages related to the resource.
    Links     *ReadTaskHateoasLinks `json:"_links"`
    // The Clumio-assigned ID of the preview generated by this request. Only valid if
    // `execution_type` is set to `dryrun`.
    PreviewId *string               `json:"preview_id"`
    // A rule applies an action subject to a condition criteria.
    Rule      *Rule                 `json:"rule"`
    // The Clumio-assigned ID of the task generated by this request.
    TaskId    *string               `json:"task_id"`
}

// UpdateSubgroupResponse represents a custom type struct for Success
type UpdateSubgroupResponse struct {
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

// UpdateTaskResponse represents a custom type struct for Success
type UpdateTaskResponse struct {
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

// UpdateUserResponse represents a custom type struct for Success
type UpdateUserResponse struct {
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
