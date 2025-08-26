#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import compliance_controls as compliance_controls_
from clumioapi.models import compliance_filters as compliance_filters_
import requests

T = TypeVar('T', bound='Parameter')


@dataclasses.dataclass
class Parameter:
    """Implementation of the 'Parameter' model.

    Filter and control parameters of compliance report.

    Attributes:
        Controls:
            The set of controls supported in compliance report.

        Filters:
            The set of filters supported in compliance report.

    """

    Controls: compliance_controls_.ComplianceControls | None = None
    Filters: compliance_filters_.ComplianceFilters | None = None

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
        val = dictionary.get('controls', None)
        val_controls = compliance_controls_.ComplianceControls.from_dictionary(val)

        val = dictionary.get('filters', None)
        val_filters = compliance_filters_.ComplianceFilters.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_controls,
            val_filters,
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
