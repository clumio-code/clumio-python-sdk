#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import error_model as error_model_
from clumioapi.models import wallet_links as wallet_links_

T = TypeVar('T', bound='CreateWalletResponse')


class CreateWalletResponse:
    """Implementation of the 'CreateWalletResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            AWS Account ID associated with the wallet.
        available_version:
            Version of the template available
        aws_region:
            The AWS region associated with the wallet.
        clumio_aws_account_id:
            Clumio AWS Account ID.
        deployment_url:
            DeploymentURL is an (external) link to an AWS console page for quick-creation
            of the stack.
        error_code:
            ErrorCode is a short string describing the error, if any.
        error_message:
            ErrorMessage is a longer description explaining the error, if any, and how to
            fix it.
        p_id:
            The Clumio-assigned ID of the wallet.
        installed_regions:
            The regions where the wallet is installed.
        key_errors:
            Errors, if any, in accessing the multi-region key in the wallet.
        role_arn:
            RoleArn is the AWS Resource Name of the IAM Role created by the stack.
        stack_version:
            The version of the stack used or being used.
        state:
            State describes the state of the wallet. Valid states are:
            Waiting: The wallet has been created, but a stack hasn't been created. The
            wallet can't be used in this state.
            Enabled: The wallet has been created and a stack has been created for the
            wallet. This is the normal expected state of a wallet in use.
            Error:   The wallet is inaccessible. See ErrorCode and ErrorMessage fields for
            additional details.
        supported_regions:
            The supported regions for the wallet.
        template_url:
            TemplateURL is the URL to the CloudFormation template to be used to create the
            CloudFormation stack.
        token:
            Token is used to identify and authenticate the CloudFormation stack creation.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'available_version': 'available_version',
        'aws_region': 'aws_region',
        'clumio_aws_account_id': 'clumio_aws_account_id',
        'deployment_url': 'deployment_url',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'p_id': 'id',
        'installed_regions': 'installed_regions',
        'key_errors': 'key_errors',
        'role_arn': 'role_arn',
        'stack_version': 'stack_version',
        'state': 'state',
        'supported_regions': 'supported_regions',
        'template_url': 'template_url',
        'token': 'token',
    }

    def __init__(
        self,
        embedded: object | None = None,
        links: wallet_links_.WalletLinks | None = None,
        account_native_id: str | None = None,
        available_version: int | None = None,
        aws_region: str | None = None,
        clumio_aws_account_id: str | None = None,
        deployment_url: str | None = None,
        error_code: str | None = None,
        error_message: str | None = None,
        p_id: str | None = None,
        installed_regions: Sequence[str] | None = None,
        key_errors: Mapping[str, error_model_.ErrorModel] | None = None,
        role_arn: str | None = None,
        stack_version: int | None = None,
        state: str | None = None,
        supported_regions: Sequence[str] | None = None,
        template_url: str | None = None,
        token: str | None = None,
    ) -> None:
        """Constructor for the CreateWalletResponse class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: wallet_links_.WalletLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.available_version: int | None = available_version
        self.aws_region: str | None = aws_region
        self.clumio_aws_account_id: str | None = clumio_aws_account_id
        self.deployment_url: str | None = deployment_url
        self.error_code: str | None = error_code
        self.error_message: str | None = error_message
        self.p_id: str | None = p_id
        self.installed_regions: Sequence[str] | None = installed_regions
        self.key_errors: Mapping[str, error_model_.ErrorModel] | None = key_errors
        self.role_arn: str | None = role_arn
        self.stack_version: int | None = stack_version
        self.state: str | None = state
        self.supported_regions: Sequence[str] | None = supported_regions
        self.template_url: str | None = template_url
        self.token: str | None = token

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = wallet_links_.WalletLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('available_version', None)
        val_available_version = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('clumio_aws_account_id', None)
        val_clumio_aws_account_id = val

        val = dictionary.get('deployment_url', None)
        val_deployment_url = val

        val = dictionary.get('error_code', None)
        val_error_code = val

        val = dictionary.get('error_message', None)
        val_error_message = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('installed_regions', None)
        val_installed_regions = val

        val = dictionary.get('key_errors', None)
        val_key_errors: Dict[str, error_model_.ErrorModel] = {}
        for key, value in val.items():
            val_key_errors[key] = error_model_.ErrorModel.from_dictionary(value)

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        val = dictionary.get('stack_version', None)
        val_stack_version = val

        val = dictionary.get('state', None)
        val_state = val

        val = dictionary.get('supported_regions', None)
        val_supported_regions = val

        val = dictionary.get('template_url', None)
        val_template_url = val

        val = dictionary.get('token', None)
        val_token = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_available_version,
            val_aws_region,
            val_clumio_aws_account_id,
            val_deployment_url,
            val_error_code,
            val_error_message,
            val_p_id,
            val_installed_regions,
            val_key_errors,
            val_role_arn,
            val_stack_version,
            val_state,
            val_supported_regions,
            val_template_url,
            val_token,
        )
