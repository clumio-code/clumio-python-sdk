#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import resources

T = TypeVar('T', bound='UpdateAwsConnectionV1Request')


class UpdateAwsConnectionV1Request:
    """Implementation of the 'UpdateAwsConnectionV1Request' model.

    Attributes:
        asset_types_enabled:
            Asset types enabled with the given resource ARNs.
            This field is only applicable to manually configured connections.
        description:
            An optional, user-provided description for this connection.
        resources:
            Partial updates are not supported, therefore you must provide ARNs for all
            configured resources,
            including those for resources that are not being updated.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'description': 'description',
        'resources': 'resources',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        description: str = None,
        resources: resources.Resources = None,
    ) -> None:
        """Constructor for the UpdateAwsConnectionV1Request class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.description: str = description
        self.resources: resources.Resources = resources

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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        description = dictionary.get('description')
        key = 'resources'
        p_resources = (
            resources.Resources.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset_types_enabled, description, p_resources)
