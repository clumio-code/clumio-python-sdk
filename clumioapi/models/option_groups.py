#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import option_groups_links
from clumioapi.models import option_model

T = TypeVar('T', bound='OptionGroups')


class OptionGroups:
    """Implementation of the 'OptionGroups' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        engine:
            The AWS database engine at the time of backup.
        engine_version:
            The AWS database engine version at the time of backup.
        has_additional_non_permanent_options:
            Determines whether this option group contains additional non-permanent options
            apart from
            the non-permanent options at the time of backup.
        has_additional_non_persistent_options:
            Determines whether this option group contains additional non-persistent options
            apart from
            the non-persistent options at time of backup.
        has_additional_permanent_options:
            Determines whether this option group contains additional permanent options apart
            from
            the permanent options at the time of backup.
        has_additional_persistent_options:
            Determines whether this option group contains additional persistent options
            apart from
            the persistent options at the time of backup.
        is_compatible:
            Compatibility of the Option Group
        minimum_required_minor_engine_version:
            Minimum required minor engine version for this option-group to be applicable.
        name:
            Name of the option group
        options:
            List of options configurations.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'has_additional_non_permanent_options': 'has_additional_non_permanent_options',
        'has_additional_non_persistent_options': 'has_additional_non_persistent_options',
        'has_additional_permanent_options': 'has_additional_permanent_options',
        'has_additional_persistent_options': 'has_additional_persistent_options',
        'is_compatible': 'is_compatible',
        'minimum_required_minor_engine_version': 'minimum_required_minor_engine_version',
        'name': 'name',
        'options': 'options',
    }

    def __init__(
        self,
        embedded: object = None,
        links: option_groups_links.OptionGroupsLinks = None,
        engine: str = None,
        engine_version: str = None,
        has_additional_non_permanent_options: bool = None,
        has_additional_non_persistent_options: bool = None,
        has_additional_permanent_options: bool = None,
        has_additional_persistent_options: bool = None,
        is_compatible: bool = None,
        minimum_required_minor_engine_version: str = None,
        name: str = None,
        options: Sequence[option_model.OptionModel] = None,
    ) -> None:
        """Constructor for the OptionGroups class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: option_groups_links.OptionGroupsLinks = links
        self.engine: str = engine
        self.engine_version: str = engine_version
        self.has_additional_non_permanent_options: bool = has_additional_non_permanent_options
        self.has_additional_non_persistent_options: bool = has_additional_non_persistent_options
        self.has_additional_permanent_options: bool = has_additional_permanent_options
        self.has_additional_persistent_options: bool = has_additional_persistent_options
        self.is_compatible: bool = is_compatible
        self.minimum_required_minor_engine_version: str = minimum_required_minor_engine_version
        self.name: str = name
        self.options: Sequence[option_model.OptionModel] = options

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
        embedded = dictionary.get('_embedded')
        key = '_links'
        links = (
            option_groups_links.OptionGroupsLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        engine = dictionary.get('engine')
        engine_version = dictionary.get('engine_version')
        has_additional_non_permanent_options = dictionary.get(
            'has_additional_non_permanent_options'
        )
        has_additional_non_persistent_options = dictionary.get(
            'has_additional_non_persistent_options'
        )
        has_additional_permanent_options = dictionary.get('has_additional_permanent_options')
        has_additional_persistent_options = dictionary.get('has_additional_persistent_options')
        is_compatible = dictionary.get('is_compatible')
        minimum_required_minor_engine_version = dictionary.get(
            'minimum_required_minor_engine_version'
        )
        name = dictionary.get('name')
        options = None
        if dictionary.get('options'):
            options = list()
            for value in dictionary.get('options'):
                options.append(option_model.OptionModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            embedded,
            links,
            engine,
            engine_version,
            has_additional_non_permanent_options,
            has_additional_non_persistent_options,
            has_additional_permanent_options,
            has_additional_persistent_options,
            is_compatible,
            minimum_required_minor_engine_version,
            name,
            options,
        )
