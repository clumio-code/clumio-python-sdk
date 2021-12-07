#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_connection_config_model

T = TypeVar('T', bound='CreateConnectionTemplateV1Request')


class CreateConnectionTemplateV1Request:
    """Implementation of the 'CreateConnectionTemplateV1Request' model.

    The body of the request.

    Attributes:
        config:

    """

    # Create a mapping from Model property names to API property names
    _names = {'config': 'config'}

    def __init__(self, config: aws_connection_config_model.AWSConnectionConfigModel = None) -> None:
        """Constructor for the CreateConnectionTemplateV1Request class."""

        # Initialize members of the class
        self.config: aws_connection_config_model.AWSConnectionConfigModel = config

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
        key = 'config'
        config = (
            aws_connection_config_model.AWSConnectionConfigModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(config)
