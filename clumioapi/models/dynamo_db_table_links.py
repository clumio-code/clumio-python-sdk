#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

T = TypeVar('T', bound='DynamoDBTableLinks')


class DynamoDBTableLinks:
    """Implementation of the 'DynamoDBTableLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        create_backup_aws_dynamodb_table:
            A resource-specific HATEOAS link.
        list_backup_aws_dynamodb_tables:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        restore_aws_dynamodb_table:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'create_backup_aws_dynamodb_table': 'create-backup-aws-dynamodb-table',
        'list_backup_aws_dynamodb_tables': 'list-backup-aws-dynamodb-tables',
        'read_policy_definition': 'read-policy-definition',
        'restore_aws_dynamodb_table': 'restore-aws-dynamodb-table',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        create_backup_aws_dynamodb_table: hateoas_link_.HateoasLink | None = None,
        list_backup_aws_dynamodb_tables: hateoas_link_.HateoasLink | None = None,
        read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = None,
        restore_aws_dynamodb_table: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the DynamoDBTableLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.create_backup_aws_dynamodb_table: hateoas_link_.HateoasLink | None = (
            create_backup_aws_dynamodb_table
        )
        self.list_backup_aws_dynamodb_tables: hateoas_link_.HateoasLink | None = (
            list_backup_aws_dynamodb_tables
        )
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
        ) = read_policy_definition
        self.restore_aws_dynamodb_table: hateoas_link_.HateoasLink | None = (
            restore_aws_dynamodb_table
        )

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

        val = dictionary.get('create-backup-aws-dynamodb-table', None)
        val_create_backup_aws_dynamodb_table = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-backup-aws-dynamodb-tables', None)
        val_list_backup_aws_dynamodb_tables = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary.get('restore-aws-dynamodb-table', None)
        val_restore_aws_dynamodb_table = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_create_backup_aws_dynamodb_table,
            val_list_backup_aws_dynamodb_tables,
            val_read_policy_definition,
            val_restore_aws_dynamodb_table,
        )
