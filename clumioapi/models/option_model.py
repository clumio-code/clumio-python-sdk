#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import option_setting as option_setting_

T = TypeVar('T', bound='OptionModel')


class OptionModel:
    """Implementation of the 'OptionModel' model.

    OptionModel denotes the Model for OptionModel

    Attributes:
        is_permanent:
            Determines whether or not the option is permanent.
        is_persistent:
            Determines whether or not the option is persistent.
        is_required_for_restore:
            Determines whether the option is required to restore from a given backup.
        name:
            The AWS-assigned name of the RDS option.
        option_setting:
            List of option settings.
        option_version:
            Option version of the option.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'is_permanent': 'is_permanent',
        'is_persistent': 'is_persistent',
        'is_required_for_restore': 'is_required_for_restore',
        'name': 'name',
        'option_setting': 'option_setting',
        'option_version': 'option_version',
    }

    def __init__(
        self,
        is_permanent: bool | None = None,
        is_persistent: bool | None = None,
        is_required_for_restore: bool | None = None,
        name: str | None = None,
        option_setting: Sequence[option_setting_.OptionSetting] | None = None,
        option_version: str | None = None,
    ) -> None:
        """Constructor for the OptionModel class."""

        # Initialize members of the class
        self.is_permanent: bool | None = is_permanent
        self.is_persistent: bool | None = is_persistent
        self.is_required_for_restore: bool | None = is_required_for_restore
        self.name: str | None = name
        self.option_setting: Sequence[option_setting_.OptionSetting] | None = option_setting
        self.option_version: str | None = option_version

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
        val = dictionary.get('is_permanent', None)
        val_is_permanent = val

        val = dictionary.get('is_persistent', None)
        val_is_persistent = val

        val = dictionary.get('is_required_for_restore', None)
        val_is_required_for_restore = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('option_setting', None)

        val_option_setting = None
        if val:
            val_option_setting = list()
            for value in val:
                val_option_setting.append(option_setting_.OptionSetting.from_dictionary(value))

        val = dictionary.get('option_version', None)
        val_option_version = val

        # Return an object of this model
        return cls(
            val_is_permanent,
            val_is_persistent,
            val_is_required_for_restore,
            val_name,
            val_option_setting,
            val_option_version,
        )
