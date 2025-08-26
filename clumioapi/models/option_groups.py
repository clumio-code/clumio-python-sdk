#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import option_groups_links as option_groups_links_
from clumioapi.models import option_model as option_model_
import requests

T = TypeVar('T', bound='OptionGroups')


@dataclasses.dataclass
class OptionGroups:
    """Implementation of the 'OptionGroups' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            Engine:
                The aws database engine at the time of backup.

            EngineVersion:
                The aws database engine version at the time of backup.

            HasAdditionalNonPermanentOptions:
                Determines whether this option group contains additional non-permanent options apart from
    the non-permanent options at the time of backup.

            HasAdditionalNonPersistentOptions:
                Determines whether this option group contains additional non-persistent options apart from
    the non-persistent options at time of backup.

            HasAdditionalPermanentOptions:
                Determines whether this option group contains additional permanent options apart from
    the permanent options at the time of backup.

            HasAdditionalPersistentOptions:
                Determines whether this option group contains additional persistent options apart from
    the persistent options at the time of backup.

            IsCompatible:
                Compatibility of the option group.

            MinimumRequiredMinorEngineVersion:
                Minimum required minor engine version for this option-group to be applicable.

            Name:
                Name of the option group.

            Options:
                List of options configurations.

    """

    Embedded: object | None = None
    Links: option_groups_links_.OptionGroupsLinks | None = None
    Engine: str | None = None
    EngineVersion: str | None = None
    HasAdditionalNonPermanentOptions: bool | None = None
    HasAdditionalNonPersistentOptions: bool | None = None
    HasAdditionalPermanentOptions: bool | None = None
    HasAdditionalPersistentOptions: bool | None = None
    IsCompatible: bool | None = None
    MinimumRequiredMinorEngineVersion: str | None = None
    Name: str | None = None
    Options: Sequence[option_model_.OptionModel] | None = None

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

        val_options = []
        if val:
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
