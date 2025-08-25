#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

import requests

T = TypeVar('T', bound='AutoUserProvisioningRuleEmbedded')


@dataclasses.dataclass
class AutoUserProvisioningRuleEmbedded:
    """Implementation of the 'AutoUserProvisioningRuleEmbedded' model.

        Embedded responses related to the resource.

        Attributes:
            ReadOrganizationalUnit:
                Embeds the associated organizational units for the ou uuids in the response
    if requested using the `embed` query parameter.

            ReadRole:
                Embeds the associated role for the role uuid in the response if requested using the `embed` query parameter.

    """

    ReadOrganizationalUnit: object | None = None
    ReadRole: object | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(self)

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
        val = dictionary.get('read-organizational-unit', None)
        val_read_organizational_unit = val

        val = dictionary.get('read-role', None)
        val_read_role = val

        # Return an object of this model
        return cls(
            val_read_organizational_unit,
            val_read_role,
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
