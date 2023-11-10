#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import prefix_filter

T = TypeVar('T', bound='ObjectFilter')


class ObjectFilter:
    """Implementation of the 'ObjectFilter' model.

    ObjectFilterdefines which objects will be backed up.

    Attributes:
        exclude_prefix_expressions:
            A list of desired object prefixes to exclude in this protection group's backups.
            An object that matches any of these prefixes will not be in the backup, even if
            it
            matches an include expression. A wildcard * can be used to match any number of
            characters, except for the / character that is used as a folder separator, and
            must
            be matched explicitly. If an asterisk * needs to be matched explicitly, escape
            the
            asterisk with \\*.
        include_prefix_expressions:
            A list of desired object prefixes to include in this protection group's backups.
            If this input is non-empty, an object must match one of the given prefixes to be
            included in the backup. A wildcard * can be used to match any number of
            characters,
            except for the / character that is used as a folder separator, and must be
            matched
            explicitly. If an asterisk * needs to be matched explicitly, escape the asterisk
            with \\*.
        latest_version_only:
            Whether to back up only the latest object version.
        prefix_filters:
            DEPRECATED: Please use the new include_prefix_expressions and
            exclude_prefix_expressions fields to specify all desired prefix constraints. Any
            prefix filters here will be converted to the new expression fields.
        storage_classes:
            Storage class to include in the backup. If not specified, then all objects
            across all storage
            classes will be backed up. Valid values are: `S3 Standard`, `S3 Standard-IA`,
            `S3 Intelligent-Tiering`, and `S3 One Zone-IA`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'exclude_prefix_expressions': 'exclude_prefix_expressions',
        'include_prefix_expressions': 'include_prefix_expressions',
        'latest_version_only': 'latest_version_only',
        'prefix_filters': 'prefix_filters',
        'storage_classes': 'storage_classes',
    }

    def __init__(
        self,
        exclude_prefix_expressions: Sequence[str] = None,
        include_prefix_expressions: Sequence[str] = None,
        latest_version_only: bool = None,
        prefix_filters: Sequence[prefix_filter.PrefixFilter] = None,
        storage_classes: Sequence[str] = None,
    ) -> None:
        """Constructor for the ObjectFilter class."""

        # Initialize members of the class
        self.exclude_prefix_expressions: Sequence[str] = exclude_prefix_expressions
        self.include_prefix_expressions: Sequence[str] = include_prefix_expressions
        self.latest_version_only: bool = latest_version_only
        self.prefix_filters: Sequence[prefix_filter.PrefixFilter] = prefix_filters
        self.storage_classes: Sequence[str] = storage_classes

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
        exclude_prefix_expressions = dictionary.get('exclude_prefix_expressions')
        include_prefix_expressions = dictionary.get('include_prefix_expressions')
        latest_version_only = dictionary.get('latest_version_only')
        prefix_filters = None
        if dictionary.get('prefix_filters'):
            prefix_filters = list()
            for value in dictionary.get('prefix_filters'):
                prefix_filters.append(prefix_filter.PrefixFilter.from_dictionary(value))

        storage_classes = dictionary.get('storage_classes')
        # Return an object of this model
        return cls(
            exclude_prefix_expressions,
            include_prefix_expressions,
            latest_version_only,
            prefix_filters,
            storage_classes,
        )
