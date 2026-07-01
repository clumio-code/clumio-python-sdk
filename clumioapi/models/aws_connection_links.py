#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='AWSConnectionLinks')


@dataclasses.dataclass
class AWSConnectionLinks:
    """Implementation of the 'AWSConnectionLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        CreatePolicyRule:
            A resource-specific hateoas link.

        CreateProtectionGroup:
            A resource-specific hateoas link.

        DeleteConnectionAws:
            A resource-specific hateoas link.

        ReadOrganizationalUnit:
            A resource-specific hateoas link.

        UpdateConnectionAws:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'CreatePolicyRule': 'create-policy-rule',
        'CreateProtectionGroup': 'create-protection-group',
        'DeleteConnectionAws': 'delete-connection-aws',
        'ReadOrganizationalUnit': 'read-organizational-unit',
        'UpdateConnectionAws': 'update-connection-aws',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    CreatePolicyRule: hateoas_link_.HateoasLink | None = None
    CreateProtectionGroup: hateoas_link_.HateoasLink | None = None
    DeleteConnectionAws: hateoas_link_.HateoasLink | None = None
    ReadOrganizationalUnit: hateoas_link_.HateoasLink | None = None
    UpdateConnectionAws: hateoas_link_.HateoasLink | None = None

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
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('create-policy-rule', None)
        val_create_policy_rule = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('create-protection-group', None)
        val_create_protection_group = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('delete-connection-aws', None)
        val_delete_connection_aws = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('read-organizational-unit', None)
        val_read_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('update-connection-aws', None)
        val_update_connection_aws = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_create_policy_rule,
            val_create_protection_group,
            val_delete_connection_aws,
            val_read_organizational_unit,
            val_update_connection_aws,
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
