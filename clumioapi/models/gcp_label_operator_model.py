#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_bucket_rule_label_model as gcp_bucket_rule_label_model_
import requests

T = TypeVar('T', bound='GCPLabelOperatorModel')


@dataclasses.dataclass
class GCPLabelOperatorModel:
    """Implementation of the 'GCPLabelOperatorModel' model.

    At most one include and one exclude operator may be set.

    Attributes:
        All

        Contains

        Eq

        In

        NotAll

        NotContains

        NotEq

        NotIn

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'All': '$all',
        'Contains': '$contains',
        'Eq': '$eq',
        'In': '$in',
        'NotAll': '$not_all',
        'NotContains': '$not_contains',
        'NotEq': '$not_eq',
        'NotIn': '$not_in',
    }

    All: Sequence[gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel] | None = None
    Contains: gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel | None = None
    Eq: gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel | None = None
    In: Sequence[gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel] | None = None
    NotAll: Sequence[gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel] | None = None
    NotContains: gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel | None = None
    NotEq: gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel | None = None
    NotIn: Sequence[gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel] | None = None

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
        val = dictionary.get('$all', None)

        val_all = []
        if val:
            for value in val:
                val_all.append(
                    gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(value)
                )

        val = dictionary.get('$contains', None)
        val_contains = gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(val)

        val = dictionary.get('$eq', None)
        val_eq = gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(val)

        val = dictionary.get('$in', None)

        val_in = []
        if val:
            for value in val:
                val_in.append(
                    gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(value)
                )

        val = dictionary.get('$not_all', None)

        val_not_all = []
        if val:
            for value in val:
                val_not_all.append(
                    gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(value)
                )

        val = dictionary.get('$not_contains', None)
        val_not_contains = gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(val)

        val = dictionary.get('$not_eq', None)
        val_not_eq = gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(val)

        val = dictionary.get('$not_in', None)

        val_not_in = []
        if val:
            for value in val:
                val_not_in.append(
                    gcp_bucket_rule_label_model_.GCPBucketRuleLabelModel.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_all,
            val_contains,
            val_eq,
            val_in,
            val_not_all,
            val_not_contains,
            val_not_eq,
            val_not_in,
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
