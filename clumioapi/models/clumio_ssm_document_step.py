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
        action: str,
        inputs: clumio_ssm_document_inputs_.ClumioSsmDocumentInputs,
        name: str,
        precondition: Mapping[str, Sequence[str]],
    ) -> None:
        """Constructor for the ClumioSsmDocumentStep class."""

        # Initialize members of the class
        self.action: str = action
        self.inputs: clumio_ssm_document_inputs_.ClumioSsmDocumentInputs = inputs
        self.name: str = name
        self.precondition: Mapping[str, Sequence[str]] = precondition

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
        val = dictionary['action']
        val_action = val

        val = dictionary['inputs']
        val_inputs = clumio_ssm_document_inputs_.ClumioSsmDocumentInputs.from_dictionary(val)

        val = dictionary['name']
        val_name = val

        val = dictionary['precondition']
        val_precondition = val

        # Return an object of this model
        return cls(
            val_action,  # type: ignore
            val_inputs,  # type: ignore
            val_name,  # type: ignore
            val_precondition,  # type: ignore
        )
