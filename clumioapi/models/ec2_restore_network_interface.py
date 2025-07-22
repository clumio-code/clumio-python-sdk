#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2RestoreNetworkInterface')


class EC2RestoreNetworkInterface:
    """Implementation of the 'EC2RestoreNetworkInterface' model.

    Attributes:
        device_index:
            The position of the network interface in the attachment order. A primary
            network interface has a device index of 0.
        network_interface_native_id:
            The AWS-assigned ID of the existing network interface to attach to the
            restored instance. If one wishes to restore this network interface from the
            backup,
            then this field should be set to `null`.
        restore_default:
            Whether or not a default network interface should be restored. It will not have
            any of
            the same configurations as the backup network interface.
        restore_from_backup:
            Whether or not the network interface should be restored the backup network
            interface.
            It will be configured with the same configurations as the backup network
            interface.
        security_group_native_ids:
            The AWS-assigned IDs for the security groups to associate with this network
            interface.
            If one wishes to attach an existing network interface, then this field should be
            set to `null`.
        subnet_native_id:
            The AWS-assigned ID of the subnet associated with the network interface.
            If one wishes to attach an existing network interface, then this field should be
            set to `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'device_index': 'device_index',
        'network_interface_native_id': 'network_interface_native_id',
        'restore_default': 'restore_default',
        'restore_from_backup': 'restore_from_backup',
        'security_group_native_ids': 'security_group_native_ids',
        'subnet_native_id': 'subnet_native_id',
    }

    def __init__(
        self,
        device_index: int,
        network_interface_native_id: str,
        restore_default: bool,
        restore_from_backup: bool,
        security_group_native_ids: Sequence[str],
        subnet_native_id: str,
    ) -> None:
        """Constructor for the EC2RestoreNetworkInterface class."""

        # Initialize members of the class
        self.device_index: int = device_index
        self.network_interface_native_id: str = network_interface_native_id
        self.restore_default: bool = restore_default
        self.restore_from_backup: bool = restore_from_backup
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.subnet_native_id: str = subnet_native_id

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
        val = dictionary['device_index']
        val_device_index = val

        val = dictionary['network_interface_native_id']
        val_network_interface_native_id = val

        val = dictionary['restore_default']
        val_restore_default = val

        val = dictionary['restore_from_backup']
        val_restore_from_backup = val

        val = dictionary['security_group_native_ids']
        val_security_group_native_ids = val

        val = dictionary['subnet_native_id']
        val_subnet_native_id = val

        # Return an object of this model
        return cls(
            val_device_index,  # type: ignore
            val_network_interface_native_id,  # type: ignore
            val_restore_default,  # type: ignore
            val_restore_from_backup,  # type: ignore
            val_security_group_native_ids,  # type: ignore
            val_subnet_native_id,  # type: ignore
        )
