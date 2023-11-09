#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links
from clumioapi.models import host

T = TypeVar('T', bound='CreateHcmHostResponse')


class CreateHcmHostResponse:
    """Implementation of the 'CreateHcmHostResponse' model.

    Attributes:
        links:
            HateoasCommonLinks are the common fields for HATEOAS response.
        hosts:
            Hosts that are successfully added
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'hosts': 'hosts'}

    def __init__(
        self,
        links: hateoas_common_links.HateoasCommonLinks = None,
        hosts: Sequence[host.Host] = None,
    ) -> None:
        """Constructor for the CreateHcmHostResponse class."""

        # Initialize members of the class
        self.links: hateoas_common_links.HateoasCommonLinks = links
        self.hosts: Sequence[host.Host] = hosts

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
        key = '_links'
        links = (
            hateoas_common_links.HateoasCommonLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        hosts = None
        if dictionary.get('hosts'):
            hosts = list()
            for value in dictionary.get('hosts'):
                hosts.append(host.Host.from_dictionary(value))

        # Return an object of this model
        return cls(links, hosts)
