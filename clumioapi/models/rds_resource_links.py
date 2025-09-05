#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

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
    _names: dict[str, str] = {
        'p_self': '_self',
        'list_backup_aws_rds_resources': 'list-backup-aws-rds-resources',
        'list_rds_restored_records': 'list-rds-restored-records',
        'read_policy_definition': 'read-policy-definition',
        'restore_aws_rds_resource': 'restore-aws-rds-resource',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        list_backup_aws_rds_resources: hateoas_link_.HateoasLink | None = None,
        list_rds_restored_records: hateoas_link_.HateoasLink | None = None,
        read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = None,
        restore_aws_rds_resource: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the RdsResourceLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.list_backup_aws_rds_resources: hateoas_link_.HateoasLink | None = (
            list_backup_aws_rds_resources
        )
        self.list_rds_restored_records: hateoas_link_.HateoasLink | None = list_rds_restored_records
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = read_policy_definition
        self.restore_aws_rds_resource: hateoas_link_.HateoasLink | None = restore_aws_rds_resource

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

        val = dictionary.get('list-backup-aws-rds-resources', None)
        val_list_backup_aws_rds_resources = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-rds-restored-records', None)
        val_list_rds_restored_records = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary.get('restore-aws-rds-resource', None)
        val_restore_aws_rds_resource = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_list_backup_aws_rds_resources,
            val_list_rds_restored_records,
            val_read_policy_definition,
            val_restore_aws_rds_resource,
        )
