#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import control_info as control_info_
from clumioapi.models import items_covered as items_covered_

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
    _names: dict[str, str] = {
        'compliance_status': 'compliance_status',
        'compliant_count': 'compliant_count',
        'controls': 'controls',
        'items_covered': 'items_covered',
        'non_compliant_count': 'non_compliant_count',
        'unknown_count': 'unknown_count',
    }

    def __init__(
        self,
        compliance_status: str,
        compliant_count: int,
        controls: Sequence[control_info_.ControlInfo],
        items_covered: items_covered_.ItemsCovered,
        non_compliant_count: int,
        unknown_count: int,
    ) -> None:
        """Constructor for the ComplianceInfo class."""

        # Initialize members of the class
        self.compliance_status: str = compliance_status
        self.compliant_count: int = compliant_count
        self.controls: Sequence[control_info_.ControlInfo] = controls
        self.items_covered: items_covered_.ItemsCovered = items_covered
        self.non_compliant_count: int = non_compliant_count
        self.unknown_count: int = unknown_count

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
        val = dictionary['compliance_status']
        val_compliance_status = val

        val = dictionary['compliant_count']
        val_compliant_count = val

        val = dictionary['controls']

        val_controls = None
        if val:
            val_controls = list()
            for value in val:
                val_controls.append(control_info_.ControlInfo.from_dictionary(value))

        val = dictionary['items_covered']
        val_items_covered = items_covered_.ItemsCovered.from_dictionary(val)

        val = dictionary['non_compliant_count']
        val_non_compliant_count = val

        val = dictionary['unknown_count']
        val_unknown_count = val

        # Return an object of this model
        return cls(
            val_compliance_status,  # type: ignore
            val_compliant_count,  # type: ignore
            val_controls,  # type: ignore
            val_items_covered,  # type: ignore
            val_non_compliant_count,  # type: ignore
            val_unknown_count,  # type: ignore
        )
