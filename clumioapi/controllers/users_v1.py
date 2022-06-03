#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import change_password_v1_request
from clumioapi.models import create_user_response
from clumioapi.models import create_user_v1_request
from clumioapi.models import edit_profile_response
from clumioapi.models import list_users_response
from clumioapi.models import read_user_response
from clumioapi.models import update_user_profile_v1_request
from clumioapi.models import update_user_response
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
        }

    def list_users(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_users_response.ListUsersResponse:
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
            ListUsersResponse: Response from the API.
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
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_users.', errors
            )
        return list_users_response.ListUsersResponse.from_dictionary(resp)

    def create_user(
        self, body: create_user_v1_request.CreateUserV1Request = None
    ) -> create_user_response.CreateUserResponse:
        """Creates a new user. Specify the user's full name and email address to generate
        an email message that is sent to the user with an invitation to activate their
        Clumio account.

        Args:
            body:

        Returns:
            CreateUserResponse: Response from the API.
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_user.', errors
            )
        return create_user_response.CreateUserResponse.from_dictionary(resp)

    def update_user_profile(
        self, body: update_user_profile_v1_request.UpdateUserProfileV1Request = None
    ) -> edit_profile_response.EditProfileResponse:
        """Manages the current user's profile, such as changing the user's full name.

        Args:
            body:

        Returns:
            EditProfileResponse: Response from the API.
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_user_profile.', errors
            )
        return edit_profile_response.EditProfileResponse.from_dictionary(resp)

    def read_user(self, user_id: int) -> read_user_response.ReadUserResponse:
        """Returns a representation of the specified Clumio user.

        Args:
            user_id:
                Performs the operation on the user with the specified ID.
        Returns:
            ReadUserResponse: Response from the API.
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
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_user.', errors
            )
        return read_user_response.ReadUserResponse.from_dictionary(resp)

    def delete_user(self, user_id: int) -> object:
        """Deletes an existing user from Clumio, revoking the user's access to Clumio. A
        deleted user cannot be recovered.

        Args:
            user_id:
                The Clumio-assigned ID of the user to delete.
        Returns:
            object: Response from the API.
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
            resp = self.client.delete(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_user.', errors
            )
        return resp

    def update_user(
        self, user_id: int, body: update_user_v1_request.UpdateUserV1Request = None
    ) -> update_user_response.UpdateUserResponse:
        """Manages an existing user. Managing a user includes enabling or disabling the
        user,
        changing the user's full name or updating the user's role.

        Args:
            user_id:
                The Clumio-assigned ID of the user to delete.
            body:

        Returns:
            UpdateUserResponse: Response from the API.
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_user.', errors
            )
        return update_user_response.UpdateUserResponse.from_dictionary(resp)

    def change_password(
        self, user_id: int, body: change_password_v1_request.ChangePasswordV1Request = None
    ) -> object:
        """Change the password of the specified user. Users can change their own passwords.

        Args:
            user_id:
                Performs the operation on the user with the specified ID.
            body:

        Returns:
            object: Response from the API.
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing change_password.', errors
            )
        return resp
