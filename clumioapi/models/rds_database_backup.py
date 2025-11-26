#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import rds_database_backup_links as rds_database_backup_links_
from clumioapi.models import rds_instance_model as rds_instance_model_
import requests

T = TypeVar('T', bound='RdsDatabaseBackup')


@dataclasses.dataclass
class RdsDatabaseBackup:
    """Implementation of the 'RdsDatabaseBackup' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with this database at the time of
            backup.

        AwsAzs:
            The aws availability zones associated with this database at the time of backup.

        AwsRegion:
            The aws region associated with this environment.

        DatabaseNativeId:
            The aws-assigned id of the database at the time of backup.

        Engine:
            The aws database engine at the time of backup.

        EngineVersion:
            The aws database engine version at the time of backup.

        ExpirationTimestamp:
            The timestamp of when this backup expires. represented in rfc-3339 format.

        Id:
            The clumio-assigned id of the backup.

        Instances:
            The instances associated with a backup rds resource.

        KmsKeyNativeId:
            The aws-assigned id of the kms key associated with this database at the time of
            backup.

        MigrationTimestamp:
            The timestamp of when the migration was triggered. this field will be set only
            for
            migration granular backups. represented in rfc-3339 format.

        OptionGroupName:
            Option group name associated with the backed up rds resource.

        ResourceId:
            The clumio-assigned id of the database associated with this backup.

        ResourceType:
            The type of the rds resource associated with this backup. possible values
            include `aws_rds_cluster` and `aws_rds_instance`.

        SecurityGroupNativeIds:
            The aws-assigned ids of the security groups associated with this rds resource
            backup.

        Size:
            The size of the rds resource backup. measured in bytes (b).

        StartTimestamp:
            The timestamp of when this backup started. represented in rfc-3339 format.

        SubnetGroupName:
            The aws-assigned name of the subnet group associated with this rds resource
            backup.

        Tags:
            The aws tags associated with the database at the time of backup.

        Type:
            The type of backup. possible values include `clumio_snapshot` and
            `granular_backup`.

    """

    Links: rds_database_backup_links_.RdsDatabaseBackupLinks | None = None
    AccountNativeId: str | None = None
    AwsAzs: Sequence[str] | None = None
    AwsRegion: str | None = None
    DatabaseNativeId: str | None = None
    Engine: str | None = None
    EngineVersion: str | None = None
    ExpirationTimestamp: str | None = None
    Id: str | None = None
    Instances: Sequence[rds_instance_model_.RdsInstanceModel] | None = None
    KmsKeyNativeId: str | None = None
    MigrationTimestamp: str | None = None
    OptionGroupName: str | None = None
    ResourceId: str | None = None
    ResourceType: str | None = None
    SecurityGroupNativeIds: Sequence[str] | None = None
    Size: int | None = None
    StartTimestamp: str | None = None
    SubnetGroupName: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    Type: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val_id = val

        val = dictionary.get('instances', None)

        val_instances = []
        if val:
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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
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
            val_type,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
