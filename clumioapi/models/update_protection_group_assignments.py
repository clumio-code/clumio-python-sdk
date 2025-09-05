#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='UpdateProtectionGroupAssignments')


@dataclasses.dataclass
class UpdateProtectionGroupAssignments:
    """Implementation of the 'UpdateProtectionGroupAssignments' model.

        UpdateProtectionGroupAssignments denotes the protection groups to be assigned
        orunassigned.Updates to the protection group assignments.

        Attributes:
            Assign:
    List of protection group ids to assign to this organizational unit.

            Unassign:
    List of protection group ids to un-assign from this organizational unit.

    """

    Assign: Sequence[str] | None = None
    Unassign: Sequence[str] | None = None

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
        val = dictionary.get('assign', None)
        val_assign = val

        val = dictionary.get('unassign', None)
        val_unassign = val

        # Return an object of this model
        return cls(
            val_assign,
            val_unassign,
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
