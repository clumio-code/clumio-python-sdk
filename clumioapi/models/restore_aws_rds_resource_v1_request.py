#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rds_resource_restore_source as rds_resource_restore_source_
from clumioapi.models import rds_resource_restore_target as rds_resource_restore_target_
import requests

T = TypeVar('T', bound='RestoreAwsRdsResourceV1Request')


@dataclasses.dataclass
class RestoreAwsRdsResourceV1Request:
    """Implementation of the 'RestoreAwsRdsResourceV1Request' model.

    Attributes:
        Source:
            The rds resource backup or snapshot to be restored.  only one of these fields should be set.

        Target:
            The configuration of the rds resource to be restored.

    """

    Source: rds_resource_restore_source_.RdsResourceRestoreSource | None = None
    Target: rds_resource_restore_target_.RdsResourceRestoreTarget | None = None

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
        val = dictionary.get('source', None)
        val_source = rds_resource_restore_source_.RdsResourceRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = rds_resource_restore_target_.RdsResourceRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
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
