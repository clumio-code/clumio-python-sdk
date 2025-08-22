#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_service_instance_profiles as mssql_service_instance_profiles_

T = TypeVar('T', bound='ServiceInstanceProfiles')


class ServiceInstanceProfiles:
    """Implementation of the 'ServiceInstanceProfiles' model.

    Attributes:
        mssql:

    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'mssql': 'mssql'}

    def __init__(
        self, mssql: mssql_service_instance_profiles_.MssqlServiceInstanceProfiles | None = None
    ) -> None:
        """Constructor for the ServiceInstanceProfiles class."""

        # Initialize members of the class
        self.mssql: mssql_service_instance_profiles_.MssqlServiceInstanceProfiles | None = mssql

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
        val = dictionary.get('mssql', None)
        val_mssql = mssql_service_instance_profiles_.MssqlServiceInstanceProfiles.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_mssql,
        )
