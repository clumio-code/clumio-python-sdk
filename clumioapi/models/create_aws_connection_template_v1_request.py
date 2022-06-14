#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protect_template_config

T = TypeVar('T', bound='CreateAwsConnectionTemplateV1Request')


class CreateAwsConnectionTemplateV1Request:
    """Implementation of the 'CreateAwsConnectionTemplateV1Request' model.

    The body of the request.

    Attributes:
        protect:

    """

    # Create a mapping from Model property names to API property names
    _names = {'protect': 'protect'}

    def __init__(self, protect: protect_template_config.ProtectTemplateConfig = None) -> None:
        """Constructor for the CreateAwsConnectionTemplateV1Request class."""

        # Initialize members of the class
        self.protect: protect_template_config.ProtectTemplateConfig = protect

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
        key = 'protect'
        protect = (
            protect_template_config.ProtectTemplateConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(protect)
