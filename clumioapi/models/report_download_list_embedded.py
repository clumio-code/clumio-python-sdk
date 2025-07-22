#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import report_download as report_download_

T = TypeVar('T', bound='ReportDownloadListEmbedded')


class ReportDownloadListEmbedded:
    """Implementation of the 'ReportDownloadListEmbedded' model.

    _embedded contains the list of items of a list report CSV download query

    Attributes:
        items:
            items denotes the list of CSV downloads in the current scope.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(self, items: Sequence[report_download_.ReportDownload]) -> None:
        """Constructor for the ReportDownloadListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[report_download_.ReportDownload] = items

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
        val = dictionary['items']

        val_items = None
        if val:
            val_items = list()
            for value in val:
                val_items.append(report_download_.ReportDownload.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_items,  # type: ignore
        )
