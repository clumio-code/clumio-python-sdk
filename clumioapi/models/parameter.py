#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_controls
from clumioapi.models import compliance_filters

T = TypeVar('T', bound='Parameter')


class Parameter:
    """Implementation of the 'Parameter' model.

    Filter and control parameters of compliance report.

    Attributes:
        controls:
            The set of controls supported in compliance report.
        filters:
            The set of filters supported in compliance report.
    """

    # Create a mapping from Model property names to API property names
    _names = {'controls': 'controls', 'filters': 'filters'}

    def __init__(
        self,
        controls: compliance_controls.ComplianceControls = None,
        filters: compliance_filters.ComplianceFilters = None,
    ) -> None:
        """Constructor for the Parameter class."""

        # Initialize members of the class
        self.controls: compliance_controls.ComplianceControls = controls
        self.filters: compliance_filters.ComplianceFilters = filters

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
        key = 'controls'
        controls = (
            compliance_controls.ComplianceControls.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'filters'
        filters = (
            compliance_filters.ComplianceFilters.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(controls, filters)
