#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssqlfci_embedded
from clumioapi.models import ec2_mssqlfci_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='EC2MSSQLFCI')


class EC2MSSQLFCI:
    """Implementation of the 'EC2MSSQLFCI' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        compliance_status:
            ComplianceStatus of the resource
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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'compliance_status': 'compliance_status',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: ec2_mssqlfci_embedded.EC2MSSQLFCIEmbedded = None,
        links: ec2_mssqlfci_links.EC2MSSQLFCILinks = None,
        compliance_status: str = None,
        p_id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
        status: str = None,
    ) -> None:
        """Constructor for the EC2MSSQLFCI class."""

        # Initialize members of the class
        self.embedded: ec2_mssqlfci_embedded.EC2MSSQLFCIEmbedded = embedded
        self.links: ec2_mssqlfci_links.EC2MSSQLFCILinks = links
        self.compliance_status: str = compliance_status
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.status: str = status

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        key = '_embedded'
        embedded = (
            ec2_mssqlfci_embedded.EC2MSSQLFCIEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            ec2_mssqlfci_links.EC2MSSQLFCILinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        compliance_status = dictionary.get('compliance_status')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        status = dictionary.get('status')
        # Return an object of this model
        return cls(
            embedded,
            links,
            compliance_status,
            p_id,
            name,
            organizational_unit_id,
            p_protection_info,
            protection_status,
            status,
        )
