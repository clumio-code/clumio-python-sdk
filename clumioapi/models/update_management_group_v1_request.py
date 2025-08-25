#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

import requests

T = TypeVar('T', bound='UpdateManagementGroupV1Request')


@dataclasses.dataclass
class UpdateManagementGroupV1Request:
    """Implementation of the 'UpdateManagementGroupV1Request' model.

    Attributes:
        BackupAcrossSubgroups:
            Determines whether backups are allowed to occur across different subgroups or cloud connectors.

        Name:
            The name of the management group.

    """

    BackupAcrossSubgroups: bool | None = None
    Name: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(self)

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
        val = dictionary.get('backup_across_subgroups', None)
        val_backup_across_subgroups = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_backup_across_subgroups,
            val_name,
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
