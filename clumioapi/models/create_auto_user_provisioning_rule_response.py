#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    auto_user_provisioning_rule_embedded as auto_user_provisioning_rule_embedded_
from clumioapi.models import auto_user_provisioning_rule_links as auto_user_provisioning_rule_links_
from clumioapi.models import rule_provision as rule_provision_

T = TypeVar('T', bound='CreateAutoUserProvisioningRuleResponse')


class CreateAutoUserProvisioningRuleResponse:
    """Implementation of the 'CreateAutoUserProvisioningRuleResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        condition:
            The following table describes the possible conditions for a rule.

            +--------------------------+-------------------------+-------------------------+
            |     Group Selection      |     Rule Condition      |       Description       |
            +==========================+=========================+=========================+
            | This group               |                         | User must belong to the |
            |                          |                         | specified group.        |
            |                          | {"user.groups":{"$eq":" |                         |
            |                          | Admin"}}                |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
            | ANY of these groups      |                         | User must belong to at  |
            |                          |                         | least one of the        |
            |                          | {"user.groups":{"$in":[ | specified groups.       |
            |                          | "Admin", "Eng",         |                         |
            |                          | "Sales"]}}              |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
            | ALL of these groups      |                         | User must belong to all |
            |                          |                         | the specified groups.   |
            |                          | {"user.groups":{"$all": |                         |
            |                          | ["Admin", "Eng",        |                         |
            |                          | "Sales"]}}              |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
            | Group CONTAINS this      |                         | User's group must       |
            | keyword                  |                         | contain the specified   |
            |                          | {"user.groups":{"$conta | keyword.                |
            |                          | ins":{"$in":["Admin"]}} |                         |
            |                          | }                       |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
            | Group CONTAINS ANY of    |                         | User's group must       |
            | these keywords           |                         | contain at least one of |
            |                          | {"user.groups":{"$conta | the specified keywords. |
            |                          | ins":{"$in":["Admin",   |                         |
            |                          | "Eng", "Sales"]}}}      |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
            | Group CONTAINS ALL of    |                         | User's group must       |
            | these keywords           |                         | contain all the         |
            |                          | {"user.groups":{"$conta | specified keywords.     |
            |                          | ins":{"$all":["Admin",  |                         |
            |                          | "Eng", "Sales"]}}}      |                         |
            |                          |                         |                         |
            |                          |                         |                         |
            +--------------------------+-------------------------+-------------------------+
        name:
            Unique name assigned to the rule.
        provision:
            Specifies the role and the organizational units to be assigned to the user
            subject to the rule criteria.
        rule_id:
            The Clumio-assigned ID of the rule.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'condition': 'condition',
        'name': 'name',
        'provision': 'provision',
        'rule_id': 'rule_id',
    }

    def __init__(
        self,
        embedded: (
            auto_user_provisioning_rule_embedded_.AutoUserProvisioningRuleEmbedded | None
        ) = None,
        links: auto_user_provisioning_rule_links_.AutoUserProvisioningRuleLinks | None = None,
        condition: str | None = None,
        name: str | None = None,
        provision: rule_provision_.RuleProvision | None = None,
        rule_id: str | None = None,
    ) -> None:
        """Constructor for the CreateAutoUserProvisioningRuleResponse class."""

        # Initialize members of the class
        self.embedded: (
            auto_user_provisioning_rule_embedded_.AutoUserProvisioningRuleEmbedded | None
        ) = embedded
        self.links: auto_user_provisioning_rule_links_.AutoUserProvisioningRuleLinks | None = links
        self.condition: str | None = condition
        self.name: str | None = name
        self.provision: rule_provision_.RuleProvision | None = provision
        self.rule_id: str | None = rule_id

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
