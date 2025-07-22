#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EventRules')


class EventRules:
    """Implementation of the 'EventRules' model.

    Attributes:
        cloudtrail_rule_arn:
            Cloudtrail rule for the service if any.
        cloudwatch_rule_arn:
            Cloudwatch rule for the service if any.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'cloudtrail_rule_arn': 'cloudtrail_rule_arn',
        'cloudwatch_rule_arn': 'cloudwatch_rule_arn',
    }

    def __init__(self, cloudtrail_rule_arn: str, cloudwatch_rule_arn: str) -> None:
        """Constructor for the EventRules class."""

        # Initialize members of the class
        self.cloudtrail_rule_arn: str = cloudtrail_rule_arn
        self.cloudwatch_rule_arn: str = cloudwatch_rule_arn

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
        val = dictionary['cloudtrail_rule_arn']
        val_cloudtrail_rule_arn = val

        val = dictionary['cloudwatch_rule_arn']
        val_cloudwatch_rule_arn = val

        # Return an object of this model
        return cls(
            val_cloudtrail_rule_arn,  # type: ignore
            val_cloudwatch_rule_arn,  # type: ignore
        )
