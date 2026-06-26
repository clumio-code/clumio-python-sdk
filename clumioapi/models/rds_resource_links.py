#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
import requests

T = TypeVar('T', bound='RdsResourceLinks')


@dataclasses.dataclass
class RdsResourceLinks:
    """Implementation of the 'RdsResourceLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        ListBackupAwsRdsResources:
            A resource-specific hateoas link.

        ListRdsRestoredRecords:
            A resource-specific hateoas link.

        ReadPolicyDefinition:
            A hateoas link to the policy protecting this resource. will be omitted for
            unprotected entities.

        RestoreAwsRdsResource:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'ListBackupAwsRdsResources': 'list-backup-aws-rds-resources',
        'ListRdsRestoredRecords': 'list-rds-restored-records',
        'ReadPolicyDefinition': 'read-policy-definition',
        'RestoreAwsRdsResource': 'restore-aws-rds-resource',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    ListBackupAwsRdsResources: hateoas_link_.HateoasLink | None = None
    ListRdsRestoredRecords: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None
    RestoreAwsRdsResource: hateoas_link_.HateoasLink | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
            val_self,
            val_list_backup_aws_rds_resources,
            val_list_rds_restored_records,
            val_read_policy_definition,
            val_restore_aws_rds_resource,
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
