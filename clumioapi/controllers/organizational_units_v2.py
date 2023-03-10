#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_organizational_unit_no_task_response
from clumioapi.models import create_organizational_unit_response
from clumioapi.models import create_organizational_unit_v2_request
from clumioapi.models import delete_organizational_unit_response
from clumioapi.models import list_organizational_units_response
from clumioapi.models import patch_organizational_unit_no_task_response
from clumioapi.models import patch_organizational_unit_response
from clumioapi.models import patch_organizational_unit_v2_request
from clumioapi.models import read_organizational_unit_response
import requests


class OrganizationalUnitsV2Controller(base_controller.BaseController):
    """A Controller to access Endpoints for organizational-units resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.organizational-units=v2+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_organizational_units(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_organizational_units_response.ListOrganizationalUnitsResponse:
        """Returns a list of organizational units.

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

                +-----------+------------------+-----------------------------------------------+
                |   Field   | Filter Condition |                  Description                  |
                +===========+==================+===============================================+
                | parent_id | $eq              | Retrieve the list of child OUs under this     |
                |           |                  | organizational unit.                          |
                +-----------+------------------+-----------------------------------------------+
                | name      | $contains        | A substring of the name of the organizational |
                |           |                  | unit.                                         |
                +-----------+------------------+-----------------------------------------------+
                | id        | $in              | Filter OUs whose ID is one of the given       |
                |           |                  | values.                                       |
                +-----------+------------------+-----------------------------------------------+

        Returns:
            list_organizational_units_response.ListOrganizationalUnitsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/organizational-units'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_organizational_units.', errors
            )

        return list_organizational_units_response.ListOrganizationalUnitsResponse.from_dictionary(
            resp
        )

    def create_organizational_unit(
        self,
        embed: str = None,
        body: create_organizational_unit_v2_request.CreateOrganizationalUnitV2Request = None,
    ) -> (
        create_organizational_unit_no_task_response.CreateOrganizationalUnitNoTaskResponse
        | create_organizational_unit_response.CreateOrganizationalUnitResponse
    ):
        """Create a new organizational unit. Adding entities to the OU is an asynchronous
        operation and has a task associated.
        When the request has entities to be added, the response has a task ID which can
        be used to
        track the progress of the operation.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        Returns:
            create_organizational_unit_no_task_response.CreateOrganizationalUnitNoTaskResponse | create_organizational_unit_response.CreateOrganizationalUnitResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/organizational-units'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_organizational_unit.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            return create_organizational_unit_no_task_response.CreateOrganizationalUnitNoTaskResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            return create_organizational_unit_response.CreateOrganizationalUnitResponse.from_dictionary(
                unmarshalled_dict
            )

    def read_organizational_unit(
        self, id: str, embed: str = None
    ) -> read_organizational_unit_response.ReadOrganizationalUnitResponse:
        """Returns a representation of the specified organizational unit.

        Args:
            id:
                Retrieve the organizational unit with the specified ID.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

        Returns:
            read_organizational_unit_response.ReadOrganizationalUnitResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_organizational_unit.', errors
            )

        return read_organizational_unit_response.ReadOrganizationalUnitResponse.from_dictionary(
            resp
        )

    def delete_organizational_unit(
        self, id: str, embed: str = None
    ) -> delete_organizational_unit_response.DeleteOrganizationalUnitResponse:
        """Delete the specified organizational unit.

        Args:
            id:
                Delete the organizational unit with the specified ID.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

        Returns:
            delete_organizational_unit_response.DeleteOrganizationalUnitResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.delete(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_organizational_unit.', errors
            )

        return delete_organizational_unit_response.DeleteOrganizationalUnitResponse.from_dictionary(
            resp
        )

    def patch_organizational_unit(
        self,
        id: str,
        embed: str = None,
        body: patch_organizational_unit_v2_request.PatchOrganizationalUnitV2Request = None,
    ) -> (
        patch_organizational_unit_no_task_response.PatchOrganizationalUnitNoTaskResponse
        | patch_organizational_unit_response.PatchOrganizationalUnitResponse
    ):
        """Patch the specified organizational unit.
        The complete updated attribute(s) of the organizational unit have to be provided
        in the request.
        Adding or removing entities from the OU is an asynchronous operation and has a
        task associated.
        When the request has entities to be added or removed, the response has a task ID
        which can be used to track the progress of the operation.

        Args:
            id:
                Patch the organizational unit with the specified ID.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        Returns:
            patch_organizational_unit_no_task_response.PatchOrganizationalUnitNoTaskResponse | patch_organizational_unit_response.PatchOrganizationalUnitResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing patch_organizational_unit.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            return patch_organizational_unit_no_task_response.PatchOrganizationalUnitNoTaskResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            return (
                patch_organizational_unit_response.PatchOrganizationalUnitResponse.from_dictionary(
                    unmarshalled_dict
                )
            )
