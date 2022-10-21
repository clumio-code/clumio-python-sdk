#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_operation

T = TypeVar('T', bound='UpdatePolicyDefinitionV1Request')


class UpdatePolicyDefinitionV1Request:
    """Implementation of the 'UpdatePolicyDefinitionV1Request' model.

    Attributes:
        activation_status:
            The status of the policy.
            Refer to the Policy Activation Status table for a complete list of policy
            statuses.
        created_time:
            The created time of the policy in unix time.
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
        'activation_status': 'activation_status',
        'created_time': 'created_time',
        'name': 'name',
        'operations': 'operations',
        'organizational_unit_id': 'organizational_unit_id',
        'timezone': 'timezone',
        'updated_time': 'updated_time',
    }

    def __init__(
        self,
        activation_status: str = None,
        created_time: int = None,
        name: str = None,
        operations: Sequence[policy_operation.PolicyOperation] = None,
        organizational_unit_id: str = None,
        timezone: str = None,
        updated_time: int = None,
    ) -> None:
        """Constructor for the UpdatePolicyDefinitionV1Request class."""

        # Initialize members of the class
        self.activation_status: str = activation_status
        self.created_time: int = created_time
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
        activation_status = dictionary.get('activation_status')
        created_time = dictionary.get('created_time')
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
            activation_status,
            created_time,
            name,
            operations,
            organizational_unit_id,
            timezone,
            updated_time,
        )
