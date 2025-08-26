#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rule_action as rule_action_
from clumioapi.models import rule_embedded as rule_embedded_
from clumioapi.models import rule_links as rule_links_
from clumioapi.models import rule_priority as rule_priority_

T = TypeVar('T', bound='ReadRuleResponse')


class ReadRuleResponse:
    """Implementation of the 'ReadRuleResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
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
        p_id:
            The Clumio-assigned ID of the policy rule.
        name:
            Name of the rule. Max 100 characters.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit (OU) to which the policy rule
            belongs.
        priority:
            A priority relative to other rules.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'action': 'action',
        'condition': 'condition',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'priority': 'priority',
    }

    def __init__(
        self,
        embedded: rule_embedded_.RuleEmbedded | None = None,
        links: rule_links_.RuleLinks | None = None,
        action: rule_action_.RuleAction | None = None,
        condition: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        priority: rule_priority_.RulePriority | None = None,
    ) -> None:
        """Constructor for the ReadRuleResponse class."""

        # Initialize members of the class
        self.embedded: rule_embedded_.RuleEmbedded | None = embedded
        self.links: rule_links_.RuleLinks | None = links
        self.action: rule_action_.RuleAction | None = action
        self.condition: str | None = condition
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.priority: rule_priority_.RulePriority | None = priority

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
        val = dictionary.get('_embedded', None)
        val_embedded = rule_embedded_.RuleEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = rule_links_.RuleLinks.from_dictionary(val)

        val = dictionary.get('action', None)
        val_action = rule_action_.RuleAction.from_dictionary(val)

        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('priority', None)
        val_priority = rule_priority_.RulePriority.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_action,
            val_condition,
            val_p_id,
            val_name,
            val_organizational_unit_id,
            val_priority,
        )
