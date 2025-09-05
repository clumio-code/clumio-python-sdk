#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import policy_embedded as policy_embedded_
from clumioapi.models import policy_links as policy_links_
from clumioapi.models import policy_operation as policy_operation_
import requests

T = TypeVar('T', bound='ReadPolicyResponse')


@dataclasses.dataclass
class ReadPolicyResponse:
    """Implementation of the 'ReadPolicyResponse' model.

        Attributes:
            Embedded:
    If the `embed` query parameter is set, displays the responses of the related resource,
    as defined by the embeddable link specified.

            Links:
    Urls to pages related to the resource.

            ActivationStatus:
    The status of the policy.
    refer to the policy activation status table for a complete list of policy statuses.

            CreatedTime:
    The created time of the policy in unix time.

            Id:
    The clumio-assigned id of the policy.

            LockStatus:
    The following table describes the possible lock statuses of a policy.

    +----------+-------------------------------------------------------------------+
    |  status  |                            description                            |
    +==========+===================================================================+
    | unlocked | policies are unlocked until an update or deletion task is queued. |
    +----------+-------------------------------------------------------------------+
    | updating | during a policy edit, concurrent edits or deletion requests will  |
    |          | be rejected.                                                      |
    +----------+-------------------------------------------------------------------+
    | deleting | during policy deletion, concurrent edits or deletion requests     |
    |          | will be rejected.                                                 |
    +----------+-------------------------------------------------------------------+
    .

            Name:
    The user-provided name of the policy.

            Operations:
    A set of service level agreements (sla) for the policy. a policy can include
    one or more sla sets that span across various operations.

            OrganizationalUnitId:
    The clumio-assigned id of the organizational unit associated with the policy.

            Timezone:
    True.

            UpdatedTime:
    The updated time of the policy in unix time.

    """

    Embedded: policy_embedded_.PolicyEmbedded | None = None
    Links: policy_links_.PolicyLinks | None = None
    ActivationStatus: str | None = None
    CreatedTime: int | None = None
    Id: str | None = None
    LockStatus: str | None = None
    Name: str | None = None
    Operations: Sequence[policy_operation_.PolicyOperation] | None = None
    OrganizationalUnitId: str | None = None
    Timezone: str | None = None
    UpdatedTime: int | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val_embedded = policy_embedded_.PolicyEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = policy_links_.PolicyLinks.from_dictionary(val)

        val = dictionary.get('activation_status', None)
        val_activation_status = val

        val = dictionary.get('created_time', None)
        val_created_time = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('lock_status', None)
        val_lock_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('operations', None)

        val_operations = []
        if val:
            for value in val:
                val_operations.append(policy_operation_.PolicyOperation.from_dictionary(value))

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('timezone', None)
        val_timezone = val

        val = dictionary.get('updated_time', None)
        val_updated_time = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_activation_status,
            val_created_time,
            val_id,
            val_lock_status,
            val_name,
            val_operations,
            val_organizational_unit_id,
            val_timezone,
            val_updated_time,
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
