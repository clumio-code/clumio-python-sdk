#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import protect_entities_hateoas_link as protect_entities_hateoas_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
from clumioapi.models import unprotect_entities_hateoas_link as unprotect_entities_hateoas_link_
import requests

T = TypeVar('T', bound='AwsTagLinks')


@dataclasses.dataclass
class AwsTagLinks:
    """Implementation of the 'AwsTagLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        ProtectEntities:
            A hateoas link to protect the entities.

        ReadAwsEnvironmentTagBackupStatusStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagDocumentdbProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagDynamodbTablesProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagEbsVolumesProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagEc2InstancesProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagIcebergS3TablesProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagNeptuneProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagProtectionGroupsProtectionStats:
            A resource-specific hateoas link.

        ReadAwsEnvironmentTagRdsResourcesProtectionStats:
            A resource-specific hateoas link.

        ReadPolicyDefinition:
            A hateoas link to the policy protecting this resource. will be omitted for
            unprotected entities.

        UnprotectEntities:
            A hateoas link to unprotect the entities.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'ProtectEntities': 'protect-entities',
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
        'UnprotectEntities': 'unprotect-entities',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    ProtectEntities: protect_entities_hateoas_link_.ProtectEntitiesHateoasLink | None = None
    ReadAwsEnvironmentTagBackupStatusStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagDocumentdbProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagDynamodbTablesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagEbsVolumesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagEc2InstancesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagIcebergS3TablesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagNeptuneProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagProtectionGroupsProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironmentTagRdsResourcesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None
    UnprotectEntities: unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink | None = None

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
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('protect-entities', None)
        val_protect_entities = (
            protect_entities_hateoas_link_.ProtectEntitiesHateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-backup-status-stats', None)
        val_read_aws_environment_tag_backup_status_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-documentdb-protection-stats', None)
        val_read_aws_environment_tag_documentdb_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-dynamodb-tables-protection-stats', None)
        val_read_aws_environment_tag_dynamodb_tables_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-ebs-volumes-protection-stats', None)
        val_read_aws_environment_tag_ebs_volumes_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-ec2-instances-protection-stats', None)
        val_read_aws_environment_tag_ec2_instances_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-iceberg-s3-tables-protection-stats', None)
        val_read_aws_environment_tag_iceberg_s3_tables_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-neptune-protection-stats', None)
        val_read_aws_environment_tag_neptune_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-protection-groups-protection-stats', None)
        val_read_aws_environment_tag_protection_groups_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-rds-resources-protection-stats', None)
        val_read_aws_environment_tag_rds_resources_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary.get('unprotect-entities', None)
        val_unprotect_entities = (
            unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_self,
            val_protect_entities,
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
            val_unprotect_entities,
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
