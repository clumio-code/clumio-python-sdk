#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import control_info as control_info_
from clumioapi.models import items_covered as items_covered_
import requests

T = TypeVar('T', bound='ComplianceInfo')


@dataclasses.dataclass
class ComplianceInfo:
    """Implementation of the 'ComplianceInfo' model.

    The status per controls in the compliance report created by the report run.

    Attributes:
        ComplianceStatus:
            The compliance status of the report run.

        CompliantCount:
            The count of compliant items of the report run.

        Controls:
            The status per controls in the compliance report created by the report run.

        ItemsCovered:
            The items covered in the compliance report created by the report run.

        NonCompliantCount:
            The count of non-compliant items of the report run.

        UnknownCount:
            The count of unknown items of the report run.

    """

    ComplianceStatus: str | None = None
    CompliantCount: int | None = None
    Controls: Sequence[control_info_.ControlInfo] | None = None
    ItemsCovered: items_covered_.ItemsCovered | None = None
    NonCompliantCount: int | None = None
    UnknownCount: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('compliance_status', None)
        val_compliance_status = val

        val = dictionary.get('compliant_count', None)
        val_compliant_count = val

        val = dictionary.get('controls', None)

        val_controls = []
        if val:
            for value in val:
                val_controls.append(control_info_.ControlInfo.from_dictionary(value))

        val = dictionary.get('items_covered', None)
        val_items_covered = items_covered_.ItemsCovered.from_dictionary(val)

        val = dictionary.get('non_compliant_count', None)
        val_non_compliant_count = val

        val = dictionary.get('unknown_count', None)
        val_unknown_count = val

        # Return an object of this model
        return cls(
            val_compliance_status,
            val_compliant_count,
            val_controls,
            val_items_covered,
            val_non_compliant_count,
            val_unknown_count,
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
