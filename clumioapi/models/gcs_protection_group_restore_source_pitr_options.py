#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GCSProtectionGroupRestoreSourcePitrOptions')


@dataclasses.dataclass
class GCSProtectionGroupRestoreSourcePitrOptions:
    """Implementation of the 'GCSProtectionGroupRestoreSourcePitrOptions' model.

    The parameters for initiating a GCS protection group restore from a point in
    time.

    Attributes:
        GcsProtectionGroupId:
            Clumio-assigned id of gcs protection group, representing the
            protection group to restore from.

        RestoreEndTimestamp:
            The end timestamp of the period within which objects are to be restored, in
            rfc-3339
            format. clumio searches for objects modified before the given time. if
            `restore_end_timestamp`
            is empty, clumio searches for objects modified up to the current time of the
            restore request.

        RestoreStartTimestamp:
            The start timestamp of the period within which objects are to be restored, in
            rfc-3339
            format. clumio searches for objects modified since the given time. if
            `restore_start_timestamp`
            is empty, clumio searches for objects from the beginning of the first backup.

    """

    GcsProtectionGroupId: str | None = None
    RestoreEndTimestamp: str | None = None
    RestoreStartTimestamp: str | None = None

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
        val = dictionary.get('gcs_protection_group_id', None)
        val_gcs_protection_group_id = val

        val = dictionary.get('restore_end_timestamp', None)
        val_restore_end_timestamp = val

        val = dictionary.get('restore_start_timestamp', None)
        val_restore_start_timestamp = val

        # Return an object of this model
        return cls(
            val_gcs_protection_group_id,
            val_restore_end_timestamp,
            val_restore_start_timestamp,
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
