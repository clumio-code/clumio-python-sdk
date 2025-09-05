#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import protect_entities_hateoas_link as protect_entities_hateoas_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_
from clumioapi.models import unprotect_entities_hateoas_link as unprotect_entities_hateoas_link_
import requests

T = TypeVar('T', bound='AwsTagLinks')


@dataclasses.dataclass
class AwsTagLinks:
    """Implementation of the 'AwsTagLinks' model.

        URLs to pages related to the resource.

        Attributes:
            Self:
    The hateoas link to this resource.

            ProtectEntities:
    A hateoas link to protect the entities.

            ReadAwsEnvironmentTagEbsVolumesProtectionStats:
    A resource-specific hateoas link.

            ReadPolicyDefinition:
    A hateoas link to the policy protecting this resource. will be omitted for unprotected entities.

            UnprotectEntities:
    A hateoas link to unprotect the entities.

    """

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    ProtectEntities: protect_entities_hateoas_link_.ProtectEntitiesHateoasLink | None = None
    ReadAwsEnvironmentTagEbsVolumesProtectionStats: hateoas_link_.HateoasLink | None = None
    ReadPolicyDefinition: (
        read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink | None
    ) = None
    UnprotectEntities: unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink | None = None

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

        val = dictionary.get('protect-entities', None)
        val_protect_entities = (
            protect_entities_hateoas_link_.ProtectEntitiesHateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-aws-environment-tag-ebs-volumes-protection-stats', None)
        val_read_aws_environment_tag_ebs_volumes_protection_stats = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary.get('unprotect-entities', None)
        val_unprotect_entities = (
            unprotect_entities_hateoas_link_.UnprotectEntitiesHateoasLink.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_self,
            val_protect_entities,
            val_read_aws_environment_tag_ebs_volumes_protection_stats,
            val_read_policy_definition,
            val_unprotect_entities,
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
