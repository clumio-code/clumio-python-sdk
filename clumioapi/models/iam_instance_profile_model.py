#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='IamInstanceProfileModel')


@dataclasses.dataclass
class IamInstanceProfileModel:
    """Implementation of the 'IamInstanceProfileModel' model.

    Denotes an IAM instance profile. An instance profile is a container for anIAM
    role that you can use to pass role information to an EC2 instance whenthe
    instance starts.

    Attributes:
        Arn:
            The amazon resource name (arn) specifying the iam instance profile.

        Name:
            The aws-assigned name of the iam instance profile.

        NativeId:
            The aws-assigned id of the iam instance profile.

    """

    Arn: str | None = None
    Name: str | None = None
    NativeId: str | None = None

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
        val = dictionary.get('arn', None)
        val_arn = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('native_id', None)
        val_native_id = val

        # Return an object of this model
        return cls(
            val_arn,
            val_name,
            val_native_id,
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
