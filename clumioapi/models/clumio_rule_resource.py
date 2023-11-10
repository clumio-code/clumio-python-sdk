#
# Copyright 2023. Clumio, Inc.
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
    _names = {
        'description': 'description',
        'event_pattern': 'event_pattern',
        'steps': 'steps',
        'targets': 'targets',
    }

    def __init__(
        self,
        description: str = None,
        event_pattern: object = None,
        steps: str = None,
        targets: Sequence[object] = None,
    ) -> None:
        """Constructor for the ClumioRuleResource class."""

        # Initialize members of the class
        self.description: str = description
        self.event_pattern: object = event_pattern
        self.steps: str = steps
        self.targets: Sequence[object] = targets

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
        event_pattern = dictionary.get('event_pattern')
        steps = dictionary.get('steps')
        targets = dictionary.get('targets')
        # Return an object of this model
        return cls(description, event_pattern, steps, targets)
