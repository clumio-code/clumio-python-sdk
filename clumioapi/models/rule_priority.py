#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'before_rule_id': 'before_rule_id'}

    def __init__(self, before_rule_id: str | None = None) -> None:
        """Constructor for the RulePriority class."""

        # Initialize members of the class
        self.before_rule_id: str | None = before_rule_id

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
        val = dictionary.get('before_rule_id', None)
        val_before_rule_id = val

        # Return an object of this model
        return cls(
            val_before_rule_id,
        )
