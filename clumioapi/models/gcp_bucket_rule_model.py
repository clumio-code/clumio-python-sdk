#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_label_operator_model as gcp_label_operator_model_
from clumioapi.models import gcp_string_operator_model as gcp_string_operator_model_
import requests

T = TypeVar('T', bound='GCPBucketRuleModel')


@dataclasses.dataclass
class GCPBucketRuleModel:
    """Implementation of the 'GCPBucketRuleModel' model.

    Attributes:
        GcpLabel:
            At most one include and one exclude operator may be set.

        GcpLocation

        GcpProjectId

    """

    GcpLabel: gcp_label_operator_model_.GCPLabelOperatorModel | None = None
    GcpLocation: gcp_string_operator_model_.GCPStringOperatorModel | None = None
    GcpProjectId: gcp_string_operator_model_.GCPStringOperatorModel | None = None

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
        val = dictionary.get('gcp_label', None)
        val_gcp_label = gcp_label_operator_model_.GCPLabelOperatorModel.from_dictionary(val)

        val = dictionary.get('gcp_location', None)
        val_gcp_location = gcp_string_operator_model_.GCPStringOperatorModel.from_dictionary(val)

        val = dictionary.get('gcp_project_id', None)
        val_gcp_project_id = gcp_string_operator_model_.GCPStringOperatorModel.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_gcp_label,
            val_gcp_location,
            val_gcp_project_id,
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
