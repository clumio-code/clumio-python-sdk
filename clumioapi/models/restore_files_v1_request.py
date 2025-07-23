#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_restore_source as file_restore_source_
from clumioapi.models import file_restore_target as file_restore_target_

T = TypeVar('T', bound='RestoreFilesV1Request')


class RestoreFilesV1Request:
    """Implementation of the 'RestoreFilesV1Request' model.

    Attributes:
        source:
            The files to be restored and from which backup they are to be restored from.
        target:
            The destination information for the file level restore, representing the access
            option
            for the restored file. Users can access the restored file by direct download or
            by
            email. The direct download (`direct_download`) option allows users to directly
            download
            the restored file from the Clumio UI. The email (`email`) option allows users to
            access
            the restored file using a downloadable link they receive by email. If a target
            is not
            specified, then `target` defaults to `direct_download`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: file_restore_source_.FileRestoreSource | None = None,
        target: file_restore_target_.FileRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreFilesV1Request class."""

        # Initialize members of the class
        self.source: file_restore_source_.FileRestoreSource | None = source
        self.target: file_restore_target_.FileRestoreTarget | None = target

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        dictionary = dictionary or {}
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
