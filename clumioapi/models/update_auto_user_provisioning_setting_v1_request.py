#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateAutoUserProvisioningSettingV1Request')


class UpdateAutoUserProvisioningSettingV1Request:
    """Implementation of the 'UpdateAutoUserProvisioningSettingV1Request' model.

    Attributes:
        is_enabled:
            Whether auto user provisioning is enabled or not.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'is_enabled': 'is_enabled'}

    def __init__(self, is_enabled: bool) -> None:
        """Constructor for the UpdateAutoUserProvisioningSettingV1Request class."""

        # Initialize members of the class
        self.is_enabled: bool = is_enabled

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
        val = dictionary['is_enabled']
        val_is_enabled = val

        # Return an object of this model
        return cls(
            val_is_enabled,  # type: ignore
        )
