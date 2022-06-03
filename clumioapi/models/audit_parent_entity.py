#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AuditParentEntity')


class AuditParentEntity:
    """Implementation of the 'AuditParentEntity' model.

    The parent object of the primary entity associated with or affected by the
    audit.If the primary entity is not a vmware entity, this field will have a value
    of nullFor example, "vmware_vcenter" is the parent entity of primary entity
    "vmware_vm".

    Attributes:
        p_id:
            A system-generated ID assigned to this entity.
        p_type:
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
    _names = {'p_id': 'id', 'p_type': 'type', 'value': 'value'}

    def __init__(self, p_id: str = None, p_type: str = None, value: str = None) -> None:
        """Constructor for the AuditParentEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.p_type: str = p_type
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
        p_id = dictionary.get('id')
        p_type = dictionary.get('type')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(p_id, p_type, value)
