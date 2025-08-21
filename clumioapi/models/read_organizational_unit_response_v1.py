#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_embedded as entity_group_embedded_
from clumioapi.models import organizational_unit_links as organizational_unit_links_

T = TypeVar('T', bound='ReadOrganizationalUnitResponseV1')


class ReadOrganizationalUnitResponseV1:
    """Implementation of the 'ReadOrganizationalUnitResponseV1' model.

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
        embedded: entity_group_embedded_.EntityGroupEmbedded | None = None,
        etag: str | None = None,
        links: organizational_unit_links_.OrganizationalUnitLinks | None = None,
        children_count: int | None = None,
        configured_datasource_types: Sequence[str] | None = None,
        descendant_ids: Sequence[str] | None = None,
        description: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        parent_id: str | None = None,
        task_id: str | None = None,
        user_count: int | None = None,
        users: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the ReadOrganizationalUnitResponseV1 class."""

        # Initialize members of the class
        self.embedded: entity_group_embedded_.EntityGroupEmbedded | None = embedded
        self.etag: str | None = etag
        self.links: organizational_unit_links_.OrganizationalUnitLinks | None = links
        self.children_count: int | None = children_count
        self.configured_datasource_types: Sequence[str] | None = configured_datasource_types
        self.descendant_ids: Sequence[str] | None = descendant_ids
        self.description: str | None = description
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.parent_id: str | None = parent_id
        self.task_id: str | None = task_id
        self.user_count: int | None = user_count
        self.users: Sequence[str] | None = users

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
        val_embedded = entity_group_embedded_.EntityGroupEmbedded.from_dictionary(val)

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = organizational_unit_links_.OrganizationalUnitLinks.from_dictionary(val)

        val = dictionary.get('children_count', None)
        val_children_count = val

        val = dictionary.get('configured_datasource_types', None)
        val_configured_datasource_types = val

        val = dictionary.get('descendant_ids', None)
        val_descendant_ids = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('parent_id', None)
        val_parent_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        val = dictionary.get('user_count', None)
        val_user_count = val

        val = dictionary.get('users', None)
        val_users = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_children_count,
            val_configured_datasource_types,
            val_descendant_ids,
            val_description,
            val_p_id,
            val_name,
            val_parent_id,
            val_task_id,
            val_user_count,
            val_users,
        )
