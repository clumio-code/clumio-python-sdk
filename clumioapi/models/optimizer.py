#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import glue_optimizer as glue_optimizer_
from clumioapi.models import s3_tables_optimizer as s3_tables_optimizer_
import requests

T = TypeVar('T', bound='Optimizer')


@dataclasses.dataclass
class Optimizer:
    """Implementation of the 'Optimizer' model.

    Attributes:
        Glue

        Mode

        S3tables

    """

    Glue: glue_optimizer_.GlueOptimizer | None = None
    Mode: str | None = None
    S3tables: s3_tables_optimizer_.S3TablesOptimizer | None = None

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
        val = dictionary.get('glue', None)
        val_glue = glue_optimizer_.GlueOptimizer.from_dictionary(val)

        val = dictionary.get('mode', None)
        val_mode = val

        val = dictionary.get('s3tables', None)
        val_s3tables = s3_tables_optimizer_.S3TablesOptimizer.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_glue,
            val_mode,
            val_s3tables,
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
