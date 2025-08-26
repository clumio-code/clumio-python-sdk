#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='AmiModel')


@dataclasses.dataclass
class AmiModel:
    """Implementation of the 'AmiModel' model.

        An Amazon Machine Image is a supported and maintained image provided by AWSthat
        provides the information required to launch an instance.

        Attributes:
            AmiNativeId:
                The aws-assigned id of the ami.

            Architecture:
                The architecture of the ami. possible values include 'i386', 'x86_64', and 'arm64'.

            HasEnaSupport:
                Specifies whether enhanced networking with ena is enabled.

            HypervisorType:
                The hypervisor type of the ami. possible values include 'ovm' and 'xen'.

            ImageType:
                Type of image (machine | kernel | ramdisk ).

            IsPublic:
                A boolean that indicates whether the image is public.

            Name:
                The name of the ami.

            NumberOfEbsVolumes:
                Number of ebs volumes.

            NumberOfEphemeralVolumes:
                Number of ephemeral volumes.

            OwnerId:
                The id of the amazon web services account that owns the image.

            Platform:
                The platform of the ami. possible values include "windows" and "linux".

            RootDeviceName:
                The name of the root device used by the ami.

            RootDeviceType:
                The type of root device used by the ami.

            SriovNetSupport:
                A value of simple indicates that enhanced networking with the intel 82599 vf
    interface is enabled.

            VirtualizationType:
                The type of virtualization of the ami. possible values include 'hvm' and 'paravirtual.'.

    """

    AmiNativeId: str | None = None
    Architecture: str | None = None
    HasEnaSupport: bool | None = None
    HypervisorType: str | None = None
    ImageType: str | None = None
    IsPublic: bool | None = None
    Name: str | None = None
    NumberOfEbsVolumes: int | None = None
    NumberOfEphemeralVolumes: int | None = None
    OwnerId: str | None = None
    Platform: str | None = None
    RootDeviceName: str | None = None
    RootDeviceType: str | None = None
    SriovNetSupport: str | None = None
    VirtualizationType: str | None = None

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
        val = dictionary.get('ami_native_id', None)
        val_ami_native_id = val

        val = dictionary.get('architecture', None)
        val_architecture = val

        val = dictionary.get('has_ena_support', None)
        val_has_ena_support = val

        val = dictionary.get('hypervisor_type', None)
        val_hypervisor_type = val

        val = dictionary.get('image_type', None)
        val_image_type = val

        val = dictionary.get('is_public', None)
        val_is_public = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('number_of_ebs_volumes', None)
        val_number_of_ebs_volumes = val

        val = dictionary.get('number_of_ephemeral_volumes', None)
        val_number_of_ephemeral_volumes = val

        val = dictionary.get('owner_id', None)
        val_owner_id = val

        val = dictionary.get('platform', None)
        val_platform = val

        val = dictionary.get('root_device_name', None)
        val_root_device_name = val

        val = dictionary.get('root_device_type', None)
        val_root_device_type = val

        val = dictionary.get('sriov_net_support', None)
        val_sriov_net_support = val

        val = dictionary.get('virtualization_type', None)
        val_virtualization_type = val

        # Return an object of this model
        return cls(
            val_ami_native_id,
            val_architecture,
            val_has_ena_support,
            val_hypervisor_type,
            val_image_type,
            val_is_public,
            val_name,
            val_number_of_ebs_volumes,
            val_number_of_ephemeral_volumes,
            val_owner_id,
            val_platform,
            val_root_device_name,
            val_root_device_type,
            val_sriov_net_support,
            val_virtualization_type,
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
