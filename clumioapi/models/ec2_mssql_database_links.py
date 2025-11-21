#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
import requests

T = TypeVar('T', bound='EC2MSSQLDatabaseLinks')


@dataclasses.dataclass
class EC2MSSQLDatabaseLinks:
    """Implementation of the 'EC2MSSQLDatabaseLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        CreateBackupEc2MssqlDatabase:
            A resource-specific hateoas link.

        ListBackupEc2MssqlDatabases:
            A resource-specific hateoas link.

        ReadAwsEc2Instance:
            A resource-specific hateoas link.

        ReadAwsEnvironment:
            A resource-specific hateoas link.

        ReadPolicyDefinition:
            A hateoas link to the policy protecting this resource. will be omitted for
            unprotected entities.

    """

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    CreateBackupEc2MssqlDatabase: hateoas_link_.HateoasLink | None = None
    ListBackupEc2MssqlDatabases: hateoas_link_.HateoasLink | None = None
    ReadAwsEc2Instance: hateoas_link_.HateoasLink | None = None
    ReadAwsEnvironment: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('create-backup-ec2-mssql-database', None)
        val_create_backup_ec2_mssql_database = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-backup-ec2-mssql-databases', None)
        val_list_backup_ec2_mssql_databases = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-aws-ec2-instance', None)
        val_read_aws_ec2_instance = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-aws-environment', None)
        val_read_aws_environment = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_self,
            val_create_backup_ec2_mssql_database,
            val_list_backup_ec2_mssql_databases,
            val_read_aws_ec2_instance,
            val_read_aws_environment,
            val_read_policy_definition,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
