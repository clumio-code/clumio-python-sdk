#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

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
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> list_wallets_response.ListWalletsResponse:
        """Returns a list of wallets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_wallets_response.ListWalletsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/wallets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start}

        resp_instance: list_wallets_response.ListWalletsResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_wallets for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_wallet(
        self, body: create_wallet_v1_request.CreateWalletV1Request | None = None, **kwargs
    ) -> create_wallet_response.CreateWalletResponse:
        """Create a wallet.

        Args:
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_wallet_response.CreateWalletResponse.from_response(response)

        # Prepare query URL
        _url_path = '/wallets'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_wallet_response.CreateWalletResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'create_wallet for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_wallet(
        self, wallet_id: str | None = None, **kwargs
    ) -> read_wallet_response.ReadWalletResponse:
        """Returns a representation of the specified KMS wallet.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_wallet_response.ReadWalletResponse.from_response(response)

        # Prepare query URL
        _url_path = '/wallets/{wallet_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_wallet_response.ReadWalletResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_wallet for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_wallet(self, wallet_id: str | None = None, **kwargs) -> object:
        """Delete the wallet with the specified id.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/wallets/{wallet_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: object
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'delete_wallet for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def refresh_wallet(
        self, wallet_id: str | None = None, **kwargs
    ) -> refresh_wallet_response.RefreshWalletResponse:
        """Refresh the access status of a wallet with the specified id to verify if it can
        be used for backup/restore.

        Args:
            wallet_id:
                Performs the operation on the wallet with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return refresh_wallet_response.RefreshWalletResponse.from_response(response)

        # Prepare query URL
        _url_path = '/wallets/{wallet_id}/_refresh'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'wallet_id': wallet_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: refresh_wallet_response.RefreshWalletResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'refresh_wallet for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class WalletsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for wallets resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = WalletsV1Controller(config)

    def list_wallets(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> Iterator[list_wallets_response.ListWalletsResponse]:
        """Returns a list of wallets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """
        start = start or '1'
        while True:
            response = self.controller.list_wallets(limit=limit, start=start, **kwargs)
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
