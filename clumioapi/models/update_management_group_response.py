#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import management_group_links

T = TypeVar('T', bound='UpdateManagementGroupResponse')


class UpdateManagementGroupResponse:
    """Implementation of the 'UpdateManagementGroupResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the management group.
        name:
            The name of the management group.
        p_type:
            The type of the management group. Possible values include `on_prem`.
        vcenter_id:
            The Clumio-assigned ID of the vCenter server associated with the management
            group.
            All management groups are associated with a vCenter server.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'p_id': 'id',
        'name': 'name',
        'p_type': 'type',
        'vcenter_id': 'vcenter_id',
    }

    def __init__(
        self,
        links: management_group_links.ManagementGroupLinks = None,
        p_id: str = None,
        name: str = None,
        p_type: str = None,
        vcenter_id: str = None,
    ) -> None:
        """Constructor for the UpdateManagementGroupResponse class."""

        # Initialize members of the class
        self.links: management_group_links.ManagementGroupLinks = links
        self.p_id: str = p_id
        self.name: str = name
        self.p_type: str = p_type
        self.vcenter_id: str = vcenter_id

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
        key = '_links'
        links = (
            management_group_links.ManagementGroupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        name = dictionary.get('name')
        p_type = dictionary.get('type')
        vcenter_id = dictionary.get('vcenter_id')
        # Return an object of this model
        return cls(links, p_id, name, p_type, vcenter_id)
