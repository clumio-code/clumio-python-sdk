#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='CreateGcpConnectionV1Request')

DeploymentTypeValues = [
    'direct_terraform',
    'infrastructure_manager',
]


@dataclasses.dataclass
class CreateGcpConnectionV1Request:
    """Implementation of the 'CreateGcpConnectionV1Request' model.

    The body of the request.

    Attributes:
        DeploymentType:
            The method by which the gcp terraform template was deployed.

        Description:
            The user defined description for the connection.

        ProjectId:
            The user-assigned id of the gcp project associated with the connection.

        Regions:
            The gcp regions to be used for inventory.
            each region must be a valid gcp region identifier (e.g., "us-central1", "europe-
            west1").

    """

    DeploymentType: str | None = None
    Description: str | None = None
    ProjectId: str | None = None
    Regions: Sequence[str] | None = None

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
        val = dictionary.get('deployment_type', None)
        val_deployment_type = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('regions', None)
        val_regions = val

        # Return an object of this model
        return cls(
            val_deployment_type,
            val_description,
            val_project_id,
            val_regions,
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
