#
# Copyright 2023. Clumio, Inc.
#

__all__ = [
    'add_bucket_protection_group_v1_request',
    'add_bucket_to_protection_group_response',
    'add_protection_group_instant_access_endpoint_role_v1_request',
    'add_s3_instant_access_endpoint_role_response',
    'alert_embedded',
    'alert_links',
    'alert_list_embedded',
    'alert_list_links',
    'alert_parent_entity',
    'alert_primary_entity',
    'ami_model',
    'ancestor_ref_model',
    'assign_policy_action',
    'assignment_entity',
    'assignment_input_model',
    'attached_ebs_volume_full_model',
    'attribute_definition',
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
    'categorised_resources',
    'change_password_response',
    'change_password_v1_request',
    'change_password_v2_request',
    'cloud_connector_count_by_status',
    'clumio_role_resource',
    'clumio_rule_resource',
    'clumio_ssm_document_inputs',
    'clumio_ssm_document_parameter_value',
    'clumio_ssm_document_resource',
    'clumio_ssm_document_step',
    'clumio_topic_resource',
    'compliance_stats_deprecated',
    'compute_resource_embedded',
    'compute_resource_id_model',
    'compute_resource_links',
    'connection_region',
    'connection_region_list_embedded',
    'connection_region_list_links',
    'consolidated_alert_details',
    'consolidated_alert_links',
    'consolidated_alert_list_embedded',
    'consolidated_alert_list_links',
    'consolidated_alert_parent_entity',
    'consolidated_alert_with_e_tag',
    'consolidated_config',
    'cost_estimates_protection_group_instant_access_endpoint_v1_request',
    'create_auto_user_provisioning_rule_response',
    'create_auto_user_provisioning_rule_v1_request',
    'create_aws_connection_response',
    'create_aws_connection_v1_request',
    'create_aws_template_v2_response',
    'create_backup_aws_dynamodb_table_v1_request',
    'create_backup_aws_ebs_volume_v1_request',
    'create_backup_aws_ebs_volume_v2_request',
    'create_backup_aws_ec2_instance_v1_request',
    'create_backup_ec2_mssql_database_v1_request',
    'create_backup_mssql_database_v1_request',
    'create_backup_vmware_vm_v1_request',
    'create_connection_template_v1_request',
    'create_ec2_mssql_database_restore_response',
    'create_ec2_mssql_database_restore_response_links',
    'create_hcm_host_response',
    'create_host_ec_credentials_response',
    'create_mssql_database_restore_response',
    'create_mssql_host_connection_credentials_v1_request',
    'create_mssql_host_connections_v1_request',
    'create_on_demand_ec2_mssql_database_backup_response_links',
    'create_on_demand_mssql_database_backup_response_links',
    'create_organizational_unit_no_task_response',
    'create_organizational_unit_no_task_response_v1',
    'create_organizational_unit_response',
    'create_organizational_unit_response_v1',
    'create_organizational_unit_v1_request',
    'create_organizational_unit_v2_request',
    'create_policy_definition_v1_request',
    'create_policy_response',
    'create_policy_rule_v1_request',
    'create_protection_group_instant_access_endpoint_v1_request',
    'create_protection_group_response',
    'create_protection_group_v1_request',
    'create_rds_database_restore_response_links',
    'create_rds_resource_restore_response',
    'create_report_download_response',
    'create_report_download_v1_request',
    'create_restore_record_response_links',
    'create_rule_response',
    'create_rule_response_links',
    'create_s3_instant_access_endpoint_response',
    'create_s3_instant_access_endpoint_response_embedded',
    'create_s3_instant_access_endpoint_response_links',
    'create_user_response',
    'create_user_response_v1',
    'create_user_v1_request',
    'create_user_v2_request',
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
    'delete_host_response_links',
    'delete_mssql_host_connections_v1_request',
    'delete_organizational_unit_response',
    'delete_policy_response',
    'delete_policy_response_links',
    'delete_rule_response',
    'delete_rule_response_links',
    'delete_s3_instant_access_endpoint_role_response',
    'delete_user_response_v1',
    'direct_download_data_access_object',
    'directory',
    'directory_browse_embedded',
    'directory_browse_links',
    'directory_links',
    'discover_config',
    'download_shared_file_links',
    'download_shared_file_response',
    'download_shared_file_v1_request',
    'dynamo_db_grr_source',
    'dynamo_db_grr_target',
    'dynamo_db_keys',
    'dynamo_db_query_preview_result',
    'dynamo_db_restore_source_backup_options',
    'dynamo_db_restore_source_pitr_options',
    'dynamo_db_table',
    'dynamo_db_table_backup_links',
    'dynamo_db_table_backup_list_embedded',
    'dynamo_db_table_backup_list_links',
    'dynamo_db_table_backup_with_e_tag',
    'dynamo_db_table_embedded',
    'dynamo_db_table_links',
    'dynamo_db_table_list_embedded',
    'dynamo_db_table_list_links',
    'dynamo_db_table_restore_source',
    'dynamo_db_table_restore_target',
    'dynamo_dbgrr_attribute_filter',
    'dynamo_dbgrr_query_filter',
    'dynamo_dbgrr_sort_key_filter',
    'dynamodb_asset_info',
    'dynamodb_template_info',
    'ebs',
    'ebs_asset_info',
    'ebs_backup',
    'ebs_backup_advanced_setting',
    'ebs_backup_links',
    'ebs_backup_links_v1',
    'ebs_backup_list_embedded',
    'ebs_backup_list_embedded_v1',
    'ebs_backup_list_links',
    'ebs_backup_list_links_v1',
    'ebs_backup_v1',
    'ebs_restore_source',
    'ebs_restore_source_v1',
    'ebs_restore_target',
    'ebs_restore_target_v1',
    'ebs_template_info',
    'ebs_volume_embedded',
    'ebs_volume_links',
    'ebs_volume_list_embedded',
    'ebs_volume_list_links',
    'ec2',
    'ec2_ami_restore_target',
    'ec2_backup',
    'ec2_backup_advanced_setting',
    'ec2_backup_links',
    'ec2_backup_list_embedded',
    'ec2_backup_list_links',
    'ec2_instance_embedded',
    'ec2_instance_links',
    'ec2_instance_list_embedded',
    'ec2_instance_list_links',
    'ec2_instance_restore_target',
    'ec2_mssql_database',
    'ec2_mssql_database_backup',
    'ec2_mssql_database_backup_advanced_setting',
    'ec2_mssql_database_backup_embedded',
    'ec2_mssql_database_backup_links',
    'ec2_mssql_database_backup_list_embedded',
    'ec2_mssql_database_backup_list_links',
    'ec2_mssql_database_embedded',
    'ec2_mssql_database_links',
    'ec2_mssql_database_list_embedded',
    'ec2_mssql_database_list_links',
    'ec2_mssql_database_pitr_interval',
    'ec2_mssql_database_pitr_interval_links',
    'ec2_mssql_database_pitr_interval_list_embedded',
    'ec2_mssql_database_pitr_interval_list_links',
    'ec2_mssql_instance',
    'ec2_mssql_instance_embedded',
    'ec2_mssql_instance_links',
    'ec2_mssql_instance_list_embedded',
    'ec2_mssql_instance_list_links',
    'ec2_mssql_inv_host',
    'ec2_mssql_inv_host_links',
    'ec2_mssql_inv_host_list_embedded',
    'ec2_mssql_inv_host_list_links',
    'ec2_mssql_log_backup_advanced_setting',
    'ec2_mssql_protect_config',
    'ec2_mssql_restore_from_backup_options',
    'ec2_mssql_restore_source',
    'ec2_mssql_restore_target',
    'ec2_mssql_restore_to_aag_options',
    'ec2_mssql_template_info',
    'ec2_mssqlag',
    'ec2_mssqlag_embedded',
    'ec2_mssqlag_links',
    'ec2_mssqlag_list_embedded',
    'ec2_mssqlag_list_links',
    'ec2_mssqlfci',
    'ec2_mssqlfci_embedded',
    'ec2_mssqlfci_links',
    'ec2_mssqlfci_list_embedded',
    'ec2_mssqlfci_list_links',
    'ec2_mssqlpitr_options',
    'ec2_restore_ebs_block_device_mapping',
    'ec2_restore_network_interface',
    'ec2_restore_source',
    'ec2_restore_target',
    'ec2_volumes_restore_target',
    'edit_profile_response',
    'edit_profile_response_v1',
    'email_download_data_access_object',
    'email_download_data_access_option',
    'email_recipients_data_access_option',
    'entity_group_assignment_updates',
    'entity_group_assignment_updates_v1',
    'entity_group_embedded',
    'entity_model',
    'error',
    'error_model',
    'estimate_cost_details_s3_instant_access_endpoint_response',
    'estimate_cost_details_s3_instant_access_endpoint_response_links',
    'estimate_cost_s3_instant_access_endpoint_async_response',
    'estimate_cost_s3_instant_access_endpoint_async_response_links',
    'estimate_cost_s3_instant_access_endpoint_sync_response',
    'estimate_cost_s3_instant_access_endpoint_sync_response_links',
    'event_rules',
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
    'generate_restored_file_passcode_links',
    'generate_restored_file_passcode_response',
    'global_secondary_index',
    'grr_source',
    'grr_target',
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
    'iam_instance_profile_model',
    'individual_alert_details',
    'inherited_from',
    'instance_store_block_device_mapping',
    'key_schema_element',
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
    'list_dynamo_db_table_backups_response',
    'list_dynamo_db_table_response',
    'list_ebs_backups_response',
    'list_ebs_backups_response_v1',
    'list_ebs_volumes_response',
    'list_ec2_backups_response',
    'list_ec2_instances_response',
    'list_ec2_mssql_a_gs_response',
    'list_ec2_mssql_database_backups_response',
    'list_ec2_mssql_database_pitr_intervals_response',
    'list_ec2_mssql_databases_response',
    'list_ec2_mssql_instances_response',
    'list_ec2_mssql_inv_hosts_response',
    'list_ec2_mssqlfc_is_response',
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
    'list_organizational_units_response_v1',
    'list_policies_response',
    'list_protection_group_backups_response',
    'list_protection_group_s3_asset_backups_response',
    'list_protection_group_s3_assets_response',
    'list_protection_groups_response',
    'list_rds_backup_databases_response',
    'list_rds_database_backups_response',
    'list_rds_database_tables_response',
    'list_rds_option_groups_response',
    'list_rds_resources_response',
    'list_report_downloads_response',
    'list_resource_pools_response',
    'list_restored_records_response',
    'list_roles_response',
    'list_rules_response',
    'list_s3_instant_access_endpoints_response',
    'list_subgroups_response',
    'list_tag_categories2_response',
    'list_tags_response',
    'list_tasks_response',
    'list_users_response',
    'list_users_response_v1',
    'list_v_mware_datastores_response',
    'list_v_mware_v_center_networks_response',
    'list_vcenters_response',
    'list_vm_backups_response',
    'list_vms_response',
    'list_wallets_response',
    'local_secondary_index',
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
    'mssql_service_roles',
    'network_interface',
    'object',
    'object_filter',
    'on_demand_dynamo_db_backup_links',
    'on_demand_dynamo_db_backup_response',
    'on_demand_ebs_backup_links',
    'on_demand_ebs_backup_response',
    'on_demand_ebs_backup_response_v1',
    'on_demand_ec2_backup_links',
    'on_demand_ec2_backup_response',
    'on_demand_ec2_mssql_database_backup_response',
    'on_demand_mssql_backup_response',
    'on_demand_setting',
    'on_demand_vm_backup_response',
    'on_demand_vm_backup_response_links',
    'option_groups',
    'option_groups_links',
    'option_groups_list_embedded',
    'option_groups_list_links',
    'option_model',
    'option_setting',
    'organizational_unit_links',
    'organizational_unit_links_for_delete',
    'organizational_unit_list_embedded',
    'organizational_unit_list_embedded_v1',
    'organizational_unit_list_links',
    'organizational_unit_parent_entity',
    'organizational_unit_primary_entity',
    'organizational_unit_with_e_tag',
    'organizational_unit_with_e_tag_v1',
    'ou_grouping_criteria',
    'ou_links',
    'patch_general_settings_response_v2',
    'patch_organizational_unit_no_task_response',
    'patch_organizational_unit_no_task_response_v1',
    'patch_organizational_unit_response',
    'patch_organizational_unit_response_v1',
    'patch_organizational_unit_v1_request',
    'patch_organizational_unit_v2_request',
    'permission_model',
    'policy',
    'policy_advanced_settings',
    'policy_details',
    'policy_embedded',
    'policy_links',
    'policy_list_embedded',
    'policy_list_links',
    'policy_operation',
    'policy_operation_input',
    'post_process_aws_connection_v1_request',
    'post_process_kms_v1_request',
    'prefix_filter',
    'preview_details_protection_group_links',
    'preview_details_protection_group_response',
    'preview_protection_group_async_links',
    'preview_protection_group_async_response',
    'preview_protection_group_s3_asset_async_links',
    'preview_protection_group_s3_asset_async_response',
    'preview_protection_group_s3_asset_details_links',
    'preview_protection_group_s3_asset_details_response',
    'preview_protection_group_s3_asset_sync_links',
    'preview_protection_group_s3_asset_sync_response',
    'preview_protection_group_s3_asset_v1_request',
    'preview_protection_group_sync_links',
    'preview_protection_group_sync_response',
    'preview_protection_group_v1_request',
    'projection',
    'protect_config',
    'protect_entities_hateoas_link',
    'protected_stats_deprecated',
    'protection_compliance_stats_with_seeding',
    'protection_group',
    'protection_group_backup',
    'protection_group_backup_advanced_setting',
    'protection_group_backup_links',
    'protection_group_backup_list_embedded',
    'protection_group_backup_list_links',
    'protection_group_bucket',
    'protection_group_bucket_continuous_backup_stats',
    'protection_group_bucket_continuous_backup_stats_links',
    'protection_group_bucket_embedded',
    'protection_group_bucket_links',
    'protection_group_bucket_list_embedded',
    'protection_group_bucket_list_links',
    'protection_group_embedded',
    'protection_group_links',
    'protection_group_list_embedded',
    'protection_group_list_links',
    'protection_group_restore_source',
    'protection_group_restore_source_pitr_options',
    'protection_group_restore_target',
    'protection_group_s3_asset_backup',
    'protection_group_s3_asset_backup_links',
    'protection_group_s3_asset_backup_list_embedded',
    'protection_group_s3_asset_backup_list_links',
    'protection_group_s3_asset_restore_source',
    'protection_group_s3_asset_restore_source_pitr_options',
    'protection_group_version_links',
    'protection_info',
    'protection_info_deprecated',
    'protection_info_with_rule',
    'provisioned_throughput',
    'provisioned_throughput_override',
    'rds_asset_info',
    'rds_backup_database',
    'rds_backup_database_list_embedded',
    'rds_backup_database_list_links',
    'rds_config_sync_advanced_setting',
    'rds_database_backup',
    'rds_database_backup_links',
    'rds_database_backup_list_embedded',
    'rds_database_backup_list_links',
    'rds_database_table',
    'rds_database_table_column',
    'rds_database_table_column_links',
    'rds_database_table_embedded',
    'rds_database_table_links',
    'rds_database_table_list_embedded',
    'rds_database_table_list_links',
    'rds_instance_model',
    'rds_logical_backup_advanced_setting',
    'rds_logical_preview_query_result',
    'rds_resource',
    'rds_resource_embedded',
    'rds_resource_links',
    'rds_resource_list_embedded',
    'rds_resource_list_links',
    'rds_resource_restore_source',
    'rds_resource_restore_source_air_gap_options',
    'rds_resource_restore_source_pitr_options',
    'rds_resource_restore_target',
    'rds_template_info',
    'read_alert_response',
    'read_auto_user_provisioning_rule_response',
    'read_auto_user_provisioning_setting_response',
    'read_aws_connection_response',
    'read_aws_environment_response',
    'read_aws_tag_response',
    'read_aws_templates_v2_response',
    'read_bucket_response',
    'read_compute_resource_response',
    'read_consolidated_alert_response',
    'read_datacenter_response',
    'read_directory_response',
    'read_dynamo_db_table_backup_response',
    'read_dynamo_db_table_response',
    'read_ebs_backup_response',
    'read_ebs_backup_response_v1',
    'read_ebs_tag_compliance_stats_response',
    'read_ebs_volume_response',
    'read_ec2_backup_response',
    'read_ec2_instance_response',
    'read_ec2_mssql_ag_response',
    'read_ec2_mssql_database_backup_response',
    'read_ec2_mssql_database_response',
    'read_ec2_mssql_instance_response',
    'read_ec2_mssql_inv_host_response',
    'read_ec2_mssqlfci_response',
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
    'read_organizational_unit_response_v1',
    'read_policy_definition_hateoas_link',
    'read_policy_response',
    'read_protection_group_backup_response',
    'read_protection_group_response',
    'read_protection_group_s3_asset_backup_response',
    'read_protection_group_s3_asset_continuous_backup_stats_response',
    'read_protection_group_s3_asset_response',
    'read_rds_database_backup_response',
    'read_rds_database_table_columns_response',
    'read_rds_database_table_response',
    'read_rds_resource_response',
    'read_resource_pool_response',
    'read_role_response',
    'read_rule_response',
    'read_s3_instant_access_endpoint_response',
    'read_s3_instant_access_endpoint_role_permission_response',
    'read_s3_instant_access_endpoint_uri_response',
    'read_subgroup_response',
    'read_tag_category2_response',
    'read_tag_response',
    'read_task_hateoas_link',
    'read_task_hateoas_links',
    'read_task_hateoas_outer_embedded',
    'read_task_response',
    'read_user_response',
    'read_user_response_v1',
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
    'replica_description',
    'replica_global_secondary_index_description',
    'report_download',
    'report_download_links',
    'report_download_list_embedded',
    'report_download_list_links',
    'resource_pool_datacenter_model',
    'resource_pool_links',
    'resource_pool_list_embedded',
    'resource_pool_list_links',
    'resource_pool_with_e_tag',
    'resources',
    'rest_entity',
    'restore_aws_dynamodb_table_v1_request',
    'restore_aws_ebs_volume_v1_request',
    'restore_aws_ebs_volume_v2_request',
    'restore_aws_ec2_instance_v1_request',
    'restore_aws_rds_resource_v1_request',
    'restore_dynamo_db_table_links',
    'restore_dynamo_db_table_response',
    'restore_ebs_links',
    'restore_ebs_response',
    'restore_ebs_response_v1',
    'restore_ec2_links',
    'restore_ec2_mssql_database_v1_request',
    'restore_ec2_response',
    'restore_file_links',
    'restore_file_response',
    'restore_files_v1_request',
    'restore_mssql_database_v1_request',
    'restore_objects_links',
    'restore_objects_response',
    'restore_protection_group_links',
    'restore_protection_group_response',
    'restore_protection_group_s3_asset_links',
    'restore_protection_group_s3_asset_response',
    'restore_protection_group_s3_asset_v1_request',
    'restore_protection_group_s3_objects_v1_request',
    'restore_protection_group_v1_request',
    'restore_rds_record_v1_request',
    'restore_record_preview_response',
    'restore_record_response',
    'restore_records_aws_dynamodb_table_v1_request',
    'restore_records_links_async',
    'restore_records_links_sync',
    'restore_records_response_async',
    'restore_records_response_sync',
    'restore_v_mware_vm_response',
    'restore_vmware_vm_v1_request',
    'restored_file_info',
    'restored_files_list_embedded',
    'restored_files_list_links',
    'restored_files_response',
    'restored_record',
    'restored_record_links',
    'restored_record_list_embedded',
    'restored_record_list_links',
    'retention_backup_sla_param',
    'role_for_organizational_units',
    'role_links',
    'role_list_embedded',
    'role_list_links',
    'role_model',
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
    's3_asset_info',
    's3_bucket_size_res',
    's3_buckets_inventory_summary_bucket_size_breakdown',
    's3_cloudwatch_metrics',
    's3_delete_marker_replication',
    's3_destination',
    's3_encryption_configuration',
    's3_encryption_output',
    's3_existing_object_replication',
    's3_instant_access_endpoint',
    's3_instant_access_endpoint_embedded',
    's3_instant_access_endpoint_links',
    's3_instant_access_endpoint_list_embedded',
    's3_instant_access_endpoint_list_links',
    's3_instant_access_endpoint_role',
    's3_instant_access_endpoint_stat',
    's3_instant_access_source',
    's3_instant_access_source_pitr_options',
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
    's3_service_roles',
    's3_source_selection_criteria',
    's3_sse_kms_encrypted_objects',
    's3_tag',
    's3_template_info',
    's3_versioning_output',
    'service_roles',
    'set_assignments_response',
    'set_assignments_response_links',
    'set_bucket_properties_response',
    'set_bucket_properties_response_links',
    'set_bucket_properties_v1_request',
    'set_policy_assignments_v1_request',
    'share_file_restore_email_links',
    'share_file_restore_email_response',
    'share_restored_file_v1_request',
    'single_error_response',
    'source_object_filters',
    'sse_specification',
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
    'task_links',
    'task_list_embedded',
    'task_list_links',
    'task_parent_entity',
    'task_primary_entity',
    'task_with_e_tag',
    'template_configuration_v2',
    'template_links',
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
    'update_policy_definition_v1_request',
    'update_policy_response',
    'update_policy_response_links',
    'update_policy_rule_v1_request',
    'update_protection_group_assignments',
    'update_protection_group_instant_access_endpoint_role_v1_request',
    'update_protection_group_instant_access_endpoint_v1_request',
    'update_protection_group_response',
    'update_protection_group_v1_request',
    'update_rule_response',
    'update_rule_response_links',
    'update_s3_instant_access_endpoint_response',
    'update_s3_instant_access_endpoint_role_response',
    'update_task_response',
    'update_task_v1_request',
    'update_user_assignments',
    'update_user_assignments_with_role',
    'update_user_profile_v1_request',
    'update_user_profile_v2_request',
    'update_user_response',
    'update_user_response_v1',
    'update_user_v1_request',
    'update_user_v2_request',
    'user_embedded',
    'user_embedded_v1',
    'user_hateoas_v1',
    'user_links',
    'user_list_embedded',
    'user_list_embedded_v1',
    'user_list_hateoas_links',
    'user_with_e_tag',
    'user_with_role',
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
    'warm_tier_protect_config',
    'warm_tier_protect_template_info',
]
