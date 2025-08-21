#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_access_control_translation as s3_access_control_translation_
from clumioapi.models import s3_encryption_configuration as s3_encryption_configuration_
from clumioapi.models import s3_metrics as s3_metrics_
from clumioapi.models import s3_replication_time as s3_replication_time_

T = TypeVar('T', bound='S3Destination')


class S3Destination:
    """Implementation of the 'S3Destination' model.

    Specifies information about where to publish analysis or configuration results.

    Attributes:
        access_control_translation:
            A container for information about access control for replicas.
        account:
            Destination bucket owner account ID.
        bucket:
            The Amazon Resource Name (ARN) of the bucket where
            you want Amazon S3 to store the results.
        encryption_configuration:
            Specifies encryption-related information for an Amazon S3 bucket
            that is a destination for replicated objects.
        metrics:
            A container specifying replication metrics-related settings
            enabling replication metrics and events.
        replication_time:
            A container specifying S3 Replication Time Control (S3 RTC)
            related information.
        storage_class:
            The storage class to use when replicating objects.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'access_control_translation': 'access_control_translation',
        'account': 'account',
        'bucket': 'bucket',
        'encryption_configuration': 'encryption_configuration',
        'metrics': 'metrics',
        'replication_time': 'replication_time',
        'storage_class': 'storage_class',
    }

    def __init__(
        self,
        access_control_translation: (
            s3_access_control_translation_.S3AccessControlTranslation | None
        ) = None,
        account: str | None = None,
        bucket: str | None = None,
        encryption_configuration: (
            s3_encryption_configuration_.S3EncryptionConfiguration | None
        ) = None,
        metrics: s3_metrics_.S3Metrics | None = None,
        replication_time: s3_replication_time_.S3ReplicationTime | None = None,
        storage_class: str | None = None,
    ) -> None:
        """Constructor for the S3Destination class."""

        # Initialize members of the class
        self.access_control_translation: (
            s3_access_control_translation_.S3AccessControlTranslation | None
        ) = access_control_translation
        self.account: str | None = account
        self.bucket: str | None = bucket
        self.encryption_configuration: (
            s3_encryption_configuration_.S3EncryptionConfiguration | None
        ) = encryption_configuration
        self.metrics: s3_metrics_.S3Metrics | None = metrics
        self.replication_time: s3_replication_time_.S3ReplicationTime | None = replication_time
        self.storage_class: str | None = storage_class

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
