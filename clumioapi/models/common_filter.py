#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CommonFilter')


class CommonFilter:
    """Implementation of the 'CommonFilter' model.

    The common filter which will be applied to all controls.

    Attributes:
        asset_types:
            The asset types to be included in the report.
            For example, ["aws_ec2_instance", "microsoft365_drive"].
        data_sources:
            The data sources to be included in the report. Possible values include `aws`,
            `microsoft365` or `vmware`.
        organizational_units:
            The organizational units to be included in the report.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types': 'asset_types',
        'data_sources': 'data_sources',
        'organizational_units': 'organizational_units',
    }

    def __init__(
        self,
        asset_types: Sequence[str] | None = None,
        data_sources: Sequence[str] | None = None,
        organizational_units: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the CommonFilter class."""

        # Initialize members of the class
        self.asset_types: Sequence[str] | None = asset_types
        self.data_sources: Sequence[str] | None = data_sources
        self.organizational_units: Sequence[str] | None = organizational_units

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
        val = dictionary.get('asset_types', None)
        val_asset_types = val

        val = dictionary.get('data_sources', None)
        val_data_sources = val

        val = dictionary.get('organizational_units', None)
        val_organizational_units = val

        # Return an object of this model
        return cls(
            val_asset_types,
            val_data_sources,
            val_organizational_units,
        )
