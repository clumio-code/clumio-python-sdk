#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_access_control_translation
from clumioapi.models import s3_encryption_configuration
from clumioapi.models import s3_metrics
from clumioapi.models import s3_replication_time

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
    _names = {
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
        access_control_translation: s3_access_control_translation.S3AccessControlTranslation = None,
        account: str = None,
        bucket: str = None,
        encryption_configuration: s3_encryption_configuration.S3EncryptionConfiguration = None,
        metrics: s3_metrics.S3Metrics = None,
        replication_time: s3_replication_time.S3ReplicationTime = None,
        storage_class: str = None,
    ) -> None:
        """Constructor for the S3Destination class."""

        # Initialize members of the class
        self.access_control_translation: (
            s3_access_control_translation.S3AccessControlTranslation
        ) = access_control_translation
        self.account: str = account
        self.bucket: str = bucket
        self.encryption_configuration: s3_encryption_configuration.S3EncryptionConfiguration = (
            encryption_configuration
        )
        self.metrics: s3_metrics.S3Metrics = metrics
        self.replication_time: s3_replication_time.S3ReplicationTime = replication_time
        self.storage_class: str = storage_class

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
        key = 'access_control_translation'
        access_control_translation = (
            s3_access_control_translation.S3AccessControlTranslation.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        account = dictionary.get('account')
        bucket = dictionary.get('bucket')
        key = 'encryption_configuration'
        encryption_configuration = (
            s3_encryption_configuration.S3EncryptionConfiguration.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'metrics'
        metrics = (
            s3_metrics.S3Metrics.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'replication_time'
        replication_time = (
            s3_replication_time.S3ReplicationTime.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        storage_class = dictionary.get('storage_class')
        # Return an object of this model
        return cls(
            access_control_translation,
            account,
            bucket,
            encryption_configuration,
            metrics,
            replication_time,
            storage_class,
        )
