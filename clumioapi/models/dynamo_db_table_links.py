#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_policy_definition_hateoas_link

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
    _names = {
        'p_self': '_self',
        'create_backup_aws_dynamodb_table': 'create-backup-aws-dynamodb-table',
        'list_backup_aws_dynamodb_tables': 'list-backup-aws-dynamodb-tables',
        'read_policy_definition': 'read-policy-definition',
        'restore_aws_dynamodb_table': 'restore-aws-dynamodb-table',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        create_backup_aws_dynamodb_table: hateoas_link.HateoasLink = None,
        list_backup_aws_dynamodb_tables: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        restore_aws_dynamodb_table: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the DynamoDBTableLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.create_backup_aws_dynamodb_table: hateoas_link.HateoasLink = (
            create_backup_aws_dynamodb_table
        )
        self.list_backup_aws_dynamodb_tables: hateoas_link.HateoasLink = (
            list_backup_aws_dynamodb_tables
        )
        self.read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = (
            read_policy_definition
        )
        self.restore_aws_dynamodb_table: hateoas_link.HateoasLink = restore_aws_dynamodb_table

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

        key = 'create-backup-aws-dynamodb-table'
        create_backup_aws_dynamodb_table = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'list-backup-aws-dynamodb-tables'
        list_backup_aws_dynamodb_tables = (
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

        key = 'restore-aws-dynamodb-table'
        restore_aws_dynamodb_table = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            create_backup_aws_dynamodb_table,
            list_backup_aws_dynamodb_tables,
            read_policy_definition,
            restore_aws_dynamodb_table,
        )
