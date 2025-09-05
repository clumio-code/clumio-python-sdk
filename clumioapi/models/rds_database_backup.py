#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import rds_database_backup_links as rds_database_backup_links_
from clumioapi.models import rds_instance_model as rds_instance_model_

T = TypeVar('T', bound='RdsDatabaseBackup')


class RdsDatabaseBackup:
    """Implementation of the 'RdsDatabaseBackup' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with this database at the time of
            backup.
        aws_azs:
            The AWS availability zones associated with this database at the time of backup.
        aws_region:
            The AWS region associated with this environment.
        database_native_id:
            The AWS-assigned ID of the database at the time of backup.
        engine:
            The AWS database engine at the time of backup.
        engine_version:
            The aws database engine version at the time of backup.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        p_id:
            The Clumio-assigned ID of the backup.
        instances:
            The instances associated with a backup RDS resource.
        kms_key_native_id:
            The AWS-assigned ID of the KMS key associated with this database at the time of
            backup.
        migration_timestamp:
            The timestamp of when the migration was triggered. This field will be set only
            for
            migration granular backups. Represented in RFC-3339 format.
        option_group_name:
            Option group name associated with the backed up RDS resource
        resource_id:
            The Clumio-assigned ID of the database associated with this backup.
        resource_type:
            The type of the RDS resource associated with this backup. Possible values
            include `aws_rds_cluster` and `aws_rds_instance`.
        security_group_native_ids:
            The AWS-assigned IDs of the security groups associated with this RDS resource
            backup.
        size:
            The size of the RDS resource backup. Measured in bytes (B).
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        subnet_group_name:
            The AWS-assigned name of the subnet group associated with this RDS resource
            backup.
        tags:
            The AWS tags associated with the database at the time of backup.
        p_type:
            The type of backup. Possible values include `clumio_snapshot` and
            `granular_backup`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_azs': 'aws_azs',
        'aws_region': 'aws_region',
        'database_native_id': 'database_native_id',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'expiration_timestamp': 'expiration_timestamp',
        'p_id': 'id',
        'instances': 'instances',
        'kms_key_native_id': 'kms_key_native_id',
        'migration_timestamp': 'migration_timestamp',
        'option_group_name': 'option_group_name',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'security_group_native_ids': 'security_group_native_ids',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
        'subnet_group_name': 'subnet_group_name',
        'tags': 'tags',
        'p_type': 'type',
    }

    def __init__(
        self,
        links: rds_database_backup_links_.RdsDatabaseBackupLinks | None = None,
        account_native_id: str | None = None,
        aws_azs: Sequence[str] | None = None,
        aws_region: str | None = None,
        database_native_id: str | None = None,
        engine: str | None = None,
        engine_version: str | None = None,
        expiration_timestamp: str | None = None,
        p_id: str | None = None,
        instances: Sequence[rds_instance_model_.RdsInstanceModel] | None = None,
        kms_key_native_id: str | None = None,
        migration_timestamp: str | None = None,
        option_group_name: str | None = None,
        resource_id: str | None = None,
        resource_type: str | None = None,
        security_group_native_ids: Sequence[str] | None = None,
        size: int | None = None,
        start_timestamp: str | None = None,
        subnet_group_name: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the RdsDatabaseBackup class."""

        # Initialize members of the class
        self.links: rds_database_backup_links_.RdsDatabaseBackupLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_azs: Sequence[str] | None = aws_azs
        self.aws_region: str | None = aws_region
        self.database_native_id: str | None = database_native_id
        self.engine: str | None = engine
        self.engine_version: str | None = engine_version
        self.expiration_timestamp: str | None = expiration_timestamp
        self.p_id: str | None = p_id
        self.instances: Sequence[rds_instance_model_.RdsInstanceModel] | None = instances
        self.kms_key_native_id: str | None = kms_key_native_id
        self.migration_timestamp: str | None = migration_timestamp
        self.option_group_name: str | None = option_group_name
        self.resource_id: str | None = resource_id
        self.resource_type: str | None = resource_type
        self.security_group_native_ids: Sequence[str] | None = security_group_native_ids
        self.size: int | None = size
        self.start_timestamp: str | None = start_timestamp
        self.subnet_group_name: str | None = subnet_group_name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.p_type: str | None = p_type

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_links', None)
        val_links = rds_database_backup_links_.RdsDatabaseBackupLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_azs', None)
        val_aws_azs = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('database_native_id', None)
        val_database_native_id = val

        val = dictionary.get('engine', None)
        val_engine = val

        val = dictionary.get('engine_version', None)
        val_engine_version = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('instances', None)

        val_instances = None
        if val:
            val_instances = list()
            for value in val:
                val_instances.append(rds_instance_model_.RdsInstanceModel.from_dictionary(value))

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('migration_timestamp', None)
        val_migration_timestamp = val

        val = dictionary.get('option_group_name', None)
        val_option_group_name = val

        val = dictionary.get('resource_id', None)
        val_resource_id = val

        val = dictionary.get('resource_type', None)
        val_resource_type = val

        val = dictionary.get('security_group_native_ids', None)
        val_security_group_native_ids = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('subnet_group_name', None)
        val_subnet_group_name = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_links,
            val_account_native_id,
            val_aws_azs,
            val_aws_region,
            val_database_native_id,
            val_engine,
            val_engine_version,
            val_expiration_timestamp,
            val_p_id,
            val_instances,
            val_kms_key_native_id,
            val_migration_timestamp,
            val_option_group_name,
            val_resource_id,
            val_resource_type,
            val_security_group_native_ids,
            val_size,
            val_start_timestamp,
            val_subnet_group_name,
            val_tags,
            val_p_type,
        )
