#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RulePriority')


class RulePriority:
    """Implementation of the 'RulePriority' model.

    A priority relative to other rules.

    Attributes:
        before_rule_id:
            The rule ID before which this rule should be inserted.
    """

    # Create a mapping from Model property names to API property names
    _names = {'before_rule_id': 'before_rule_id'}

    def __init__(self, before_rule_id: str = None) -> None:
        """Constructor for the RulePriority class."""

        # Initialize members of the class
        self.before_rule_id: str = before_rule_id

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
        before_rule_id = dictionary.get('before_rule_id')
        # Return an object of this model
        return cls(before_rule_id)
