#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import grr_source as grr_source_
from clumioapi.models import grr_target as grr_target_

T = TypeVar('T', bound='RestoreRdsRecordV1Request')


class RestoreRdsRecordV1Request:
    """Implementation of the 'RestoreRdsRecordV1Request' model.

    Attributes:
        source:
            The RDS database backup to be queried.
        target:
            The query to perform on the source RDS database.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: grr_source_.GrrSource | None = None,
        target: grr_target_.GrrTarget | None = None,
    ) -> None:
        """Constructor for the RestoreRdsRecordV1Request class."""

        # Initialize members of the class
        self.source: grr_source_.GrrSource | None = source
        self.target: grr_target_.GrrTarget | None = target

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
        val = dictionary.get('source', None)
        val_source = grr_source_.GrrSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = grr_target_.GrrTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
