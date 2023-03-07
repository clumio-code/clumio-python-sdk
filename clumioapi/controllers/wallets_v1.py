#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_wallet_response
from clumioapi.models import create_wallet_v1_request
from clumioapi.models import list_wallets_response
from clumioapi.models import read_wallet_response
from clumioapi.models import refresh_wallet_response
import requests


class WalletsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for wallets resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.wallets=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_wallets(
        self, limit: int = None, start: str = None
    ) -> list_wallets_response.ListWalletsResponse:
        """Returns a list of wallets.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            list_wallets_response.ListWalletsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_wallets.', errors
            )

        return list_wallets_response.ListWalletsResponse.from_dictionary(resp)

    def create_wallet(
        self, body: create_wallet_v1_request.CreateWalletV1Request = None
    ) -> create_wallet_response.CreateWalletResponse:
        """Create a wallet.

        Args:
            body:

        Returns:
            create_wallet_response.CreateWalletResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_wallet.', errors
            )

        return create_wallet_response.CreateWalletResponse.from_dictionary(resp)

    def read_wallet(self, wallet_id: str) -> read_wallet_response.ReadWalletResponse:
        """Returns a representation of the specified KMS wallet.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        Returns:
            read_wallet_response.ReadWalletResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets/{wallet_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_wallet.', errors
            )

        return read_wallet_response.ReadWalletResponse.from_dictionary(resp)

    def delete_wallet(self, wallet_id: str) -> object:
        """Delete the wallet with the specified id.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        Returns:
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets/{wallet_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_wallet.', errors
            )

        return resp

    def refresh_wallet(self, wallet_id: str) -> refresh_wallet_response.RefreshWalletResponse:
        """Refresh the access status of a wallet with the specified id to verify if it can
        be used for backup/restore.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        Returns:
            refresh_wallet_response.RefreshWalletResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets/{wallet_id}/_refresh'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing refresh_wallet.', errors
            )

        return refresh_wallet_response.RefreshWalletResponse.from_dictionary(resp)
