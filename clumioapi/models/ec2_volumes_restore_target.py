#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    ec2_restore_ebs_block_device_mapping as ec2_restore_ebs_block_device_mapping_
import requests

T = TypeVar('T', bound='EC2VolumesRestoreTarget')


@dataclasses.dataclass
class EC2VolumesRestoreTarget:
    """Implementation of the 'EC2VolumesRestoreTarget' model.

    The target configuration for the volumes to be restored.

    Attributes:
        AwsAz:
            The availability zone for restoring the volumes unattached. either this or
            target_instance_native_id needs to be specified.

        EbsBlockDeviceMappings:
            Block device mappings chosen for the ebs volumes being restored.

        EnvironmentId:
            The clumio-assigned id of the aws environment to be used as the restore
            destination.
            use the [get /datasources/aws/environments](#operation/list-aws-environments)
            endpoint
            to fetch valid values.

        TargetInstanceNativeId:
            The aws native id of the ec2 instance to be used to attach the restored volumes.
            if not present, then aws_az need to be specified.

    """

    AwsAz: str | None = None
    EbsBlockDeviceMappings: (
        Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
    ) = None
    EnvironmentId: str | None = None
    TargetInstanceNativeId: str | None = None

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
        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('ebs_block_device_mappings', None)

        val_ebs_block_device_mappings = []
        if val:
            for value in val:
                val_ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('target_instance_native_id', None)
        val_target_instance_native_id = val

        # Return an object of this model
        return cls(
            val_aws_az,
            val_ebs_block_device_mappings,
            val_environment_id,
            val_target_instance_native_id,
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
