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
    _names = {
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
        ami_native_id: str = None,
        architecture: str = None,
        has_ena_support: bool = None,
        hypervisor_type: str = None,
        image_type: str = None,
        is_public: bool = None,
        name: str = None,
        number_of_ebs_volumes: int = None,
        number_of_ephemeral_volumes: int = None,
        owner_id: str = None,
        platform: str = None,
        root_device_name: str = None,
        root_device_type: str = None,
        sriov_net_support: str = None,
        virtualization_type: str = None,
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
        ami_native_id = dictionary.get('ami_native_id')
        architecture = dictionary.get('architecture')
        has_ena_support = dictionary.get('has_ena_support')
        hypervisor_type = dictionary.get('hypervisor_type')
        image_type = dictionary.get('image_type')
        is_public = dictionary.get('is_public')
        name = dictionary.get('name')
        number_of_ebs_volumes = dictionary.get('number_of_ebs_volumes')
        number_of_ephemeral_volumes = dictionary.get('number_of_ephemeral_volumes')
        owner_id = dictionary.get('owner_id')
        platform = dictionary.get('platform')
        root_device_name = dictionary.get('root_device_name')
        root_device_type = dictionary.get('root_device_type')
        sriov_net_support = dictionary.get('sriov_net_support')
        virtualization_type = dictionary.get('virtualization_type')
        # Return an object of this model
        return cls(
            ami_native_id,
            architecture,
            has_ena_support,
            hypervisor_type,
            image_type,
            is_public,
            name,
            number_of_ebs_volumes,
            number_of_ephemeral_volumes,
            owner_id,
            platform,
            root_device_name,
            root_device_type,
            sriov_net_support,
            virtualization_type,
        )
