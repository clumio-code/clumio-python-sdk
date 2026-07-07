#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
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

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Allowedpattern': 'allowedPattern',
    }

    Allowedpattern: str | None = None
    Default: str | None = None
    Description: str | None = None
    Type: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
