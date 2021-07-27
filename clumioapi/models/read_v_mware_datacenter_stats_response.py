#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import v_mware_datacenter_stats_links

T = TypeVar('T', bound='ReadVMwareDatacenterStatsResponse')


class ReadVMwareDatacenterStatsResponse:
    """Implementation of the 'ReadVMwareDatacenterStatsResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        compliant_count:
            The total number of compliant entities.
        deactivated_count:
            The total number of entities associated with deactivated policies.
        has_seeding_entities:
            Determines whether one or more entities is currently seeding or waiting for
            seeding.
            If set to `true`, at least one entity is currently seeding or waiting for
            seeding.
        non_compliant_count:
            The total number of non-compliant entities.
        protected_count:
            The number of entities with protection applied.
        unprotected_count:
            The number of entities without protection applied.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'compliant_count': 'compliant_count',
        'deactivated_count': 'deactivated_count',
        'has_seeding_entities': 'has_seeding_entities',
        'non_compliant_count': 'non_compliant_count',
        'protected_count': 'protected_count',
        'unprotected_count': 'unprotected_count',
    }

    def __init__(
        self,
        etag: str = None,
        links: v_mware_datacenter_stats_links.VMwareDatacenterStatsLinks = None,
        compliant_count: int = None,
        deactivated_count: int = None,
        has_seeding_entities: bool = None,
        non_compliant_count: int = None,
        protected_count: int = None,
        unprotected_count: int = None,
    ) -> None:
        """Constructor for the ReadVMwareDatacenterStatsResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: v_mware_datacenter_stats_links.VMwareDatacenterStatsLinks = links
        self.compliant_count: int = compliant_count
        self.deactivated_count: int = deactivated_count
        self.has_seeding_entities: bool = has_seeding_entities
        self.non_compliant_count: int = non_compliant_count
        self.protected_count: int = protected_count
        self.unprotected_count: int = unprotected_count

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            v_mware_datacenter_stats_links.VMwareDatacenterStatsLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        compliant_count = dictionary.get('compliant_count')
        deactivated_count = dictionary.get('deactivated_count')
        has_seeding_entities = dictionary.get('has_seeding_entities')
        non_compliant_count = dictionary.get('non_compliant_count')
        protected_count = dictionary.get('protected_count')
        unprotected_count = dictionary.get('unprotected_count')
        # Return an object of this model
        return cls(
            etag,
            links,
            compliant_count,
            deactivated_count,
            has_seeding_entities,
            non_compliant_count,
            protected_count,
            unprotected_count,
        )
