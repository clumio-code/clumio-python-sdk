#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_embedded as entity_group_embedded_
from clumioapi.models import organizational_unit_links as organizational_unit_links_

T = TypeVar('T', bound='OrganizationalUnitWithETagV1')


class OrganizationalUnitWithETagV1:
    """Implementation of the 'OrganizationalUnitWithETagV1' model.

    OrganizationalUnitWithETagV1 to support etag string to be calculated

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            ETag value
        links:
            URLs to pages related to the resource.
        children_count:
            Number of immediate children of the organizational unit.
        configured_datasource_types:
            Datasource types configured in this organizational unit. Possible values include
            `aws`, `microsoft365`, `vmware`, or `mssql`.
        descendant_ids:
            List of all recursive descendant organizational units of this OU.
        description:
            A description of the organizational unit.
        p_id:
            The Clumio assigned ID of the organizational unit.
        name:
            Unique name assigned to the organizational unit.
        parent_id:
            The Clumio assigned ID of the parent organizational unit.
            The parent organizational unit contains the entities in this organizational unit
            and can update this organizational unit.
            If this organizational unit is the global organizational unit, then this field
            has a value of `null`.
        task_id:
            The Clumio-assigned ID of the task associated with this organizational unit.
            The progress of the task can be monitored using the
            [GET /tasks/{task_id}](#operation/read-task) endpoint.
        user_count:
            Number of users to whom this organizational unit or any of its descendants have
            been assigned.
        users:
            Users IDs to whom the organizational unit has been assigned.
            This attribute will be available when reading a single OU and not when listing
            OUs.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'children_count': 'children_count',
        'configured_datasource_types': 'configured_datasource_types',
        'descendant_ids': 'descendant_ids',
        'description': 'description',
        'p_id': 'id',
        'name': 'name',
        'parent_id': 'parent_id',
        'task_id': 'task_id',
        'user_count': 'user_count',
        'users': 'users',
    }

    def __init__(
        self,
        embedded: entity_group_embedded_.EntityGroupEmbedded,
        etag: str,
        links: organizational_unit_links_.OrganizationalUnitLinks,
        children_count: int,
        configured_datasource_types: Sequence[str],
        descendant_ids: Sequence[str],
        description: str,
        p_id: str,
        name: str,
        parent_id: str,
        task_id: str,
        user_count: int,
        users: Sequence[str],
    ) -> None:
        """Constructor for the OrganizationalUnitWithETagV1 class."""

        # Initialize members of the class
        self.embedded: entity_group_embedded_.EntityGroupEmbedded = embedded
        self.etag: str = etag
        self.links: organizational_unit_links_.OrganizationalUnitLinks = links
        self.children_count: int = children_count
        self.configured_datasource_types: Sequence[str] = configured_datasource_types
        self.descendant_ids: Sequence[str] = descendant_ids
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name
        self.parent_id: str = parent_id
        self.task_id: str = task_id
        self.user_count: int = user_count
        self.users: Sequence[str] = users

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
        val_embedded = entity_group_embedded_.EntityGroupEmbedded.from_dictionary(val)

        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = organizational_unit_links_.OrganizationalUnitLinks.from_dictionary(val)

        val = dictionary['children_count']
        val_children_count = val

        val = dictionary['configured_datasource_types']
        val_configured_datasource_types = val

        val = dictionary['descendant_ids']
        val_descendant_ids = val

        val = dictionary['description']
        val_description = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['parent_id']
        val_parent_id = val

        val = dictionary['task_id']
        val_task_id = val

        val = dictionary['user_count']
        val_user_count = val

        val = dictionary['users']
        val_users = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_children_count,  # type: ignore
            val_configured_datasource_types,  # type: ignore
            val_descendant_ids,  # type: ignore
            val_description,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_parent_id,  # type: ignore
            val_task_id,  # type: ignore
            val_user_count,  # type: ignore
            val_users,  # type: ignore
        )
