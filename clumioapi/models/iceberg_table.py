#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import iceberg_table_embedded as iceberg_table_embedded_
from clumioapi.models import iceberg_table_links as iceberg_table_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
import requests

T = TypeVar('T', bound='IcebergTable')


@dataclasses.dataclass
class IcebergTable:
    """Implementation of the 'IcebergTable' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the iceberg table.

        AwsRegion:
            The aws region associated with the iceberg table.

        BackupStatusInfo:
            The backup status information applied to this resource.

        Catalog:
            The catalog name of the iceberg table.

        CatalogType:
            Type is mostly an asset type or the type of entity. some examples are
            "restored_file", "aws_ebs_volume",  etc.

        CreationTimestamp:
            The timestamp of when the iceberg table was created. represented in rfc-3339
            format.

        DeletionTimestamp:
            The timestamp of when the table was deleted. represented in rfc-3339 format. if
            this table has not been deleted, then this field has a value of `null`.

        DirectAssignmentPolicyId:
            The clumio-assigned id of the policy directly assigned to the entity.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the iceberg table.

        HasDirectAssignment:
            Determines whether the table has a direct assignment.

        Id:
            The clumio-assigned id of the iceberg table.

        IsDeleted:
            Determines whether the iceberg table has been deleted. if `true`, the table has
            been
            deleted.

        IsSupported:
            Determines whether the iceberg table is supported for backups.

        LastBackupTimestamp:
            The timestamp of the most recent backup of the iceberg table. represented in
            rfc-3339
            format. if the table has never been backed up, then this field has a value of
            `null`.

        Name:
            The aws-assigned name of the iceberg table.

        Namespace:
            The namespace of the iceberg table.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the iceberg
            table.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        ProtectionStatus:
            The protection status of the iceberg table. possible values include "protected",
            "unprotected", and "unsupported". if the iceberg table does not support backups,
            then
            this field has a value of `unsupported`. if the table has been deleted, then
            this
            field has a value of `null`.

        Tags:
            The aws tags applied to the iceberg table.

        UnsupportedReason:
            The reason why protection is not available. if the table is supported, then this
            field has a value of `null`.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: iceberg_table_embedded_.IcebergTableEmbedded | None = None
    Links: iceberg_table_links_.IcebergTableLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    Catalog: str | None = None
    CatalogType: str | None = None
    CreationTimestamp: str | None = None
    DeletionTimestamp: str | None = None
    DirectAssignmentPolicyId: str | None = None
    EnvironmentId: str | None = None
    HasDirectAssignment: bool | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    IsSupported: bool | None = None
    LastBackupTimestamp: str | None = None
    Name: str | None = None
    Namespace: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStatus: str | None = None
    Tags: Sequence[aws_tag_model_.AwsTagModel] | None = None
    UnsupportedReason: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('_embedded', None)
        val_embedded = iceberg_table_embedded_.IcebergTableEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = iceberg_table_links_.IcebergTableLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('catalog', None)
        val_catalog = val

        val = dictionary.get('catalog_type', None)
        val_catalog_type = val

        val = dictionary.get('creation_timestamp', None)
        val_creation_timestamp = val

        val = dictionary.get('deletion_timestamp', None)
        val_deletion_timestamp = val

        val = dictionary.get('direct_assignment_policy_id', None)
        val_direct_assignment_policy_id = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('has_direct_assignment', None)
        val_has_direct_assignment = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('namespace', None)
        val_namespace = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_backup_status_info,
            val_catalog,
            val_catalog_type,
            val_creation_timestamp,
            val_deletion_timestamp,
            val_direct_assignment_policy_id,
            val_environment_id,
            val_has_direct_assignment,
            val_id,
            val_is_deleted,
            val_is_supported,
            val_last_backup_timestamp,
            val_name,
            val_namespace,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_tags,
            val_unsupported_reason,
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
