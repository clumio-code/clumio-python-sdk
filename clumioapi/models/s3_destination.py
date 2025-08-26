#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_access_control_translation as s3_access_control_translation_
from clumioapi.models import s3_encryption_configuration as s3_encryption_configuration_
from clumioapi.models import s3_metrics as s3_metrics_
from clumioapi.models import s3_replication_time as s3_replication_time_
import requests

T = TypeVar('T', bound='S3Destination')


@dataclasses.dataclass
class S3Destination:
    """Implementation of the 'S3Destination' model.

        Specifies information about where to publish analysis or configuration results.

        Attributes:
            AccessControlTranslation:
                A container for information about access control for replicas.

            Account:
                Destination bucket owner account id.

            Bucket:
                The amazon resource name (arn) of the bucket where
    you want amazon s3 to store the results.

            EncryptionConfiguration:
                Specifies encryption-related information for an amazon s3 bucket
    that is a destination for replicated objects.

            Metrics:
                A container specifying replication metrics-related settings
    enabling replication metrics and events.

            ReplicationTime:
                A container specifying s3 replication time control (s3 rtc)
    related information.

            StorageClass:
                The storage class to use when replicating objects.

    """

    AccessControlTranslation: s3_access_control_translation_.S3AccessControlTranslation | None = (
        None
    )
    Account: str | None = None
    Bucket: str | None = None
    EncryptionConfiguration: s3_encryption_configuration_.S3EncryptionConfiguration | None = None
    Metrics: s3_metrics_.S3Metrics | None = None
    ReplicationTime: s3_replication_time_.S3ReplicationTime | None = None
    StorageClass: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('access_control_translation', None)
        val_access_control_translation = (
            s3_access_control_translation_.S3AccessControlTranslation.from_dictionary(val)
        )

        val = dictionary.get('account', None)
        val_account = val

        val = dictionary.get('bucket', None)
        val_bucket = val

        val = dictionary.get('encryption_configuration', None)
        val_encryption_configuration = (
            s3_encryption_configuration_.S3EncryptionConfiguration.from_dictionary(val)
        )

        val = dictionary.get('metrics', None)
        val_metrics = s3_metrics_.S3Metrics.from_dictionary(val)

        val = dictionary.get('replication_time', None)
        val_replication_time = s3_replication_time_.S3ReplicationTime.from_dictionary(val)

        val = dictionary.get('storage_class', None)
        val_storage_class = val

        # Return an object of this model
        return cls(
            val_access_control_translation,
            val_account,
            val_bucket,
            val_encryption_configuration,
            val_metrics,
            val_replication_time,
            val_storage_class,
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
