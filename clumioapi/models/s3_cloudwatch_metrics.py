#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_bucket_size_res as s3_bucket_size_res_
import requests

T = TypeVar('T', bound='S3CloudwatchMetrics')


@dataclasses.dataclass
class S3CloudwatchMetrics:
    """Implementation of the 'S3CloudwatchMetrics' model.

    The Cloudwatch metrics of the bucket.

    Attributes:
        AverageObjectSizeBytes:
            The average size of object in bucket.

        AverageObjectSizeBytesTime:
            Timestamp when average size of the bucket is calculated.

        ObjectCount:
            Number of objects in bucket.

        ObjectCountRetrievedTime:
            Timestamp when cloudwatch reported the bucket object count.

        SizeBytes:
            Size of bucket in bytes.

        SizeBytesPerStorageClass:
            The size breakdown in bytes with timestamps of a bucket per storage class.

        SizeBytesRetrievedTime:
            Timestamp when cloudwatch reported the bucket size.

    """

    AverageObjectSizeBytes: float | None = None
    AverageObjectSizeBytesTime: str | None = None
    ObjectCount: int | None = None
    ObjectCountRetrievedTime: str | None = None
    SizeBytes: int | None = None
    SizeBytesPerStorageClass: s3_bucket_size_res_.S3BucketSizeRes | None = None
    SizeBytesRetrievedTime: str | None = None

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
        val = dictionary.get('average_object_size_bytes', None)
        val_average_object_size_bytes = val

        val = dictionary.get('average_object_size_bytes_time', None)
        val_average_object_size_bytes_time = val

        val = dictionary.get('object_count', None)
        val_object_count = val

        val = dictionary.get('object_count_retrieved_time', None)
        val_object_count_retrieved_time = val

        val = dictionary.get('size_bytes', None)
        val_size_bytes = val

        val = dictionary.get('size_bytes_per_storage_class', None)
        val_size_bytes_per_storage_class = s3_bucket_size_res_.S3BucketSizeRes.from_dictionary(val)

        val = dictionary.get('size_bytes_retrieved_time', None)
        val_size_bytes_retrieved_time = val

        # Return an object of this model
        return cls(
            val_average_object_size_bytes,
            val_average_object_size_bytes_time,
            val_object_count,
            val_object_count_retrieved_time,
            val_size_bytes,
            val_size_bytes_per_storage_class,
            val_size_bytes_retrieved_time,
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
