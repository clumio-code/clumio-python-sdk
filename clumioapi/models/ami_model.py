#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AmiModel')


class AmiModel:
    """Implementation of the 'AmiModel' model.

    An Amazon Machine Image is a supported and maintained image provided by AWSthat
    provides the information required to launch an instance.

    Attributes:
        ami_native_id:
            The AWS-assigned ID of the AMI.
        architecture:
            The architecture of the AMI. Possible values include 'i386', 'x86_64', and
            'arm64'.
        has_ena_support:
            Specifies whether enhanced networking with ENA is enabled.
        hypervisor_type:
            The hypervisor type of the AMI. Possible values include 'ovm' and 'xen'.
        image_type:
            Type of Image (machine | kernel | ramdisk ).
        is_public:
            A Boolean that indicates whether the image is public.
        name:
            The name of the AMI.
        number_of_ebs_volumes:
            Number of ebs volumes.
        number_of_ephemeral_volumes:
            Number of ephemeral volumes.
        owner_id:
            The ID of the Amazon Web Services account that owns the image.
        platform:
            The platform of the AMI. Possible values include "windows" and "linux".
        root_device_name:
            The name of the root device used by the AMI.
        root_device_type:
            The type of root device used by the AMI.
        sriov_net_support:
            A value of simple indicates that enhanced networking with the Intel 82599 VF
            interface is enabled.
        virtualization_type:
            The type of virtualization of the AMI. Possible values include 'hvm' and
            'paravirtual.'
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'ami_native_id': 'ami_native_id',
        'architecture': 'architecture',
        'has_ena_support': 'has_ena_support',
        'hypervisor_type': 'hypervisor_type',
        'image_type': 'image_type',
        'is_public': 'is_public',
        'name': 'name',
        'number_of_ebs_volumes': 'number_of_ebs_volumes',
        'number_of_ephemeral_volumes': 'number_of_ephemeral_volumes',
        'owner_id': 'owner_id',
        'platform': 'platform',
        'root_device_name': 'root_device_name',
        'root_device_type': 'root_device_type',
        'sriov_net_support': 'sriov_net_support',
        'virtualization_type': 'virtualization_type',
    }

    def __init__(
        self,
        ami_native_id: str,
        architecture: str,
        has_ena_support: bool,
        hypervisor_type: str,
        image_type: str,
        is_public: bool,
        name: str,
        number_of_ebs_volumes: int,
        number_of_ephemeral_volumes: int,
        owner_id: str,
        platform: str,
        root_device_name: str,
        root_device_type: str,
        sriov_net_support: str,
        virtualization_type: str,
    ) -> None:
        """Constructor for the AmiModel class."""

        # Initialize members of the class
        self.ami_native_id: str = ami_native_id
        self.architecture: str = architecture
        self.has_ena_support: bool = has_ena_support
        self.hypervisor_type: str = hypervisor_type
        self.image_type: str = image_type
        self.is_public: bool = is_public
        self.name: str = name
        self.number_of_ebs_volumes: int = number_of_ebs_volumes
        self.number_of_ephemeral_volumes: int = number_of_ephemeral_volumes
        self.owner_id: str = owner_id
        self.platform: str = platform
        self.root_device_name: str = root_device_name
        self.root_device_type: str = root_device_type
        self.sriov_net_support: str = sriov_net_support
        self.virtualization_type: str = virtualization_type

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
        val = dictionary['ami_native_id']
        val_ami_native_id = val

        val = dictionary['architecture']
        val_architecture = val

        val = dictionary['has_ena_support']
        val_has_ena_support = val

        val = dictionary['hypervisor_type']
        val_hypervisor_type = val

        val = dictionary['image_type']
        val_image_type = val

        val = dictionary['is_public']
        val_is_public = val

        val = dictionary['name']
        val_name = val

        val = dictionary['number_of_ebs_volumes']
        val_number_of_ebs_volumes = val

        val = dictionary['number_of_ephemeral_volumes']
        val_number_of_ephemeral_volumes = val

        val = dictionary['owner_id']
        val_owner_id = val

        val = dictionary['platform']
        val_platform = val

        val = dictionary['root_device_name']
        val_root_device_name = val

        val = dictionary['root_device_type']
        val_root_device_type = val

        val = dictionary['sriov_net_support']
        val_sriov_net_support = val

        val = dictionary['virtualization_type']
        val_virtualization_type = val

        # Return an object of this model
        return cls(
            val_ami_native_id,  # type: ignore
            val_architecture,  # type: ignore
            val_has_ena_support,  # type: ignore
            val_hypervisor_type,  # type: ignore
            val_image_type,  # type: ignore
            val_is_public,  # type: ignore
            val_name,  # type: ignore
            val_number_of_ebs_volumes,  # type: ignore
            val_number_of_ephemeral_volumes,  # type: ignore
            val_owner_id,  # type: ignore
            val_platform,  # type: ignore
            val_root_device_name,  # type: ignore
            val_root_device_type,  # type: ignore
            val_sriov_net_support,  # type: ignore
            val_virtualization_type,  # type: ignore
        )
