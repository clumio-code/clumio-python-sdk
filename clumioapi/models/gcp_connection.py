#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import configuration as configuration_
from clumioapi.models import gcp_connection_links as gcp_connection_links_
import requests

T = TypeVar('T', bound='GCPConnection')


@dataclasses.dataclass
class GCPConnection:
    """Implementation of the 'GCPConnection' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        Configuration

        ConnectionStatus:
            The status of the connection.

        ConnectionType:
            The type of this connection, which identifies its use.

        CreatedTimestamp:
            The timestamp of when the connection was created.

        DeploymentType:
            The method by which the gcp terraform template was deployed.

        Description:
            The user defined description for the connection.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the
            gcp connection.
            for more information about organizational units, refer to the
            organizational-units documentation.

        ProjectId:
            The user-assigned id of the gcp project associated with the connection.

        ProjectName:
            The user-friendly name of the gcp project associated with the connection.

        ProjectNumber:
            The gcp-assigned numeric int64 project number associated with the connection.

        Regions:
            The gcp regions used for inventory.

        TemplatePermissionSet:
            The permission set selected during registration.

        Token:
            The 36-character clumio gcp integration token used to identify the
            installation of the clumio gcp integration resources in the project.

        UpdatedTimestamp:
            The timestamp of when the connection was updated.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: gcp_connection_links_.GCPConnectionLinks | None = None
    Configuration: configuration_.Configuration | None = None
    ConnectionStatus: str | None = None
    ConnectionType: str | None = None
    CreatedTimestamp: str | None = None
    DeploymentType: str | None = None
    Description: str | None = None
    OrganizationalUnitId: str | None = None
    ProjectId: str | None = None
    ProjectName: str | None = None
    ProjectNumber: str | None = None
    Regions: Sequence[str] | None = None
    TemplatePermissionSet: str | None = None
    Token: str | None = None
    UpdatedTimestamp: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_links', None)
        val_links = gcp_connection_links_.GCPConnectionLinks.from_dictionary(val)

        val = dictionary.get('configuration', None)
        val_configuration = configuration_.Configuration.from_dictionary(val)

        val = dictionary.get('connection_status', None)
        val_connection_status = val

        val = dictionary.get('connection_type', None)
        val_connection_type = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('deployment_type', None)
        val_deployment_type = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('project_name', None)
        val_project_name = val

        val = dictionary.get('project_number', None)
        val_project_number = val

        val = dictionary.get('regions', None)
        val_regions = val

        val = dictionary.get('template_permission_set', None)
        val_template_permission_set = val

        val = dictionary.get('token', None)
        val_token = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_links,
            val_configuration,
            val_connection_status,
            val_connection_type,
            val_created_timestamp,
            val_deployment_type,
            val_description,
            val_organizational_unit_id,
            val_project_id,
            val_project_name,
            val_project_number,
            val_regions,
            val_template_permission_set,
            val_token,
            val_updated_timestamp,
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
