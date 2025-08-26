#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='PolicyEmbedded')


@dataclasses.dataclass
class PolicyEmbedded:
    """Implementation of the 'PolicyEmbedded' model.

    If the `embed` query parameter is set, displays the responses of the related
    resource,as defined by the embeddable link specified.

    Attributes:
        ReadPolicyAwsEbsVolumesProtectionStats:
            Embeds the ebs protection statistics into the response.

    """

    ReadPolicyAwsEbsVolumesProtectionStats: object | None = None

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
        val = dictionary.get('read-policy-aws-ebs-volumes-protection-stats', None)
        val_read_policy_aws_ebs_volumes_protection_stats = val

        # Return an object of this model
        return cls(
            val_read_policy_aws_ebs_volumes_protection_stats,
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
