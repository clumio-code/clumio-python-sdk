#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import file_restore_source as file_restore_source_
from clumioapi.models import file_restore_target as file_restore_target_
import requests

T = TypeVar('T', bound='RestoreFilesV1Request')


@dataclasses.dataclass
class RestoreFilesV1Request:
    """Implementation of the 'RestoreFilesV1Request' model.

    Attributes:
        Source:
            The files to be restored and from which backup they are to be restored from.

        Target:
            The destination information for the file level restore, representing the access
            option
            for the restored file. users can access the restored file by direct download or
            by
            email. the direct download (`direct_download`) option allows users to directly
            download
            the restored file from the clumio ui. the email (`email`) option allows users to
            access
            the restored file using a downloadable link they receive by email. if a target
            is not
            specified, then `target` defaults to `direct_download`.

    """

    Source: file_restore_source_.FileRestoreSource | None = None
    Target: file_restore_target_.FileRestoreTarget | None = None

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
        val_source = file_restore_source_.FileRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = file_restore_target_.FileRestoreTarget.from_dictionary(val)

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
