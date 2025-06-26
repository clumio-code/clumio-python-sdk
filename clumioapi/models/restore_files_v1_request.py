#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_restore_source
from clumioapi.models import file_restore_target

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
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: file_restore_source.FileRestoreSource = None,
        target: file_restore_target.FileRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreFilesV1Request class."""

        # Initialize members of the class
        self.source: file_restore_source.FileRestoreSource = source
        self.target: file_restore_target.FileRestoreTarget = target

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        key = 'source'
        source = (
            file_restore_source.FileRestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            file_restore_target.FileRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
