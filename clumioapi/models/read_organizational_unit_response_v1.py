#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_embedded
from clumioapi.models import organizational_unit_links

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
    _names = {
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
        embedded: entity_group_embedded.EntityGroupEmbedded = None,
        etag: str = None,
        links: organizational_unit_links.OrganizationalUnitLinks = None,
        children_count: int = None,
        configured_datasource_types: Sequence[str] = None,
        descendant_ids: Sequence[str] = None,
        description: str = None,
        p_id: str = None,
        name: str = None,
        parent_id: str = None,
        task_id: str = None,
        user_count: int = None,
        users: Sequence[str] = None,
    ) -> None:
        """Constructor for the ReadOrganizationalUnitResponseV1 class."""

        # Initialize members of the class
        self.embedded: entity_group_embedded.EntityGroupEmbedded = embedded
        self.etag: str = etag
        self.links: organizational_unit_links.OrganizationalUnitLinks = links
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
            entity_group_embedded.EntityGroupEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            organizational_unit_links.OrganizationalUnitLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        children_count = dictionary.get('children_count')
        configured_datasource_types = dictionary.get('configured_datasource_types')
        descendant_ids = dictionary.get('descendant_ids')
        description = dictionary.get('description')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        parent_id = dictionary.get('parent_id')
        task_id = dictionary.get('task_id')
        user_count = dictionary.get('user_count')
        users = dictionary.get('users')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            children_count,
            configured_datasource_types,
            descendant_ids,
            description,
            p_id,
            name,
            parent_id,
            task_id,
            user_count,
            users,
        )
