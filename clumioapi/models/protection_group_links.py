#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

T = TypeVar('T', bound='ProtectionGroupLinks')


class ProtectionGroupLinks:
    """Implementation of the 'ProtectionGroupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        add_bucket_protection_group:
            A resource-specific HATEOAS link.
        delete_bucket_protection_group:
            A resource-specific HATEOAS link.
        list_backup_protection_groups:
            A resource-specific HATEOAS link.
        read_organizational_unit:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        update_protection_group:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'add_bucket_protection_group': 'add-bucket-protection-group',
        'delete_bucket_protection_group': 'delete-bucket-protection-group',
        'list_backup_protection_groups': 'list-backup-protection-groups',
        'read_organizational_unit': 'read-organizational-unit',
        'read_policy_definition': 'read-policy-definition',
        'update_protection_group': 'update-protection-group',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        add_bucket_protection_group: hateoas_link_.HateoasLink,
        delete_bucket_protection_group: hateoas_link_.HateoasLink,
        list_backup_protection_groups: hateoas_link_.HateoasLink,
        read_organizational_unit: hateoas_link_.HateoasLink,
        read_policy_definition: read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink,
        update_protection_group: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the ProtectionGroupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.add_bucket_protection_group: hateoas_link_.HateoasLink = add_bucket_protection_group
        self.delete_bucket_protection_group: hateoas_link_.HateoasLink = (
            delete_bucket_protection_group
        )
        self.list_backup_protection_groups: hateoas_link_.HateoasLink = (
            list_backup_protection_groups
        )
        self.read_organizational_unit: hateoas_link_.HateoasLink = read_organizational_unit
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition
        self.update_protection_group: hateoas_link_.HateoasLink = update_protection_group

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

        # Extract variables from the dictionary
        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['add-bucket-protection-group']
        val_add_bucket_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['delete-bucket-protection-group']
        val_delete_bucket_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['list-backup-protection-groups']
        val_list_backup_protection_groups = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-organizational-unit']
        val_read_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-policy-definition']
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary['update-protection-group']
        val_update_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_add_bucket_protection_group,  # type: ignore
            val_delete_bucket_protection_group,  # type: ignore
            val_list_backup_protection_groups,  # type: ignore
            val_read_organizational_unit,  # type: ignore
            val_read_policy_definition,  # type: ignore
            val_update_protection_group,  # type: ignore
        )
