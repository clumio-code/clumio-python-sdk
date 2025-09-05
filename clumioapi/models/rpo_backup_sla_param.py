#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RPOBackupSLAParam')


class RPOBackupSLAParam:
    """Implementation of the 'RPOBackupSLAParam' model.

    The minimum frequency between backups for this SLA. Also known as the recovery
    point objective (RPO) interval.For example, to configure the minimum frequency
    between backups to be every 2 days, set `unit="days"` and `value=2`.To configure
    the SLA for on-demand backups, set `unit="on_demand"` and leave the `value`
    field empty.

    Attributes:
        offsets:
            The weekday in decimal of the Weekly SLA parameter. Valid values are integers
            from 0 to 6, incidates Sunday, Monday, ..., Saturday. For example, to configure
            backup on every Monday, set `unit="weekly"`, `value=1`, and `offsets={1}`.
        unit:
            The measurement unit of the SLA parameter.
        value:
            The measurement value of the SLA parameter.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'offsets': 'offsets', 'unit': 'unit', 'value': 'value'}

    def __init__(
        self,
        offsets: Sequence[int] | None = None,
        unit: str | None = None,
        value: int | None = None,
    ) -> None:
        """Constructor for the RPOBackupSLAParam class."""

        # Initialize members of the class
        self.offsets: Sequence[int] | None = offsets
        self.unit: str | None = unit
        self.value: int | None = value

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
