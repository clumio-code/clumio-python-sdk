#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_wallet_response
from clumioapi.models import create_wallet_v1_request
from clumioapi.models import list_wallets_response
from clumioapi.models import read_wallet_response
from clumioapi.models import refresh_wallet_response
import requests
import retrying


class WalletsV1Controller:
    """A Controller to access Endpoints for wallets resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.wallets=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_wallets_response.ListWalletsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/wallets'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
        }

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_wallet_response.CreateWalletResponse.from_response(resp)

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_wallet_response.ReadWalletResponse.from_response(resp)

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

        def get_instance_from_response(resp: requests.Response) -> Any:
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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return refresh_wallet_response.RefreshWalletResponse.from_response(resp)

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


class WalletsV1ControllerPaginator:
    """A Controller to access Endpoints for wallets resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
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
        controller = WalletsV1Controller(self.controller)
        while True:
            response = controller.list_wallets(limit=limit, start=start, **kwargs)
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
