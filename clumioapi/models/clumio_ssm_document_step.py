#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import clumio_ssm_document_inputs as clumio_ssm_document_inputs_

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
    _names: dict[str, str] = {
        'action': 'action',
        'inputs': 'inputs',
        'name': 'name',
        'precondition': 'precondition',
    }

    def __init__(
        self,
        action: str | None = None,
        inputs: clumio_ssm_document_inputs_.ClumioSsmDocumentInputs | None = None,
        name: str | None = None,
        precondition: Mapping[str, Sequence[str]] | None = None,
    ) -> None:
        """Constructor for the ClumioSsmDocumentStep class."""

        # Initialize members of the class
        self.action: str | None = action
        self.inputs: clumio_ssm_document_inputs_.ClumioSsmDocumentInputs | None = inputs
        self.name: str | None = name
        self.precondition: Mapping[str, Sequence[str]] | None = precondition

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
