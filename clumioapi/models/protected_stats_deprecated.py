#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_stats_deprecated

T = TypeVar('T', bound='ProtectedStatsDeprecated')


class ProtectedStatsDeprecated:
    """Implementation of the 'ProtectedStatsDeprecated' model.

    ProtectedStatsDeprecated contains the compliance stats for policies which are
    protected along withthe unprotected policies count

    Attributes:
        protected:
            ComplianceStatsDeprecated denotes compliance metrics for all entities associated
            with a given type
        unprotected:
            Unprotected count.
    """

    # Create a mapping from Model property names to API property names
    _names = {'protected': 'protected', 'unprotected': 'unprotected'}

    def __init__(
        self,
        protected: compliance_stats_deprecated.ComplianceStatsDeprecated = None,
        unprotected: int = None,
    ) -> None:
        """Constructor for the ProtectedStatsDeprecated class."""

        # Initialize members of the class
        self.protected: compliance_stats_deprecated.ComplianceStatsDeprecated = protected
        self.unprotected: int = unprotected

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
        key = 'protected'
        protected = (
            compliance_stats_deprecated.ComplianceStatsDeprecated.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        unprotected = dictionary.get('unprotected')
        # Return an object of this model
        return cls(protected, unprotected)
