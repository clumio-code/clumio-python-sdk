#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import control_info
from clumioapi.models import items_covered

T = TypeVar('T', bound='ComplianceInfo')


class ComplianceInfo:
    """Implementation of the 'ComplianceInfo' model.

    The status per controls in the compliance report created by the report run.

    Attributes:
        compliance_status:
            The compliance status of the report run.
        compliant_count:
            The count of compliant items of the report run.
        controls:
            The status per controls in the compliance report created by the report run.
        items_covered:
            The items covered in the compliance report created by the report run.
        non_compliant_count:
            The count of non-compliant items of the report run.
        unknown_count:
            The count of unknown items of the report run.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'compliance_status': 'compliance_status',
        'compliant_count': 'compliant_count',
        'controls': 'controls',
        'items_covered': 'items_covered',
        'non_compliant_count': 'non_compliant_count',
        'unknown_count': 'unknown_count',
    }

    def __init__(
        self,
        compliance_status: str = None,
        compliant_count: int = None,
        controls: Sequence[control_info.ControlInfo] = None,
        items_covered: items_covered.ItemsCovered = None,
        non_compliant_count: int = None,
        unknown_count: int = None,
    ) -> None:
        """Constructor for the ComplianceInfo class."""

        # Initialize members of the class
        self.compliance_status: str = compliance_status
        self.compliant_count: int = compliant_count
        self.controls: Sequence[control_info.ControlInfo] = controls
        self.items_covered: items_covered.ItemsCovered = items_covered
        self.non_compliant_count: int = non_compliant_count
        self.unknown_count: int = unknown_count

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
        compliance_status = dictionary.get('compliance_status')
        compliant_count = dictionary.get('compliant_count')
        controls = None
        if dictionary.get('controls'):
            controls = list()
            for value in dictionary.get('controls'):
                controls.append(control_info.ControlInfo.from_dictionary(value))

        key = 'items_covered'
        p_items_covered = (
            items_covered.ItemsCovered.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        non_compliant_count = dictionary.get('non_compliant_count')
        unknown_count = dictionary.get('unknown_count')
        # Return an object of this model
        return cls(
            compliance_status,
            compliant_count,
            controls,
            p_items_covered,
            non_compliant_count,
            unknown_count,
        )
