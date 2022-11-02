#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_embedded
from clumioapi.models import policy_links
from clumioapi.models import policy_operation

T = TypeVar('T', bound='ReadPolicyResponse')


class ReadPolicyResponse:
    """Implementation of the 'ReadPolicyResponse' model.

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
        assigned_organizational_unit_ids:
            The Clumio-assigned IDs of the organizational units to whom the policy has been
            assigned.
        created_time:
            The created time of the policy in unix time.
        id:
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
            The timezone for the policy.
        updated_time:
            The updated time of the policy in unix time.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'activation_status': 'activation_status',
        'assigned_organizational_unit_ids': 'assigned_organizational_unit_ids',
        'created_time': 'created_time',
        'id': 'id',
        'lock_status': 'lock_status',
        'name': 'name',
        'operations': 'operations',
        'organizational_unit_id': 'organizational_unit_id',
        'timezone': 'timezone',
        'updated_time': 'updated_time',
    }

    def __init__(
        self,
        embedded: policy_embedded.PolicyEmbedded = None,
        links: policy_links.PolicyLinks = None,
        activation_status: str = None,
        assigned_organizational_unit_ids: Sequence[str] = None,
        created_time: int = None,
        id: str = None,
        lock_status: str = None,
        name: str = None,
        operations: Sequence[policy_operation.PolicyOperation] = None,
        organizational_unit_id: str = None,
        timezone: str = None,
        updated_time: int = None,
    ) -> None:
        """Constructor for the ReadPolicyResponse class."""

        # Initialize members of the class
        self.embedded: policy_embedded.PolicyEmbedded = embedded
        self.links: policy_links.PolicyLinks = links
        self.activation_status: str = activation_status
        self.assigned_organizational_unit_ids: Sequence[str] = assigned_organizational_unit_ids
        self.created_time: int = created_time
        self.id: str = id
        self.lock_status: str = lock_status
        self.name: str = name
        self.operations: Sequence[policy_operation.PolicyOperation] = operations
        self.organizational_unit_id: str = organizational_unit_id
        self.timezone: str = timezone
        self.updated_time: int = updated_time

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
            policy_embedded.PolicyEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            policy_links.PolicyLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        activation_status = dictionary.get('activation_status')
        assigned_organizational_unit_ids = dictionary.get('assigned_organizational_unit_ids')
        created_time = dictionary.get('created_time')
        id = dictionary.get('id')
        lock_status = dictionary.get('lock_status')
        name = dictionary.get('name')
        operations = None
        if dictionary.get('operations'):
            operations = list()
            for value in dictionary.get('operations'):
                operations.append(policy_operation.PolicyOperation.from_dictionary(value))

        organizational_unit_id = dictionary.get('organizational_unit_id')
        timezone = dictionary.get('timezone')
        updated_time = dictionary.get('updated_time')
        # Return an object of this model
        return cls(
            embedded,
            links,
            activation_status,
            assigned_organizational_unit_ids,
            created_time,
            id,
            lock_status,
            name,
            operations,
            organizational_unit_id,
            timezone,
            updated_time,
        )
