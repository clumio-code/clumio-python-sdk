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
from clumioapi.controllers.types import users_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import change_password_response
from clumioapi.models import change_password_v1_request
from clumioapi.models import create_user_response_v1
from clumioapi.models import create_user_v1_request
from clumioapi.models import delete_user_response_v1
from clumioapi.models import edit_profile_response_v1
from clumioapi.models import list_users_response_v1
from clumioapi.models import read_user_response_v1
from clumioapi.models import update_user_profile_v1_request
from clumioapi.models import update_user_response_v1
from clumioapi.models import update_user_v1_request
import requests
import retrying


class UsersV1Controller:
    """A Controller to access Endpoints for users resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.users=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_users(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: users_types.ListUsersV1FilterT | None = None,
        **kwargs,
    ) -> list_users_response_v1.ListUsersResponseV1:
        """Returns a list of Clumio users.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------------------------------+
                | Field | Filter Condition |                    Description                    |
                +=======+==================+===================================================+
                | name  | $contains        | A case insensitive substring of the name of the   |
                |       |                  | user.                                             |
                +-------+------------------+---------------------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_users_response_v1.ListUsersResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_users_response_v1.ListUsersResponseV1
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
            error_str = f'list_users for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_user(
        self, body: create_user_v1_request.CreateUserV1Request | None = None, **kwargs
    ) -> create_user_response_v1.CreateUserResponseV1:
        """Creates a new user. Specify the user's full name and email address to generate
        an email message that is sent to the user with an invitation to activate their
        Clumio account.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_user_response_v1.CreateUserResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_user_response_v1.CreateUserResponseV1
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
            error_str = f'create_user for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_user_profile(
        self,
        body: update_user_profile_v1_request.UpdateUserProfileV1Request | None = None,
        **kwargs,
    ) -> edit_profile_response_v1.EditProfileResponseV1:
        """Manages the current user's profile, such as changing the user's full name.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return edit_profile_response_v1.EditProfileResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users/my-profile'

        _query_parameters: dict[str, Any] = {}

        resp_instance: edit_profile_response_v1.EditProfileResponseV1
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
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
            error_str = f'update_user_profile for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_user(
        self, user_id: int | None = None, **kwargs
    ) -> read_user_response_v1.ReadUserResponseV1:
        """Returns a representation of the specified Clumio user.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be retrieved.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_user_response_v1.ReadUserResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_user_response_v1.ReadUserResponseV1
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
            error_str = f'read_user for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_user(
        self, user_id: int | None = None, **kwargs
    ) -> delete_user_response_v1.DeleteUserResponseV1:
        """Deletes an existing user from Clumio, revoking the user's access to Clumio. A
        deleted user cannot be recovered.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be deleted.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return delete_user_response_v1.DeleteUserResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: delete_user_response_v1.DeleteUserResponseV1
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
            error_str = f'delete_user for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_user(
        self,
        user_id: int | None = None,
        body: update_user_v1_request.UpdateUserV1Request | None = None,
        **kwargs,
    ) -> update_user_response_v1.UpdateUserResponseV1:
        """Manages an existing user. Managing a user includes enabling or disabling the
        user,
        changing the user's full name or updating the user's role.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be updated.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_user_response_v1.UpdateUserResponseV1.from_response(resp)

        # Prepare query URL
        _url_path = '/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: update_user_response_v1.UpdateUserResponseV1
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
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
            error_str = f'update_user for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def change_password(
        self,
        user_id: int | None = None,
        body: change_password_v1_request.ChangePasswordV1Request | None = None,
        **kwargs,
    ) -> change_password_response.ChangePasswordResponse:
        """Change the password of the specified user. Users can change their own passwords.

        Args:
            user_id:
                Performs the operation on the user with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return change_password_response.ChangePasswordResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/users/{user_id}/password'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: change_password_response.ChangePasswordResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
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
            error_str = f'change_password for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class UsersV1ControllerPaginator:
    """A Controller to access Endpoints for users resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_users(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: users_types.ListUsersV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_users_response_v1.ListUsersResponseV1]:
        """Returns a list of Clumio users.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------------------------------+
                | Field | Filter Condition |                    Description                    |
                +=======+==================+===================================================+
                | name  | $contains        | A case insensitive substring of the name of the   |
                |       |                  | user.                                             |
                +-------+------------------+---------------------------------------------------+

        """
        controller = UsersV1Controller(self.controller)
        while True:
            response = controller.list_users(limit=limit, start=start, filter=filter, **kwargs)
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
