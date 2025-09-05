#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import option_groups_links as option_groups_links_
from clumioapi.models import option_model as option_model_

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
    _names: dict[str, str] = {
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
        embedded: object | None = None,
        links: option_groups_links_.OptionGroupsLinks | None = None,
        engine: str | None = None,
        engine_version: str | None = None,
        has_additional_non_permanent_options: bool | None = None,
        has_additional_non_persistent_options: bool | None = None,
        has_additional_permanent_options: bool | None = None,
        has_additional_persistent_options: bool | None = None,
        is_compatible: bool | None = None,
        minimum_required_minor_engine_version: str | None = None,
        name: str | None = None,
        options: Sequence[option_model_.OptionModel] | None = None,
    ) -> None:
        """Constructor for the OptionGroups class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: option_groups_links_.OptionGroupsLinks | None = links
        self.engine: str | None = engine
        self.engine_version: str | None = engine_version
        self.has_additional_non_permanent_options: bool | None = (
            has_additional_non_permanent_options
        )
        self.has_additional_non_persistent_options: bool | None = (
            has_additional_non_persistent_options
        )
        self.has_additional_permanent_options: bool | None = has_additional_permanent_options
        self.has_additional_persistent_options: bool | None = has_additional_persistent_options
        self.is_compatible: bool | None = is_compatible
        self.minimum_required_minor_engine_version: str | None = (
            minimum_required_minor_engine_version
        )
        self.name: str | None = name
        self.options: Sequence[option_model_.OptionModel] | None = options

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = option_groups_links_.OptionGroupsLinks.from_dictionary(val)

        val = dictionary.get('engine', None)
        val_engine = val

        val = dictionary.get('engine_version', None)
        val_engine_version = val

        val = dictionary.get('has_additional_non_permanent_options', None)
        val_has_additional_non_permanent_options = val

        val = dictionary.get('has_additional_non_persistent_options', None)
        val_has_additional_non_persistent_options = val

        val = dictionary.get('has_additional_permanent_options', None)
        val_has_additional_permanent_options = val

        val = dictionary.get('has_additional_persistent_options', None)
        val_has_additional_persistent_options = val

        val = dictionary.get('is_compatible', None)
        val_is_compatible = val

        val = dictionary.get('minimum_required_minor_engine_version', None)
        val_minimum_required_minor_engine_version = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('options', None)

        val_options = None
        if val:
            val_options = list()
            for value in val:
                val_options.append(option_model_.OptionModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_engine,
            val_engine_version,
            val_has_additional_non_permanent_options,
            val_has_additional_non_persistent_options,
            val_has_additional_permanent_options,
            val_has_additional_persistent_options,
            val_is_compatible,
            val_minimum_required_minor_engine_version,
            val_name,
            val_options,
        )
