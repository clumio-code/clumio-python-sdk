#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import event_rules as event_rules_
from clumioapi.models import service_instance_profiles as service_instance_profiles_
from clumioapi.models import service_roles as service_roles_

T = TypeVar('T', bound='Resources')


class Resources:
    """Implementation of the 'Resources' model.

    Partial updates are not supported, therefore you must provide ARNs for all
    configured resources,including those for resources that are not being updated.

    Attributes:
        clumio_event_pub_arn:
            SNS topic created in the account to receive relevant events.
        clumio_iam_role_arn:
            ARN of the IAM role created in the account, which will be assumed by Clumio.
        clumio_support_role_arn:
            ARN of the support role which will be used by the Clumio support team.
        event_rules:

        service_instance_profiles:

        service_roles:

    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'clumio_event_pub_arn': 'clumio_event_pub_arn',
        'clumio_iam_role_arn': 'clumio_iam_role_arn',
        'clumio_support_role_arn': 'clumio_support_role_arn',
        'event_rules': 'event_rules',
        'service_instance_profiles': 'service_instance_profiles',
        'service_roles': 'service_roles',
    }

    def __init__(
        self,
        clumio_event_pub_arn: str,
        clumio_iam_role_arn: str,
        clumio_support_role_arn: str,
        event_rules: event_rules_.EventRules,
        service_instance_profiles: service_instance_profiles_.ServiceInstanceProfiles,
        service_roles: service_roles_.ServiceRoles,
    ) -> None:
        """Constructor for the Resources class."""

        # Initialize members of the class
        self.clumio_event_pub_arn: str = clumio_event_pub_arn
        self.clumio_iam_role_arn: str = clumio_iam_role_arn
        self.clumio_support_role_arn: str = clumio_support_role_arn
        self.event_rules: event_rules_.EventRules = event_rules
        self.service_instance_profiles: service_instance_profiles_.ServiceInstanceProfiles = (
            service_instance_profiles
        )
        self.service_roles: service_roles_.ServiceRoles = service_roles

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
        val = dictionary['clumio_event_pub_arn']
        val_clumio_event_pub_arn = val

        val = dictionary['clumio_iam_role_arn']
        val_clumio_iam_role_arn = val

        val = dictionary['clumio_support_role_arn']
        val_clumio_support_role_arn = val

        val = dictionary['event_rules']
        val_event_rules = event_rules_.EventRules.from_dictionary(val)

        val = dictionary['service_instance_profiles']
        val_service_instance_profiles = (
            service_instance_profiles_.ServiceInstanceProfiles.from_dictionary(val)
        )

        val = dictionary['service_roles']
        val_service_roles = service_roles_.ServiceRoles.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_clumio_event_pub_arn,  # type: ignore
            val_clumio_iam_role_arn,  # type: ignore
            val_clumio_support_role_arn,  # type: ignore
            val_event_rules,  # type: ignore
            val_service_instance_profiles,  # type: ignore
            val_service_roles,  # type: ignore
        )
