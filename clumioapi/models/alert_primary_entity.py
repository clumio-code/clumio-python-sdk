#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AlertPrimaryEntity')


class AlertPrimaryEntity:
    """Implementation of the 'AlertPrimaryEntity' model.

    The primary object associated with or affected by the alert. Examples of primary
    entities include "aws_connection", "aws_ebs_volume" and "vmware_vm".

    Attributes:
        id:
            A system-generated ID assigned to this entity.
        type:
            The following table describes the entity types that Clumio supports.

            +--------------------------------+---------------------------------------------+
            |          Entity Type           |                   Details                   |
            +================================+=============================================+
            | vmware_vcenter                 | VMware vCenter.                             |
            +--------------------------------+---------------------------------------------+
            | vmware_vm                      | VMware virtual machine.                     |
            +--------------------------------+---------------------------------------------+
            | vmware_vm_folder               | VMware VM folder.                           |
            +--------------------------------+---------------------------------------------+
            | vmware_datacenter              | VMware data center.                         |
            +--------------------------------+---------------------------------------------+
            | vmware_datacenter_folder       | VMware data center folder.                  |
            +--------------------------------+---------------------------------------------+
            | vmware_tag                     | VMware tag.                                 |
            +--------------------------------+---------------------------------------------+
            | vmware_category                | VMware tag category.                        |
            +--------------------------------+---------------------------------------------+
            | vmware_compute_resource        | VMware compute resource.                    |
            +--------------------------------+---------------------------------------------+
            | vmware_compute_resource_folder | VMware compute resource folder.             |
            +--------------------------------+---------------------------------------------+
            | aws_ebs_volume                 | AWS EBS volume.                             |
            +--------------------------------+---------------------------------------------+
            | aws_connection                 | AWS connection mediated by a CloudFormation |
            |                                | stack.                                      |
            +--------------------------------+---------------------------------------------+
            | aws_environment                | AWS environment specified by an             |
            |                                | account/region pair.                        |
            +--------------------------------+---------------------------------------------+
            | aws_tag                        | AWS tag.                                    |
            +--------------------------------+---------------------------------------------+
            | aws_cmk                        | AWS Customer Master Key used to encrypt     |
            |                                | data.                                       |
            +--------------------------------+---------------------------------------------+
        value:
            A system-generated value assigned to the entity. For example, if the primary
            entity type is "vmware_vm" for a virtual machine, then the value is the name of
            the VM.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id', 'type': 'type', 'value': 'value'}

    def __init__(self, id: str = None, type: str = None, value: str = None) -> None:
        """Constructor for the AlertPrimaryEntity class."""

        # Initialize members of the class
        self.id: str = id
        self.type: str = type
        self.value: str = value

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
        id = dictionary.get('id')
        type = dictionary.get('type')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(id, type, value)
