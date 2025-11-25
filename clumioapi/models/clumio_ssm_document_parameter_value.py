#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ClumioSsmDocumentParameterValue')


@dataclasses.dataclass
class ClumioSsmDocumentParameterValue:
    """Implementation of the 'ClumioSsmDocumentParameterValue' model.

    Details for each parameters of the ssm document

    Attributes:
        Allowedpattern:
            "allowedpattern" refers to the pattern that must be satisfied by the parameter.

        Default:
            "default" refers to the default value for that parameter.

        Description:
            "description" is optional.

        Type:
            "type" refers to the parameter type.

    """

    Allowedpattern: str | None = None
    Default: str | None = None
    Description: str | None = None
    Type: str | None = None

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
        val = dictionary.get('allowedPattern', None)
        val_allowedPattern = val

        val = dictionary.get('default', None)
        val_default = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_allowedPattern,
            val_default,
            val_description,
            val_type,
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
