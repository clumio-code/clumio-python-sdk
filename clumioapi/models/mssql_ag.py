#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_ag_embedded
from clumioapi.models import mssql_ag_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='MssqlAG')


class MssqlAG:
    """Implementation of the 'MssqlAG' model.

    Attributes:
        embedded:
            MssqlAGEmbedded is embed of MSSQL Availability Groups
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        id:
            The Clumio-assigned ID of the availability group.
        name:
            The Microsoft SQL-assigned name of the availability group.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            availability group.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
    }

    def __init__(
        self,
        embedded: mssql_ag_embedded.MssqlAGEmbedded = None,
        links: mssql_ag_links.MssqlAGLinks = None,
        id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
    ) -> None:
        """Constructor for the MssqlAG class."""

        # Initialize members of the class
        self.embedded: mssql_ag_embedded.MssqlAGEmbedded = embedded
        self.links: mssql_ag_links.MssqlAGLinks = links
        self.id: str = id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info

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

        id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links, id, name, organizational_unit_id, p_protection_info)
