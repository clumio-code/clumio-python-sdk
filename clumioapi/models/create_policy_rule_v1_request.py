#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import rule_action as rule_action_
from clumioapi.models import rule_priority as rule_priority_
import requests

T = TypeVar('T', bound='CreatePolicyRuleV1Request')


@dataclasses.dataclass
class CreatePolicyRuleV1Request:
    """Implementation of the 'CreatePolicyRuleV1Request' model.

    Attributes:
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
            | asset_name            | $eq, $not_eq, $in,        | denotes the asset        |
            |                       | $not_in, $contains,       | name(s) to               |
            |                       | $not_contains             | conditionalize on. max   |
            |                       |                           | 100 names allowed        |
            |                       |                           | in each rule and each    |
            |                       |                           | name can be upto 256     |
            |                       |                           | characters long. for ec2 |
            |                       |                           | instances and ebs        |
            |                       |                           | volumes, asset_name is   |
            |                       |                           | derived from the         |
            |                       |                           | aws name tag (case-      |
            |                       |                           | sensitive key);          |
            |                       |                           | resources without a      |
            |                       |                           | name tag will have an    |
            |                       |                           | empty asset name.        |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$eq":"my |
            |                       |                           | -asset"}}                |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$not_eq" |
            |                       |                           | :"my-asset"}}            |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$in":["a |
            |                       |                           | sset-1", "asset-2"]}}    |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$not_in" |
            |                       |                           | :["asset-1",             |
            |                       |                           | "asset-2"]}}             |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$contain |
            |                       |                           | s":"backup"}}            |
            |                       |                           |                          |
            |                       |                           |                          |
            |                       |                           | {"asset_name":{"$not_con |
            |                       |                           | tains":"temp"}}          |
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
            |                       |                           | aws_documentdb",         |
            |                       |                           | "aws_dynamodb_table",    |
            |                       |                           | "aws_ebs_volume",        |
            |                       |                           | "aws_ec2_instance",      |
            |                       |                           | "aws_iceberg_s3_table",  |
            |                       |                           | "aws_neptune",           |
            |                       |                           | "aws_rds_cluster",       |
            |                       |                           | "aws_rds_instance"]}}    |
            |                       |                           |                          |
            |                       |                           |                          |
            +-----------------------+---------------------------+--------------------------+

        Name:
            Name of the rule. max 100 characters.

        Priority:
            A priority relative to other rules.

    """

    Action: rule_action_.RuleAction | None = None
    Condition: str | None = None
    Name: str | None = None
    Priority: rule_priority_.RulePriority | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('action', None)
        val_action = rule_action_.RuleAction.from_dictionary(val)

        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('priority', None)
        val_priority = rule_priority_.RulePriority.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_action,
            val_condition,
            val_name,
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
        return model_instance
