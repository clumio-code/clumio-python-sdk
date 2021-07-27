#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ComputeResourceEmbedded')


class ComputeResourceEmbedded:
    """Implementation of the 'ComputeResourceEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
        read_vmware_vcenter_compute_resource_compliance_stats:
            Embeds the compliance statistics of VMs into each vCenter resource in the
            response, if requested using the `_embed` query parameter.
        read_vmware_vcenter_compute_resource_connection_stats:

    """

    # Create a mapping from Model property names to API property names
    _names = {
        'read_policy_definition': 'read-policy-definition',
        'read_vmware_vcenter_compute_resource_compliance_stats': 'read-vmware-vcenter-compute-resource-compliance-stats',
        'read_vmware_vcenter_compute_resource_connection_stats': 'read-vmware-vcenter-compute-resource-connection-stats',
    }

    def __init__(
        self,
        read_policy_definition: object = None,
        read_vmware_vcenter_compute_resource_compliance_stats: object = None,
        read_vmware_vcenter_compute_resource_connection_stats: object = None,
    ) -> None:
        """Constructor for the ComputeResourceEmbedded class."""

        # Initialize members of the class
        self.read_policy_definition: object = read_policy_definition
        self.read_vmware_vcenter_compute_resource_compliance_stats: object = (
            read_vmware_vcenter_compute_resource_compliance_stats
        )
        self.read_vmware_vcenter_compute_resource_connection_stats: object = (
            read_vmware_vcenter_compute_resource_connection_stats
        )

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
        read_policy_definition = dictionary.get('read-policy-definition')
        read_vmware_vcenter_compute_resource_compliance_stats = dictionary.get(
            'read-vmware-vcenter-compute-resource-compliance-stats'
        )
        read_vmware_vcenter_compute_resource_connection_stats = dictionary.get(
            'read-vmware-vcenter-compute-resource-connection-stats'
        )
        # Return an object of this model
        return cls(
            read_policy_definition,
            read_vmware_vcenter_compute_resource_compliance_stats,
            read_vmware_vcenter_compute_resource_connection_stats,
        )
