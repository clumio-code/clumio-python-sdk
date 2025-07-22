#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssqlfci_embedded as ec2_mssqlfci_embedded_
from clumioapi.models import ec2_mssqlfci_links as ec2_mssqlfci_links_
from clumioapi.models import protection_info as protection_info_

T = TypeVar('T', bound='EC2MSSQLFCI')


class EC2MSSQLFCI:
    """Implementation of the 'EC2MSSQLFCI' model.

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
        embedded: ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded,
        links: ec2_mssqlfci_links_.EC2MSSQLFCILinks,
        p_id: str,
        name: str,
        organizational_unit_id: str,
        protection_info: protection_info_.ProtectionInfo,
        protection_status: str,
        status: str,
    ) -> None:
        """Constructor for the EC2MSSQLFCI class."""

        # Initialize members of the class
        self.embedded: ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded = embedded
        self.links: ec2_mssqlfci_links_.EC2MSSQLFCILinks = links
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.status: str = status

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = ec2_mssqlfci_embedded_.EC2MSSQLFCIEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = ec2_mssqlfci_links_.EC2MSSQLFCILinks.from_dictionary(val)

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary['protection_status']
        val_protection_status = val

        val = dictionary['status']
        val_status = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_protection_status,  # type: ignore
            val_status,  # type: ignore
        )
