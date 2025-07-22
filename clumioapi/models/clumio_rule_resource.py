#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ClumioRuleResource')


class ClumioRuleResource:
    """Implementation of the 'ClumioRuleResource' model.

    Attributes:
        description:
            "description" is optional
        event_pattern:
            "event_pattern" has stringified JSON blob. The user has to JSONify it and then
            paste
            the JSONified blob in aws console while creating the rule.
        steps:
            "steps" refers to commands to be executed
        targets:
            "targets" is a string that essentially stores the target for the rule. It
            generally is an ARN.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'event_pattern': 'event_pattern',
        'steps': 'steps',
        'targets': 'targets',
    }

    def __init__(
        self, description: str, event_pattern: object, steps: str, targets: Sequence[object]
    ) -> None:
        """Constructor for the ClumioRuleResource class."""

        # Initialize members of the class
        self.description: str = description
        self.event_pattern: object = event_pattern
        self.steps: str = steps
        self.targets: Sequence[object] = targets

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

        val = dictionary['event_pattern']
        val_event_pattern = val

        val = dictionary['steps']
        val_steps = val

        val = dictionary['targets']
        val_targets = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_event_pattern,  # type: ignore
            val_steps,  # type: ignore
            val_targets,  # type: ignore
        )
