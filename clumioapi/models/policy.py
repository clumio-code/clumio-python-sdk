#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_embedded as policy_embedded_
from clumioapi.models import policy_links as policy_links_
from clumioapi.models import policy_operation as policy_operation_

T = TypeVar('T', bound='Policy')


class Policy:
    """Implementation of the 'Policy' model.

    Attributes:
        embedded:
            If the `embed` query parameter is set, displays the responses of the related
            resource,
            as defined by the embeddable link specified.
        links:
            URLs to pages related to the resource.
        activation_status:
            The status of the policy.
            Refer to the Policy Activation Status table for a complete list of policy
            statuses.
        created_time:
            The created time of the policy in unix time.
        p_id:
            The Clumio-assigned ID of the policy.
        lock_status:
            The following table describes the possible lock statuses of a policy.

            +----------+-------------------------------------------------------------------+
            |  Status  |                            Description                            |
            +==========+===================================================================+
            | unlocked | Policies are unlocked until an update or deletion task is queued. |
            +----------+-------------------------------------------------------------------+
            | updating | During a policy edit, concurrent edits or deletion requests will  |
            |          | be rejected.                                                      |
            +----------+-------------------------------------------------------------------+
            | deleting | During policy deletion, concurrent edits or deletion requests     |
            |          | will be rejected.                                                 |
            +----------+-------------------------------------------------------------------+
        name:
            The user-provided name of the policy.
        operations:
            A set of service level agreements (SLA) for the policy. A policy can include
            one or more SLA sets that span across various operations.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the policy.
        timezone:
            The policy-level timezone is deprecated, as the operation-level timezone should
            be used instead.
            The timezone must be a valid location name from the IANA Time Zone database.
            For instance, "America/New_York", "US/Central", "UTC".
            Deprecated: true
        updated_time:
            The updated time of the policy in unix time.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'activation_status': 'activation_status',
        'created_time': 'created_time',
        'p_id': 'id',
        'lock_status': 'lock_status',
        'name': 'name',
        'operations': 'operations',
        'organizational_unit_id': 'organizational_unit_id',
        'timezone': 'timezone',
        'updated_time': 'updated_time',
    }

    def __init__(
        self,
        embedded: policy_embedded_.PolicyEmbedded | None = None,
        links: policy_links_.PolicyLinks | None = None,
        activation_status: str | None = None,
        created_time: int | None = None,
        p_id: str | None = None,
        lock_status: str | None = None,
        name: str | None = None,
        operations: Sequence[policy_operation_.PolicyOperation] | None = None,
        organizational_unit_id: str | None = None,
        timezone: str | None = None,
        updated_time: int | None = None,
    ) -> None:
        """Constructor for the Policy class."""

        # Initialize members of the class
        self.embedded: policy_embedded_.PolicyEmbedded | None = embedded
        self.links: policy_links_.PolicyLinks | None = links
        self.activation_status: str | None = activation_status
        self.created_time: int | None = created_time
        self.p_id: str | None = p_id
        self.lock_status: str | None = lock_status
        self.name: str | None = name
        self.operations: Sequence[policy_operation_.PolicyOperation] | None = operations
        self.organizational_unit_id: str | None = organizational_unit_id
        self.timezone: str | None = timezone
        self.updated_time: int | None = updated_time

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
        val_embedded = policy_embedded_.PolicyEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = policy_links_.PolicyLinks.from_dictionary(val)

        val = dictionary.get('activation_status', None)
        val_activation_status = val

        val = dictionary.get('created_time', None)
        val_created_time = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('lock_status', None)
        val_lock_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('operations', None)

        val_operations = None
        if val:
            val_operations = list()
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
            val_p_id,
            val_lock_status,
            val_name,
            val_operations,
            val_organizational_unit_id,
            val_timezone,
            val_updated_time,
        )
