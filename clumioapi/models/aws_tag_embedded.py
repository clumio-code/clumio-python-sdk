#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='AwsTagEmbedded')


@dataclasses.dataclass
class AwsTagEmbedded:
    """Implementation of the 'AwsTagEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        ReadAwsEnvironmentTagBackupStatusStats:
            Embedded aws backup statistics for each tag.

        ReadAwsEnvironmentTagDocumentdbProtectionStats:
            Embedded aws documentdb statistics for each tag.

        ReadAwsEnvironmentTagDynamodbTablesProtectionStats:
            Embedded aws dynamodb statistics for each tag.

        ReadAwsEnvironmentTagEbsVolumesProtectionStats:
            Embedded aws ebs statistics for each tag.

        ReadAwsEnvironmentTagEc2InstancesProtectionStats:
            Embedded aws ec2 statistics for each tag.

        ReadAwsEnvironmentTagIcebergS3TablesProtectionStats:
            Embedded aws s3 iceberg table statistics for each tag.

        ReadAwsEnvironmentTagNeptuneProtectionStats:
            Embedded aws neptune statistics for each tag.

        ReadAwsEnvironmentTagProtectionGroupsProtectionStats:
            Embedded protection group statistics for each tag.

        ReadAwsEnvironmentTagRdsResourcesProtectionStats:
            Embedded aws rds statistics for each tag.

        ReadPolicyDefinition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. unprotected resources will not have
            an associated policy.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'ReadAwsEnvironmentTagBackupStatusStats': 'read-aws-environment-tag-backup-status-stats',
        'ReadAwsEnvironmentTagDocumentdbProtectionStats': 'read-aws-environment-tag-documentdb-protection-stats',
        'ReadAwsEnvironmentTagDynamodbTablesProtectionStats': 'read-aws-environment-tag-dynamodb-tables-protection-stats',
        'ReadAwsEnvironmentTagEbsVolumesProtectionStats': 'read-aws-environment-tag-ebs-volumes-protection-stats',
        'ReadAwsEnvironmentTagEc2InstancesProtectionStats': 'read-aws-environment-tag-ec2-instances-protection-stats',
        'ReadAwsEnvironmentTagIcebergS3TablesProtectionStats': 'read-aws-environment-tag-iceberg-s3-tables-protection-stats',
        'ReadAwsEnvironmentTagNeptuneProtectionStats': 'read-aws-environment-tag-neptune-protection-stats',
        'ReadAwsEnvironmentTagProtectionGroupsProtectionStats': 'read-aws-environment-tag-protection-groups-protection-stats',
        'ReadAwsEnvironmentTagRdsResourcesProtectionStats': 'read-aws-environment-tag-rds-resources-protection-stats',
        'ReadPolicyDefinition': 'read-policy-definition',
    }

    ReadAwsEnvironmentTagBackupStatusStats: object | None = None
    ReadAwsEnvironmentTagDocumentdbProtectionStats: object | None = None
    ReadAwsEnvironmentTagDynamodbTablesProtectionStats: object | None = None
    ReadAwsEnvironmentTagEbsVolumesProtectionStats: object | None = None
    ReadAwsEnvironmentTagEc2InstancesProtectionStats: object | None = None
    ReadAwsEnvironmentTagIcebergS3TablesProtectionStats: object | None = None
    ReadAwsEnvironmentTagNeptuneProtectionStats: object | None = None
    ReadAwsEnvironmentTagProtectionGroupsProtectionStats: object | None = None
    ReadAwsEnvironmentTagRdsResourcesProtectionStats: object | None = None
    ReadPolicyDefinition: object | None = None

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
        val = dictionary.get('read-aws-environment-tag-backup-status-stats', None)
        val_read_aws_environment_tag_backup_status_stats = val

        val = dictionary.get('read-aws-environment-tag-documentdb-protection-stats', None)
        val_read_aws_environment_tag_documentdb_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-dynamodb-tables-protection-stats', None)
        val_read_aws_environment_tag_dynamodb_tables_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-ebs-volumes-protection-stats', None)
        val_read_aws_environment_tag_ebs_volumes_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-ec2-instances-protection-stats', None)
        val_read_aws_environment_tag_ec2_instances_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-iceberg-s3-tables-protection-stats', None)
        val_read_aws_environment_tag_iceberg_s3_tables_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-neptune-protection-stats', None)
        val_read_aws_environment_tag_neptune_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-protection-groups-protection-stats', None)
        val_read_aws_environment_tag_protection_groups_protection_stats = val

        val = dictionary.get('read-aws-environment-tag-rds-resources-protection-stats', None)
        val_read_aws_environment_tag_rds_resources_protection_stats = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_read_aws_environment_tag_backup_status_stats,
            val_read_aws_environment_tag_documentdb_protection_stats,
            val_read_aws_environment_tag_dynamodb_tables_protection_stats,
            val_read_aws_environment_tag_ebs_volumes_protection_stats,
            val_read_aws_environment_tag_ec2_instances_protection_stats,
            val_read_aws_environment_tag_iceberg_s3_tables_protection_stats,
            val_read_aws_environment_tag_neptune_protection_stats,
            val_read_aws_environment_tag_protection_groups_protection_stats,
            val_read_aws_environment_tag_rds_resources_protection_stats,
            val_read_policy_definition,
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
