#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {
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
        account_native_id: str,
        aws_region: str,
        created_multi_region_cmk: bool,
        intermediate_role_arn: str,
        multi_region_cmk_key_id: str,
        request_type: str,
        role_arn: str,
        role_external_id: str,
        role_id: str,
        token: str,
        version: int,
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
        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['created_multi_region_cmk']
        val_created_multi_region_cmk = val

        val = dictionary['intermediate_role_arn']
        val_intermediate_role_arn = val

        val = dictionary['multi_region_cmk_key_id']
        val_multi_region_cmk_key_id = val

        val = dictionary['request_type']
        val_request_type = val

        val = dictionary['role_arn']
        val_role_arn = val

        val = dictionary['role_external_id']
        val_role_external_id = val

        val = dictionary['role_id']
        val_role_id = val

        val = dictionary['token']
        val_token = val

        val = dictionary['version']
        val_version = val

        # Return an object of this model
        return cls(
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_created_multi_region_cmk,  # type: ignore
            val_intermediate_role_arn,  # type: ignore
            val_multi_region_cmk_key_id,  # type: ignore
            val_request_type,  # type: ignore
            val_role_arn,  # type: ignore
            val_role_external_id,  # type: ignore
            val_role_id,  # type: ignore
            val_token,  # type: ignore
            val_version,  # type: ignore
        )
