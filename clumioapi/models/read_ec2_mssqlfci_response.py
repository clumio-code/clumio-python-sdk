#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssqlfci_embedded as ec2_mssqlfci_embedded_
from clumioapi.models import ec2_mssqlfci_links as ec2_mssqlfci_links_
from clumioapi.models import protection_info as protection_info_

T = TypeVar('T', bound='ReadEC2MSSQLFCIResponse')


class ReadEC2MSSQLFCIResponse:
    """Implementation of the 'ReadEC2MSSQLFCIResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the failover cluster.
        name:
            The Microsoft SQL-assigned name of the failover cluster.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the FCI.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            ProtectionStatus of the FCI
        status:
            The status of the FCI, Possible values include 'active' and 'inactive'.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded | None = None,
        links: ec2_mssqlfci_links_.EC2MSSQLFCILinks | None = None,
        p_id: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_.ProtectionInfo | None = None,
        protection_status: str | None = None,
        status: str | None = None,
    ) -> None:
        """Constructor for the ReadEC2MSSQLFCIResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded | None = embedded
        self.links: ec2_mssqlfci_links_.EC2MSSQLFCILinks | None = links
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo | None = protection_info
        self.protection_status: str | None = protection_status
        self.status: str | None = status

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
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
        val_p_id = val

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
            val_p_id,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_status,
        )
