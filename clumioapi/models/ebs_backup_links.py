#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='EBSBackupLinks')


@dataclasses.dataclass
class EBSBackupLinks:
    """Implementation of the 'EBSBackupLinks' model.

        URLs to pages related to the resource.

        Attributes:
            Self:
    The hateoas link to this resource.

            RestoreAwsEbsVolume:
    A resource-specific hateoas link.

    """

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    RestoreAwsEbsVolume: hateoas_link_.HateoasLink | None = None

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
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('restore-aws-ebs-volume', None)
        val_restore_aws_ebs_volume = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_restore_aws_ebs_volume,
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
