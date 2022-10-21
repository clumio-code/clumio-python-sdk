#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import move_hosts_source, move_hosts_target

T = TypeVar('T', bound='MoveMssqlHostConnectionsV1Request')


class MoveMssqlHostConnectionsV1Request:
    """Implementation of the 'MoveMssqlHostConnectionsV1Request' model.

    Attributes:
        source:
            The hosts to be moved to a different management subgroup.
        target:
            The target configuration of the hosts to be moved.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: move_hosts_source.MoveHostsSource = None,
        target: move_hosts_target.MoveHostsTarget = None,
    ) -> None:
        """Constructor for the MoveMssqlHostConnectionsV1Request class."""

        # Initialize members of the class
        self.source: move_hosts_source.MoveHostsSource = source
        self.target: move_hosts_target.MoveHostsTarget = target

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
        key = 'source'
        source = (
            move_hosts_source.MoveHostsSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            move_hosts_target.MoveHostsTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
