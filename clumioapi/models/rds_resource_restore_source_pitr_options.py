#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RdsResourceRestoreSourcePitrOptions')


@dataclasses.dataclass
class RdsResourceRestoreSourcePitrOptions:
    """Implementation of the 'RdsResourceRestoreSourcePitrOptions' model.

        The parameters for initiating an RDS restore from a snapshot.

        Attributes:
            ResourceId:
                The clumio-assigned id of the rds resource to be restored.
    use the [get /datasources/aws/rds-resources](#operation/list-aws-rds-resources)
    endpoint to fetch valid values.

            Timestamp:
                A point in time to be restored in rfc-3339 format.

    """

    ResourceId: str | None = None
    Timestamp: str | None = None

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
        val = dictionary.get('resource_id', None)
        val_resource_id = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        # Return an object of this model
        return cls(
            val_resource_id,
            val_timestamp,
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
