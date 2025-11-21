#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RPOBackupSLAParam')


@dataclasses.dataclass
class RPOBackupSLAParam:
    """Implementation of the 'RPOBackupSLAParam' model.

    The minimum frequency between backups for this SLA. Also known as the recovery
    point objective (RPO) interval.For example, to configure the minimum frequency
    between backups to be every 2 days, set `unit="days"` and `value=2`.To configure
    the SLA for on-demand backups, set `unit="on_demand"` and leave the `value`
    field empty.

    Attributes:
        Offsets:
            The weekday in decimal of the weekly sla parameter. valid values are integers
            from 0 to 6, indicates sunday, monday, ..., saturday. for example, to configure
            backup on every monday, set `unit="weekly"`, `value=1`, and `offsets={1}`.

        Unit:
            The measurement unit of the sla parameter.

        Value:
            The measurement value of the sla parameter.

    """

    Offsets: Sequence[int] | None = None
    Unit: str | None = None
    Value: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('offsets', None)
        val_offsets = val

        val = dictionary.get('unit', None)
        val_unit = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_offsets,
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
