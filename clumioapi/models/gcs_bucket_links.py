#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='GCSBucketLinks')


@dataclasses.dataclass
class GCSBucketLinks:
    """Implementation of the 'GCSBucketLinks' model.

    Attributes:
        Self:
            The hateoas link to this resource.

        CreateGcpProtectionGroup:
            A resource-specific hateoas link.

        ListBackupGcpProtectionGroupGcsAssets:
            A resource-specific hateoas link.

        RestoreGcsProtectionGroupAsset:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'CreateGcpProtectionGroup': 'create-gcp-protection-group',
        'ListBackupGcpProtectionGroupGcsAssets': 'list-backup-gcp-protection-group-gcs-assets',
        'RestoreGcsProtectionGroupAsset': 'restore-gcs-protection-group-asset',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    CreateGcpProtectionGroup: hateoas_link_.HateoasLink | None = None
    ListBackupGcpProtectionGroupGcsAssets: hateoas_link_.HateoasLink | None = None
    RestoreGcsProtectionGroupAsset: hateoas_link_.HateoasLink | None = None

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

        val = dictionary.get('create-gcp-protection-group', None)
        val_create_gcp_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('list-backup-gcp-protection-group-gcs-assets', None)
        val_list_backup_gcp_protection_group_gcs_assets = hateoas_link_.HateoasLink.from_dictionary(
            val
        )

        val = dictionary.get('restore-gcs-protection-group-asset', None)
        val_restore_gcs_protection_group_asset = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_create_gcp_protection_group,
            val_list_backup_gcp_protection_group_gcs_assets,
            val_restore_gcs_protection_group_asset,
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
