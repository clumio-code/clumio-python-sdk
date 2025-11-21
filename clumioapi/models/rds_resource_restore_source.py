#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    rds_resource_restore_source_air_gap_options as rds_resource_restore_source_air_gap_options_
from clumioapi.models import \
    rds_resource_restore_source_pitr_options as rds_resource_restore_source_pitr_options_
import requests

T = TypeVar('T', bound='RdsResourceRestoreSource')


@dataclasses.dataclass
class RdsResourceRestoreSource:
    """Implementation of the 'RdsResourceRestoreSource' model.

    The RDS resource backup or snapshot to be restored.  Only one of these fields
    should be set.

    Attributes:
        Backup:
            The parameters for initiating an rds restore from a backup.

        Snapshot:
            The parameters for initiating an rds restore from a snapshot.

    """

    Backup: (
        rds_resource_restore_source_air_gap_options_.RdsResourceRestoreSourceAirGapOptions | None
    ) = None
    Snapshot: (
        rds_resource_restore_source_pitr_options_.RdsResourceRestoreSourcePitrOptions | None
    ) = None

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
        val = dictionary.get('backup', None)
        val_backup = rds_resource_restore_source_air_gap_options_.RdsResourceRestoreSourceAirGapOptions.from_dictionary(
            val
        )

        val = dictionary.get('snapshot', None)
        val_snapshot = rds_resource_restore_source_pitr_options_.RdsResourceRestoreSourcePitrOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_backup,
            val_snapshot,
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
