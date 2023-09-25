#
# Copyright 2021. Clumio, Inc.
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
    _names = {
        'cloudtrail_rule_arn': 'cloudtrail_rule_arn',
        'cloudwatch_rule_arn': 'cloudwatch_rule_arn',
    }

    def __init__(self, cloudtrail_rule_arn: str = None, cloudwatch_rule_arn: str = None) -> None:
        """Constructor for the EventRules class."""

        # Initialize members of the class
        self.cloudtrail_rule_arn: str = cloudtrail_rule_arn
        self.cloudwatch_rule_arn: str = cloudwatch_rule_arn

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
        cloudtrail_rule_arn = dictionary.get('cloudtrail_rule_arn')
        cloudwatch_rule_arn = dictionary.get('cloudwatch_rule_arn')
        # Return an object of this model
        return cls(cloudtrail_rule_arn, cloudwatch_rule_arn)
