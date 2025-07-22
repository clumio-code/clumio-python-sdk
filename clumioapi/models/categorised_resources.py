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
        policies: Mapping[str, policy_details_.PolicyDetails],
        roles: Mapping[str, clumio_role_resource_.ClumioRoleResource],
        rules: Mapping[str, clumio_rule_resource_.ClumioRuleResource],
        ssm_documents: Mapping[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource],
        topics: Mapping[str, clumio_topic_resource_.ClumioTopicResource],
    ) -> None:
        """Constructor for the CategorisedResources class."""

        # Initialize members of the class
        self.policies: Mapping[str, policy_details_.PolicyDetails] = policies
        self.roles: Mapping[str, clumio_role_resource_.ClumioRoleResource] = roles
        self.rules: Mapping[str, clumio_rule_resource_.ClumioRuleResource] = rules
        self.ssm_documents: Mapping[
            str, clumio_ssm_document_resource_.ClumioSsmDocumentResource
        ] = ssm_documents
        self.topics: Mapping[str, clumio_topic_resource_.ClumioTopicResource] = topics

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
        val = dictionary['policies']
        val_policies: Dict[str, policy_details_.PolicyDetails] = {}
        for key, value in val.items():
            val_policies[key] = policy_details_.PolicyDetails.from_dictionary(value)

        val = dictionary['roles']
        val_roles: Dict[str, clumio_role_resource_.ClumioRoleResource] = {}
        for key, value in val.items():
            val_roles[key] = clumio_role_resource_.ClumioRoleResource.from_dictionary(value)

        val = dictionary['rules']
        val_rules: Dict[str, clumio_rule_resource_.ClumioRuleResource] = {}
        for key, value in val.items():
            val_rules[key] = clumio_rule_resource_.ClumioRuleResource.from_dictionary(value)

        val = dictionary['ssm_documents']
        val_ssm_documents: Dict[str, clumio_ssm_document_resource_.ClumioSsmDocumentResource] = {}
        for key, value in val.items():
            val_ssm_documents[key] = (
                clumio_ssm_document_resource_.ClumioSsmDocumentResource.from_dictionary(value)
            )

        val = dictionary['topics']
        val_topics: Dict[str, clumio_topic_resource_.ClumioTopicResource] = {}
        for key, value in val.items():
            val_topics[key] = clumio_topic_resource_.ClumioTopicResource.from_dictionary(value)

        # Return an object of this model
        return cls(
            val_policies,  # type: ignore
            val_roles,  # type: ignore
            val_rules,  # type: ignore
            val_ssm_documents,  # type: ignore
            val_topics,  # type: ignore
        )
