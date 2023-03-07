#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import cloud_connector_count_by_status
from clumioapi.models import subgroup_links

T = TypeVar('T', bound='Subgroup')


class Subgroup:
    """Implementation of the 'Subgroup' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        cloud_connector_count_by_status:
            The number of cloud connectors in this subgroup, aggregated by their status.
        cloud_connector_status:
            The overall health of cloud connectors in this subgroup. Possible values
            include: 'healthy', indicating
            that all cloud connectors in the subgroup are connected; 'degraded' indicating
            that one or more cloud
            connectors in the subgroup have connection issues; `none`, indicating that no
            cloud connectors are in the subgroup.
        group_id:
            The Clumio-assigned ID of the management group associated with this subgroup.
        p_id:
            The Clumio-assigned ID of the management subgroup.
        name:
            The name of the management subgroup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'cloud_connector_count_by_status': 'cloud_connector_count_by_status',
        'cloud_connector_status': 'cloud_connector_status',
        'group_id': 'group_id',
        'p_id': 'id',
        'name': 'name',
    }

    def __init__(
        self,
        links: subgroup_links.SubgroupLinks = None,
        cloud_connector_count_by_status: cloud_connector_count_by_status.CloudConnectorCountByStatus = None,
        cloud_connector_status: str = None,
        group_id: str = None,
        p_id: str = None,
        name: str = None,
    ) -> None:
        """Constructor for the Subgroup class."""

        # Initialize members of the class
        self.links: subgroup_links.SubgroupLinks = links
        self.cloud_connector_count_by_status: cloud_connector_count_by_status.CloudConnectorCountByStatus = (
            cloud_connector_count_by_status
        )
        self.cloud_connector_status: str = cloud_connector_status
        self.group_id: str = group_id
        self.p_id: str = p_id
        self.name: str = name

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
            subgroup_links.SubgroupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'cloud_connector_count_by_status'
        p_cloud_connector_count_by_status = (
            cloud_connector_count_by_status.CloudConnectorCountByStatus.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        cloud_connector_status = dictionary.get('cloud_connector_status')
        group_id = dictionary.get('group_id')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(
            links, p_cloud_connector_count_by_status, cloud_connector_status, group_id, p_id, name
        )
