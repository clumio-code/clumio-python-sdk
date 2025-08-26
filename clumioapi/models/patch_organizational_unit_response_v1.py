#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import entity_group_embedded as entity_group_embedded_
from clumioapi.models import organizational_unit_links as organizational_unit_links_
import requests

T = TypeVar('T', bound='PatchOrganizationalUnitResponseV1')


@dataclasses.dataclass
class PatchOrganizationalUnitResponseV1:
    """Implementation of the 'PatchOrganizationalUnitResponseV1' model.

        Accepted

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            ChildrenCount:
                Number of immediate children of the organizational unit.

            ConfiguredDatasourceTypes:
                Datasource types configured in this organizational unit. possible values include `aws`, `microsoft365`, `vmware`, or `mssql`.

            DescendantIds:
                List of all recursive descendant organizational units of this ou.

            Description:
                A description of the organizational unit.

            Id:
                The clumio assigned id of the organizational unit.

            Name:
                Unique name assigned to the organizational unit.

            ParentId:
                The clumio assigned id of the parent organizational unit.
    the parent organizational unit contains the entities in this organizational unit and can update this organizational unit.
    if this organizational unit is the global organizational unit, then this field has a value of `null`.

            TaskId:
                The clumio-assigned id of the task associated with this organizational unit.
    the progress of the task can be monitored using the
    [get /tasks/{task_id}](#operation/read-task) endpoint.

            UserCount:
                Number of users to whom this organizational unit or any of its descendants have been assigned.

            Users:
                Users ids to whom the organizational unit has been assigned.
    this attribute will be available when reading a single ou and not when listing ous.

    """

    Embedded: entity_group_embedded_.EntityGroupEmbedded | None = None
    Links: organizational_unit_links_.OrganizationalUnitLinks | None = None
    ChildrenCount: int | None = None
    ConfiguredDatasourceTypes: Sequence[str] | None = None
    DescendantIds: Sequence[str] | None = None
    Description: str | None = None
    Id: str | None = None
    Name: str | None = None
    ParentId: str | None = None
    TaskId: str | None = None
    UserCount: int | None = None
    Users: Sequence[str] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val_id = val

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
            val_links,
            val_children_count,
            val_configured_datasource_types,
            val_descendant_ids,
            val_description,
            val_id,
            val_name,
            val_parent_id,
            val_task_id,
            val_user_count,
            val_users,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
