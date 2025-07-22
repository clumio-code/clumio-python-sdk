#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3InstantAccessEndpointRole')


class S3InstantAccessEndpointRole:
    """Implementation of the 'S3InstantAccessEndpointRole' model.

    IAM role which is allowed access to the OLAP endpoint.

    Attributes:
        alias:
            The alias of the IAM role given by the user in the UI.
        arn:
            The ARN of the IAM role.
        p_id:
            The ID of the IAM role. Used as an identifier in the API URL.
        last_modified_timestamp:
            The time when the role was last modified, in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'alias': 'alias',
        'arn': 'arn',
        'p_id': 'id',
        'last_modified_timestamp': 'last_modified_timestamp',
    }

    def __init__(self, alias: str, arn: str, p_id: str, last_modified_timestamp: str) -> None:
        """Constructor for the S3InstantAccessEndpointRole class."""

        # Initialize members of the class
        self.alias: str = alias
        self.arn: str = arn
        self.p_id: str = p_id
        self.last_modified_timestamp: str = last_modified_timestamp

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
        val = dictionary['alias']
        val_alias = val

        val = dictionary['arn']
        val_arn = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['last_modified_timestamp']
        val_last_modified_timestamp = val

        # Return an object of this model
        return cls(
            val_alias,  # type: ignore
            val_arn,  # type: ignore
            val_p_id,  # type: ignore
            val_last_modified_timestamp,  # type: ignore
        )
