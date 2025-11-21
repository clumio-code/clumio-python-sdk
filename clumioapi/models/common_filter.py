#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CommonFilter')


@dataclasses.dataclass
class CommonFilter:
    """Implementation of the 'CommonFilter' model.

    The common filter which will be applied to all controls.

    Attributes:
        AssetTypes:
            The asset types to be included in the report.
            for example, ["aws_ec2_instance", "microsoft365_drive"].

        DataSources:
            The data sources to be included in the report. possible values include `aws`,
            `microsoft365` or `vmware`.

        OrganizationalUnits:
            The organizational units to be included in the report.

    """

    AssetTypes: Sequence[str] | None = None
    DataSources: Sequence[str] | None = None
    OrganizationalUnits: Sequence[str] | None = None

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
