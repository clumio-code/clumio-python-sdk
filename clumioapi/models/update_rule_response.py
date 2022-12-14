#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_links
from clumioapi.models import rule

T = TypeVar('T', bound='UpdateRuleResponse')


class UpdateRuleResponse:
    """Implementation of the 'UpdateRuleResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        preview_id:
            The Clumio-assigned ID of the preview generated by this request. Only valid if
            `execution_type` is set to `dryrun`.
        rule:
            A rule applies an action subject to a condition criteria.
        task_id:
            The Clumio-assigned ID of the task generated by this request.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'preview_id': 'preview_id', 'rule': 'rule', 'task_id': 'task_id'}

    def __init__(
        self,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        preview_id: str = None,
        rule: rule.Rule = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the UpdateRuleResponse class."""

        # Initialize members of the class
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links
        self.preview_id: str = preview_id
        self.rule: rule.Rule = rule
        self.task_id: str = task_id

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
        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        preview_id = dictionary.get('preview_id')
        key = 'rule'
        p_rule = rule.Rule.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(links, preview_id, p_rule, task_id)
