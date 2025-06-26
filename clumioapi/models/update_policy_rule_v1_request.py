#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rule_action
from clumioapi.models import rule_priority

T = TypeVar('T', bound='UpdatePolicyRuleV1Request')


class UpdatePolicyRuleV1Request:
    """Implementation of the 'UpdatePolicyRuleV1Request' model.

    Attributes:
        action:
            An action to be applied subject to the rule criteria.
        condition:
            The following table describes the possible conditions for a rule.

            +-----------------------+---------------------------+--------------------------+
            |         Field         |      Rule Condition       |       Description        |
            +=======================+===========================+==========================+
            | aws_account_native_id | $eq, $in                  | Denotes the AWS account  |
            |                       |                           | to conditionalize on     |
            |                       |                           |                          |
            |                       |                           | {"aws_account_native_id" |
            |                       |                           | :{"$eq":"111111111111"}} |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_account_native_id" |
            |                       |                           | :{"$in":["111111111111", |
            |                       |                           | "222222222222"]}}        |
            |                       |                           |                          |
            |                       |                           |                          |
            +-----------------------+---------------------------+--------------------------+
            | aws_region            | $eq, $in                  | Denotes the AWS region   |
            |                       |                           | to conditionalize on     |
            |                       |                           |                          |
            |                       |                           | {"aws_region":{"$eq":"us |
            |                       |                           | -west-2"}}               |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_region":{"$in":["u |
            |                       |                           | s-west-2", "us-          |
            |                       |                           | east-1"]}}               |
            |                       |                           |                          |
            |                       |                           |                          |
            +-----------------------+---------------------------+--------------------------+
            | aws_tag               | $eq, $in, $all,           | Denotes the AWS tag(s)   |
            |                       | $contains, $not_eq,       | to conditionalize on.    |
            |                       | $not_in, $not_all,        | Max 100 tags allowed in  |
            |                       | $not_contains             | each rule                |
            |                       |                           | and tag key can be upto  |
            |                       |                           | 128 characters and value |
            |                       |                           | can be upto 256          |
            |                       |                           | characters long.         |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$eq":{"key" |
            |                       |                           | :"Environment",          |
            |                       |                           | "value":"Prod"}}}        |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$in":[{"key |
            |                       |                           | ":"Environment",         |
            |                       |                           | "value":"Prod"},         |
            |                       |                           | {"key":"Hello",          |
            |                       |                           | "value":"World"}]}}      |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$all":[{"ke |
            |                       |                           | y":"Environment",        |
            |                       |                           | "value":"Prod"},         |
            |                       |                           | {"key":"Hello",          |
            |                       |                           | "value":"World"}]}}      |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$contains": |
            |                       |                           | {"key":"Environment",    |
            |                       |                           | "value":"Prod"}}}        |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$not_eq":{" |
            |                       |                           | key":"Environment",      |
            |                       |                           | "value":"Prod"}}}        |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$not_in":[{ |
            |                       |                           | "key":"Environment",     |
            |                       |                           | "value":"Prod"},         |
            |                       |                           | {"key":"Hello",          |
            |                       |                           | "value":"World"}]}}      |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$not_all":[ |
            |                       |                           | {"key":"Environment",    |
            |                       |                           | "value":"Prod"},         |
            |                       |                           | {"key":"Hello",          |
            |                       |                           | "value":"World"}]}}      |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"aws_tag":{"$not_contai |
            |                       |                           | ns":{"key":"Environment" |
            |                       |                           | , "value":"Prod"}}}      |
            |                       |                           |                          |
            |                       |                           |                          |
            +-----------------------+---------------------------+--------------------------+
            | entity_type           | $eq, $in                  | Denotes the AWS entity   |
            |                       |                           | type to conditionalize   |
            |                       |                           | on. (Required)           |
            |                       |                           |                          |
            |                       |                           | {"entity_type":{"$eq":"a |
            |                       |                           | ws_rds_instance"}}       |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"entity_type":{"$in":[" |
            |                       |                           | aws_rds_instance",       |
            |                       |                           | "aws_ebs_volume", "aws_e |
            |                       |                           | c2_instance","aws_dynamo |
            |                       |                           | db_table",               |
            |                       |                           | "aws_rds_cluster"]}}     |
            |                       |                           |                          |
            |                       |                           |                          |
            +-----------------------+---------------------------+--------------------------+
        name:
            Name of the rule. Max 100 characters.
        priority:
            A priority relative to other rules.
    """

    # Create a mapping from Model property names to API property names
    _names = {'action': 'action', 'condition': 'condition', 'name': 'name', 'priority': 'priority'}

    def __init__(
        self,
        action: rule_action.RuleAction = None,
        condition: str = None,
        name: str = None,
        priority: rule_priority.RulePriority = None,
    ) -> None:
        """Constructor for the UpdatePolicyRuleV1Request class."""

        # Initialize members of the class
        self.action: rule_action.RuleAction = action
        self.condition: str = condition
        self.name: str = name
        self.priority: rule_priority.RulePriority = priority

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
        key = 'action'
        action = (
            rule_action.RuleAction.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        condition = dictionary.get('condition')
        name = dictionary.get('name')
        key = 'priority'
        priority = (
            rule_priority.RulePriority.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(action, condition, name, priority)
