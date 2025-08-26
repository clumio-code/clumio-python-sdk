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
        ami_native_id: str | None = None,
        architecture: str | None = None,
        has_ena_support: bool | None = None,
        hypervisor_type: str | None = None,
        image_type: str | None = None,
        is_public: bool | None = None,
        name: str | None = None,
        number_of_ebs_volumes: int | None = None,
        number_of_ephemeral_volumes: int | None = None,
        owner_id: str | None = None,
        platform: str | None = None,
        root_device_name: str | None = None,
        root_device_type: str | None = None,
        sriov_net_support: str | None = None,
        virtualization_type: str | None = None,
    ) -> None:
        """Constructor for the AmiModel class."""

        # Initialize members of the class
        self.ami_native_id: str | None = ami_native_id
        self.architecture: str | None = architecture
        self.has_ena_support: bool | None = has_ena_support
        self.hypervisor_type: str | None = hypervisor_type
        self.image_type: str | None = image_type
        self.is_public: bool | None = is_public
        self.name: str | None = name
        self.number_of_ebs_volumes: int | None = number_of_ebs_volumes
        self.number_of_ephemeral_volumes: int | None = number_of_ephemeral_volumes
        self.owner_id: str | None = owner_id
        self.platform: str | None = platform
        self.root_device_name: str | None = root_device_name
        self.root_device_type: str | None = root_device_type
        self.sriov_net_support: str | None = sriov_net_support
        self.virtualization_type: str | None = virtualization_type

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
