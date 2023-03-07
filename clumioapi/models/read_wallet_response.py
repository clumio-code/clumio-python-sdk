#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import error_model
from clumioapi.models import wallet_links

T = TypeVar('T', bound='ReadWalletResponse')


class ReadWalletResponse:
    """Implementation of the 'ReadWalletResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            AWS Account ID associated with the wallet.
        available_version:
            Version of the template available
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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'available_version': 'available_version',
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
        embedded: object = None,
        links: wallet_links.WalletLinks = None,
        account_native_id: str = None,
        available_version: int = None,
        clumio_aws_account_id: str = None,
        deployment_url: str = None,
        error_code: str = None,
        error_message: str = None,
        p_id: str = None,
        installed_regions: Sequence[str] = None,
        key_errors: Mapping[str, error_model.ErrorModel] = None,
        role_arn: str = None,
        stack_version: int = None,
        state: str = None,
        supported_regions: Sequence[str] = None,
        template_url: str = None,
        token: str = None,
    ) -> None:
        """Constructor for the ReadWalletResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: wallet_links.WalletLinks = links
        self.account_native_id: str = account_native_id
        self.available_version: int = available_version
        self.clumio_aws_account_id: str = clumio_aws_account_id
        self.deployment_url: str = deployment_url
        self.error_code: str = error_code
        self.error_message: str = error_message
        self.p_id: str = p_id
        self.installed_regions: Sequence[str] = installed_regions
        self.key_errors: Mapping[str, error_model.ErrorModel] = key_errors
        self.role_arn: str = role_arn
        self.stack_version: int = stack_version
        self.state: str = state
        self.supported_regions: Sequence[str] = supported_regions
        self.template_url: str = template_url
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
        embedded = dictionary.get('_embedded')
        key = '_links'
        links = (
            wallet_links.WalletLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        available_version = dictionary.get('available_version')
        clumio_aws_account_id = dictionary.get('clumio_aws_account_id')
        deployment_url = dictionary.get('deployment_url')
        error_code = dictionary.get('error_code')
        error_message = dictionary.get('error_message')
        p_id = dictionary.get('id')
        installed_regions = dictionary.get('installed_regions')
        key_errors: Dict[str, error_model.ErrorModel] = {}
        for key, value in dictionary.get('key_errors').items():
            key_errors[key] = error_model.ErrorModel.from_dictionary(value) if value else None

        role_arn = dictionary.get('role_arn')
        stack_version = dictionary.get('stack_version')
        state = dictionary.get('state')
        supported_regions = dictionary.get('supported_regions')
        template_url = dictionary.get('template_url')
        token = dictionary.get('token')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            available_version,
            clumio_aws_account_id,
            deployment_url,
            error_code,
            error_message,
            p_id,
            installed_regions,
            key_errors,
            role_arn,
            stack_version,
            state,
            supported_regions,
            template_url,
            token,
        )
