#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

T = TypeVar('T', bound='ProtectionGroupBucketLinks')


class ProtectionGroupBucketLinks:
    """Implementation of the 'ProtectionGroupBucketLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_bucket_protection_group:
            A resource-specific HATEOAS link.
        list_backup_protection_group_s3_assets:
            A resource-specific HATEOAS link.
        read_organizational_unit:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_bucket_protection_group': 'delete-bucket-protection-group',
        'list_backup_protection_group_s3_assets': 'list-backup-protection-group-s3-assets',
        'read_organizational_unit': 'read-organizational-unit',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        delete_bucket_protection_group: hateoas_link_.HateoasLink | None = None,
        list_backup_protection_group_s3_assets: hateoas_link_.HateoasLink | None = None,
        read_organizational_unit: hateoas_link_.HateoasLink | None = None,
        read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = None,
    ) -> None:
        """Constructor for the ProtectionGroupBucketLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.delete_bucket_protection_group: hateoas_link_.HateoasLink | None = (
            delete_bucket_protection_group
        )
        self.list_backup_protection_group_s3_assets: hateoas_link_.HateoasLink | None = (
            list_backup_protection_group_s3_assets
        )
        self.read_organizational_unit: hateoas_link_.HateoasLink | None = read_organizational_unit
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = read_policy_definition

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
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('delete-bucket-protection-group', None)
        val_delete_bucket_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-backup-protection-group-s3-assets', None)
        val_list_backup_protection_group_s3_assets = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-organizational-unit', None)
        val_read_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_p_self,
            val_delete_bucket_protection_group,
            val_list_backup_protection_group_s3_assets,
            val_read_organizational_unit,
            val_read_policy_definition,
        )
