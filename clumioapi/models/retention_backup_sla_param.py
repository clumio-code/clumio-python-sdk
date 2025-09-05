#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RetentionBackupSLAParam')


@dataclasses.dataclass
class RetentionBackupSLAParam:
    """Implementation of the 'RetentionBackupSLAParam' model.

        The retention time for this SLA. For example, to retain the backup for 1 month,
        set `unit="months"` and `value=1`.

        Attributes:
            Unit:
    The measurement unit of the sla parameter.

            Value:
    The measurement value of the sla parameter.

    """

    Unit: str | None = None
    Value: int | None = None

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
        val = dictionary.get('unit', None)
        val_unit = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_unit,
            val_value,
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
