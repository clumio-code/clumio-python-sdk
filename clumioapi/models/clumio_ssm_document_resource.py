#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    clumio_ssm_document_parameter_value as clumio_ssm_document_parameter_value_
from clumioapi.models import clumio_ssm_document_step as clumio_ssm_document_step_
import requests

T = TypeVar('T', bound='ClumioSsmDocumentResource')


@dataclasses.dataclass
class ClumioSsmDocumentResource:
    """Implementation of the 'ClumioSsmDocumentResource' model.

    Details for the ssm document attached to any resource

    Attributes:
        Description:
            "description" must contain the version being followed.

        Mainsteps:
            "mainsteps" refers to commands to be executed.

        Parameters:
            "parameters" refers to the parameters to be applied while executing commands.

        Schemaversion:
            "schemaversion" is an aws value for versioning.

    """

    Description: str | None = None
    Mainsteps: Sequence[clumio_ssm_document_step_.ClumioSsmDocumentStep] | None = None
    Parameters: (
        Mapping[str, clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue] | None
    ) = None
    Schemaversion: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None
        # Extract variables from the dictionary
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('mainSteps', None)

        val_mainSteps = []
        if val:
            for value in val:
                val_mainSteps.append(
                    clumio_ssm_document_step_.ClumioSsmDocumentStep.from_dictionary(value)
                )

        val = dictionary.get('parameters', None)
        val_parameters: Dict[
            str, clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue
        ] = {}
        for key, value in val.items():
            val_parameters[key] = (
                clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue.from_dictionary(
                    value
                )
            )

        val = dictionary.get('schemaVersion', None)
        val_schemaVersion = val

        # Return an object of this model
        return cls(
            val_description,
            val_mainSteps,
            val_parameters,
            val_schemaVersion,
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
