#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import error_model as error_model_
from clumioapi.models import wallet_links as wallet_links_
import requests

T = TypeVar('T', bound='RefreshWalletResponse')


@dataclasses.dataclass
class RefreshWalletResponse:
    """Implementation of the 'RefreshWalletResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            Aws account id associated with the wallet.

        AvailableVersion:
            Version of the template available.

        AwsRegion:
            The aws region associated with the wallet.

        ClumioAwsAccountId:
            Clumio aws account id.

        DeploymentUrl:
            Deploymenturl is an (external) link to an aws console page for quick-creation
            of the stack.

        ErrorCode:
            Errorcode is a short string describing the error, if any.

        ErrorMessage:
            Errormessage is a longer description explaining the error, if any, and how to
            fix it.

        Id:
            The clumio-assigned id of the wallet.

        InstalledRegions:
            The regions where the wallet is installed.

        KeyErrors:
            Errors, if any, in accessing the multi-region key in the wallet.

        RoleArn:
            Rolearn is the aws resource name of the iam role created by the stack.

        StackVersion:
            The version of the stack used or being used.

        State:
              the wallet is inaccessible. see errorcode and errormessage fields for
            additional details.

        SupportedRegions:
            The supported regions for the wallet.

        TemplateUrl:
            Templateurl is the url to the cloudformation template to be used to create the
            cloudformation stack.

        Token:
            Token is used to identify and authenticate the cloudformation stack creation.

    """

    Embedded: object | None = None
    Links: wallet_links_.WalletLinks | None = None
    AccountNativeId: str | None = None
    AvailableVersion: int | None = None
    AwsRegion: str | None = None
    ClumioAwsAccountId: str | None = None
    DeploymentUrl: str | None = None
    ErrorCode: str | None = None
    ErrorMessage: str | None = None
    Id: str | None = None
    InstalledRegions: Sequence[str] | None = None
    KeyErrors: Mapping[str, error_model_.ErrorModel] | None = None
    RoleArn: str | None = None
    StackVersion: int | None = None
    State: str | None = None
    SupportedRegions: Sequence[str] | None = None
    TemplateUrl: str | None = None
    Token: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val_id = val

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
            val_id,
            val_installed_regions,
            val_key_errors,
            val_role_arn,
            val_stack_version,
            val_state,
            val_supported_regions,
            val_template_url,
            val_token,
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
        model_instance.raw_response = response
        return model_instance
