#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='IndividualAlertDetails')


@dataclasses.dataclass
class IndividualAlertDetails:
    """Implementation of the 'IndividualAlertDetails' model.

        Additional information about the alert.

        Attributes:
            Cause:
                A brief description of the condition that caused the alert. examples include "size limit exceeded" and "insufficient cloud connector capacity".

            Description:
                A detailed description of the alert, including the reason why the alert occurred
    and the steps you must take to resolve the issue.

            Type:
                The general alert category. examples include "policy violated" and "restore failed".

            Variables:
                Data specific to the alert generated. if the alert has no variables, then this
    field has a value of `null`.

    """

    Cause: str | None = None
    Description: str | None = None
    Type: str | None = None
    Variables: Mapping[str, str] | None = None

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
        val = dictionary.get('cause', None)
        val_cause = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('variables', None)
        val_variables = val

        # Return an object of this model
        return cls(
            val_cause,
            val_description,
            val_type,
            val_variables,
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
