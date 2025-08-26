#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import data_access_object as data_access_object_
import requests

T = TypeVar('T', bound='RestoredFileInfo')


@dataclasses.dataclass
class RestoredFileInfo:
    """Implementation of the 'RestoredFileInfo' model.

        Attributes:
            AccessMethods:
                The access options for this restored file. users can access the restored file in
    one of two ways, depending on the option selected by the user who generated the
    restored file. the direct download (`direct_download`) option allows users to
    directly download the restored file from the clumio ui. the email (`email`) option
    allows users to access the restored file using a downloadable link they receive by
    email.

            BackupId:
                The clumio-assigned id of the backup associated with this restored file.

            BackupTimestamp:
                The timestamp of the when the backup associated with this file started.
    represented in rfc-3339 format.

            ExpirationTimestamp:
                The timestamp of when the restored file will expire. represented in rfc-3339
    format.

            Id:
                The clumio-assigned id of the restored file.

            Name:
                The clumio-assigned name of the restored file.

            Size:
                The size of the restored file. measured in bytes (b).

            TaskId:
                The clumio-assigned id of the task which generated the restored file.

    """

    AccessMethods: Sequence[data_access_object_.DataAccessObject] | None = None
    BackupId: str | None = None
    BackupTimestamp: str | None = None
    ExpirationTimestamp: str | None = None
    Id: str | None = None
    Name: str | None = None
    Size: int | None = None
    TaskId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('access_methods', None)

        val_access_methods = []
        if val:
            for value in val:
                val_access_methods.append(
                    data_access_object_.DataAccessObject.from_dictionary(value)
                )

        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('backup_timestamp', None)
        val_backup_timestamp = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_access_methods,
            val_backup_id,
            val_backup_timestamp,
            val_expiration_timestamp,
            val_id,
            val_name,
            val_size,
            val_task_id,
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
