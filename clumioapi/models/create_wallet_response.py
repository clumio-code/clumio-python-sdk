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
        embedded: object,
        links: wallet_links_.WalletLinks,
        account_native_id: str,
        available_version: int,
        clumio_aws_account_id: str,
        deployment_url: str,
        error_code: str,
        error_message: str,
        p_id: str,
        installed_regions: Sequence[str],
        key_errors: Mapping[str, error_model_.ErrorModel],
        role_arn: str,
        stack_version: int,
        state: str,
        supported_regions: Sequence[str],
        template_url: str,
        token: str,
    ) -> None:
        """Constructor for the CreateWalletResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: wallet_links_.WalletLinks = links
        self.account_native_id: str = account_native_id
        self.available_version: int = available_version
        self.clumio_aws_account_id: str = clumio_aws_account_id
        self.deployment_url: str = deployment_url
        self.error_code: str = error_code
        self.error_message: str = error_message
        self.p_id: str = p_id
        self.installed_regions: Sequence[str] = installed_regions
        self.key_errors: Mapping[str, error_model_.ErrorModel] = key_errors
        self.role_arn: str = role_arn
        self.stack_version: int = stack_version
        self.state: str = state
        self.supported_regions: Sequence[str] = supported_regions
        self.template_url: str = template_url
        self.token: str = token

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
        val = dictionary['_embedded']
        val_embedded = val

        val = dictionary['_links']
        val_links = wallet_links_.WalletLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['available_version']
        val_available_version = val

        val = dictionary['clumio_aws_account_id']
        val_clumio_aws_account_id = val

        val = dictionary['deployment_url']
        val_deployment_url = val

        val = dictionary['error_code']
        val_error_code = val

        val = dictionary['error_message']
        val_error_message = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['installed_regions']
        val_installed_regions = val

        val = dictionary['key_errors']
        val_key_errors: Dict[str, error_model_.ErrorModel] = {}
        for key, value in val.items():
            val_key_errors[key] = error_model_.ErrorModel.from_dictionary(value)

        val = dictionary['role_arn']
        val_role_arn = val

        val = dictionary['stack_version']
        val_stack_version = val

        val = dictionary['state']
        val_state = val

        val = dictionary['supported_regions']
        val_supported_regions = val

        val = dictionary['template_url']
        val_template_url = val

        val = dictionary['token']
        val_token = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_available_version,  # type: ignore
            val_clumio_aws_account_id,  # type: ignore
            val_deployment_url,  # type: ignore
            val_error_code,  # type: ignore
            val_error_message,  # type: ignore
            val_p_id,  # type: ignore
            val_installed_regions,  # type: ignore
            val_key_errors,  # type: ignore
            val_role_arn,  # type: ignore
            val_stack_version,  # type: ignore
            val_state,  # type: ignore
            val_supported_regions,  # type: ignore
            val_template_url,  # type: ignore
            val_token,  # type: ignore
        )
