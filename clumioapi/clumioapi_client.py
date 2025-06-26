#
# Copyright 2023. Clumio, Inc.
#
import functools

from clumioapi import configuration
from clumioapi.controllers import audit_trails_v1
from clumioapi.controllers import auto_user_provisioning_rules_v1
from clumioapi.controllers import auto_user_provisioning_settings_v1
from clumioapi.controllers import aws_connection_groups_v1
from clumioapi.controllers import aws_connections_v1
from clumioapi.controllers import aws_dynamodb_tables_v1
from clumioapi.controllers import aws_ebs_volumes_v1
from clumioapi.controllers import aws_ec2_instances_v1
from clumioapi.controllers import aws_environment_tags_v1
from clumioapi.controllers import aws_environments_v1
from clumioapi.controllers import aws_rds_resource_restored_records_v1
from clumioapi.controllers import aws_rds_resources_v1
from clumioapi.controllers import aws_regions_v1
from clumioapi.controllers import aws_s3_buckets_v1
from clumioapi.controllers import aws_templates_v1
from clumioapi.controllers import backup_aws_dynamodb_tables_v1
from clumioapi.controllers import backup_aws_ebs_volumes_v1
from clumioapi.controllers import backup_aws_ebs_volumes_v2
from clumioapi.controllers import backup_aws_ec2_instances_v1
from clumioapi.controllers import backup_aws_rds_resource_database_tables_v1
from clumioapi.controllers import backup_aws_rds_resource_databases_v1
from clumioapi.controllers import backup_aws_rds_resources_v1
from clumioapi.controllers import backup_ec2_mssql_databases_v1
from clumioapi.controllers import backup_filesystem_directories_v1
from clumioapi.controllers import backup_filesystems_v1
from clumioapi.controllers import backup_protection_groups_v1
from clumioapi.controllers import backups_files_v1
from clumioapi.controllers import consolidated_alerts_v1
from clumioapi.controllers import ec2_mssql_availability_groups_v1
from clumioapi.controllers import ec2_mssql_databases_v1
from clumioapi.controllers import ec2_mssql_failover_cluster_v1
from clumioapi.controllers import ec2_mssql_failover_clusters_v1
from clumioapi.controllers import ec2_mssql_hosts_v1
from clumioapi.controllers import ec2_mssql_instance_v1
from clumioapi.controllers import general_settings_v2
from clumioapi.controllers import individual_alerts_v1
from clumioapi.controllers import management_groups_v1
from clumioapi.controllers import organizational_units_v1
from clumioapi.controllers import organizational_units_v2
from clumioapi.controllers import policy_assignments_v1
from clumioapi.controllers import policy_definitions_v1
from clumioapi.controllers import policy_rules_v1
from clumioapi.controllers import post_process_aws_connection_v1
from clumioapi.controllers import post_process_kms_v1
from clumioapi.controllers import protection_groups_s3_assets_v1
from clumioapi.controllers import protection_groups_v1
from clumioapi.controllers import report_compliance_runs_v1
from clumioapi.controllers import report_compliance_v1
from clumioapi.controllers import report_downloads_v1
from clumioapi.controllers import restore_ec2_mssql_database_v1
from clumioapi.controllers import restored_aws_dynamodb_tables_v1
from clumioapi.controllers import restored_aws_ebs_volumes_v1
from clumioapi.controllers import restored_aws_ebs_volumes_v2
from clumioapi.controllers import restored_aws_ec2_instances_v1
from clumioapi.controllers import restored_aws_rds_resources_v1
from clumioapi.controllers import restored_aws_s3_buckets_v1
from clumioapi.controllers import restored_files_v1
from clumioapi.controllers import restored_protection_group_instant_access_endpoints_v1
from clumioapi.controllers import restored_protection_group_s3_assets_v1
from clumioapi.controllers import restored_protection_groups_v1
from clumioapi.controllers import restored_records_aws_dynamodb_tables_v1
from clumioapi.controllers import roles_v1
from clumioapi.controllers import tasks_v1
from clumioapi.controllers import users_v1
from clumioapi.controllers import users_v2
from clumioapi.controllers import wallets_v1


class ClumioAPIClient:
    """Client for the Clumio APIs."""

    def __init__(self, config: configuration.Configuration = None) -> None:
        self.config: configuration.Configuration = config or configuration.Configuration()

    @property
    @functools.lru_cache(1)
    def consolidated_alerts_v1(self) -> consolidated_alerts_v1.ConsolidatedAlertsV1Controller:
        return consolidated_alerts_v1.ConsolidatedAlertsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def individual_alerts_v1(self) -> individual_alerts_v1.IndividualAlertsV1Controller:
        return individual_alerts_v1.IndividualAlertsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def audit_trails_v1(self) -> audit_trails_v1.AuditTrailsV1Controller:
        return audit_trails_v1.AuditTrailsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_dynamodb_tables_v1(
        self,
    ) -> backup_aws_dynamodb_tables_v1.BackupAwsDynamodbTablesV1Controller:
        return backup_aws_dynamodb_tables_v1.BackupAwsDynamodbTablesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_ebs_volumes_v2(
        self,
    ) -> backup_aws_ebs_volumes_v2.BackupAwsEbsVolumesV2Controller:
        return backup_aws_ebs_volumes_v2.BackupAwsEbsVolumesV2Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_ebs_volumes_v1(
        self,
    ) -> backup_aws_ebs_volumes_v1.BackupAwsEbsVolumesV1Controller:
        return backup_aws_ebs_volumes_v1.BackupAwsEbsVolumesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_ec2_instances_v1(
        self,
    ) -> backup_aws_ec2_instances_v1.BackupAwsEc2InstancesV1Controller:
        return backup_aws_ec2_instances_v1.BackupAwsEc2InstancesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_ec2_mssql_databases_v1(
        self,
    ) -> backup_ec2_mssql_databases_v1.BackupEc2MssqlDatabasesV1Controller:
        return backup_ec2_mssql_databases_v1.BackupEc2MssqlDatabasesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_rds_resources_v1(
        self,
    ) -> backup_aws_rds_resources_v1.BackupAwsRdsResourcesV1Controller:
        return backup_aws_rds_resources_v1.BackupAwsRdsResourcesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_aws_rds_resource_databases_v1(
        self,
    ) -> backup_aws_rds_resource_databases_v1.BackupAwsRdsResourceDatabasesV1Controller:
        return backup_aws_rds_resource_databases_v1.BackupAwsRdsResourceDatabasesV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def backup_aws_rds_resource_database_tables_v1(
        self,
    ) -> backup_aws_rds_resource_database_tables_v1.BackupAwsRdsResourceDatabaseTablesV1Controller:
        return backup_aws_rds_resource_database_tables_v1.BackupAwsRdsResourceDatabaseTablesV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def backups_files_v1(self) -> backups_files_v1.BackupsFilesV1Controller:
        return backups_files_v1.BackupsFilesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_protection_groups_v1(
        self,
    ) -> backup_protection_groups_v1.BackupProtectionGroupsV1Controller:
        return backup_protection_groups_v1.BackupProtectionGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_filesystems_v1(self) -> backup_filesystems_v1.BackupFilesystemsV1Controller:
        return backup_filesystems_v1.BackupFilesystemsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def backup_filesystem_directories_v1(
        self,
    ) -> backup_filesystem_directories_v1.BackupFilesystemDirectoriesV1Controller:
        return backup_filesystem_directories_v1.BackupFilesystemDirectoriesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_connections_v1(self) -> aws_connections_v1.AwsConnectionsV1Controller:
        return aws_connections_v1.AwsConnectionsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_connection_groups_v1(self) -> aws_connection_groups_v1.AwsConnectionGroupsV1Controller:
        return aws_connection_groups_v1.AwsConnectionGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def post_process_aws_connection_v1(
        self,
    ) -> post_process_aws_connection_v1.PostProcessAwsConnectionV1Controller:
        return post_process_aws_connection_v1.PostProcessAwsConnectionV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_regions_v1(self) -> aws_regions_v1.AwsRegionsV1Controller:
        return aws_regions_v1.AwsRegionsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_templates_v1(self) -> aws_templates_v1.AwsTemplatesV1Controller:
        return aws_templates_v1.AwsTemplatesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_dynamodb_tables_v1(self) -> aws_dynamodb_tables_v1.AwsDynamodbTablesV1Controller:
        return aws_dynamodb_tables_v1.AwsDynamodbTablesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_ebs_volumes_v1(self) -> aws_ebs_volumes_v1.AwsEbsVolumesV1Controller:
        return aws_ebs_volumes_v1.AwsEbsVolumesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_ec2_instances_v1(self) -> aws_ec2_instances_v1.AwsEc2InstancesV1Controller:
        return aws_ec2_instances_v1.AwsEc2InstancesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_availability_groups_v1(
        self,
    ) -> ec2_mssql_availability_groups_v1.Ec2MssqlAvailabilityGroupsV1Controller:
        return ec2_mssql_availability_groups_v1.Ec2MssqlAvailabilityGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_databases_v1(self) -> ec2_mssql_databases_v1.Ec2MssqlDatabasesV1Controller:
        return ec2_mssql_databases_v1.Ec2MssqlDatabasesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_failover_clusters_v1(
        self,
    ) -> ec2_mssql_failover_clusters_v1.Ec2MssqlFailoverClustersV1Controller:
        return ec2_mssql_failover_clusters_v1.Ec2MssqlFailoverClustersV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_failover_cluster_v1(
        self,
    ) -> ec2_mssql_failover_cluster_v1.Ec2MssqlFailoverClusterV1Controller:
        return ec2_mssql_failover_cluster_v1.Ec2MssqlFailoverClusterV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_hosts_v1(self) -> ec2_mssql_hosts_v1.Ec2MssqlHostsV1Controller:
        return ec2_mssql_hosts_v1.Ec2MssqlHostsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def ec2_mssql_instance_v1(self) -> ec2_mssql_instance_v1.Ec2MssqlInstanceV1Controller:
        return ec2_mssql_instance_v1.Ec2MssqlInstanceV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_environments_v1(self) -> aws_environments_v1.AwsEnvironmentsV1Controller:
        return aws_environments_v1.AwsEnvironmentsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_environment_tags_v1(self) -> aws_environment_tags_v1.AwsEnvironmentTagsV1Controller:
        return aws_environment_tags_v1.AwsEnvironmentTagsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_rds_resources_v1(self) -> aws_rds_resources_v1.AwsRdsResourcesV1Controller:
        return aws_rds_resources_v1.AwsRdsResourcesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_s3_buckets_v1(self) -> aws_s3_buckets_v1.AwsS3BucketsV1Controller:
        return aws_s3_buckets_v1.AwsS3BucketsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def protection_groups_v1(self) -> protection_groups_v1.ProtectionGroupsV1Controller:
        return protection_groups_v1.ProtectionGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def protection_groups_s3_assets_v1(
        self,
    ) -> protection_groups_s3_assets_v1.ProtectionGroupsS3AssetsV1Controller:
        return protection_groups_s3_assets_v1.ProtectionGroupsS3AssetsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def management_groups_v1(self) -> management_groups_v1.ManagementGroupsV1Controller:
        return management_groups_v1.ManagementGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def organizational_units_v2(self) -> organizational_units_v2.OrganizationalUnitsV2Controller:
        return organizational_units_v2.OrganizationalUnitsV2Controller(self.config)

    @property
    @functools.lru_cache(1)
    def organizational_units_v1(self) -> organizational_units_v1.OrganizationalUnitsV1Controller:
        return organizational_units_v1.OrganizationalUnitsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def policy_assignments_v1(self) -> policy_assignments_v1.PolicyAssignmentsV1Controller:
        return policy_assignments_v1.PolicyAssignmentsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def policy_definitions_v1(self) -> policy_definitions_v1.PolicyDefinitionsV1Controller:
        return policy_definitions_v1.PolicyDefinitionsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def policy_rules_v1(self) -> policy_rules_v1.PolicyRulesV1Controller:
        return policy_rules_v1.PolicyRulesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def report_compliance_v1(self) -> report_compliance_v1.ReportComplianceV1Controller:
        return report_compliance_v1.ReportComplianceV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def report_compliance_runs_v1(
        self,
    ) -> report_compliance_runs_v1.ReportComplianceRunsV1Controller:
        return report_compliance_runs_v1.ReportComplianceRunsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def report_downloads_v1(self) -> report_downloads_v1.ReportDownloadsV1Controller:
        return report_downloads_v1.ReportDownloadsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_aws_dynamodb_tables_v1(
        self,
    ) -> restored_aws_dynamodb_tables_v1.RestoredAwsDynamodbTablesV1Controller:
        return restored_aws_dynamodb_tables_v1.RestoredAwsDynamodbTablesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_records_aws_dynamodb_tables_v1(
        self,
    ) -> restored_records_aws_dynamodb_tables_v1.RestoredRecordsAwsDynamodbTablesV1Controller:
        return restored_records_aws_dynamodb_tables_v1.RestoredRecordsAwsDynamodbTablesV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def restored_aws_ebs_volumes_v2(
        self,
    ) -> restored_aws_ebs_volumes_v2.RestoredAwsEbsVolumesV2Controller:
        return restored_aws_ebs_volumes_v2.RestoredAwsEbsVolumesV2Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_aws_ebs_volumes_v1(
        self,
    ) -> restored_aws_ebs_volumes_v1.RestoredAwsEbsVolumesV1Controller:
        return restored_aws_ebs_volumes_v1.RestoredAwsEbsVolumesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_aws_ec2_instances_v1(
        self,
    ) -> restored_aws_ec2_instances_v1.RestoredAwsEc2InstancesV1Controller:
        return restored_aws_ec2_instances_v1.RestoredAwsEc2InstancesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restore_ec2_mssql_database_v1(
        self,
    ) -> restore_ec2_mssql_database_v1.RestoreEc2MssqlDatabaseV1Controller:
        return restore_ec2_mssql_database_v1.RestoreEc2MssqlDatabaseV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_aws_rds_resources_v1(
        self,
    ) -> restored_aws_rds_resources_v1.RestoredAwsRdsResourcesV1Controller:
        return restored_aws_rds_resources_v1.RestoredAwsRdsResourcesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def aws_rds_resource_restored_records_v1(
        self,
    ) -> aws_rds_resource_restored_records_v1.AwsRdsResourceRestoredRecordsV1Controller:
        return aws_rds_resource_restored_records_v1.AwsRdsResourceRestoredRecordsV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def restored_aws_s3_buckets_v1(
        self,
    ) -> restored_aws_s3_buckets_v1.RestoredAwsS3BucketsV1Controller:
        return restored_aws_s3_buckets_v1.RestoredAwsS3BucketsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_files_v1(self) -> restored_files_v1.RestoredFilesV1Controller:
        return restored_files_v1.RestoredFilesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_protection_groups_v1(
        self,
    ) -> restored_protection_groups_v1.RestoredProtectionGroupsV1Controller:
        return restored_protection_groups_v1.RestoredProtectionGroupsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def restored_protection_group_instant_access_endpoints_v1(
        self,
    ) -> (
        restored_protection_group_instant_access_endpoints_v1.RestoredProtectionGroupInstantAccessEndpointsV1Controller
    ):
        return restored_protection_group_instant_access_endpoints_v1.RestoredProtectionGroupInstantAccessEndpointsV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def restored_protection_group_s3_assets_v1(
        self,
    ) -> restored_protection_group_s3_assets_v1.RestoredProtectionGroupS3AssetsV1Controller:
        return restored_protection_group_s3_assets_v1.RestoredProtectionGroupS3AssetsV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def roles_v1(self) -> roles_v1.RolesV1Controller:
        return roles_v1.RolesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def auto_user_provisioning_settings_v1(
        self,
    ) -> auto_user_provisioning_settings_v1.AutoUserProvisioningSettingsV1Controller:
        return auto_user_provisioning_settings_v1.AutoUserProvisioningSettingsV1Controller(
            self.config
        )

    @property
    @functools.lru_cache(1)
    def auto_user_provisioning_rules_v1(
        self,
    ) -> auto_user_provisioning_rules_v1.AutoUserProvisioningRulesV1Controller:
        return auto_user_provisioning_rules_v1.AutoUserProvisioningRulesV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def general_settings_v2(self) -> general_settings_v2.GeneralSettingsV2Controller:
        return general_settings_v2.GeneralSettingsV2Controller(self.config)

    @property
    @functools.lru_cache(1)
    def tasks_v1(self) -> tasks_v1.TasksV1Controller:
        return tasks_v1.TasksV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def users_v2(self) -> users_v2.UsersV2Controller:
        return users_v2.UsersV2Controller(self.config)

    @property
    @functools.lru_cache(1)
    def users_v1(self) -> users_v1.UsersV1Controller:
        return users_v1.UsersV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def wallets_v1(self) -> wallets_v1.WalletsV1Controller:
        return wallets_v1.WalletsV1Controller(self.config)

    @property
    @functools.lru_cache(1)
    def post_process_kms_v1(self) -> post_process_kms_v1.PostProcessKmsV1Controller:
        return post_process_kms_v1.PostProcessKmsV1Controller(self.config)
