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
        links: restored_record_links_.RestoredRecordLinks,
        account_native_id: str,
        aws_region: str,
        backup_id: str,
        database_name: str,
        download_link: str,
        expiration_timestamp: str,
        p_id: str,
        query_statement: str,
        resource_id: str,
        row_count: int,
        start_timestamp: str,
        task_id: str,
    ) -> None:
        """Constructor for the RestoredRecord class."""

        # Initialize members of the class
        self.links: restored_record_links_.RestoredRecordLinks = links
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
        val = dictionary['_links']
        val_links = restored_record_links_.RestoredRecordLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['database_name']
        val_database_name = val

        val = dictionary['download_link']
        val_download_link = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['query_statement']
        val_query_statement = val

        val = dictionary['resource_id']
        val_resource_id = val

        val = dictionary['row_count']
        val_row_count = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_id,  # type: ignore
            val_database_name,  # type: ignore
            val_download_link,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_p_id,  # type: ignore
            val_query_statement,  # type: ignore
            val_resource_id,  # type: ignore
            val_row_count,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_task_id,  # type: ignore
        )
