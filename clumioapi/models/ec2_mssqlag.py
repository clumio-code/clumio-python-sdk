#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssqlag_embedded as ec2_mssqlag_embedded_
from clumioapi.models import ec2_mssqlag_links as ec2_mssqlag_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='EC2MSSQLAG')


@dataclasses.dataclass
class EC2MSSQLAG:
    """Implementation of the 'EC2MSSQLAG' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Id:
            The clumio-assigned id of the availability group.

        Name:
            The microsoft sql-assigned name of the availability group.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the availability group.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not protected, then this field has a value of `null`.

        Status:
            The status of the availability group, possible values include 'active' and 'inactive'.

    """

    Embedded: ec2_mssqlag_embedded_.EC2MSSQLAGEmbedded | None = None
    Links: ec2_mssqlag_links_.EC2MSSQLAGLinks | None = None
    Id: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    Status: str | None = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = ec2_mssqlag_embedded_.EC2MSSQLAGEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_mssqlag_links_.EC2MSSQLAGLinks.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_id,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_status,
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
