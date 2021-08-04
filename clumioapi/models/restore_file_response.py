#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import read_task_hateoas_links

T = TypeVar('T', bound='RestoreFileResponse')


class RestoreFileResponse:
    """Implementation of the 'RestoreFileResponse' model.

    Attributes:
        embedded:
            URLs to pages related to the resource.
        links:
            URLs to pages related to the resource.
        id:
            The Clumio-assigned ID of the restored file.
        passcode:
            passcode that the end-user must use to access the restored
            file, in the case the restored file was emailed to the end-user as part
            of transparent data access.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'id': 'id', 'passcode': 'passcode'}

    def __init__(
        self,
        embedded: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        id: str = None,
        passcode: str = None,
    ) -> None:
        """Constructor for the RestoreFileResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_links.ReadTaskHateoasLinks = embedded
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links
        self.id: str = id
        self.passcode: str = passcode

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
        key = '_embedded'
        embedded = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        id = dictionary.get('id')
        passcode = dictionary.get('passcode')
        # Return an object of this model
        return cls(embedded, links, id, passcode)
