#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
import requests

T = TypeVar('T', bound='ProtectionGroupLinks')


@dataclasses.dataclass
class ProtectionGroupLinks:
    """Implementation of the 'ProtectionGroupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        AddBucketProtectionGroup:
            A resource-specific hateoas link.

        DeleteBucketProtectionGroup:
            A resource-specific hateoas link.

        ListBackupProtectionGroups:
            A resource-specific hateoas link.

        ReadOrganizationalUnit:
            A resource-specific hateoas link.

        ReadPolicyDefinition:
            A hateoas link to the policy protecting this resource. will be omitted for unprotected entities.

        UpdateProtectionGroup:
            A resource-specific hateoas link.

    """

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    AddBucketProtectionGroup: hateoas_link_.HateoasLink | None = None
    DeleteBucketProtectionGroup: hateoas_link_.HateoasLink | None = None
    ListBackupProtectionGroups: hateoas_link_.HateoasLink | None = None
    ReadOrganizationalUnit: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None
    UpdateProtectionGroup: hateoas_link_.HateoasLink | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('add-bucket-protection-group', None)
        val_add_bucket_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('delete-bucket-protection-group', None)
        val_delete_bucket_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-backup-protection-groups', None)
        val_list_backup_protection_groups = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-organizational-unit', None)
        val_read_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary.get('update-protection-group', None)
        val_update_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_add_bucket_protection_group,
            val_delete_bucket_protection_group,
            val_list_backup_protection_groups,
            val_read_organizational_unit,
            val_read_policy_definition,
            val_update_protection_group,
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
