#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PostProcessKmsV1Request')


class PostProcessKmsV1Request:
    """Implementation of the 'PostProcessKmsV1Request' model.

    The body of the request.

    Attributes:
        account_native_id:
            The AWS-assigned ID of the account associated with the connection.
        aws_region:
            The AWS region associated with the connection. For example, `us-east-1`.
        multi_region_cmk_key_id:
            The multi-region CMK Key ID.
        other_regions:
            Other regions where the stack set instances are created.
        request_type:
            Indicates whether this is a Create, Update or Delete request.
        stack_set_id:
            The stack set ID.
        token:
            The 36-character Clumio AWS integration ID token used to identify the
            installation of the CloudFormation/Terraform template on the account.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'multi_region_cmk_key_id': 'multi_region_cmk_key_id',
        'other_regions': 'other_regions',
        'request_type': 'request_type',
        'stack_set_id': 'stack_set_id',
        'token': 'token',
    }

    def __init__(
        self,
        account_native_id: str = None,
        aws_region: str = None,
        multi_region_cmk_key_id: str = None,
        other_regions: str = None,
        request_type: str = None,
        stack_set_id: str = None,
        token: str = None,
    ) -> None:
        """Constructor for the PostProcessKmsV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.multi_region_cmk_key_id: str = multi_region_cmk_key_id
        self.other_regions: str = other_regions
        self.request_type: str = request_type
        self.stack_set_id: str = stack_set_id
        self.token: str = token

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
        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        multi_region_cmk_key_id = dictionary.get('multi_region_cmk_key_id')
        other_regions = dictionary.get('other_regions')
        request_type = dictionary.get('request_type')
        stack_set_id = dictionary.get('stack_set_id')
        token = dictionary.get('token')
        # Return an object of this model
        return cls(
            account_native_id,
            aws_region,
            multi_region_cmk_key_id,
            other_regions,
            request_type,
            stack_set_id,
            token,
        )
