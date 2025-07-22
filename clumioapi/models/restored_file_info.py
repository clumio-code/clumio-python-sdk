#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import data_access_object as data_access_object_

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
    _names: dict[str, str] = {
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
        access_methods: Sequence[data_access_object_.DataAccessObject],
        backup_id: str,
        backup_timestamp: str,
        expiration_timestamp: str,
        p_id: str,
        name: str,
        size: int,
        task_id: str,
    ) -> None:
        """Constructor for the RestoredFileInfo class."""

        # Initialize members of the class
        self.access_methods: Sequence[data_access_object_.DataAccessObject] = access_methods
        self.backup_id: str = backup_id
        self.backup_timestamp: str = backup_timestamp
        self.expiration_timestamp: str = expiration_timestamp
        self.p_id: str = p_id
        self.name: str = name
        self.size: int = size
        self.task_id: str = task_id

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

        # Extract variables from the dictionary
        val = dictionary['access_methods']

        val_access_methods = None
        if val:
            val_access_methods = list()
            for value in val:
                val_access_methods.append(
                    data_access_object_.DataAccessObject.from_dictionary(value)
                )

        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['backup_timestamp']
        val_backup_timestamp = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['size']
        val_size = val

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_access_methods,  # type: ignore
            val_backup_id,  # type: ignore
            val_backup_timestamp,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_size,  # type: ignore
            val_task_id,  # type: ignore
        )
