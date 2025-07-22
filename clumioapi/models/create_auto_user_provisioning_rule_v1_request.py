#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rule_provision as rule_provision_

T = TypeVar('T', bound='CreateAutoUserProvisioningRuleV1Request')


class CreateAutoUserProvisioningRuleV1Request:
    """Implementation of the 'CreateAutoUserProvisioningRuleV1Request' model.

    Attributes:
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
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'condition': 'condition', 'name': 'name', 'provision': 'provision'}

    def __init__(self, condition: str, name: str, provision: rule_provision_.RuleProvision) -> None:
        """Constructor for the CreateAutoUserProvisioningRuleV1Request class."""

        # Initialize members of the class
        self.condition: str = condition
        self.name: str = name
        self.provision: rule_provision_.RuleProvision = provision

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

        # Extract variables from the dictionary
        val = dictionary['condition']
        val_condition = val

        val = dictionary['name']
        val_name = val

        val = dictionary['provision']
        val_provision = rule_provision_.RuleProvision.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_condition,  # type: ignore
            val_name,  # type: ignore
            val_provision,  # type: ignore
        )
