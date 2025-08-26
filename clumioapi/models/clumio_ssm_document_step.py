#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import clumio_ssm_document_inputs as clumio_ssm_document_inputs_
import requests

T = TypeVar('T', bound='ClumioSsmDocumentStep')


@dataclasses.dataclass
class ClumioSsmDocumentStep:
    """Implementation of the 'ClumioSsmDocumentStep' model.

    Details for each step present inside an ssm document

    Attributes:
        Action:
            "action" refers to a unique action identified for this step.

        Inputs:
            .

        Name:
            "name" refers to name of that step.

        Precondition:
            "preconditon" is used for targeting a os or validating input parameters.

    """

    Action: str | None = None
    Inputs: clumio_ssm_document_inputs_.ClumioSsmDocumentInputs | None = None
    Name: str | None = None
    Precondition: Mapping[str, Sequence[str]] | None = None

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
        val = dictionary.get('action', None)
        val_action = val

        val = dictionary.get('inputs', None)
        val_inputs = clumio_ssm_document_inputs_.ClumioSsmDocumentInputs.from_dictionary(val)

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('precondition', None)
        val_precondition = val

        # Return an object of this model
        return cls(
            val_action,
            val_inputs,
            val_name,
            val_precondition,
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
