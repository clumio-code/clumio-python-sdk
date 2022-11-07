#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import auto_user_provisioning_rule_embedded
from clumioapi.models import auto_user_provisioning_rule_links
from clumioapi.models import rule_provision

T = TypeVar('T', bound='UpdateAutoUserProvisioningRuleResponse')


class UpdateAutoUserProvisioningRuleResponse:
    """Implementation of the 'UpdateAutoUserProvisioningRuleResponse' model.

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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'condition': 'condition',
        'name': 'name',
        'provision': 'provision',
        'rule_id': 'rule_id',
    }

    def __init__(
        self,
        embedded: auto_user_provisioning_rule_embedded.AutoUserProvisioningRuleEmbedded = None,
        links: auto_user_provisioning_rule_links.AutoUserProvisioningRuleLinks = None,
        condition: str = None,
        name: str = None,
        provision: rule_provision.RuleProvision = None,
        rule_id: str = None,
    ) -> None:
        """Constructor for the UpdateAutoUserProvisioningRuleResponse class."""

        # Initialize members of the class
        self.embedded: auto_user_provisioning_rule_embedded.AutoUserProvisioningRuleEmbedded = (
            embedded
        )
        self.links: auto_user_provisioning_rule_links.AutoUserProvisioningRuleLinks = links
        self.condition: str = condition
        self.name: str = name
        self.provision: rule_provision.RuleProvision = provision
        self.rule_id: str = rule_id

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
            auto_user_provisioning_rule_embedded.AutoUserProvisioningRuleEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            auto_user_provisioning_rule_links.AutoUserProvisioningRuleLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        condition = dictionary.get('condition')
        name = dictionary.get('name')
        key = 'provision'
        provision = (
            rule_provision.RuleProvision.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        rule_id = dictionary.get('rule_id')
        # Return an object of this model
        return cls(embedded, links, condition, name, provision, rule_id)
