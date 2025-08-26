#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import protect_entities_hateoas_link as protect_entities_hateoas_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
from clumioapi.models import unprotect_entities_hateoas_link as unprotect_entities_hateoas_link_

T = TypeVar('T', bound='AwsTagLinks')


class AwsTagLinks:
    """Implementation of the 'AwsTagLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        protect_entities:
            A HATEOAS link to protect the entities.
        read_aws_environment_tag_ebs_volumes_protection_stats:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        unprotect_entities:
            A HATEOAS link to unprotect the entities.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'protect_entities': 'protect-entities',
        'read_aws_environment_tag_ebs_volumes_protection_stats': 'read-aws-environment-tag-ebs-volumes-protection-stats',
        'read_policy_definition': 'read-policy-definition',
        'unprotect_entities': 'unprotect-entities',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        protect_entities: protect_entities_hateoas_link_.ProtectEntitiesHateoasLink | None = None,
        read_aws_environment_tag_ebs_volumes_protection_stats: (
            hateoas_link_.HateoasLink | None
        ) = None,
        read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = None,
        unprotect_entities: (
            unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink | None
        ) = None,
    ) -> None:
        """Constructor for the AwsTagLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.protect_entities: protect_entities_hateoas_link_.ProtectEntitiesHateoasLink | None = (
            protect_entities
        )
        self.read_aws_environment_tag_ebs_volumes_protection_stats: (
            hateoas_link_.HateoasLink | None
        ) = read_aws_environment_tag_ebs_volumes_protection_stats
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = read_policy_definition
        self.unprotect_entities: (
            unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink | None
        ) = unprotect_entities

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

        val = dictionary.get('protect-entities', None)
        val_protect_entities = (
            protect_entities_hateoas_link_.ProtectEntitiesHateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-ebs-volumes-protection-stats', None)
        val_read_aws_environment_tag_ebs_volumes_protection_stats = (
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
            val_p_self,
            val_protect_entities,
            val_read_aws_environment_tag_ebs_volumes_protection_stats,
            val_read_policy_definition,
            val_unprotect_entities,
        )
