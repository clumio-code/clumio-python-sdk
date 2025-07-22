#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import management_group_links as management_group_links_

T = TypeVar('T', bound='ReadManagementGroupResponse')


class ReadManagementGroupResponse:
    """Implementation of the 'ReadManagementGroupResponse' model.

    Attributes:
        etag:
            Etag
        links:
            URLs to pages related to the resource.
        backup_across_subgroups:
            Determines whether backups are allowed to occur across different subgroups or
            cloud connectors.
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
    _names: dict[str, str] = {
        'etag': '_etag',
        'links': '_links',
        'backup_across_subgroups': 'backup_across_subgroups',
        'p_id': 'id',
        'name': 'name',
        'p_type': 'type',
        'vcenter_id': 'vcenter_id',
    }

    def __init__(
        self,
        etag: str,
        links: management_group_links_.ManagementGroupLinks,
        backup_across_subgroups: bool,
        p_id: str,
        name: str,
        p_type: str,
        vcenter_id: str,
    ) -> None:
        """Constructor for the ReadManagementGroupResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: management_group_links_.ManagementGroupLinks = links
        self.backup_across_subgroups: bool = backup_across_subgroups
        self.p_id: str = p_id
        self.name: str = name
        self.p_type: str = p_type
        self.vcenter_id: str = vcenter_id

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
        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = management_group_links_.ManagementGroupLinks.from_dictionary(val)

        val = dictionary['backup_across_subgroups']
        val_backup_across_subgroups = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['vcenter_id']
        val_vcenter_id = val

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_backup_across_subgroups,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_p_type,  # type: ignore
            val_vcenter_id,  # type: ignore
        )
