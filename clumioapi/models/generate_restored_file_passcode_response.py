#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    generate_restored_file_passcode_links as generate_restored_file_passcode_links_
import requests

T = TypeVar('T', bound='GenerateRestoredFilePasscodeResponse')


@dataclasses.dataclass
class GenerateRestoredFilePasscodeResponse:
    """Implementation of the 'GenerateRestoredFilePasscodeResponse' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        Passcode:
            The new passcode that has been generated for the restored file. send the
            passcode to the email recipient, who must use it to access the restored file.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: generate_restored_file_passcode_links_.GenerateRestoredFilePasscodeLinks | None = None
    Passcode: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = generate_restored_file_passcode_links_.GenerateRestoredFilePasscodeLinks.from_dictionary(
            val
        )

        val = dictionary.get('passcode', None)
        val_passcode = val

        # Return an object of this model
        return cls(
            val_links,
            val_passcode,
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
        model_instance.raw_response = response
        return model_instance
