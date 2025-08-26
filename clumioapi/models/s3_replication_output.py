#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replication_configuration as s3_replication_configuration_
import requests

T = TypeVar('T', bound='S3ReplicationOutput')


@dataclasses.dataclass
class S3ReplicationOutput:
    """Implementation of the 'S3ReplicationOutput' model.

        The AWS replication output of the bucket.

        Attributes:
            ReplicationConfiguration:
                A container for replication rules with a maximum size
    of 2mb and a maximum of 1,000 rules.

    """

    ReplicationConfiguration: s3_replication_configuration_.S3ReplicationConfiguration | None = None

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
        val = dictionary.get('replication_configuration', None)
        val_replication_configuration = (
            s3_replication_configuration_.S3ReplicationConfiguration.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_replication_configuration,
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
