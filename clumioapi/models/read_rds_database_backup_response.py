#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import rds_database_backup_links
from clumioapi.models import rds_instance_model

T = TypeVar('T', bound='ReadRdsDatabaseBackupResponse')


class ReadRdsDatabaseBackupResponse:
    """Implementation of the 'ReadRdsDatabaseBackupResponse' model.

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
    _names = {
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
        links: rds_database_backup_links.RdsDatabaseBackupLinks = None,
        account_native_id: str = None,
        aws_azs: Sequence[str] = None,
        aws_region: str = None,
        database_native_id: str = None,
        engine: str = None,
        engine_version: str = None,
        expiration_timestamp: str = None,
        p_id: str = None,
        instances: Sequence[rds_instance_model.RdsInstanceModel] = None,
        kms_key_native_id: str = None,
        migration_timestamp: str = None,
        option_group_name: str = None,
        resource_id: str = None,
        resource_type: str = None,
        security_group_native_ids: Sequence[str] = None,
        size: int = None,
        start_timestamp: str = None,
        subnet_group_name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the ReadRdsDatabaseBackupResponse class."""

        # Initialize members of the class
        self.links: rds_database_backup_links.RdsDatabaseBackupLinks = links
        self.account_native_id: str = account_native_id
        self.aws_azs: Sequence[str] = aws_azs
        self.aws_region: str = aws_region
        self.database_native_id: str = database_native_id
        self.engine: str = engine
        self.engine_version: str = engine_version
        self.expiration_timestamp: str = expiration_timestamp
        self.p_id: str = p_id
        self.instances: Sequence[rds_instance_model.RdsInstanceModel] = instances
        self.kms_key_native_id: str = kms_key_native_id
        self.migration_timestamp: str = migration_timestamp
        self.option_group_name: str = option_group_name
        self.resource_id: str = resource_id
        self.resource_type: str = resource_type
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.size: int = size
        self.start_timestamp: str = start_timestamp
        self.subnet_group_name: str = subnet_group_name
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.p_type: str = p_type

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None

        # Extract variables from the dictionary
        key = '_links'
        links = (
            rds_database_backup_links.RdsDatabaseBackupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_azs = dictionary.get('aws_azs')
        aws_region = dictionary.get('aws_region')
        database_native_id = dictionary.get('database_native_id')
        engine = dictionary.get('engine')
        engine_version = dictionary.get('engine_version')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        p_id = dictionary.get('id')
        instances = None
        if dictionary.get('instances'):
            instances = list()
            for value in dictionary.get('instances'):
                instances.append(rds_instance_model.RdsInstanceModel.from_dictionary(value))

        kms_key_native_id = dictionary.get('kms_key_native_id')
        migration_timestamp = dictionary.get('migration_timestamp')
        option_group_name = dictionary.get('option_group_name')
        resource_id = dictionary.get('resource_id')
        resource_type = dictionary.get('resource_type')
        security_group_native_ids = dictionary.get('security_group_native_ids')
        size = dictionary.get('size')
        start_timestamp = dictionary.get('start_timestamp')
        subnet_group_name = dictionary.get('subnet_group_name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            links,
            account_native_id,
            aws_azs,
            aws_region,
            database_native_id,
            engine,
            engine_version,
            expiration_timestamp,
            p_id,
            instances,
            kms_key_native_id,
            migration_timestamp,
            option_group_name,
            resource_id,
            resource_type,
            security_group_native_ids,
            size,
            start_timestamp,
            subnet_group_name,
            tags,
            p_type,
        )
