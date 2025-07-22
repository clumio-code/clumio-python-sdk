#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_operation_input as policy_operation_input_

T = TypeVar('T', bound='UpdatePolicyDefinitionV1Request')


class UpdatePolicyDefinitionV1Request:
    """Implementation of the 'UpdatePolicyDefinitionV1Request' model.

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
        activation_status: str,
        name: str,
        operations: Sequence[policy_operation_input_.PolicyOperationInput],
        organizational_unit_id: str,
        timezone: str,
    ) -> None:
        """Constructor for the UpdatePolicyDefinitionV1Request class."""

        # Initialize members of the class
        self.activation_status: str = activation_status
        self.name: str = name
        self.operations: Sequence[policy_operation_input_.PolicyOperationInput] = operations
        self.organizational_unit_id: str = organizational_unit_id
        self.timezone: str = timezone

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
        val = dictionary['activation_status']
        val_activation_status = val

        val = dictionary['name']
        val_name = val

        val = dictionary['operations']

        val_operations = None
        if val:
            val_operations = list()
            for value in val:
                val_operations.append(
                    policy_operation_input_.PolicyOperationInput.from_dictionary(value)
                )

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['timezone']
        val_timezone = val

        # Return an object of this model
        return cls(
            val_activation_status,  # type: ignore
            val_name,  # type: ignore
            val_operations,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_timezone,  # type: ignore
        )
