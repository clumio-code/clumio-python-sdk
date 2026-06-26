#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_first_link as hateoas_first_link_
from clumioapi.models import hateoas_last_link as hateoas_last_link_
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_next_link as hateoas_next_link_
from clumioapi.models import hateoas_prev_link as hateoas_prev_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='BucketListLinks')


@dataclasses.dataclass
class BucketListLinks:
    """Implementation of the 'BucketListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        First:
            The hateoas link to the first page of results.

        Last:
            The hateoas link to the last page of results.

        Next:
            The hateoas link to the next page of results.

        Prev:
            The hateoas link to the previous page of results.

        Self:
            The hateoas link to this resource.

        ListBackupProtectionGroupBuckets:
            A resource-specific hateoas link.

        RestoreProtectionGroupS3Asset:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'First': '_first',
        'Last': '_last',
        'Next': '_next',
        'Prev': '_prev',
        'Self': '_self',
        'ListBackupProtectionGroupBuckets': 'list-backup-protection-group-buckets',
        'RestoreProtectionGroupS3Asset': 'restore-protection-group-s3-asset',
    }

    First: hateoas_first_link_.HateoasFirstLink | None = None
    Last: hateoas_last_link_.HateoasLastLink | None = None
    Next: hateoas_next_link_.HateoasNextLink | None = None
    Prev: hateoas_prev_link_.HateoasPrevLink | None = None
    Self: hateoas_self_link_.HateoasSelfLink | None = None
    ListBackupProtectionGroupBuckets: hateoas_link_.HateoasLink | None = None
    RestoreProtectionGroupS3Asset: hateoas_link_.HateoasLink | None = None

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
        val = dictionary.get('_first', None)
        val_first = hateoas_first_link_.HateoasFirstLink.from_dictionary(val)

        val = dictionary.get('_last', None)
        val_last = hateoas_last_link_.HateoasLastLink.from_dictionary(val)

        val = dictionary.get('_next', None)
        val_next = hateoas_next_link_.HateoasNextLink.from_dictionary(val)

        val = dictionary.get('_prev', None)
        val_prev = hateoas_prev_link_.HateoasPrevLink.from_dictionary(val)

        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('list-backup-protection-group-buckets', None)
        val_list_backup_protection_group_buckets = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('restore-protection-group-s3-asset', None)
        val_restore_protection_group_s3_asset = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_first,
            val_last,
            val_next,
            val_prev,
            val_self,
            val_list_backup_protection_group_buckets,
            val_restore_protection_group_s3_asset,
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
