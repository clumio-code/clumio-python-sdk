#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import restored_record_links as restored_record_links_
import requests

T = TypeVar('T', bound='RestoredRecord')


@dataclasses.dataclass
class RestoredRecord:
    """Implementation of the 'RestoredRecord' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account with this record.

        AwsRegion:
            The aws region associated with this record. for example, `us-west-2`.

        BackupId:
            The clumio-assigned id of the backup associated with this record.

        DatabaseName:
            The aws-assigned name of the database associated with this record.

        DownloadLink:
            The download link of the query result.

        ExpirationTimestamp:
            The timestamp of when the record will expire. represented in rfc-3339 format.

        Id:
            The clumio-assigned id of the restored record.

        QueryStatement:
            The sql query statement which produced this record.

        ResourceId:
            The clumio-assigned id of the rds resource associated with this record.

        RowCount:
            The number of rows produced by the query.

        StartTimestamp:
            The timestamp of when the query was executed. represented in rfc-3339 format.

        TaskId:
            The clumio-assigned id of the task which generated the restored record.

    """

    Links: restored_record_links_.RestoredRecordLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BackupId: str | None = None
    DatabaseName: str | None = None
    DownloadLink: str | None = None
    ExpirationTimestamp: str | None = None
    Id: str | None = None
    QueryStatement: str | None = None
    ResourceId: str | None = None
    RowCount: int | None = None
    StartTimestamp: str | None = None
    TaskId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val_id = val

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
            val_id,
            val_query_statement,
            val_resource_id,
            val_row_count,
            val_start_timestamp,
            val_task_id,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
