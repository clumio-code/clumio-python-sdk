#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_resource_restore_source
from clumioapi.models import rds_resource_restore_target

T = TypeVar('T', bound='RestoreAwsRdsResourceV1Request')


class RestoreAwsRdsResourceV1Request:
    """Implementation of the 'RestoreAwsRdsResourceV1Request' model.

    Attributes:
        source:
            The RDS resource backup or snapshot to be restored.  Only one of these fields
            should be set.
        target:
            The configuration of the RDS resource to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: rds_resource_restore_source.RdsResourceRestoreSource = None,
        target: rds_resource_restore_target.RdsResourceRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreAwsRdsResourceV1Request class."""

        # Initialize members of the class
        self.source: rds_resource_restore_source.RdsResourceRestoreSource = source
        self.target: rds_resource_restore_target.RdsResourceRestoreTarget = target

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
            rds_resource_restore_source.RdsResourceRestoreSource.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            rds_resource_restore_target.RdsResourceRestoreTarget.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
