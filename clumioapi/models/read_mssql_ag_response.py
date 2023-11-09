#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_ag_embedded
from clumioapi.models import mssql_ag_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='ReadMssqlAGResponse')


class ReadMssqlAGResponse:
    """Implementation of the 'ReadMssqlAGResponse' model.

    Attributes:
        embedded:
            MssqlAGEmbedded is embed of MSSQL Availability Groups
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the availability group.
        name:
            The Microsoft SQL-assigned name of the availability group.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            availability group.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        status:
            The status of the availability group, Possible values include 'active' and
            'inactive'.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'status': 'status',
    }

    def __init__(
        self,
        embedded: mssql_ag_embedded.MssqlAGEmbedded = None,
        links: mssql_ag_links.MssqlAGLinks = None,
        p_id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        status: str = None,
    ) -> None:
        """Constructor for the ReadMssqlAGResponse class."""

        # Initialize members of the class
        self.embedded: mssql_ag_embedded.MssqlAGEmbedded = embedded
        self.links: mssql_ag_links.MssqlAGLinks = links
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
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
            mssql_ag_embedded.MssqlAGEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            mssql_ag_links.MssqlAGLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        status = dictionary.get('status')
        # Return an object of this model
        return cls(embedded, links, p_id, name, organizational_unit_id, p_protection_info, status)
