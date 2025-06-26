#
# Copyright 2023. Clumio, Inc.
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
        created_multi_region_cmk:
            Whether the CMK was created or an existing CMK was used.
        intermediate_role_arn:
            Role arn to be assumed before accessing ClumioRole in customer account.
        multi_region_cmk_key_id:
            The multi-region CMK Key ID.
        request_type:
            Indicates whether this is a Create, Update or Delete request.
        role_arn:
            The ARN of the role.
        role_external_id:
            The external ID to use with the role.
        role_id:
            The ID of the role.
        token:
            The 36-character Clumio AWS integration ID token used to identify the
            installation of the CloudFormation/Terraform template on the account.
        version:
            The cloudformation/terraform template version used.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'created_multi_region_cmk': 'created_multi_region_cmk',
        'intermediate_role_arn': 'intermediate_role_arn',
        'multi_region_cmk_key_id': 'multi_region_cmk_key_id',
        'request_type': 'request_type',
        'role_arn': 'role_arn',
        'role_external_id': 'role_external_id',
        'role_id': 'role_id',
        'token': 'token',
        'version': 'version',
    }

    def __init__(
        self,
        account_native_id: str = None,
        aws_region: str = None,
        created_multi_region_cmk: bool = None,
        intermediate_role_arn: str = None,
        multi_region_cmk_key_id: str = None,
        request_type: str = None,
        role_arn: str = None,
        role_external_id: str = None,
        role_id: str = None,
        token: str = None,
        version: int = None,
    ) -> None:
        """Constructor for the PostProcessKmsV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.created_multi_region_cmk: bool = created_multi_region_cmk
        self.intermediate_role_arn: str = intermediate_role_arn
        self.multi_region_cmk_key_id: str = multi_region_cmk_key_id
        self.request_type: str = request_type
        self.role_arn: str = role_arn
        self.role_external_id: str = role_external_id
        self.role_id: str = role_id
        self.token: str = token
        self.version: int = version

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
        created_multi_region_cmk = dictionary.get('created_multi_region_cmk')
        intermediate_role_arn = dictionary.get('intermediate_role_arn')
        multi_region_cmk_key_id = dictionary.get('multi_region_cmk_key_id')
        request_type = dictionary.get('request_type')
        role_arn = dictionary.get('role_arn')
        role_external_id = dictionary.get('role_external_id')
        role_id = dictionary.get('role_id')
        token = dictionary.get('token')
        version = dictionary.get('version')
        # Return an object of this model
        return cls(
            account_native_id,
            aws_region,
            created_multi_region_cmk,
            intermediate_role_arn,
            multi_region_cmk_key_id,
            request_type,
            role_arn,
            role_external_id,
            role_id,
            token,
            version,
        )
