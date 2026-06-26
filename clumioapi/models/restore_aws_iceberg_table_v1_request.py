#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import iceberg_restore_source as iceberg_restore_source_
from clumioapi.models import iceberg_restore_target as iceberg_restore_target_
import requests

T = TypeVar('T', bound='RestoreAwsIcebergTableV1Request')


@dataclasses.dataclass
class RestoreAwsIcebergTableV1Request:
    """Implementation of the 'RestoreAwsIcebergTableV1Request' model.

    Attributes:
        Source:
            Icebergrestoresource
            the iceberg snapshot records to be restored.

        Target:
            Icebergrestoretarget
            the target destination for the restored iceberg table.

    """

    Source: iceberg_restore_source_.IcebergRestoreSource | None = None
    Target: iceberg_restore_target_.IcebergRestoreTarget | None = None

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
        val_source = iceberg_restore_source_.IcebergRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = iceberg_restore_target_.IcebergRestoreTarget.from_dictionary(val)

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
