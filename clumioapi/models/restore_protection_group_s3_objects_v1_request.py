#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import object as object_
from clumioapi.models import protection_group_restore_target as protection_group_restore_target_
import requests

T = TypeVar('T', bound='RestoreProtectionGroupS3ObjectsV1Request')


@dataclasses.dataclass
class RestoreProtectionGroupS3ObjectsV1Request:
    """Implementation of the 'RestoreProtectionGroupS3ObjectsV1Request' model.

    Attributes:
        Source:
            Objects to restore. these objects must
            belong to a single bucket.

        Target:
            The destination where the protection group will be restored.

    """

    Source: Sequence[object_.Object] | None = None
    Target: protection_group_restore_target_.ProtectionGroupRestoreTarget | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
                val_source.append(object_.Object.from_dictionary(value))

        val = dictionary.get('target', None)
        val_target = protection_group_restore_target_.ProtectionGroupRestoreTarget.from_dictionary(
            val
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
