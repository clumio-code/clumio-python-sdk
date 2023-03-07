#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import option_setting

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
    _names = {
        'is_permanent': 'is_permanent',
        'is_persistent': 'is_persistent',
        'is_required_for_restore': 'is_required_for_restore',
        'name': 'name',
        'option_setting': 'option_setting',
        'option_version': 'option_version',
    }

    def __init__(
        self,
        is_permanent: bool = None,
        is_persistent: bool = None,
        is_required_for_restore: bool = None,
        name: str = None,
        option_setting: Sequence[option_setting.OptionSetting] = None,
        option_version: str = None,
    ) -> None:
        """Constructor for the OptionModel class."""

        # Initialize members of the class
        self.is_permanent: bool = is_permanent
        self.is_persistent: bool = is_persistent
        self.is_required_for_restore: bool = is_required_for_restore
        self.name: str = name
        self.option_setting: Sequence[option_setting.OptionSetting] = option_setting
        self.option_version: str = option_version

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
        is_permanent = dictionary.get('is_permanent')
        is_persistent = dictionary.get('is_persistent')
        is_required_for_restore = dictionary.get('is_required_for_restore')
        name = dictionary.get('name')
        p_option_setting = None
        if dictionary.get('option_setting'):
            p_option_setting = list()
            for value in dictionary.get('option_setting'):
                p_option_setting.append(option_setting.OptionSetting.from_dictionary(value))

        option_version = dictionary.get('option_version')
        # Return an object of this model
        return cls(
            is_permanent,
            is_persistent,
            is_required_for_restore,
            name,
            p_option_setting,
            option_version,
        )
