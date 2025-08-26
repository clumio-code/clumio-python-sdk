#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ClumioRuleResource')


@dataclasses.dataclass
class ClumioRuleResource:
    """Implementation of the 'ClumioRuleResource' model.

        Attributes:
            Description:
                "description" is optional.

            EventPattern:
                "event_pattern" has stringified json blob. the user has to jsonify it and then paste
    the jsonified blob in aws console while creating the rule.

            Steps:
                "steps" refers to commands to be executed.

            Targets:
                "targets" is a string that essentially stores the target for the rule. it generally is an arn.

    """

    Description: str | None = None
    EventPattern: object | None = None
    Steps: str | None = None
    Targets: Sequence[object] | None = None

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('event_pattern', None)
        val_event_pattern = val

        val = dictionary.get('steps', None)
        val_steps = val

        val = dictionary.get('targets', None)
        val_targets = val

        # Return an object of this model
        return cls(
            val_description,
            val_event_pattern,
            val_steps,
            val_targets,
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
