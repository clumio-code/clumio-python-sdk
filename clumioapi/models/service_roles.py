#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_service_roles as mssql_service_roles_
from clumioapi.models import s3_service_roles as s3_service_roles_

T = TypeVar('T', bound='ServiceRoles')


class ServiceRoles:
    """Implementation of the 'ServiceRoles' model.

    Attributes:
        mssql:

        s3:

    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'mssql': 'mssql', 's3': 's3'}

    def __init__(
        self,
        mssql: mssql_service_roles_.MssqlServiceRoles | None = None,
        s3: s3_service_roles_.S3ServiceRoles | None = None,
    ) -> None:
        """Constructor for the ServiceRoles class."""

        # Initialize members of the class
        self.mssql: mssql_service_roles_.MssqlServiceRoles | None = mssql
        self.s3: s3_service_roles_.S3ServiceRoles | None = s3

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
        val_mssql = mssql_service_roles_.MssqlServiceRoles.from_dictionary(val)

        val = dictionary.get('s3', None)
        val_s3 = s3_service_roles_.S3ServiceRoles.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_mssql,
            val_s3,
        )
