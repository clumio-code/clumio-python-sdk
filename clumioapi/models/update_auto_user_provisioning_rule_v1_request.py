#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rule_provision as rule_provision_
import requests

T = TypeVar('T', bound='UpdateAutoUserProvisioningRuleV1Request')


@dataclasses.dataclass
class UpdateAutoUserProvisioningRuleV1Request:
    """Implementation of the 'UpdateAutoUserProvisioningRuleV1Request' model.

        Attributes:
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

    """

    Condition: str | None = None
    Name: str | None = None
    Provision: rule_provision_.RuleProvision | None = None

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
        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('provision', None)
        val_provision = rule_provision_.RuleProvision.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_condition,
            val_name,
            val_provision,
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
