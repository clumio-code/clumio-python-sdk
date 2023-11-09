#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import data_access_object

T = TypeVar('T', bound='RestoredFileInfo')


class RestoredFileInfo:
    """Implementation of the 'RestoredFileInfo' model.

    Attributes:
        access_methods:
            The access options for this restored file. Users can access the restored file in
            one of two ways, depending on the option selected by the user who generated the
            restored file. The direct download (`direct_download`) option allows users to
            directly download the restored file from the Clumio UI. The email (`email`)
            option
            allows users to access the restored file using a downloadable link they receive
            by
            email.
        backup_id:
            The Clumio-assigned ID of the backup associated with this restored file.
        backup_timestamp:
            The timestamp of the when the backup associated with this file started.
            Represented in RFC-3339 format.
        expiration_timestamp:
            The timestamp of when the restored file will expire. Represented in RFC-3339
            format.
        p_id:
            The Clumio-assigned ID of the restored file.
        name:
            The Clumio-assigned name of the restored file.
        size:
            The size of the restored file. Measured in bytes (B).
        task_id:
            The Clumio-assigned ID of the task which generated the restored file.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'access_methods': 'access_methods',
        'backup_id': 'backup_id',
        'backup_timestamp': 'backup_timestamp',
        'expiration_timestamp': 'expiration_timestamp',
        'p_id': 'id',
        'name': 'name',
        'size': 'size',
        'task_id': 'task_id',
    }

    def __init__(
        self,
        access_methods: Sequence[data_access_object.DataAccessObject] = None,
        backup_id: str = None,
        backup_timestamp: str = None,
        expiration_timestamp: str = None,
        p_id: str = None,
        name: str = None,
        size: int = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the RestoredFileInfo class."""

        # Initialize members of the class
        self.access_methods: Sequence[data_access_object.DataAccessObject] = access_methods
        self.backup_id: str = backup_id
        self.backup_timestamp: str = backup_timestamp
        self.expiration_timestamp: str = expiration_timestamp
        self.p_id: str = p_id
        self.name: str = name
        self.size: int = size
        self.task_id: str = task_id

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
        access_methods = None
        if dictionary.get('access_methods'):
            access_methods = list()
            for value in dictionary.get('access_methods'):
                access_methods.append(data_access_object.DataAccessObject.from_dictionary(value))

        backup_id = dictionary.get('backup_id')
        backup_timestamp = dictionary.get('backup_timestamp')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        size = dictionary.get('size')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(
            access_methods,
            backup_id,
            backup_timestamp,
            expiration_timestamp,
            p_id,
            name,
            size,
            task_id,
        )
