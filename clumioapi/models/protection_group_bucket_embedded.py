#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupBucketEmbedded')


class ProtectionGroupBucketEmbedded:
    """Implementation of the 'ProtectionGroupBucketEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_organizational_unit:
            This embed is for internal use only since an embed results in additional HTTP
            calls. "embeds" can affect the performance of "list" API calls as an embed is
            processed once per item in the result list.
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_organizational_unit': 'read-organizational-unit',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(self, read_organizational_unit: object, read_policy_definition: object) -> None:
        """Constructor for the ProtectionGroupBucketEmbedded class."""

        # Initialize members of the class
        self.read_organizational_unit: object = read_organizational_unit
        self.read_policy_definition: object = read_policy_definition

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
        val = dictionary['read-organizational-unit']
        val_read_organizational_unit = val

        val = dictionary['read-policy-definition']
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_read_organizational_unit,  # type: ignore
            val_read_policy_definition,  # type: ignore
        )
