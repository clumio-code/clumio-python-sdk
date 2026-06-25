#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_bucket_rule_model as gcp_bucket_rule_model_
import requests

T = TypeVar('T', bound='UpdateGcpProtectionGroupV1Request')

StorageClassesValues = [
    'STANDARD',
    'NEARLINE',
    'COLDLINE',
    'ARCHIVE',
]


@dataclasses.dataclass
class UpdateGcpProtectionGroupV1Request:
    """Implementation of the 'UpdateGcpProtectionGroupV1Request' model.

    The protection group update data

    Attributes:
        AddBucketUuids:
            A list of bucket uuids to add to this protection group.

        BucketRule

        ClearBucketRule:
            Set to true to remove an existing bucket rule from this protection group.
            mutually exclusive with bucket_rule.

        ExcludePrefixes:
            A list of prefixes to exclude from the backup. if multiple prefixes are
            specified,
            then any object whose path matches one of the prefixes will be excluded from the
            backup.
            part of the put-style filter group (see model docs); a non-nil empty list
            clears existing excludes, while omitting the field leaves the filter
            unchanged unless another group field is present.

        IncludePrefixes:
            A list of prefixes to include in the backup. if multiple prefixes are specified,
            then any object whose path matches one of the prefixes will be included in the
            backup.
            part of the put-style filter group (see model docs); a non-nil empty list
            clears existing includes, while omitting the field leaves the filter
            unchanged unless another group field is present.

        LatestVersionOnly:
            Whether to back up only the latest object version. part of the
            put-style filter group (see model docs); when any group field is present,
            an absent latest_version_only defaults to true.

        Name:
            The user-assigned name of the protection group.

        RemoveBucketUuids:
            A list of bucket uuids to remove from this protection group.

        StorageClasses:
            Storage classes to include in the backup. part of the put-style filter
            group (see model docs); an empty array is rejected. omitting the field
            leaves the filter unchanged unless another group field is present, in which
            case the storage-class filter resets to all storage classes.

        UpdatedAfter:
            Only back up objects created after this timestamp (rfc-3339). part of the
            put-style filter group (see model docs); an empty string clears the
            creation-time filter, while omitting the field leaves the filter unchanged
            unless another group field is present.

    """

    AddBucketUuids: Sequence[str] | None = None
    BucketRule: gcp_bucket_rule_model_.GCPBucketRuleModel | None = None
    ClearBucketRule: bool | None = None
    ExcludePrefixes: Sequence[str] | None = None
    IncludePrefixes: Sequence[str] | None = None
    LatestVersionOnly: bool | None = None
    Name: str | None = None
    RemoveBucketUuids: Sequence[str] | None = None

    StorageClasses: Sequence[str] | None = None
    UpdatedAfter: str | None = None

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
        val = dictionary.get('add_bucket_uuids', None)
        val_add_bucket_uuids = val

        val = dictionary.get('bucket_rule', None)
        val_bucket_rule = gcp_bucket_rule_model_.GCPBucketRuleModel.from_dictionary(val)

        val = dictionary.get('clear_bucket_rule', None)
        val_clear_bucket_rule = val

        val = dictionary.get('exclude_prefixes', None)
        val_exclude_prefixes = val

        val = dictionary.get('include_prefixes', None)
        val_include_prefixes = val

        val = dictionary.get('latest_version_only', None)
        val_latest_version_only = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('remove_bucket_uuids', None)
        val_remove_bucket_uuids = val

        val = dictionary.get('storage_classes', None)
        val_storage_classes = val

        val = dictionary.get('updated_after', None)
        val_updated_after = val

        # Return an object of this model
        return cls(
            val_add_bucket_uuids,
            val_bucket_rule,
            val_clear_bucket_rule,
            val_exclude_prefixes,
            val_include_prefixes,
            val_latest_version_only,
            val_name,
            val_remove_bucket_uuids,
            val_storage_classes,
            val_updated_after,
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
