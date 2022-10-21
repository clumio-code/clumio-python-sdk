#
# Copyright 2021. Clumio, Inc.
#

__all__ = [
    'add_bucket_protection_group_v1_request',
    'add_bucket_to_protection_group_response',
    'alert',
    'alert_embedded',
    'alert_links',
    'alert_list_embedded',
    'alert_list_links',
    'alert_parent_entity',
    'alert_primary_entity',
    'ancestor_ref_model',
    'assign_policy_action',
    'assignment_entity',
    'assignment_input_model',
    'audit_parent_entity',
    'audit_primary_entity',
    'audit_trail_list_embedded',
    'audit_trail_list_links',
    'audit_trails',
    'auto_user_provisioning_rule_embedded',
    'auto_user_provisioning_rule_links',
    'auto_user_provisioning_rule_list_embedded',
    'auto_user_provisioning_rule_list_links',
    'auto_user_provisioning_rule_with_e_tag',
    'auto_user_provisioning_setting_links',
    'aws_connection',
    'aws_connection_links',
    'aws_connection_list_embedded',
    'aws_connection_list_links',
    'aws_ds_grouping_criteria',
    'aws_environment',
    'aws_environment_embedded',
    'aws_environment_links',
    'aws_environment_list_embedded',
    'aws_environment_list_links',
    'aws_tag',
    'aws_tag_common_model',
    'aws_tag_embedded',
    'aws_tag_links',
    'aws_tag_list_embedded',
    'aws_tag_list_links',
    'aws_tag_model',
    'backup_sla',
    'backup_window',
    'bucket',
    'bucket_links',
    'bucket_list_embedded',
    'bucket_list_links',
    'change_password_v1_request',
    'cloud_connector_count_by_status',
    'compliance_stats_deprecated',
    'compute_resource_embedded',
    'compute_resource_id_model',
    'compute_resource_links',
    'connection_region',
    'connection_region_list_embedded',
    'connection_region_list_links',
    'consolidated_alert',
    'consolidated_alert_details',
    'consolidated_alert_links',
    'consolidated_alert_list_embedded',
    'consolidated_alert_list_links',
    'consolidated_alert_parent_entity',
    'consolidated_config',
    'create_auto_user_provisioning_rule_response',
    'create_auto_user_provisioning_rule_v1_request',
    'create_aws_connection_response',
    'create_aws_connection_template_v1_request',
    'create_aws_connection_v1_request',
    'create_aws_template_response',
    'create_aws_template_v2_response',
    'create_backup_aws_ebs_volume_v1_request',
    'create_backup_mssql_database_v1_request',
    'create_backup_vmware_vm_v1_request',
    'create_connection_template_v1_request',
    'create_hcm_host_response',
    'create_host_ec_credentials_response',
    'create_mssql_database_restore_response',
    'create_mssql_host_connection_credentials_v1_request',
    'create_mssql_host_connections_v1_request',
    'create_organizational_unit_response',
    'create_organizational_unit_v1_request',
    'create_policy_definition_v1_request',
    'create_policy_response',
    'create_policy_rule_v1_request',
    'create_protection_group_response',
    'create_protection_group_v1_request',
    'create_report_download_response',
    'create_report_download_v1_request',
    'create_rule_response',
    'create_user_response',
    'create_user_v1_request',
    'create_wallet_response',
    'create_wallet_v1_request',
    'data_access_object',
    'database_links',
    'datacenter_embedded',
    'datacenter_links',
    'datacenter_list_embedded',
    'datacenter_list_links',
    'datacenter_with_e_tag',
    'delete_bucket_from_protection_group_response',
    'delete_hcm_host_response',
    'delete_mssql_host_connections_v1_request',
    'delete_organizational_unit_response',
    'delete_policy_response',
    'delete_rule_response',
    'direct_download_data_access_object',
    'directory',
    'directory_browse_embedded',
    'directory_browse_links',
    'directory_links',
    'discover_config',
    'discover_template_info',
    'discover_template_info_v2',
    'ebs',
    'ebs_asset_info',
    'ebs_backup_advanced_setting',
    'ebs_backup_links_v1',
    'ebs_backup_list_embedded_v1',
    'ebs_backup_list_links_v1',
    'ebs_backup_v1',
    'ebs_restore_source_v1',
    'ebs_restore_target_v1',
    'ebs_template_info',
    'ebs_volume_embedded',
    'ebs_volume_links',
    'ebs_volume_list_embedded',
    'ebs_volume_list_links',
    'ec2_backup_advanced_setting',
    'edit_profile_response',
    'email_download_data_access_object',
    'email_download_data_access_option',
    'entity_group_assignmet_updates',
    'entity_group_embedded',
    'entity_model',
    'error',
    'error_model',
    'file_descriptor',
    'file_list_response',
    'file_restore_source',
    'file_restore_target',
    'file_search_list_embedded',
    'file_search_list_links',
    'file_search_response',
    'file_search_result',
    'file_system',
    'file_system_list_embedded',
    'file_system_list_links',
    'file_version',
    'file_version_hateoas',
    'file_versions_list_embedded',
    'file_versions_list_links',
    'folder_embedded',
    'folder_links',
    'folder_list_embedded',
    'folder_list_links',
    'folder_with_e_tag',
    'general_settings_links',
    'hateoas_common_links',
    'hateoas_first_link',
    'hateoas_last_link',
    'hateoas_link',
    'hateoas_next_link',
    'hateoas_prev_link',
    'hateoas_self_link',
    'host',
    'host_id_model',
    'host_links',
    'host_list_embedded',
    'host_list_links',
    'host_with_e_tag',
    'individual_alert_details',
    'inherited_from',
    'list_alerts_response',
    'list_audit_trails_response',
    'list_auto_user_provisioning_rules_response',
    'list_aws_connections_response',
    'list_aws_environments_response',
    'list_aws_regions_response',
    'list_aws_tags_response',
    'list_buckets_response',
    'list_compute_resources_response',
    'list_consolidated_alerts_response',
    'list_datacenters_response',
    'list_ebs_backups_response_v1',
    'list_ebs_volumes_response',
    'list_file_systems_response',
    'list_file_versions_hateoas_link',
    'list_file_versions_hateoas_links',
    'list_folders_response',
    'list_hcm_hosts_response',
    'list_hosts_response',
    'list_management_groups_response',
    'list_mssql_a_gs_response',
    'list_mssql_database_backups_response',
    'list_mssql_database_pitr_intervals_response',
    'list_mssql_databases_response',
    'list_mssql_hosts_response',
    'list_mssql_instances_response',
    'list_organizational_units_response',
    'list_policies_response',
    'list_protection_group_backups_response',
    'list_protection_group_s3_asset_backups_response',
    'list_protection_group_s3_assets_response',
    'list_protection_groups_response',
    'list_report_downloads_response',
    'list_resource_pools_response',
    'list_roles_response',
    'list_rules_response',
    'list_subgroups_response',
    'list_tag_categories2_response',
    'list_tags_response',
    'list_tasks_response',
    'list_users_response',
    'list_v_mware_datastores_response',
    'list_v_mware_v_center_networks_response',
    'list_vcenters_response',
    'list_vm_backups_response',
    'list_vms_response',
    'list_wallets_response',
    'm365_grouping_criteria',
    'management_group',
    'management_group_links',
    'management_group_list_embedded',
    'management_group_list_links',
    'move_hcm_hosts_response',
    'move_hosts_links',
    'move_hosts_source',
    'move_hosts_target',
    'move_mssql_host_connections_v1_request',
    'mssql_ag',
    'mssql_ag_embedded',
    'mssql_ag_links',
    'mssql_ag_list_embedded',
    'mssql_ag_list_links',
    'mssql_database',
    'mssql_database_backup',
    'mssql_database_backup_advanced_setting',
    'mssql_database_backup_embedded',
    'mssql_database_backup_links',
    'mssql_database_backup_list_embedded',
    'mssql_database_backup_list_links',
    'mssql_database_embedded',
    'mssql_database_file',
    'mssql_database_list_embedded',
    'mssql_database_list_links',
    'mssql_database_pitr_interval',
    'mssql_database_pitr_interval_list_embedded',
    'mssql_database_pitr_interval_list_links',
    'mssql_host',
    'mssql_host_embedded',
    'mssql_host_links',
    'mssql_host_list_embedded',
    'mssql_host_list_links',
    'mssql_instance',
    'mssql_instance_embedded',
    'mssql_instance_links',
    'mssql_instance_list_embedded',
    'mssql_instance_list_links',
    'mssql_log_backup_advanced_setting',
    'mssql_pitr_options',
    'mssql_restore_from_backup_options',
    'mssql_restore_source',
    'mssql_restore_target',
    'object_filter',
    'on_demand_mssql_backup_response',
    'on_demand_setting',
    'organizational_unit_links',
    'organizational_unit_list_embedded',
    'organizational_unit_list_links',
    'organizational_unit_parent_entity',
    'organizational_unit_primary_entity',
    'organizational_unit_with_e_tag',
    'ou_grouping_criteria',
    'patch_general_settings_response_v2',
    'patch_organizational_unit_response',
    'patch_organizational_unit_v1_request',
    'permission_model',
    'policy',
    'policy_advanced_settings',
    'policy_embedded',
    'policy_links',
    'policy_list_embedded',
    'policy_list_links',
    'policy_operation',
    'post_process_aws_connection_v1_request',
    'post_process_kms_v1_request',
    'prefix_filter',
    'protect_config',
    'protect_entities_hateoas_link',
    'protect_template_config',
    'protect_template_info',
    'protect_template_info_v2',
    'protected_stats_deprecated',
    'protection_compliance_stats_with_seeding',
    'protection_group',
    'protection_group_backup',
    'protection_group_backup_advanced_setting',
    'protection_group_backup_links',
    'protection_group_backup_list_embedded',
    'protection_group_backup_list_links',
    'protection_group_bucket',
    'protection_group_bucket_embedded',
    'protection_group_bucket_links',
    'protection_group_bucket_list_embedded',
    'protection_group_bucket_list_links',
    'protection_group_embedded',
    'protection_group_links',
    'protection_group_list_embedded',
    'protection_group_list_links',
    'protection_group_restore_source',
    'protection_group_restore_target',
    'protection_group_s3_asset_backup',
    'protection_group_s3_asset_backup_links',
    'protection_group_s3_asset_backup_list_embedded',
    'protection_group_s3_asset_backup_list_links',
    'protection_group_s3_asset_restore_source',
    'protection_group_version_links',
    'protection_info',
    'protection_info_deprecated',
    'protection_info_with_rule',
    'rds_asset_info',
    'rds_template_info',
    'read_alert_response',
    'read_auto_user_provisioning_rule_response',
    'read_auto_user_provisioning_setting_response',
    'read_aws_connection_response',
    'read_aws_environment_response',
    'read_aws_tag_response',
    'read_aws_templates_response',
    'read_aws_templates_v2_response',
    'read_bucket_response',
    'read_compute_resource_response',
    'read_consolidated_alert_response',
    'read_datacenter_response',
    'read_directory_response',
    'read_ebs_backup_response_v1',
    'read_ebs_tag_compliance_stats_response',
    'read_ebs_volume_response',
    'read_file_system_response',
    'read_folder_response',
    'read_general_settings_response_v2',
    'read_hcm_host_response',
    'read_host_response',
    'read_management_group_response',
    'read_mssql_ag_response',
    'read_mssql_database_backup_response',
    'read_mssql_database_response',
    'read_mssql_host_response',
    'read_mssql_instance_response',
    'read_organizational_unit_response',
    'read_policy_definition_hateoas_link',
    'read_policy_response',
    'read_protection_group_backup_response',
    'read_protection_group_response',
    'read_protection_group_s3_asset_backup_response',
    'read_protection_group_s3_asset_response',
    'read_resource_pool_response',
    'read_role_response',
    'read_rule_response',
    'read_subgroup_response',
    'read_tag_category2_response',
    'read_tag_response',
    'read_task_hateoas_links',
    'read_task_response',
    'read_user_response',
    'read_v_center_object_protection_stats_hateoas_link',
    'read_v_mware_compute_resource_stats_response',
    'read_v_mware_datacenter_stats_response',
    'read_v_mware_datastore_response',
    'read_v_mware_folder_stats_response',
    'read_v_mware_tag_stats_response',
    'read_v_mware_v_center_network_response',
    'read_v_mware_v_center_protection_stats_links',
    'read_v_mware_v_center_protection_stats_response',
    'read_vcenter_response',
    'read_vm_backup_response',
    'read_vm_response',
    'read_wallet_response',
    'refresh_wallet_response',
    'report_download',
    'report_download_list_embedded',
    'report_download_list_links',
    'resource_pool_datacenter_model',
    'resource_pool_links',
    'resource_pool_list_embedded',
    'resource_pool_list_links',
    'resource_pool_with_e_tag',
    'rest_entity',
    'restore_aws_ebs_volume_v1_request',
    'restore_file_response',
    'restore_files_v1_request',
    'restore_mssql_database_v1_request',
    'restore_protection_group_response',
    'restore_protection_group_s3_asset_response',
    'restore_protection_group_s3_asset_v1_request',
    'restore_protection_group_v1_request',
    'restore_v_mware_vm_response',
    'restore_vmware_vm_v1_request',
    'restored_file_info',
    'restored_files_list_embedded',
    'restored_files_list_links',
    'restored_files_response',
    'retention_backup_sla_param',
    'role_links',
    'role_list_embedded',
    'role_list_links',
    'role_with_e_tag',
    'rpo_backup_sla_param',
    'rule',
    'rule_action',
    'rule_embedded',
    'rule_links',
    'rule_list_embedded',
    'rule_list_links',
    'rule_priority',
    'rule_provision',
    's3_access_control_translation',
    's3_bucket_size_res',
    's3_buckets_inventory_summary_bucket_size_breakdown',
    's3_cloudwatch_metrics',
    's3_delete_marker_replication',
    's3_destination',
    's3_encryption_configuration',
    's3_encryption_output',
    's3_existing_object_replication',
    's3_metrics',
    's3_replica_modifications',
    's3_replication_configuration',
    's3_replication_output',
    's3_replication_rule',
    's3_replication_rule_and_operator',
    's3_replication_rule_filter',
    's3_replication_time',
    's3_replication_time_value',
    's3_server_side_encryption_by_default',
    's3_server_side_encryption_configuration',
    's3_server_side_encryption_rule',
    's3_source_selection_criteria',
    's3_sse_kms_encrypted_objects',
    's3_tag',
    's3_versioning_output',
    'set_assignments_response',
    'set_bucket_properties_response',
    'set_bucket_properties_response_links',
    'set_bucket_properties_v1_request',
    'set_policy_assignments_v1_request',
    'single_error_response',
    'source_object_filters',
    'subgroup',
    'subgroup_links',
    'subgroup_list_embedded',
    'subgroup_list_links',
    'tag2',
    'tag2_embedded',
    'tag2_links',
    'tag2_list_embedded',
    'tag2_list_links',
    'tag_category2_links',
    'tag_category2_list_embedded',
    'tag_category2_list_links',
    'tag_category2_with_e_tag',
    'tag_parent_category_model',
    'task',
    'task_links',
    'task_list_embedded',
    'task_list_links',
    'task_parent_entity',
    'task_primary_entity',
    'template_configuration',
    'template_configuration_v2',
    'unprotect_entities_hateoas_link',
    'update_alert_response',
    'update_auto_user_provisioning_rule_response',
    'update_auto_user_provisioning_rule_v1_request',
    'update_auto_user_provisioning_setting_response',
    'update_auto_user_provisioning_setting_v1_request',
    'update_aws_connection_response',
    'update_aws_connection_v1_request',
    'update_consolidated_alert_response',
    'update_consolidated_alert_v1_request',
    'update_entities',
    'update_general_settings_v2_request',
    'update_individual_alert_v1_request',
    'update_management_group_response',
    'update_management_group_v1_request',
    'update_management_subgroup_v1_request',
    'update_policy_definition_v1_request',
    'update_policy_response',
    'update_policy_rule_v1_request',
    'update_protection_group_response',
    'update_protection_group_v1_request',
    'update_rule_response',
    'update_subgroup_response',
    'update_task_response',
    'update_task_v1_request',
    'update_user_assignments',
    'update_user_profile_v1_request',
    'update_user_response',
    'update_user_v1_request',
    'user_embedded',
    'user_hateoas',
    'user_links',
    'user_list_embedded',
    'user_list_hateoas_links',
    'v_center_compute_resource',
    'v_center_compute_resource_links',
    'v_center_folder',
    'v_center_folder_links',
    'v_mware_compute_resource_compliance_stats_links',
    'v_mware_datacenter_folder_id_model',
    'v_mware_datacenter_stats_links',
    'v_mware_datastore_links',
    'v_mware_datastore_list_embedded',
    'v_mware_datastore_list_links',
    'v_mware_datastore_with_e_tag',
    'v_mware_ds_grouping_criteria',
    'v_mware_folder_stats_links',
    'v_mware_resource_pool_compute_resource_model',
    'v_mware_resource_pool_parent_model',
    'v_mware_root_compute_resource_folder_id_model',
    'v_mware_root_vm_folder_id_model',
    'v_mware_tag_stats_links',
    'v_mware_v_center_compute_resource_datacenter_model',
    'v_mware_v_center_compute_resource_folder_model',
    'v_mware_v_center_datastore_datacenter_model',
    'v_mware_v_center_datastore_folder_model',
    'v_mware_v_center_folder_datacenter_model',
    'v_mware_v_center_host_compute_resource_model',
    'v_mware_v_center_host_datacenter_model',
    'v_mware_v_center_network_datacenter_model',
    'v_mware_v_center_network_folder_model',
    'v_mware_v_center_network_links',
    'v_mware_v_center_network_list_embedded',
    'v_mware_v_center_network_list_links',
    'v_mware_v_center_network_with_e_tag',
    'v_mware_v_center_parent_folder_model',
    'vcenter',
    'vcenter_embedded',
    'vcenter_links',
    'vcenter_list_embedded',
    'vcenter_list_links',
    'vm',
    'vm_backup_hateoas',
    'vm_backup_hateoas_links',
    'vm_backup_list_embedded',
    'vm_backup_list_hateoas_links',
    'vm_compute_resource_folder_model',
    'vm_compute_resource_link',
    'vm_compute_resource_model',
    'vm_datacenter_folder_model',
    'vm_datacenter_link',
    'vm_datacenter_model',
    'vm_embedded',
    'vm_folder_link',
    'vm_folder_model',
    'vm_host_model',
    'vm_links',
    'vm_list_embedded',
    'vm_list_links',
    'vm_nic_backup_model',
    'vm_nic_model',
    'vm_nic_network_model',
    'vm_nic_restore',
    'vm_resource_pool_model',
    'vm_restore_options',
    'vm_restore_source',
    'vm_restore_tag',
    'vm_restore_target',
    'vm_tag_with_category_model',
    'wallet',
    'wallet_links',
    'wallet_list_embedded',
    'wallet_list_links',
]
