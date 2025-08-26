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
        etag: str | None = None,
        links: management_group_links_.ManagementGroupLinks | None = None,
        backup_across_subgroups: bool | None = None,
        p_id: str | None = None,
        name: str | None = None,
        p_type: str | None = None,
        vcenter_id: str | None = None,
    ) -> None:
        """Constructor for the ReadManagementGroupResponse class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: management_group_links_.ManagementGroupLinks | None = links
        self.backup_across_subgroups: bool | None = backup_across_subgroups
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.p_type: str | None = p_type
        self.vcenter_id: str | None = vcenter_id

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = management_group_links_.ManagementGroupLinks.from_dictionary(val)

        val = dictionary.get('backup_across_subgroups', None)
        val_backup_across_subgroups = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('vcenter_id', None)
        val_vcenter_id = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_backup_across_subgroups,
            val_p_id,
            val_name,
            val_p_type,
            val_vcenter_id,
        )
