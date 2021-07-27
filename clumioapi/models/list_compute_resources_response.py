#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import v_center_compute_resource
from clumioapi.models import v_center_folder

T = TypeVar('T', bound='ListComputeResourcesResponse')


class ListComputeResourcesResponse:
    """Implementation of the 'ListComputeResourcesResponse' model.

    Attributes:
        computeResourceFolders:
            Compute resource folders for the given parent folder.
        computeResources:
            Compute resources for the given parent folder.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'computeResourceFolders': 'computeResourceFolders',
        'computeResources': 'computeResources',
    }

    def __init__(
        self,
        computeResourceFolders: Sequence[v_center_folder.VCenterFolder] = None,
        computeResources: Sequence[v_center_compute_resource.VCenterComputeResource] = None,
    ) -> None:
        """Constructor for the ListComputeResourcesResponse class."""

        # Initialize members of the class
        self.computeResourceFolders: Sequence[
            v_center_folder.VCenterFolder
        ] = computeResourceFolders
        self.computeResources: Sequence[
            v_center_compute_resource.VCenterComputeResource
        ] = computeResources

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
        computeResourceFolders = None
        if dictionary.get('computeResourceFolders'):
            computeResourceFolders = list()
            for value in dictionary.get('computeResourceFolders'):
                computeResourceFolders.append(v_center_folder.VCenterFolder.from_dictionary(value))

        computeResources = None
        if dictionary.get('computeResources'):
            computeResources = list()
            for value in dictionary.get('computeResources'):
                computeResources.append(
                    v_center_compute_resource.VCenterComputeResource.from_dictionary(value)
                )

        # Return an object of this model
        return cls(computeResourceFolders, computeResources)
