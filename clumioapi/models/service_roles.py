#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_service_roles
from clumioapi.models import s3_service_roles

T = TypeVar('T', bound='ServiceRoles')


class ServiceRoles:
    """Implementation of the 'ServiceRoles' model.

    Attributes:
        mssql:

        s3:

    """

    # Create a mapping from Model property names to API property names
    _names = {'mssql': 'mssql', 's3': 's3'}

    def __init__(
        self,
        mssql: mssql_service_roles.MssqlServiceRoles = None,
        s3: s3_service_roles.S3ServiceRoles = None,
    ) -> None:
        """Constructor for the ServiceRoles class."""

        # Initialize members of the class
        self.mssql: mssql_service_roles.MssqlServiceRoles = mssql
        self.s3: s3_service_roles.S3ServiceRoles = s3

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
            mssql_service_roles.MssqlServiceRoles.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 's3'
        s3 = (
            s3_service_roles.S3ServiceRoles.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(mssql, s3)
