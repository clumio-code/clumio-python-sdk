#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RdsInstanceModel')


@dataclasses.dataclass
class RdsInstanceModel:
    """Implementation of the 'RdsInstanceModel' model.

    Attributes:
        Class:
            The class of the rds instance at the time of backup. possible values include
            `db.r5.2xlarge` and `db.t2.small`.
            for a full list of possible values, refer to the amazon documentation at
            https://docs.aws.amazon.com/amazonrds/latest/userguide/concepts.dbinstanceclass.
            html.

        IsPubliclyAccessible:
            Determines whether the rds instance had a public ip address in addition to the
            private ip address at the time of backup.
            for more information about the public access option, refer to the amazon
            documentation at
            https://docs.aws.amazon.com/amazonrds/latest/userguide/user_vpc.workingwithrdsin
            stanceinavpc.html.

        Name:
            The aws-assigned name of the rds instance at the time of backup.

    """

    Class: str | None = None
    IsPubliclyAccessible: bool | None = None
    Name: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('class', None)
        val_class = val

        val = dictionary.get('is_publicly_accessible', None)
        val_is_publicly_accessible = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_class,
            val_is_publicly_accessible,
            val_name,
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
