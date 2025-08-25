#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

import requests

T = TypeVar('T', bound='CreateComplianceReportRunV1Request')


@dataclasses.dataclass
class CreateComplianceReportRunV1Request:
    """Implementation of the 'CreateComplianceReportRunV1Request' model.

        Attributes:
            Name:
                Name of the new compliance report run that will be created.
    if not given, default uses `{configuration id} - {mm/dd/yyyy(created time)}`.

    """

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
        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
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
