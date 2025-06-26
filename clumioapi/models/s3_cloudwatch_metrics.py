#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_bucket_size_res

T = TypeVar('T', bound='S3CloudwatchMetrics')


class S3CloudwatchMetrics:
    """Implementation of the 'S3CloudwatchMetrics' model.

    The Cloudwatch metrics of the bucket.

    Attributes:
        average_object_size_bytes:
            The average size of object in bucket.
        average_object_size_bytes_time:
            Timestamp when average size of the bucket is calculated.
        object_count:
            Number of objects in bucket.
        object_count_retrieved_time:
            Timestamp when CloudWatch reported the bucket object count.
        size_bytes:
            Size of bucket in bytes.
        size_bytes_per_storage_class:
            The size breakdown in bytes with timestamps of a bucket per storage class.
        size_bytes_retrieved_time:
            Timestamp when CloudWatch reported the bucket size.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'average_object_size_bytes': 'average_object_size_bytes',
        'average_object_size_bytes_time': 'average_object_size_bytes_time',
        'object_count': 'object_count',
        'object_count_retrieved_time': 'object_count_retrieved_time',
        'size_bytes': 'size_bytes',
        'size_bytes_per_storage_class': 'size_bytes_per_storage_class',
        'size_bytes_retrieved_time': 'size_bytes_retrieved_time',
    }

    def __init__(
        self,
        average_object_size_bytes: float = None,
        average_object_size_bytes_time: str = None,
        object_count: int = None,
        object_count_retrieved_time: str = None,
        size_bytes: int = None,
        size_bytes_per_storage_class: s3_bucket_size_res.S3BucketSizeRes = None,
        size_bytes_retrieved_time: str = None,
    ) -> None:
        """Constructor for the S3CloudwatchMetrics class."""

        # Initialize members of the class
        self.average_object_size_bytes: float = average_object_size_bytes
        self.average_object_size_bytes_time: str = average_object_size_bytes_time
        self.object_count: int = object_count
        self.object_count_retrieved_time: str = object_count_retrieved_time
        self.size_bytes: int = size_bytes
        self.size_bytes_per_storage_class: s3_bucket_size_res.S3BucketSizeRes = (
            size_bytes_per_storage_class
        )
        self.size_bytes_retrieved_time: str = size_bytes_retrieved_time

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
        average_object_size_bytes = dictionary.get('average_object_size_bytes')
        average_object_size_bytes_time = dictionary.get('average_object_size_bytes_time')
        object_count = dictionary.get('object_count')
        object_count_retrieved_time = dictionary.get('object_count_retrieved_time')
        size_bytes = dictionary.get('size_bytes')
        key = 'size_bytes_per_storage_class'
        size_bytes_per_storage_class = (
            s3_bucket_size_res.S3BucketSizeRes.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        size_bytes_retrieved_time = dictionary.get('size_bytes_retrieved_time')
        # Return an object of this model
        return cls(
            average_object_size_bytes,
            average_object_size_bytes_time,
            object_count,
            object_count_retrieved_time,
            size_bytes,
            size_bytes_per_storage_class,
            size_bytes_retrieved_time,
        )
