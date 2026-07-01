#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    gcs_protection_group_restore_source as gcs_protection_group_restore_source_
from clumioapi.models import \
    gcs_protection_group_restore_target as gcs_protection_group_restore_target_
import requests

T = TypeVar('T', bound='RestoreGcsProtectionGroupV1Request')


@dataclasses.dataclass
class RestoreGcsProtectionGroupV1Request:
    """Implementation of the 'RestoreGcsProtectionGroupV1Request' model.

    Attributes:
        Source:
            The parameters for initiating a gcs protection group restore from a backup.

        Target:
            The destination where the gcs protection group will be restored.

    """

    Source: gcs_protection_group_restore_source_.GCSProtectionGroupRestoreSource | None = None
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
        val_source = (
            gcs_protection_group_restore_source_.GCSProtectionGroupRestoreSource.from_dictionary(
                val
            )
        )

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
