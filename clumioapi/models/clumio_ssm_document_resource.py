#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import clumio_ssm_document_parameter_value
from clumioapi.models import clumio_ssm_document_step

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
    _names = {
        'description': 'description',
        'mainSteps': 'mainSteps',
        'parameters': 'parameters',
        'schemaVersion': 'schemaVersion',
    }

    def __init__(
        self,
        description: str = None,
        mainSteps: Sequence[clumio_ssm_document_step.ClumioSsmDocumentStep] = None,
        parameters: Mapping[
            str, clumio_ssm_document_parameter_value.ClumioSsmDocumentParameterValue
        ] = None,
        schemaVersion: str = None,
    ) -> None:
        """Constructor for the ClumioSsmDocumentResource class."""

        # Initialize members of the class
        self.description: str = description
        self.mainSteps: Sequence[clumio_ssm_document_step.ClumioSsmDocumentStep] = mainSteps
        self.parameters: Mapping[
            str, clumio_ssm_document_parameter_value.ClumioSsmDocumentParameterValue
        ] = parameters
        self.schemaVersion: str = schemaVersion

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        description = dictionary.get('description')
        mainSteps = None
        if dictionary.get('mainSteps'):
            mainSteps = list()
            for value in dictionary.get('mainSteps'):
                mainSteps.append(
                    clumio_ssm_document_step.ClumioSsmDocumentStep.from_dictionary(value)
                )

        parameters: Dict[
            str, clumio_ssm_document_parameter_value.ClumioSsmDocumentParameterValue
        ] = {}
        for key, value in dictionary.get('parameters').items():
            parameters[key] = (
                clumio_ssm_document_parameter_value.ClumioSsmDocumentParameterValue.from_dictionary(
                    value
                )
                if value
                else None
            )

        schemaVersion = dictionary.get('schemaVersion')
        # Return an object of this model
        return cls(description, mainSteps, parameters, schemaVersion)
