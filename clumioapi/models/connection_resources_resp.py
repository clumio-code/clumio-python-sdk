#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import event_rules as event_rules_
from clumioapi.models import service_roles as service_roles_

T = TypeVar('T', bound='ConnectionResourcesResp')


class ConnectionResourcesResp:
    """Implementation of the 'ConnectionResourcesResp' model.

    Attributes:
        clumio_event_pub_arn:
            SNS topic created in the account to receive relevant events.
        clumio_iam_role_arn:
            ARN of the IAM role created in the account, which will be assumed by Clumio.
        clumio_support_role_arn:
            ARN of the support role which will be used by the Clumio support team.
        event_rules:

        service_roles:

    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'clumio_event_pub_arn': 'clumio_event_pub_arn',
        'clumio_iam_role_arn': 'clumio_iam_role_arn',
        'clumio_support_role_arn': 'clumio_support_role_arn',
        'event_rules': 'event_rules',
        'service_roles': 'service_roles',
    }

    def __init__(
        self,
        clumio_event_pub_arn: str | None = None,
        clumio_iam_role_arn: str | None = None,
        clumio_support_role_arn: str | None = None,
        event_rules: event_rules_.EventRules | None = None,
        service_roles: service_roles_.ServiceRoles | None = None,
    ) -> None:
        """Constructor for the ConnectionResourcesResp class."""

        # Initialize members of the class
        self.clumio_event_pub_arn: str | None = clumio_event_pub_arn
        self.clumio_iam_role_arn: str | None = clumio_iam_role_arn
        self.clumio_support_role_arn: str | None = clumio_support_role_arn
        self.event_rules: event_rules_.EventRules | None = event_rules
        self.service_roles: service_roles_.ServiceRoles | None = service_roles

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
        val = dictionary.get('clumio_event_pub_arn', None)
        val_clumio_event_pub_arn = val

        val = dictionary.get('clumio_iam_role_arn', None)
        val_clumio_iam_role_arn = val

        val = dictionary.get('clumio_support_role_arn', None)
        val_clumio_support_role_arn = val

        val = dictionary.get('event_rules', None)
        val_event_rules = event_rules_.EventRules.from_dictionary(val)

        val = dictionary.get('service_roles', None)
        val_service_roles = service_roles_.ServiceRoles.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_clumio_event_pub_arn,
            val_clumio_iam_role_arn,
            val_clumio_support_role_arn,
            val_event_rules,
            val_service_roles,
        )
