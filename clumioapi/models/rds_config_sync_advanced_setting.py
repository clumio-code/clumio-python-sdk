#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RDSConfigSyncAdvancedSetting')


class RDSConfigSyncAdvancedSetting:
    """Implementation of the 'RDSConfigSyncAdvancedSetting' model.

    Advanced settings for RDS PITR configuration sync.

    Attributes:
        apply:
            Syncs the configuration of RDS PITR in AWS. Valid values are: `immediate`, and
            `maintenance_window`.
            Note that applying the setting "immediately" may cause unexpected downtime.
    """

    # Create a mapping from Model property names to API property names
    _names = {'apply': 'apply'}

    def __init__(self, apply: str = None) -> None:
        """Constructor for the RDSConfigSyncAdvancedSetting class."""

        # Initialize members of the class
        self.apply: str = apply

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
        apply = dictionary.get('apply')
        # Return an object of this model
        return cls(apply)
