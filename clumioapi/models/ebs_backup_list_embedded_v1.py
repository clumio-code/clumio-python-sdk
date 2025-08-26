#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ebs_backup_v1 as ebs_backup_v1_
import requests

T = TypeVar('T', bound='EBSBackupListEmbeddedV1')


@dataclasses.dataclass
class EBSBackupListEmbeddedV1:
    """Implementation of the 'EBSBackupListEmbeddedV1' model.

    Embedded responses related to the resource.

    Attributes:
        Items:
            A collection of requested items.

    """

    Items: Sequence[ebs_backup_v1_.EBSBackupV1] | None = None

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
        val = dictionary.get('items', None)

        val_items = []
        if val:
            for value in val:
                val_items.append(ebs_backup_v1_.EBSBackupV1.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_items,
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
