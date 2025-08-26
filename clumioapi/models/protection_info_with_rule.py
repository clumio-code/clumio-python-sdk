#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ProtectionInfoWithRule')


@dataclasses.dataclass
class ProtectionInfoWithRule:
    """Implementation of the 'ProtectionInfoWithRule' model.

        The protection policy applied to this resource. If the resource is not
        protected, then this field has a value of `null`.

        Attributes:
            InheritingEntityId:
                The id of the entity from which protection was inherited.
    if protection was not inherited, then this field has a value of `null`.

            InheritingEntityType:
                The type of entity from which protection was inherited.
    if protection was not inherited, then this field has a value of `null`.
    entities from which protection can be inherited include the following:

    +------------------------+----------+
    | inheriting entity type | details  |
    +========================+==========+
    | aws_tag                | aws tag. |
    +------------------------+----------+
    .

            PolicyId:
                A system-generated id assigned to the policy protecting this resource.

    """

    InheritingEntityId: str | None = None
    InheritingEntityType: str | None = None
    PolicyId: str | None = None

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
        val = dictionary.get('inheriting_entity_id', None)
        val_inheriting_entity_id = val

        val = dictionary.get('inheriting_entity_type', None)
        val_inheriting_entity_type = val

        val = dictionary.get('policy_id', None)
        val_policy_id = val

        # Return an object of this model
        return cls(
            val_inheriting_entity_id,
            val_inheriting_entity_type,
            val_policy_id,
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
