#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    clumio_ssm_document_parameter_value as clumio_ssm_document_parameter_value_
from clumioapi.models import clumio_ssm_document_step as clumio_ssm_document_step_

T = TypeVar('T', bound='ClumioSsmDocumentResource')


class ClumioSsmDocumentResource:
    """Implementation of the 'ClumioSsmDocumentResource' model.

    Details for the ssm document attached to any resource

    Attributes:
        description:
            "description" must contain the version being followed
        mainSteps:
            "mainSteps" refers to commands to be executed
        parameters:
            "paramters" refers to the paramters to be applied while executing commands
        schemaVersion:
            "schemaVersion" is an AWS value for versioning
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'mainSteps': 'mainSteps',
        'parameters': 'parameters',
        'schemaVersion': 'schemaVersion',
    }

    def __init__(
        self,
        description: str,
        mainSteps: Sequence[clumio_ssm_document_step_.ClumioSsmDocumentStep],
        parameters: Mapping[
            str, clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue
        ],
        schemaVersion: str,
    ) -> None:
        """Constructor for the ClumioSsmDocumentResource class."""

        # Initialize members of the class
        self.description: str = description
        self.mainSteps: Sequence[clumio_ssm_document_step_.ClumioSsmDocumentStep] = mainSteps
        self.parameters: Mapping[
            str, clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue
        ] = parameters
        self.schemaVersion: str = schemaVersion

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        # Extract variables from the dictionary
        val = dictionary['description']
        val_description = val

        val = dictionary['mainSteps']

        val_mainSteps = None
        if val:
            val_mainSteps = list()
            for value in val:
                val_mainSteps.append(
                    clumio_ssm_document_step_.ClumioSsmDocumentStep.from_dictionary(value)
                )

        val = dictionary['parameters']
        val_parameters: Dict[
            str, clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue
        ] = {}
        for key, value in val.items():
            val_parameters[key] = (
                clumio_ssm_document_parameter_value_.ClumioSsmDocumentParameterValue.from_dictionary(
                    value
                )
            )

        val = dictionary['schemaVersion']
        val_schemaVersion = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_mainSteps,  # type: ignore
            val_parameters,  # type: ignore
            val_schemaVersion,  # type: ignore
        )
