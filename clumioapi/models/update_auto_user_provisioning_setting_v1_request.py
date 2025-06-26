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
    _names = {'is_enabled': 'is_enabled'}

    def __init__(self, is_enabled: bool = None) -> None:
        """Constructor for the UpdateAutoUserProvisioningSettingV1Request class."""

        # Initialize members of the class
        self.is_enabled: bool = is_enabled

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
        is_enabled = dictionary.get('is_enabled')
        # Return an object of this model
        return cls(is_enabled)
