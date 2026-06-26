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
            A hateoas link to the policy protecting this resource. will be omitted for
            unprotected entities.

        RestoreProtectionGroup:
            A resource-specific hateoas link.

        UpdateProtectionGroup:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'AddBucketProtectionGroup': 'add-bucket-protection-group',
        'DeleteBucketProtectionGroup': 'delete-bucket-protection-group',
        'ListBackupProtectionGroups': 'list-backup-protection-groups',
        'ReadOrganizationalUnit': 'read-organizational-unit',
        'ReadPolicyDefinition': 'read-policy-definition',
        'RestoreProtectionGroup': 'restore-protection-group',
        'UpdateProtectionGroup': 'update-protection-group',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    AddBucketProtectionGroup: hateoas_link_.HateoasLink | None = None
    DeleteBucketProtectionGroup: hateoas_link_.HateoasLink | None = None
    ListBackupProtectionGroups: hateoas_link_.HateoasLink | None = None
    ReadOrganizationalUnit: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None
    RestoreProtectionGroup: hateoas_link_.HateoasLink | None = None
    UpdateProtectionGroup: hateoas_link_.HateoasLink | None = None

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

        val = dictionary.get('restore-protection-group', None)
        val_restore_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

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
            val_restore_protection_group,
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
