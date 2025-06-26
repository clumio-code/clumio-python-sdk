#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import event_rules
from clumioapi.models import service_roles

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
    _names = {
        'clumio_event_pub_arn': 'clumio_event_pub_arn',
        'clumio_iam_role_arn': 'clumio_iam_role_arn',
        'clumio_support_role_arn': 'clumio_support_role_arn',
        'event_rules': 'event_rules',
        'service_roles': 'service_roles',
    }

    def __init__(
        self,
        clumio_event_pub_arn: str = None,
        clumio_iam_role_arn: str = None,
        clumio_support_role_arn: str = None,
        event_rules: event_rules.EventRules = None,
        service_roles: service_roles.ServiceRoles = None,
    ) -> None:
        """Constructor for the ConnectionResourcesResp class."""

        # Initialize members of the class
        self.clumio_event_pub_arn: str = clumio_event_pub_arn
        self.clumio_iam_role_arn: str = clumio_iam_role_arn
        self.clumio_support_role_arn: str = clumio_support_role_arn
        self.event_rules: event_rules.EventRules = event_rules
        self.service_roles: service_roles.ServiceRoles = service_roles

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
        clumio_event_pub_arn = dictionary.get('clumio_event_pub_arn')
        clumio_iam_role_arn = dictionary.get('clumio_iam_role_arn')
        clumio_support_role_arn = dictionary.get('clumio_support_role_arn')
        key = 'event_rules'
        p_event_rules = (
            event_rules.EventRules.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'service_roles'
        p_service_roles = (
            service_roles.ServiceRoles.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            clumio_event_pub_arn,
            clumio_iam_role_arn,
            clumio_support_role_arn,
            p_event_rules,
            p_service_roles,
        )
