#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ou_links

T = TypeVar('T', bound='CreateOrganizationalUnitNoTaskResponseV1')


class CreateOrganizationalUnitNoTaskResponseV1:
    """Implementation of the 'CreateOrganizationalUnitNoTaskResponseV1' model.

    Attributes:
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
        'links': '_links',
        'children_count': 'children_count',
        'configured_datasource_types': 'configured_datasource_types',
        'descendant_ids': 'descendant_ids',
        'description': 'description',
        'p_id': 'id',
        'name': 'name',
        'parent_id': 'parent_id',
        'user_count': 'user_count',
        'users': 'users',
    }

    def __init__(
        self,
        links: ou_links.OULinks = None,
        children_count: int = None,
        configured_datasource_types: Sequence[str] = None,
        descendant_ids: Sequence[str] = None,
        description: str = None,
        p_id: str = None,
        name: str = None,
        parent_id: str = None,
        user_count: int = None,
        users: Sequence[str] = None,
    ) -> None:
        """Constructor for the CreateOrganizationalUnitNoTaskResponseV1 class."""

        # Initialize members of the class
        self.links: ou_links.OULinks = links
        self.children_count: int = children_count
        self.configured_datasource_types: Sequence[str] = configured_datasource_types
        self.descendant_ids: Sequence[str] = descendant_ids
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name
        self.parent_id: str = parent_id
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
        key = '_links'
        links = (
            ou_links.OULinks.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None
        )

        children_count = dictionary.get('children_count')
        configured_datasource_types = dictionary.get('configured_datasource_types')
        descendant_ids = dictionary.get('descendant_ids')
        description = dictionary.get('description')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        parent_id = dictionary.get('parent_id')
        user_count = dictionary.get('user_count')
        users = dictionary.get('users')
        # Return an object of this model
        return cls(
            links,
            children_count,
            configured_datasource_types,
            descendant_ids,
            description,
            p_id,
            name,
            parent_id,
            user_count,
            users,
        )
