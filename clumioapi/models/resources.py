#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import event_rules as event_rules_
from clumioapi.models import service_instance_profiles as service_instance_profiles_
from clumioapi.models import service_roles as service_roles_
import requests

T = TypeVar('T', bound='Resources')


@dataclasses.dataclass
class Resources:
    """Implementation of the 'Resources' model.

    Partial updates are not supported, therefore you must provide ARNs for all
    configured resources,including those for resources that are not being updated.

    Attributes:
        ClumioEventPubArn:
            Sns topic created in the account to receive relevant events.

        ClumioIamRoleArn:
            Arn of the iam role created in the account, which will be assumed by clumio.

        ClumioSupportRoleArn:
            Arn of the support role which will be used by the clumio support team.

        EventRules

        ServiceInstanceProfiles

        ServiceRoles

    """

    ClumioEventPubArn: str | None = None
    ClumioIamRoleArn: str | None = None
    ClumioSupportRoleArn: str | None = None
    EventRules: event_rules_.EventRules | None = None
    ServiceInstanceProfiles: service_instance_profiles_.ServiceInstanceProfiles | None = None
    ServiceRoles: service_roles_.ServiceRoles | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('clumio_event_pub_arn', None)
        val_clumio_event_pub_arn = val

        val = dictionary.get('clumio_iam_role_arn', None)
        val_clumio_iam_role_arn = val

        val = dictionary.get('clumio_support_role_arn', None)
        val_clumio_support_role_arn = val

        val = dictionary.get('event_rules', None)
        val_event_rules = event_rules_.EventRules.from_dictionary(val)

        val = dictionary.get('service_instance_profiles', None)
        val_service_instance_profiles = (
            service_instance_profiles_.ServiceInstanceProfiles.from_dictionary(val)
        )

        val = dictionary.get('service_roles', None)
        val_service_roles = service_roles_.ServiceRoles.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_clumio_event_pub_arn,
            val_clumio_iam_role_arn,
            val_clumio_support_role_arn,
            val_event_rules,
            val_service_instance_profiles,
            val_service_roles,
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
