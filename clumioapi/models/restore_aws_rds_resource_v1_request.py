#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import rds_resource_restore_source as rds_resource_restore_source_
from clumioapi.models import rds_resource_restore_target as rds_resource_restore_target_

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
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: rds_resource_restore_source_.RdsResourceRestoreSource | None = None,
        target: rds_resource_restore_target_.RdsResourceRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreAwsRdsResourceV1Request class."""

        # Initialize members of the class
        self.source: rds_resource_restore_source_.RdsResourceRestoreSource | None = source
        self.target: rds_resource_restore_target_.RdsResourceRestoreTarget | None = target

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
        val_source = rds_resource_restore_source_.RdsResourceRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = rds_resource_restore_target_.RdsResourceRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
