#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_operation_input as policy_operation_input_

T = TypeVar('T', bound='CreatePolicyDefinitionV1Request')


class CreatePolicyDefinitionV1Request:
    """Implementation of the 'CreatePolicyDefinitionV1Request' model.

    Attributes:
        activation_status:
            The status of the policy.
            Refer to the Policy Activation Status table for a complete list of policy
            statuses.
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
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'activation_status': 'activation_status',
        'name': 'name',
        'operations': 'operations',
        'organizational_unit_id': 'organizational_unit_id',
        'timezone': 'timezone',
    }

    def __init__(
        self,
        activation_status: str | None = None,
        name: str | None = None,
        operations: Sequence[policy_operation_input_.PolicyOperationInput] | None = None,
        organizational_unit_id: str | None = None,
        timezone: str | None = None,
    ) -> None:
        """Constructor for the CreatePolicyDefinitionV1Request class."""

        # Initialize members of the class
        self.activation_status: str | None = activation_status
        self.name: str | None = name
        self.operations: Sequence[policy_operation_input_.PolicyOperationInput] | None = operations
        self.organizational_unit_id: str | None = organizational_unit_id
        self.timezone: str | None = timezone

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
        val = dictionary.get('activation_status', None)
        val_activation_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('operations', None)

        val_operations = None
        if val:
            val_operations = list()
            for value in val:
                val_operations.append(
                    policy_operation_input_.PolicyOperationInput.from_dictionary(value)
                )

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('timezone', None)
        val_timezone = val

        # Return an object of this model
        return cls(
            val_activation_status,
            val_name,
            val_operations,
            val_organizational_unit_id,
            val_timezone,
        )
