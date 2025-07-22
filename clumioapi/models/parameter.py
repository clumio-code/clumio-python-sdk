#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_controls as compliance_controls_
from clumioapi.models import compliance_filters as compliance_filters_

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
    _names: dict[str, str] = {'controls': 'controls', 'filters': 'filters'}

    def __init__(
        self,
        controls: compliance_controls_.ComplianceControls,
        filters: compliance_filters_.ComplianceFilters,
    ) -> None:
        """Constructor for the Parameter class."""

        # Initialize members of the class
        self.controls: compliance_controls_.ComplianceControls = controls
        self.filters: compliance_filters_.ComplianceFilters = filters

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
        val = dictionary['controls']
        val_controls = compliance_controls_.ComplianceControls.from_dictionary(val)

        val = dictionary['filters']
        val_filters = compliance_filters_.ComplianceFilters.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_controls,  # type: ignore
            val_filters,  # type: ignore
        )
