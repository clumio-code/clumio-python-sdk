#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import grr_source
from clumioapi.models import grr_target

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
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self, source: grr_source.GrrSource = None, target: grr_target.GrrTarget = None
    ) -> None:
        """Constructor for the RestoreRdsRecordV1Request class."""

        # Initialize members of the class
        self.source: grr_source.GrrSource = source
        self.target: grr_target.GrrTarget = target

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        key = 'source'
        source = (
            grr_source.GrrSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            grr_target.GrrTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
