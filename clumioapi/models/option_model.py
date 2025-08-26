#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import option_setting as option_setting_
import requests

T = TypeVar('T', bound='OptionModel')


@dataclasses.dataclass
class OptionModel:
    """Implementation of the 'OptionModel' model.

    OptionModel denotes the Model for OptionModel

    Attributes:
        IsPermanent:
            Determines whether or not the option is permanent.

        IsPersistent:
            Determines whether or not the option is persistent.

        IsRequiredForRestore:
            Determines whether the option is required to restore from a given backup.

        Name:
            The aws-assigned name of the rds option.

        OptionSetting:
            List of option settings.

        OptionVersion:
            Option version of the option.

    """

    IsPermanent: bool | None = None
    IsPersistent: bool | None = None
    IsRequiredForRestore: bool | None = None
    Name: str | None = None
    OptionSetting: Sequence[option_setting_.OptionSetting] | None = None
    OptionVersion: str | None = None

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
        val = dictionary.get('is_permanent', None)
        val_is_permanent = val

        val = dictionary.get('is_persistent', None)
        val_is_persistent = val

        val = dictionary.get('is_required_for_restore', None)
        val_is_required_for_restore = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('option_setting', None)

        val_option_setting = []
        if val:
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
