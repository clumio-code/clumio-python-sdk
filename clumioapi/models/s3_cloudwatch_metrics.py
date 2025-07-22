#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_bucket_size_res as s3_bucket_size_res_

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
    _names: dict[str, str] = {
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
        average_object_size_bytes: float,
        average_object_size_bytes_time: str,
        object_count: int,
        object_count_retrieved_time: str,
        size_bytes: int,
        size_bytes_per_storage_class: s3_bucket_size_res_.S3BucketSizeRes,
        size_bytes_retrieved_time: str,
    ) -> None:
        """Constructor for the S3CloudwatchMetrics class."""

        # Initialize members of the class
        self.average_object_size_bytes: float = average_object_size_bytes
        self.average_object_size_bytes_time: str = average_object_size_bytes_time
        self.object_count: int = object_count
        self.object_count_retrieved_time: str = object_count_retrieved_time
        self.size_bytes: int = size_bytes
        self.size_bytes_per_storage_class: s3_bucket_size_res_.S3BucketSizeRes = (
            size_bytes_per_storage_class
        )
        self.size_bytes_retrieved_time: str = size_bytes_retrieved_time

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
        val = dictionary['average_object_size_bytes']
        val_average_object_size_bytes = val

        val = dictionary['average_object_size_bytes_time']
        val_average_object_size_bytes_time = val

        val = dictionary['object_count']
        val_object_count = val

        val = dictionary['object_count_retrieved_time']
        val_object_count_retrieved_time = val

        val = dictionary['size_bytes']
        val_size_bytes = val

        val = dictionary['size_bytes_per_storage_class']
        val_size_bytes_per_storage_class = s3_bucket_size_res_.S3BucketSizeRes.from_dictionary(val)

        val = dictionary['size_bytes_retrieved_time']
        val_size_bytes_retrieved_time = val

        # Return an object of this model
        return cls(
            val_average_object_size_bytes,  # type: ignore
            val_average_object_size_bytes_time,  # type: ignore
            val_object_count,  # type: ignore
            val_object_count_retrieved_time,  # type: ignore
            val_size_bytes,  # type: ignore
            val_size_bytes_per_storage_class,  # type: ignore
            val_size_bytes_retrieved_time,  # type: ignore
        )
