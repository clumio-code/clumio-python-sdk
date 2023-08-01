#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
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


class UsersV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for users resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.users=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_users(
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_users_response_v1.ListUsersResponseV1,
        tuple[requests.Response, Optional[list_users_response_v1.ListUsersResponseV1]],
    ]:
        """Returns a list of Clumio users.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_users_response_v1.ListUsersResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_users.', errors
            )

        if self.config.raw_response:
            return resp, list_users_response_v1.ListUsersResponseV1.from_dictionary(resp.json())
        return list_users_response_v1.ListUsersResponseV1.from_dictionary(resp)

    def create_user(
        self, body: create_user_v1_request.CreateUserV1Request = None, **kwargs
    ) -> Union[
        create_user_response_v1.CreateUserResponseV1,
        tuple[requests.Response, Optional[create_user_response_v1.CreateUserResponseV1]],
    ]:
        """Creates a new user. Specify the user's full name and email address to generate
        an email message that is sent to the user with an invitation to activate their
        Clumio account.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_user_response_v1.CreateUserResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_user.', errors
            )

        if self.config.raw_response:
            return resp, create_user_response_v1.CreateUserResponseV1.from_dictionary(resp.json())
        return create_user_response_v1.CreateUserResponseV1.from_dictionary(resp)

    def update_user_profile(
        self, body: update_user_profile_v1_request.UpdateUserProfileV1Request = None, **kwargs
    ) -> Union[
        edit_profile_response_v1.EditProfileResponseV1,
        tuple[requests.Response, Optional[edit_profile_response_v1.EditProfileResponseV1]],
    ]:
        """Manages the current user's profile, such as changing the user's full name.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            edit_profile_response_v1.EditProfileResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users/my-profile'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_user_profile.', errors
            )

        if self.config.raw_response:
            return resp, edit_profile_response_v1.EditProfileResponseV1.from_dictionary(resp.json())
        return edit_profile_response_v1.EditProfileResponseV1.from_dictionary(resp)

    def read_user(
        self, user_id: int, **kwargs
    ) -> Union[
        read_user_response_v1.ReadUserResponseV1,
        tuple[requests.Response, Optional[read_user_response_v1.ReadUserResponseV1]],
    ]:
        """Returns a representation of the specified Clumio user.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be retrieved.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_user_response_v1.ReadUserResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_user.', errors
            )

        if self.config.raw_response:
            return resp, read_user_response_v1.ReadUserResponseV1.from_dictionary(resp.json())
        return read_user_response_v1.ReadUserResponseV1.from_dictionary(resp)

    def delete_user(
        self, user_id: int, **kwargs
    ) -> Union[
        delete_user_response_v1.DeleteUserResponseV1,
        tuple[requests.Response, Optional[delete_user_response_v1.DeleteUserResponseV1]],
    ]:
        """Deletes an existing user from Clumio, revoking the user's access to Clumio. A
        deleted user cannot be recovered.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be deleted.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            delete_user_response_v1.DeleteUserResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_user.', errors
            )

        if self.config.raw_response:
            return resp, delete_user_response_v1.DeleteUserResponseV1.from_dictionary(resp.json())
        return delete_user_response_v1.DeleteUserResponseV1.from_dictionary(resp)

    def update_user(
        self, user_id: int, body: update_user_v1_request.UpdateUserV1Request = None, **kwargs
    ) -> Union[
        update_user_response_v1.UpdateUserResponseV1,
        tuple[requests.Response, Optional[update_user_response_v1.UpdateUserResponseV1]],
    ]:
        """Manages an existing user. Managing a user includes enabling or disabling the
        user,
        changing the user's full name or updating the user's role.

        Args:
            user_id:
                The Clumio-assigned ID of the user to be updated.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_user_response_v1.UpdateUserResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users/{user_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_user.', errors
            )

        if self.config.raw_response:
            return resp, update_user_response_v1.UpdateUserResponseV1.from_dictionary(resp.json())
        return update_user_response_v1.UpdateUserResponseV1.from_dictionary(resp)

    def change_password(
        self,
        user_id: int,
        body: change_password_v1_request.ChangePasswordV1Request = None,
        **kwargs,
    ) -> Union[
        change_password_response.ChangePasswordResponse,
        tuple[requests.Response, Optional[change_password_response.ChangePasswordResponse]],
    ]:
        """Change the password of the specified user. Users can change their own passwords.

        Args:
            user_id:
                Performs the operation on the user with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            change_password_response.ChangePasswordResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/users/{user_id}/password'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'user_id': user_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing change_password.', errors
            )

        if self.config.raw_response:
            return resp, change_password_response.ChangePasswordResponse.from_dictionary(
                resp.json()
            )
        return change_password_response.ChangePasswordResponse.from_dictionary(resp)
