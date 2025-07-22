#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ComplianceConfigurationEmbedded')


class ComplianceConfigurationEmbedded:
    """Implementation of the 'ComplianceConfigurationEmbedded' model.

    If the `embed` query parameter is set, displays the responses of the related
    resource,as defined by the embeddable link specified.

    Attributes:
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {}

    def __init__(
        self,
    ) -> None:
        """Constructor for the ComplianceConfigurationEmbedded class."""

        # Initialize members of the class

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

        # Return an object of this model
        return cls()
