#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2RestoreNetworkInterface')


@dataclasses.dataclass
class EC2RestoreNetworkInterface:
    """Implementation of the 'EC2RestoreNetworkInterface' model.

    Attributes:
        DeviceIndex:
            The position of the network interface in the attachment order. a primary
            network interface has a device index of 0.

        NetworkInterfaceNativeId:
            The aws-assigned id of the existing network interface to attach to the
            restored instance. if one wishes to restore this network interface from the
            backup,
            then this field should be set to `null`.

        RestoreDefault:
            Whether or not a default network interface should be restored. it will not have
            any of
            the same configurations as the backup network interface.

        RestoreFromBackup:
            Whether or not the network interface should be restored the backup network
            interface.
            it will be configured with the same configurations as the backup network
            interface.

        SecurityGroupNativeIds:
            The aws-assigned ids for the security groups to associate with this network
            interface.
            if one wishes to attach an existing network interface, then this field should be
            set to `null`.

        SubnetNativeId:
            The aws-assigned id of the subnet associated with the network interface.
            if one wishes to attach an existing network interface, then this field should be
            set to `null`.

    """

    DeviceIndex: int | None = None
    NetworkInterfaceNativeId: str | None = None
    RestoreDefault: bool | None = None
    RestoreFromBackup: bool | None = None
    SecurityGroupNativeIds: Sequence[str] | None = None
    SubnetNativeId: str | None = None

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
        val = dictionary.get('device_index', None)
        val_device_index = val

        val = dictionary.get('network_interface_native_id', None)
        val_network_interface_native_id = val

        val = dictionary.get('restore_default', None)
        val_restore_default = val

        val = dictionary.get('restore_from_backup', None)
        val_restore_from_backup = val

        val = dictionary.get('security_group_native_ids', None)
        val_security_group_native_ids = val

        val = dictionary.get('subnet_native_id', None)
        val_subnet_native_id = val

        # Return an object of this model
        return cls(
            val_device_index,
            val_network_interface_native_id,
            val_restore_default,
            val_restore_from_backup,
            val_security_group_native_ids,
            val_subnet_native_id,
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
