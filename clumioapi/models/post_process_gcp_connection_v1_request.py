#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='PostProcessGcpConnectionV1Request')


@dataclasses.dataclass
class PostProcessGcpConnectionV1Request:
    """Implementation of the 'PostProcessGcpConnectionV1Request' model.

    The body of the request.

    Attributes:
        Configuration:
            Configuration represents the gcp connection configuration in json string format.

        ProjectId:
            The user-assigned id of the gcp project associated with the connection.

        ProjectName:
            The user-friendly id of the gcp project associated with the connection.

        ProjectNumber:
            The gcp-assigned numeric int64 project number associated with the connection.

        Regions:
            The gcp regions to be used for inventory.
            each region must be a valid gcp region identifier (e.g., "us-central1", "europe-
            west1").

        RequestType:
            Requesttype indicates whether this is a create, update or delete request.

        ResourceProperties:
            Resourceproperties is a key value map meant to be used for passing additional
            information
            like resource ids.

        ServiceAccountEmail:
            The email address of the gcp service account created for this connection.

        Token:
            The 36-character clumio gcp integration token used to identify the
            installation of the clumio gcp integration resources in the project.

        WifPoolId:
            Wifpoolid is the workload identity federation pool id created for this
            connection.

        WifProviderId:
            Wifproviderid is the workload identity federation provider id created for this
            connection.

    """

    Configuration: str | None = None
    ProjectId: str | None = None
    ProjectName: str | None = None
    ProjectNumber: str | None = None
    Regions: Sequence[str] | None = None
    RequestType: str | None = None
    ResourceProperties: Mapping[str, str] | None = None
    ServiceAccountEmail: str | None = None
    Token: str | None = None
    WifPoolId: str | None = None
    WifProviderId: str | None = None

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
        val = dictionary.get('configuration', None)
        val_configuration = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('project_name', None)
        val_project_name = val

        val = dictionary.get('project_number', None)
        val_project_number = val

        val = dictionary.get('regions', None)
        val_regions = val

        val = dictionary.get('request_type', None)
        val_request_type = val

        val = dictionary.get('resource_properties', None)
        val_resource_properties = val

        val = dictionary.get('service_account_email', None)
        val_service_account_email = val

        val = dictionary.get('token', None)
        val_token = val

        val = dictionary.get('wif_pool_id', None)
        val_wif_pool_id = val

        val = dictionary.get('wif_provider_id', None)
        val_wif_provider_id = val

        # Return an object of this model
        return cls(
            val_configuration,
            val_project_id,
            val_project_name,
            val_project_number,
            val_regions,
            val_request_type,
            val_resource_properties,
            val_service_account_email,
            val_token,
            val_wif_pool_id,
            val_wif_provider_id,
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
