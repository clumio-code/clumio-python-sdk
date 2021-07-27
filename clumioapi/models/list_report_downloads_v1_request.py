#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ListReportDownloadsV1Request')


class ListReportDownloadsV1Request:
    """Implementation of the 'ListReportDownloadsV1Request' model.

    Attributes:
        filter:

            +-----------------+------------------+-----------------------------------------+
            |      Field      | Filter Condition |               Description               |
            +=================+==================+=========================================+
            | start_timestamp | $gte, $lt        | Start timestamp denotes the time filter |
            |                 |                  | for listing report CSV downloads.       |
            |                 |                  | $gte and $lt accept RFC-3999            |
            |                 |                  | timestamps. For example,                |
            |                 |                  |                                         |
            |                 |                  | "filter":"{"start_timestamp":{"$gt":"20 |
            |                 |                  | 19-10-12T07:20:50.52Z"}}"               |
            |                 |                  |                                         |
            |                 |                  |                                         |
            +-----------------+------------------+-----------------------------------------+
            | report_type     | $in              |                                         |
            |                 |                  | Filter report downloaded records whose  |
            |                 |                  | type is one of the given values. The    |
            |                 |                  | possible values are: "activity",        |
            |                 |                  | "compliance".                           |
            |                 |                  |                                         |
            |                 |                  | filter={"report_type":{"$in":["complian |
            |                 |                  | ce"]}}                                  |
            |                 |                  |                                         |
            |                 |                  |                                         |
            +-----------------+------------------+-----------------------------------------+

            For more information about filtering, refer to the
            Filtering section of this guide.
            in: query
        limit:
            Limits the size of the response on each page to the specified number of items.
            in: query
        start:
            Sets the page number used to browse the collection.
            Pages are indexed starting from 1 (i.e., `start=1`).
            in: query
    """

    # Create a mapping from Model property names to API property names
    _names = {'filter': 'filter', 'limit': 'limit', 'start': 'start'}

    def __init__(self, filter: str = None, limit: int = None, start: str = None) -> None:
        """Constructor for the ListReportDownloadsV1Request class."""

        # Initialize members of the class
        self.filter: str = filter
        self.limit: int = limit
        self.start: str = start

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
        filter = dictionary.get('filter')
        limit = dictionary.get('limit')
        start = dictionary.get('start')
        # Return an object of this model
        return cls(filter, limit, start)
