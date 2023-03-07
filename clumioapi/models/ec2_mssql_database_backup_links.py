#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='EC2MSSQLDatabaseBackupLinks')


class EC2MSSQLDatabaseBackupLinks:
    """Implementation of the 'EC2MSSQLDatabaseBackupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_aws_environment:
            A resource-specific HATEOAS link.
        restore_ec2_mssql_database:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_aws_environment': 'read-aws-environment',
        'restore_ec2_mssql_database': 'restore-ec2-mssql-database',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_aws_environment: hateoas_link.HateoasLink = None,
        restore_ec2_mssql_database: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseBackupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_aws_environment: hateoas_link.HateoasLink = read_aws_environment
        self.restore_ec2_mssql_database: hateoas_link.HateoasLink = restore_ec2_mssql_database

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

        key = 'read-aws-environment'
        read_aws_environment = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore-ec2-mssql-database'
        restore_ec2_mssql_database = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_aws_environment, restore_ec2_mssql_database)
