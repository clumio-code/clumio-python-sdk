#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import glue_compaction_configuration as glue_compaction_configuration_
from clumioapi.models import \
    glue_orphan_file_deletion_configuration as glue_orphan_file_deletion_configuration_
from clumioapi.models import glue_retention_configuration as glue_retention_configuration_
from clumioapi.models import vpc_configuration as vpc_configuration_
import requests

T = TypeVar('T', bound='GlueOptimizer')


@dataclasses.dataclass
class GlueOptimizer:
    """Implementation of the 'GlueOptimizer' model.

    Attributes:
        CompactionConfiguration

        OrphanFileDeletionConfiguration

        RetentionConfiguration

        RoleArn

        VpcConfiguration

    """

    CompactionConfiguration: glue_compaction_configuration_.GlueCompactionConfiguration | None = (
        None
    )
    OrphanFileDeletionConfiguration: (
        glue_orphan_file_deletion_configuration_.GlueOrphanFileDeletionConfiguration | None
    ) = None
    RetentionConfiguration: glue_retention_configuration_.GlueRetentionConfiguration | None = None
    RoleArn: str | None = None
    VpcConfiguration: vpc_configuration_.VpcConfiguration | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('compaction_configuration', None)
        val_compaction_configuration = (
            glue_compaction_configuration_.GlueCompactionConfiguration.from_dictionary(val)
        )

        val = dictionary.get('orphan_file_deletion_configuration', None)
        val_orphan_file_deletion_configuration = glue_orphan_file_deletion_configuration_.GlueOrphanFileDeletionConfiguration.from_dictionary(
            val
        )

        val = dictionary.get('retention_configuration', None)
        val_retention_configuration = (
            glue_retention_configuration_.GlueRetentionConfiguration.from_dictionary(val)
        )

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        val = dictionary.get('vpc_configuration', None)
        val_vpc_configuration = vpc_configuration_.VpcConfiguration.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_compaction_configuration,
            val_orphan_file_deletion_configuration,
            val_retention_configuration,
            val_role_arn,
            val_vpc_configuration,
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
