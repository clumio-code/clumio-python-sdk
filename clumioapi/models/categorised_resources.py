#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import clumio_role_resource as clumio_role_resource_
from clumioapi.models import clumio_rule_resource as clumio_rule_resource_
from clumioapi.models import clumio_ssm_document_resource as clumio_ssm_document_resource_
from clumioapi.models import clumio_topic_resource as clumio_topic_resource_
from clumioapi.models import policy_details as policy_details_
import requests

T = TypeVar('T', bound='CategorisedResources')


@dataclasses.dataclass
class CategorisedResources:
    """Implementation of the 'CategorisedResources' model.

    Categorised Resources, based on the generated template, to be created manually
    by the user

    Attributes:
        Policies:
            Consists of policies that are not attached to any other resource (roles, topics, rules).

        Roles:
            Consists of the iam roles and the attached policies.

        Rules:
            Consists of the eventbridge rules.

        SsmDocuments:
            Consists of ssm documents.

        Topics:
            Consists of the sns topics.

    """

    Policies: Mapping[str, policy_details_.PolicyDetails] | None = None
    Roles: Mapping[str, clumio_role_resource_.ClumioRoleResource] | None = None
    Rules: Mapping[str, clumio_rule_resource_.ClumioRuleResource] | None = None
    SsmDocuments: Mapping[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource] | None = (
        None
    )
    Topics: Mapping[str, clumio_topic_resource_.ClumioTopicResource] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('policies', None)
        val_policies: Dict[str, policy_details_.PolicyDetails] = {}
        for key, value in val.items():
            val_policies[key] = policy_details_.PolicyDetails.from_dictionary(value)

        val = dictionary.get('roles', None)
        val_roles: Dict[str, clumio_role_resource_.ClumioRoleResource] = {}
        for key, value in val.items():
            val_roles[key] = clumio_role_resource_.ClumioRoleResource.from_dictionary(value)

        val = dictionary.get('rules', None)
        val_rules: Dict[str, clumio_rule_resource_.ClumioRuleResource] = {}
        for key, value in val.items():
            val_rules[key] = clumio_rule_resource_.ClumioRuleResource.from_dictionary(value)

        val = dictionary.get('ssm_documents', None)
        val_ssm_documents: Dict[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource] = {}
        for key, value in val.items():
            val_ssm_documents[key] = (
                clumio_ssm_document_resource_.ClumioSsmDocumentResource.from_dictionary(value)
            )

        val = dictionary.get('topics', None)
        val_topics: Dict[str, clumio_topic_resource_.ClumioTopicResource] = {}
        for key, value in val.items():
            val_topics[key] = clumio_topic_resource_.ClumioTopicResource.from_dictionary(value)

        # Return an object of this model
        return cls(
            val_policies,
            val_roles,
            val_rules,
            val_ssm_documents,
            val_topics,
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
