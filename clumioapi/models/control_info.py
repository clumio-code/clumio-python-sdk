#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ControlInfo')


@dataclasses.dataclass
class ControlInfo:
    """Implementation of the 'ControlInfo' model.

    The status per controls in the compliance report created by the report run.

    Attributes:
        CompliantCount:
            The count of compliant items of the control.

        ControlStatus:
            The compliance status of the control.

        Name:
            The name of the control.

        NonCompliantCount:
            The count of non-compliant items of the control.

        UnknownCount:
            The count of unknown items of the control.

    """

    CompliantCount: int | None = None
    ControlStatus: str | None = None
    Name: str | None = None
    NonCompliantCount: int | None = None
    UnknownCount: int | None = None

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
        val = dictionary.get('compliant_count', None)
        val_compliant_count = val

        val = dictionary.get('control_status', None)
        val_control_status = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('non_compliant_count', None)
        val_non_compliant_count = val

        val = dictionary.get('unknown_count', None)
        val_unknown_count = val

        # Return an object of this model
        return cls(
            val_compliant_count,
            val_control_status,
            val_name,
            val_non_compliant_count,
            val_unknown_count,
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
