#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import clumio_role_resource
from clumioapi.models import clumio_rule_resource
from clumioapi.models import clumio_ssm_document_resource
from clumioapi.models import clumio_topic_resource
from clumioapi.models import policy_details

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
    _names = {
        'policies': 'policies',
        'roles': 'roles',
        'rules': 'rules',
        'ssm_documents': 'ssm_documents',
        'topics': 'topics',
    }

    def __init__(
        self,
        policies: Mapping[str, policy_details.PolicyDetails] = None,
        roles: Mapping[str, clumio_role_resource.ClumioRoleResource] = None,
        rules: Mapping[str, clumio_rule_resource.ClumioRuleResource] = None,
        ssm_documents: Mapping[str, clumio_ssm_document_resource.ClumioSsmDocumentResource] = None,
        topics: Mapping[str, clumio_topic_resource.ClumioTopicResource] = None,
    ) -> None:
        """Constructor for the CategorisedResources class."""

        # Initialize members of the class
        self.policies: Mapping[str, policy_details.PolicyDetails] = policies
        self.roles: Mapping[str, clumio_role_resource.ClumioRoleResource] = roles
        self.rules: Mapping[str, clumio_rule_resource.ClumioRuleResource] = rules
        self.ssm_documents: Mapping[
            str, clumio_ssm_document_resource.ClumioSsmDocumentResource
        ] = ssm_documents
        self.topics: Mapping[str, clumio_topic_resource.ClumioTopicResource] = topics

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
        policies: Dict[str, policy_details.PolicyDetails] = {}
        for key, value in dictionary.get('policies').items():
            policies[key] = policy_details.PolicyDetails.from_dictionary(value) if value else None

        roles: Dict[str, clumio_role_resource.ClumioRoleResource] = {}
        for key, value in dictionary.get('roles').items():
            roles[key] = (
                clumio_role_resource.ClumioRoleResource.from_dictionary(value) if value else None
            )

        rules: Dict[str, clumio_rule_resource.ClumioRuleResource] = {}
        for key, value in dictionary.get('rules').items():
            rules[key] = (
                clumio_rule_resource.ClumioRuleResource.from_dictionary(value) if value else None
            )

        ssm_documents: Dict[str, clumio_ssm_document_resource.ClumioSsmDocumentResource] = {}
        for key, value in dictionary.get('ssm_documents').items():
            ssm_documents[key] = (
                clumio_ssm_document_resource.ClumioSsmDocumentResource.from_dictionary(value)
                if value
                else None
            )

        topics: Dict[str, clumio_topic_resource.ClumioTopicResource] = {}
        for key, value in dictionary.get('topics').items():
            topics[key] = (
                clumio_topic_resource.ClumioTopicResource.from_dictionary(value) if value else None
            )

        # Return an object of this model
        return cls(policies, roles, rules, ssm_documents, topics)
