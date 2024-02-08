#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_policy_definition_hateoas_link

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
        read_organizational_unit:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        update_protection_group:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'add_bucket_protection_group': 'add-bucket-protection-group',
        'delete_bucket_protection_group': 'delete-bucket-protection-group',
        'read_organizational_unit': 'read-organizational-unit',
        'read_policy_definition': 'read-policy-definition',
        'update_protection_group': 'update-protection-group',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        add_bucket_protection_group: hateoas_link.HateoasLink = None,
        delete_bucket_protection_group: hateoas_link.HateoasLink = None,
        read_organizational_unit: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        update_protection_group: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the ProtectionGroupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.add_bucket_protection_group: hateoas_link.HateoasLink = add_bucket_protection_group
        self.delete_bucket_protection_group: hateoas_link.HateoasLink = (
            delete_bucket_protection_group
        )
        self.read_organizational_unit: hateoas_link.HateoasLink = read_organizational_unit
        self.read_policy_definition: (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition
        self.update_protection_group: hateoas_link.HateoasLink = update_protection_group

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'add-bucket-protection-group'
        add_bucket_protection_group = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'delete-bucket-protection-group'
        delete_bucket_protection_group = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-organizational-unit'
        read_organizational_unit = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-policy-definition'
        read_policy_definition = (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'update-protection-group'
        update_protection_group = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            add_bucket_protection_group,
            delete_bucket_protection_group,
            read_organizational_unit,
            read_policy_definition,
            update_protection_group,
        )
