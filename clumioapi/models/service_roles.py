#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import mssql_service_roles as mssql_service_roles_
from clumioapi.models import s3_service_roles as s3_service_roles_
import requests

T = TypeVar('T', bound='ServiceRoles')


@dataclasses.dataclass
class ServiceRoles:
    """Implementation of the 'ServiceRoles' model.

    Attributes:
        Mssql:
            .

        S3:
            .

    """

    Mssql: mssql_service_roles_.MssqlServiceRoles | None = None
    S3: s3_service_roles_.S3ServiceRoles | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
