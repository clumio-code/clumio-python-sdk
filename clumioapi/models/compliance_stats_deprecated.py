#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ComplianceStatsDeprecated')


class ComplianceStatsDeprecated:
    """Implementation of the 'ComplianceStatsDeprecated' model.

    ComplianceStatsDeprecated denotes compliance metrics for all entities associated
    with a given type

    Attributes:
        COMPLIANT:
            Compliant count.
        DEACTIVATED:
            Deactivated count.
        NON_COMPLIANT:
            Non-Compliant count.
        SEEDING:
            Seeding count.
        WAIT_FOR_SEEDING:
            Wait-for-seeding count.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'COMPLIANT': 'COMPLIANT',
        'DEACTIVATED': 'DEACTIVATED',
        'NON_COMPLIANT': 'NON_COMPLIANT',
        'SEEDING': 'SEEDING',
        'WAIT_FOR_SEEDING': 'WAIT_FOR_SEEDING',
    }

    def __init__(
        self,
        COMPLIANT: int = None,
        DEACTIVATED: int = None,
        NON_COMPLIANT: int = None,
        SEEDING: int = None,
        WAIT_FOR_SEEDING: int = None,
    ) -> None:
        """Constructor for the ComplianceStatsDeprecated class."""

        # Initialize members of the class
        self.COMPLIANT: int = COMPLIANT
        self.DEACTIVATED: int = DEACTIVATED
        self.NON_COMPLIANT: int = NON_COMPLIANT
        self.SEEDING: int = SEEDING
        self.WAIT_FOR_SEEDING: int = WAIT_FOR_SEEDING

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
        COMPLIANT = dictionary.get('COMPLIANT')
        DEACTIVATED = dictionary.get('DEACTIVATED')
        NON_COMPLIANT = dictionary.get('NON_COMPLIANT')
        SEEDING = dictionary.get('SEEDING')
        WAIT_FOR_SEEDING = dictionary.get('WAIT_FOR_SEEDING')
        # Return an object of this model
        return cls(COMPLIANT, DEACTIVATED, NON_COMPLIANT, SEEDING, WAIT_FOR_SEEDING)
