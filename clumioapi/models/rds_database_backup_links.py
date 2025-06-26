#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='RdsDatabaseBackupLinks')


class RdsDatabaseBackupLinks:
    """Implementation of the 'RdsDatabaseBackupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        list_aws_rds_resources_option_groups:
            A resource-specific HATEOAS link.
        restore_aws_rds_resource:
            A resource-specific HATEOAS link.
        restore_rds_record:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'list_aws_rds_resources_option_groups': 'list-aws-rds-resources-option-groups',
        'restore_aws_rds_resource': 'restore-aws-rds-resource',
        'restore_rds_record': 'restore-rds-record',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        list_aws_rds_resources_option_groups: hateoas_link.HateoasLink = None,
        restore_aws_rds_resource: hateoas_link.HateoasLink = None,
        restore_rds_record: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the RdsDatabaseBackupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.list_aws_rds_resources_option_groups: hateoas_link.HateoasLink = (
            list_aws_rds_resources_option_groups
        )
        self.restore_aws_rds_resource: hateoas_link.HateoasLink = restore_aws_rds_resource
        self.restore_rds_record: hateoas_link.HateoasLink = restore_rds_record

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

        key = 'list-aws-rds-resources-option-groups'
        list_aws_rds_resources_option_groups = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore-aws-rds-resource'
        restore_aws_rds_resource = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore-rds-record'
        restore_rds_record = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            list_aws_rds_resources_option_groups,
            restore_aws_rds_resource,
            restore_rds_record,
        )
