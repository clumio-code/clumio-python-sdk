#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

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
    _names: dict[str, str] = {
        'p_self': '_self',
        'list_aws_rds_resources_option_groups': 'list-aws-rds-resources-option-groups',
        'restore_aws_rds_resource': 'restore-aws-rds-resource',
        'restore_rds_record': 'restore-rds-record',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        list_aws_rds_resources_option_groups: hateoas_link_.HateoasLink,
        restore_aws_rds_resource: hateoas_link_.HateoasLink,
        restore_rds_record: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the RdsDatabaseBackupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.list_aws_rds_resources_option_groups: hateoas_link_.HateoasLink = (
            list_aws_rds_resources_option_groups
        )
        self.restore_aws_rds_resource: hateoas_link_.HateoasLink = restore_aws_rds_resource
        self.restore_rds_record: hateoas_link_.HateoasLink = restore_rds_record

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

        val = dictionary['list-aws-rds-resources-option-groups']
        val_list_aws_rds_resources_option_groups = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['restore-aws-rds-resource']
        val_restore_aws_rds_resource = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['restore-rds-record']
        val_restore_rds_record = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_list_aws_rds_resources_option_groups,  # type: ignore
            val_restore_aws_rds_resource,  # type: ignore
            val_restore_rds_record,  # type: ignore
        )
