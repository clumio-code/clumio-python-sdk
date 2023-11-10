#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_policy_definition_hateoas_link

T = TypeVar('T', bound='RdsResourceLinks')


class RdsResourceLinks:
    """Implementation of the 'RdsResourceLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        list_backup_aws_rds_resources:
            A resource-specific HATEOAS link.
        list_rds_restored_records:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        restore_aws_rds_resource:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'list_backup_aws_rds_resources': 'list-backup-aws-rds-resources',
        'list_rds_restored_records': 'list-rds-restored-records',
        'read_policy_definition': 'read-policy-definition',
        'restore_aws_rds_resource': 'restore-aws-rds-resource',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        list_backup_aws_rds_resources: hateoas_link.HateoasLink = None,
        list_rds_restored_records: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        restore_aws_rds_resource: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the RdsResourceLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.list_backup_aws_rds_resources: hateoas_link.HateoasLink = list_backup_aws_rds_resources
        self.list_rds_restored_records: hateoas_link.HateoasLink = list_rds_restored_records
        self.read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = (
            read_policy_definition
        )
        self.restore_aws_rds_resource: hateoas_link.HateoasLink = restore_aws_rds_resource

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

        key = 'list-backup-aws-rds-resources'
        list_backup_aws_rds_resources = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'list-rds-restored-records'
        list_rds_restored_records = (
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

        key = 'restore-aws-rds-resource'
        restore_aws_rds_resource = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            list_backup_aws_rds_resources,
            list_rds_restored_records,
            read_policy_definition,
            restore_aws_rds_resource,
        )
