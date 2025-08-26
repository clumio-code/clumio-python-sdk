#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import restored_record_links as restored_record_links_

T = TypeVar('T', bound='RestoredRecord')


class RestoredRecord:
    """Implementation of the 'RestoredRecord' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account with this record.
        aws_region:
            The AWS region associated with this record. For example, `us-west-2`.
        backup_id:
            The Clumio-assigned ID of the backup associated with this record.
        database_name:
            The AWS-assigned name of the database associated with this record.
        download_link:
            The download link of the query result.
        expiration_timestamp:
            The timestamp of when the record will expire. Represented in RFC-3339 format.
        p_id:
            The Clumio-assigned ID of the restored record.
        query_statement:
            The SQL query statement which produced this record.
        resource_id:
            The Clumio-assigned ID of the RDS resource associated with this record.
        row_count:
            The number of rows produced by the query.
        start_timestamp:
            The timestamp of when the query was executed. Represented in RFC-3339 format.
        task_id:
            The Clumio-assigned ID of the task which generated the restored record.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'backup_id': 'backup_id',
        'database_name': 'database_name',
        'download_link': 'download_link',
        'expiration_timestamp': 'expiration_timestamp',
        'p_id': 'id',
        'query_statement': 'query_statement',
        'resource_id': 'resource_id',
        'row_count': 'row_count',
        'start_timestamp': 'start_timestamp',
        'task_id': 'task_id',
    }

    def __init__(
        self,
        links: restored_record_links_.RestoredRecordLinks | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        backup_id: str | None = None,
        database_name: str | None = None,
        download_link: str | None = None,
        expiration_timestamp: str | None = None,
        p_id: str | None = None,
        query_statement: str | None = None,
        resource_id: str | None = None,
        row_count: int | None = None,
        start_timestamp: str | None = None,
        task_id: str | None = None,
    ) -> None:
        """Constructor for the RestoredRecord class."""

        # Initialize members of the class
        self.links: restored_record_links_.RestoredRecordLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.backup_id: str | None = backup_id
        self.database_name: str | None = database_name
        self.download_link: str | None = download_link
        self.expiration_timestamp: str | None = expiration_timestamp
        self.p_id: str | None = p_id
        self.query_statement: str | None = query_statement
        self.resource_id: str | None = resource_id
        self.row_count: int | None = row_count
        self.start_timestamp: str | None = start_timestamp
        self.task_id: str | None = task_id

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_links', None)
        val_links = restored_record_links_.RestoredRecordLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('database_name', None)
        val_database_name = val

        val = dictionary.get('download_link', None)
        val_download_link = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('query_statement', None)
        val_query_statement = val

        val = dictionary.get('resource_id', None)
        val_resource_id = val

        val = dictionary.get('row_count', None)
        val_row_count = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_account_native_id,
            val_aws_region,
            val_backup_id,
            val_database_name,
            val_download_link,
            val_expiration_timestamp,
            val_p_id,
            val_query_statement,
            val_resource_id,
            val_row_count,
            val_start_timestamp,
            val_task_id,
        )
