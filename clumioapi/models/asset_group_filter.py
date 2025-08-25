#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

import requests

T = TypeVar('T', bound='AssetGroupFilter')


@dataclasses.dataclass
class AssetGroupFilter:
    """Implementation of the 'AssetGroupFilter' model.

        The asset groups to be filtered.

        Attributes:
            Id:
                The id of asset group.

            Region:
                The region of asset group. for example, `us-west-2`.
    this is supported for aws asset groups only.

            Type:
                The type of asset group.

    """

    Id: str | None = None
    Region: str | None = None
    Type: str | None = None

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
        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_id,
            val_region,
            val_type,
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
