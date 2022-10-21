#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link, hateoas_self_link, read_policy_definition_hateoas_link

T = TypeVar('T', bound='EbsVolumeLinks')


class EbsVolumeLinks:
    """Implementation of the 'EbsVolumeLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        create_backup_aws_ebs_volume:
            A resource-specific HATEOAS link.
        list_backup_aws_ebs_volumes:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'create_backup_aws_ebs_volume': 'create-backup-aws-ebs-volume',
        'list_backup_aws_ebs_volumes': 'list-backup-aws-ebs-volumes',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        create_backup_aws_ebs_volume: hateoas_link.HateoasLink = None,
        list_backup_aws_ebs_volumes: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
    ) -> None:
        """Constructor for the EbsVolumeLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.create_backup_aws_ebs_volume: hateoas_link.HateoasLink = create_backup_aws_ebs_volume
        self.list_backup_aws_ebs_volumes: hateoas_link.HateoasLink = list_backup_aws_ebs_volumes
        self.read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = (
            read_policy_definition
        )

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

        key = 'create-backup-aws-ebs-volume'
        create_backup_aws_ebs_volume = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'list-backup-aws-ebs-volumes'
        list_backup_aws_ebs_volumes = (
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

        # Return an object of this model
        return cls(
            p_self,
            create_backup_aws_ebs_volume,
            list_backup_aws_ebs_volumes,
            read_policy_definition,
        )
