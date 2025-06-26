#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import restored_record_links

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
    _names = {
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
        links: restored_record_links.RestoredRecordLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        backup_id: str = None,
        database_name: str = None,
        download_link: str = None,
        expiration_timestamp: str = None,
        p_id: str = None,
        query_statement: str = None,
        resource_id: str = None,
        row_count: int = None,
        start_timestamp: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the RestoredRecord class."""

        # Initialize members of the class
        self.links: restored_record_links.RestoredRecordLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.backup_id: str = backup_id
        self.database_name: str = database_name
        self.download_link: str = download_link
        self.expiration_timestamp: str = expiration_timestamp
        self.p_id: str = p_id
        self.query_statement: str = query_statement
        self.resource_id: str = resource_id
        self.row_count: int = row_count
        self.start_timestamp: str = start_timestamp
        self.task_id: str = task_id

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
            restored_record_links.RestoredRecordLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        backup_id = dictionary.get('backup_id')
        database_name = dictionary.get('database_name')
        download_link = dictionary.get('download_link')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        p_id = dictionary.get('id')
        query_statement = dictionary.get('query_statement')
        resource_id = dictionary.get('resource_id')
        row_count = dictionary.get('row_count')
        start_timestamp = dictionary.get('start_timestamp')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(
            links,
            account_native_id,
            aws_region,
            backup_id,
            database_name,
            download_link,
            expiration_timestamp,
            p_id,
            query_statement,
            resource_id,
            row_count,
            start_timestamp,
            task_id,
        )
