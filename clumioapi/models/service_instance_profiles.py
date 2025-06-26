#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_service_instance_profiles

T = TypeVar('T', bound='ServiceInstanceProfiles')


class ServiceInstanceProfiles:
    """Implementation of the 'ServiceInstanceProfiles' model.

    Attributes:
        mssql:

    """

    # Create a mapping from Model property names to API property names
    _names = {'mssql': 'mssql'}

    def __init__(
        self, mssql: mssql_service_instance_profiles.MssqlServiceInstanceProfiles = None
    ) -> None:
        """Constructor for the ServiceInstanceProfiles class."""

        # Initialize members of the class
        self.mssql: mssql_service_instance_profiles.MssqlServiceInstanceProfiles = mssql

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
        key = 'mssql'
        mssql = (
            mssql_service_instance_profiles.MssqlServiceInstanceProfiles.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(mssql)
