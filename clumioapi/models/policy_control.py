#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import time_unit_param as time_unit_param_
import requests

T = TypeVar('T', bound='PolicyControl')


@dataclasses.dataclass
class PolicyControl:
    """Implementation of the 'PolicyControl' model.

        The control for policy.

        Attributes:
            MinimumRetentionDuration:
    The time unit used in control definition.

            MinimumRpoFrequency:
    The time unit used in control definition.

    """

    MinimumRetentionDuration: time_unit_param_.TimeUnitParam | None = None
    MinimumRpoFrequency: time_unit_param_.TimeUnitParam | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val = dictionary.get('minimum_retention_duration', None)
        val_minimum_retention_duration = time_unit_param_.TimeUnitParam.from_dictionary(val)

        val = dictionary.get('minimum_rpo_frequency', None)
        val_minimum_rpo_frequency = time_unit_param_.TimeUnitParam.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_minimum_retention_duration,
            val_minimum_rpo_frequency,
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
