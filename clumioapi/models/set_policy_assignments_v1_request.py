#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import assignment_input_model as assignment_input_model_
import requests

T = TypeVar('T', bound='SetPolicyAssignmentsV1Request')


@dataclasses.dataclass
class SetPolicyAssignmentsV1Request:
    """Implementation of the 'SetPolicyAssignmentsV1Request' model.

    Attributes:
        Items:
            Items are inputs that represent the list of assets to which a policy is to be
            assigned or
            unassigned.

    """

    Items: Sequence[assignment_input_model_.AssignmentInputModel] | None = None

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
        val = dictionary.get('items', None)

        val_items = []
        if val:
            for value in val:
                val_items.append(
                    assignment_input_model_.AssignmentInputModel.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_items,
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
