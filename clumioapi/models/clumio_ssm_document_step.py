#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import clumio_ssm_document_inputs

T = TypeVar('T', bound='ClumioSsmDocumentStep')


class ClumioSsmDocumentStep:
    """Implementation of the 'ClumioSsmDocumentStep' model.

    Details for each step present inside an ssm document

    Attributes:
        action:
            "action" refers to a unique action identified for this step
        inputs:

        name:
            "name" refers to name of that step
        precondition:
            "preconditon" is used for targeting a OS or validating input parameters
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'action': 'action',
        'inputs': 'inputs',
        'name': 'name',
        'precondition': 'precondition',
    }

    def __init__(
        self,
        action: str = None,
        inputs: clumio_ssm_document_inputs.ClumioSsmDocumentInputs = None,
        name: str = None,
        precondition: Mapping[str, Sequence[str]] = None,
    ) -> None:
        """Constructor for the ClumioSsmDocumentStep class."""

        # Initialize members of the class
        self.action: str = action
        self.inputs: clumio_ssm_document_inputs.ClumioSsmDocumentInputs = inputs
        self.name: str = name
        self.precondition: Mapping[str, Sequence[str]] = precondition

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
        action = dictionary.get('action')
        key = 'inputs'
        inputs = (
            clumio_ssm_document_inputs.ClumioSsmDocumentInputs.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        name = dictionary.get('name')
        precondition = dictionary.get('precondition')
        # Return an object of this model
        return cls(action, inputs, name, precondition)
