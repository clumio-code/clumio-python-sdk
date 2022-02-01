#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rule_action
from clumioapi.models import rule_embedded
from clumioapi.models import rule_links
from clumioapi.models import rule_priority

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
            | aws_tag               | $eq, $in, $all, $contains | Denotes the AWS tag(s)   |
            |                       |                           | to conditionalize on     |
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
            +-----------------------+---------------------------+--------------------------+
            | entity_type           | $eq, $in                  | Denotes the AWS entity   |
            |                       |                           | type to conditionalize   |
            |                       |                           | on                       |
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
        id:
            The Clumio-assigned ID of the policy rule.
        name:
            Name of the rule.
        priority:
            A priority relative to other rules.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'action': 'action',
        'condition': 'condition',
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
    }

    def __init__(
        self,
        embedded: rule_embedded.RuleEmbedded = None,
        links: rule_links.RuleLinks = None,
        action: rule_action.RuleAction = None,
        condition: str = None,
        id: str = None,
        name: str = None,
        priority: rule_priority.RulePriority = None,
    ) -> None:
        """Constructor for the ReadRuleResponse class."""

        # Initialize members of the class
        self.embedded: rule_embedded.RuleEmbedded = embedded
        self.links: rule_links.RuleLinks = links
        self.action: rule_action.RuleAction = action
        self.condition: str = condition
        self.id: str = id
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
        key = '_embedded'
        embedded = (
            rule_embedded.RuleEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            rule_links.RuleLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'action'
        action = (
            rule_action.RuleAction.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        condition = dictionary.get('condition')
        id = dictionary.get('id')
        name = dictionary.get('name')
        key = 'priority'
        priority = (
            rule_priority.RulePriority.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links, action, condition, id, name, priority)
