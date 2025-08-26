#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import policy_operation_input as policy_operation_input_
import requests

T = TypeVar('T', bound='UpdatePolicyDefinitionV1Request')


@dataclasses.dataclass
class UpdatePolicyDefinitionV1Request:
    """Implementation of the 'UpdatePolicyDefinitionV1Request' model.

        Attributes:
            ActivationStatus:
                The status of the policy.
    refer to the policy activation status table for a complete list of policy statuses.

            Name:
                The user-provided name of the policy.

            Operations:
                A set of service level agreements (sla) for the policy. a policy can include
    one or more sla sets that span across various operations.

            OrganizationalUnitId:
                The clumio-assigned id of the organizational unit associated with the policy.

            Timezone:
                True.

    """

    ActivationStatus: str | None = None
    Name: str | None = None
    Operations: Sequence[policy_operation_input_.PolicyOperationInput] | None = None
    OrganizationalUnitId: str | None = None
    Timezone: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
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
        val = dictionary.get('activation_status', None)
        val_activation_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('operations', None)

        val_operations = []
        if val:
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
