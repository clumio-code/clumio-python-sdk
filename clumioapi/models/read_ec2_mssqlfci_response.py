#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssqlfci_embedded as ec2_mssqlfci_embedded_
from clumioapi.models import ec2_mssqlfci_links as ec2_mssqlfci_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='ReadEC2MSSQLFCIResponse')


@dataclasses.dataclass
class ReadEC2MSSQLFCIResponse:
    """Implementation of the 'ReadEC2MSSQLFCIResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Id:
            The clumio-assigned id of the failover cluster.

        Name:
            The microsoft sql-assigned name of the failover cluster.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the fci.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not protected, then this field has a value of `null`.

        ProtectionStatus:
            Protectionstatus of the fci.

        Status:
            The status of the fci, possible values include 'active' and 'inactive'.

    """

    Embedded: ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded | None = None
    Links: ec2_mssqlfci_links_.EC2MSSQLFCILinks | None = None
    Id: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    ProtectionStatus: str | None = None
    Status: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val_embedded = ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_mssqlfci_links_.EC2MSSQLFCILinks.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

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
            val_protection_status,
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
        model_instance.raw_response = response
        return model_instance
