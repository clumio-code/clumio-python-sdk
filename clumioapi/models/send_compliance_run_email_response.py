#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import compliance_run_hateoas_links as compliance_run_hateoas_links_
import requests

T = TypeVar('T', bound='SendComplianceRunEmailResponse')


@dataclasses.dataclass
class SendComplianceRunEmailResponse:
    """Implementation of the 'SendComplianceRunEmailResponse' model.

        Attributes:
            Embedded:
    Embedded responses related to the resource.

            Links:
    Urls to pages related to the resource.

    """

    Embedded: object | None = None
    Links: compliance_run_hateoas_links_.ComplianceRunHateoasLinks | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = compliance_run_hateoas_links_.ComplianceRunHateoasLinks.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
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
