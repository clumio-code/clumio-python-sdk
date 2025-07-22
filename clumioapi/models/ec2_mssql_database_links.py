#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

T = TypeVar('T', bound='EC2MSSQLDatabaseLinks')


class EC2MSSQLDatabaseLinks:
    """Implementation of the 'EC2MSSQLDatabaseLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        create_backup_ec2_mssql_database:
            A resource-specific HATEOAS link.
        list_backup_ec2_mssql_databases:
            A resource-specific HATEOAS link.
        read_aws_ec2_instance:
            A resource-specific HATEOAS link.
        read_aws_environment:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'create_backup_ec2_mssql_database': 'create-backup-ec2-mssql-database',
        'list_backup_ec2_mssql_databases': 'list-backup-ec2-mssql-databases',
        'read_aws_ec2_instance': 'read-aws-ec2-instance',
        'read_aws_environment': 'read-aws-environment',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        create_backup_ec2_mssql_database: hateoas_link_.HateoasLink,
        list_backup_ec2_mssql_databases: hateoas_link_.HateoasLink,
        read_aws_ec2_instance: hateoas_link_.HateoasLink,
        read_aws_environment: hateoas_link_.HateoasLink,
        read_policy_definition: read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.create_backup_ec2_mssql_database: hateoas_link_.HateoasLink = (
            create_backup_ec2_mssql_database
        )
        self.list_backup_ec2_mssql_databases: hateoas_link_.HateoasLink = (
            list_backup_ec2_mssql_databases
        )
        self.read_aws_ec2_instance: hateoas_link_.HateoasLink = read_aws_ec2_instance
        self.read_aws_environment: hateoas_link_.HateoasLink = read_aws_environment
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition

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

        val = dictionary['create-backup-ec2-mssql-database']
        val_create_backup_ec2_mssql_database = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['list-backup-ec2-mssql-databases']
        val_list_backup_ec2_mssql_databases = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-aws-ec2-instance']
        val_read_aws_ec2_instance = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-aws-environment']
        val_read_aws_environment = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-policy-definition']
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_create_backup_ec2_mssql_database,  # type: ignore
            val_list_backup_ec2_mssql_databases,  # type: ignore
            val_read_aws_ec2_instance,  # type: ignore
            val_read_aws_environment,  # type: ignore
            val_read_policy_definition,  # type: ignore
        )
