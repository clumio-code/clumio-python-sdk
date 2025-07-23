#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import clumio_role_resource as clumio_role_resource_
from clumioapi.models import clumio_rule_resource as clumio_rule_resource_
from clumioapi.models import clumio_ssm_document_resource as clumio_ssm_document_resource_
from clumioapi.models import clumio_topic_resource as clumio_topic_resource_
from clumioapi.models import policy_details as policy_details_

T = TypeVar('T', bound='CategorisedResources')


class CategorisedResources:
    """Implementation of the 'CategorisedResources' model.

    Categorised Resources, based on the generated template, to be created manually
    by the user

    Attributes:
        policies:
            Consists of policies that are not attached to any other resource (Roles, Topics,
            Rules)
        roles:
            Consists of the IAM Roles and the attached policies
        rules:
            Consists of the EventBridge Rules
        ssm_documents:
            Consists of SSM Documents
        topics:
            Consists of the SNS Topics
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'policies': 'policies',
        'roles': 'roles',
        'rules': 'rules',
        'ssm_documents': 'ssm_documents',
        'topics': 'topics',
    }

    def __init__(
        self,
        policies: Mapping[str, policy_details_.PolicyDetails] | None = None,
        roles: Mapping[str, clumio_role_resource_.ClumioRoleResource] | None = None,
        rules: Mapping[str, clumio_rule_resource_.ClumioRuleResource] | None = None,
        ssm_documents: (
            Mapping[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource] | None
        ) = None,
        topics: Mapping[str, clumio_topic_resource_.ClumioTopicResource] | None = None,
    ) -> None:
        """Constructor for the CategorisedResources class."""

        # Initialize members of the class
        self.policies: Mapping[str, policy_details_.PolicyDetails] | None = policies
        self.roles: Mapping[str, clumio_role_resource_.ClumioRoleResource] | None = roles
        self.rules: Mapping[str, clumio_rule_resource_.ClumioRuleResource] | None = rules
        self.ssm_documents: (
            Mapping[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource] | None
        ) = ssm_documents
        self.topics: Mapping[str, clumio_topic_resource_.ClumioTopicResource] | None = topics

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
