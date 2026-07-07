#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcs_object as gcs_object_
from clumioapi.models import \
    gcs_protection_group_restore_target as gcs_protection_group_restore_target_
import requests

T = TypeVar('T', bound='RestoreGcsProtectionGroupObjectsV1Request')


@dataclasses.dataclass
class RestoreGcsProtectionGroupObjectsV1Request:
    """Implementation of the 'RestoreGcsProtectionGroupObjectsV1Request' model.

    Attributes:
        Source:
            Objects to restore. these are supposed to come from the preview result.

        Target:
            The destination where the gcs protection group will be restored.

    """

    Source: Sequence[gcs_object_.GCSObject] | None = None
    Target: gcs_protection_group_restore_target_.GCSProtectionGroupRestoreTarget | None = None

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
        val = dictionary.get('source', None)

        val_source = []
        if val:
            for value in val:
                val_source.append(gcs_object_.GCSObject.from_dictionary(value))

        val = dictionary.get('target', None)
        val_target = (
            gcs_protection_group_restore_target_.GCSProtectionGroupRestoreTarget.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_source,
            val_target,
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
