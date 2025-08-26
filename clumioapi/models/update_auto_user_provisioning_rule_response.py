#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    auto_user_provisioning_rule_embedded as auto_user_provisioning_rule_embedded_
from clumioapi.models import auto_user_provisioning_rule_links as auto_user_provisioning_rule_links_
from clumioapi.models import rule_provision as rule_provision_
import requests

T = TypeVar('T', bound='UpdateAutoUserProvisioningRuleResponse')


@dataclasses.dataclass
class UpdateAutoUserProvisioningRuleResponse:
    """Implementation of the 'UpdateAutoUserProvisioningRuleResponse' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            Condition:
                |                         |
    |                          | ["admin", "eng",        |                         |
    |                          | "sales"]}}              |                         |
    |                          |                         |                         |
    |                          |                         |                         |
    +--------------------------+-------------------------+-------------------------+
    | group contains this      |                         | user's group must       |
    | keyword                  |                         | contain the specified   |
    |                          | {"user.groups":{"$conta | keyword.                |
    |                          | ins":{"$in":["admin"]}} |                         |
    |                          | }                       |                         |
    |                          |                         |                         |
    |                          |                         |                         |
    +--------------------------+-------------------------+-------------------------+
    | group contains any of    |                         | user's group must       |
    | these keywords           |                         | contain at least one of |
    |                          | {"user.groups":{"$conta | the specified keywords. |
    |                          | ins":{"$in":["admin",   |                         |
    |                          | "eng", "sales"]}}}      |                         |
    |                          |                         |                         |
    |                          |                         |                         |
    +--------------------------+-------------------------+-------------------------+
    | group contains all of    |                         | user's group must       |
    | these keywords           |                         | contain all the         |
    |                          | {"user.groups":{"$conta | specified keywords.     |
    |                          | ins":{"$all":["admin",  |                         |
    |                          | "eng", "sales"]}}}      |                         |
    |                          |                         |                         |
    |                          |                         |                         |
    +--------------------------+-------------------------+-------------------------+
    .

            Name:
                Unique name assigned to the rule.

            Provision:
                Specifies the role and the organizational units to be assigned to the user subject to the rule criteria.

            RuleId:
                The clumio-assigned id of the rule.

    """

    Embedded: auto_user_provisioning_rule_embedded_.AutoUserProvisioningRuleEmbedded | None = None
    Links: auto_user_provisioning_rule_links_.AutoUserProvisioningRuleLinks | None = None
    Condition: str | None = None
    Name: str | None = None
    Provision: rule_provision_.RuleProvision | None = None
    RuleId: str | None = None
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
        val_embedded = (
            auto_user_provisioning_rule_embedded_.AutoUserProvisioningRuleEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = (
            auto_user_provisioning_rule_links_.AutoUserProvisioningRuleLinks.from_dictionary(val)
        )

        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('provision', None)
        val_provision = rule_provision_.RuleProvision.from_dictionary(val)

        val = dictionary.get('rule_id', None)
        val_rule_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_condition,
            val_name,
            val_provision,
            val_rule_id,
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
