#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rule_action as rule_action_
from clumioapi.models import rule_embedded as rule_embedded_
from clumioapi.models import rule_links as rule_links_
from clumioapi.models import rule_priority as rule_priority_
import requests

T = TypeVar('T', bound='ReadRuleResponse')


@dataclasses.dataclass
class ReadRuleResponse:
    """Implementation of the 'ReadRuleResponse' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            Action:
                An action to be applied subject to the rule criteria.

            Condition:
                |
    |                       |                           | {"key":"environment",    |
    |                       |                           | "value":"prod"}}}        |
    |                       |                           |                          |
    |                       |                           |                          |
    |                       |                           | {"aws_tag":{"$not_eq":{" |
    |                       |                           | key":"environment",      |
    |                       |                           | "value":"prod"}}}        |
    |                       |                           |                          |
    |                       |                           |                          |
    |                       |                           | {"aws_tag":{"$not_in":[{ |
    |                       |                           | "key":"environment",     |
    |                       |                           | "value":"prod"},         |
    |                       |                           | {"key":"hello",          |
    |                       |                           | "value":"world"}]}}      |
    |                       |                           |                          |
    |                       |                           |                          |
    |                       |                           | {"aws_tag":{"$not_all":[ |
    |                       |                           | {"key":"environment",    |
    |                       |                           | "value":"prod"},         |
    |                       |                           | {"key":"hello",          |
    |                       |                           | "value":"world"}]}}      |
    |                       |                           |                          |
    |                       |                           |                          |
    |                       |                           | {"aws_tag":{"$not_contai |
    |                       |                           | ns":{"key":"environment" |
    |                       |                           | , "value":"prod"}}}      |
    |                       |                           |                          |
    |                       |                           |                          |
    +-----------------------+---------------------------+--------------------------+
    | entity_type           | $eq, $in                  | denotes the aws entity   |
    |                       |                           | type to conditionalize   |
    |                       |                           | on. (required)           |
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
    .

            Id:
                The clumio-assigned id of the policy rule.

            Name:
                Name of the rule. max 100 characters.

            OrganizationalUnitId:
                The clumio-assigned id of the organizational unit (ou) to which the policy rule belongs.

            Priority:
                A priority relative to other rules.

    """

    Embedded: rule_embedded_.RuleEmbedded | None = None
    Links: rule_links_.RuleLinks | None = None
    Action: rule_action_.RuleAction | None = None
    Condition: str | None = None
    Id: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    Priority: rule_priority_.RulePriority | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = rule_embedded_.RuleEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = rule_links_.RuleLinks.from_dictionary(val)

        val = dictionary.get('action', None)
        val_action = rule_action_.RuleAction.from_dictionary(val)

        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('id', None)
        val_id = val

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
            val_id,
            val_name,
            val_organizational_unit_id,
            val_priority,
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
        model_instance.raw_response = response
        return model_instance
