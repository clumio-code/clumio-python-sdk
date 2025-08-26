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
from clumioapi.controllers.types import organizational_units_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_organizational_unit_no_task_response_v1
from clumioapi.models import create_organizational_unit_response_v1
from clumioapi.models import create_organizational_unit_v1_request
from clumioapi.models import delete_organizational_unit_response
from clumioapi.models import list_organizational_units_response_v1
from clumioapi.models import patch_organizational_unit_no_task_response_v1
from clumioapi.models import patch_organizational_unit_response_v1
from clumioapi.models import patch_organizational_unit_v1_request
from clumioapi.models import read_organizational_unit_response_v1
import requests


class OrganizationalUnitsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for organizational-units resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.organizational-units=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_organizational_units(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: organizational_units_types.ListOrganizationalUnitsV1FilterT | None = None,
        **kwargs,
    ) -> list_organizational_units_response_v1.ListOrganizationalUnitsResponseV1:
        """Returns a list of organizational units.

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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_organizational_units_response_v1.ListOrganizationalUnitsResponseV1.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/organizational-units'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_organizational_units_response_v1.ListOrganizationalUnitsResponseV1
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
            error_str = (
                f'list_organizational_units for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_organizational_unit(
        self,
        embed: str | None = None,
        body: create_organizational_unit_v1_request.CreateOrganizationalUnitV1Request | None = None,
        **kwargs,
    ) -> Union[
        create_organizational_unit_no_task_response_v1.CreateOrganizationalUnitNoTaskResponseV1,
        create_organizational_unit_response_v1.CreateOrganizationalUnitResponseV1,
    ]:
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:

            obj: Any

            obj = create_organizational_unit_no_task_response_v1.CreateOrganizationalUnitNoTaskResponseV1.from_response(
                resp
            )
            if resp.status_code == 200:
                return obj

            obj = create_organizational_unit_response_v1.CreateOrganizationalUnitResponseV1.from_response(
                resp
            )
            if resp.status_code == 202:
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for create_organizational_unit.', resp=resp
            )

        # Prepare query URL
        _url_path = '/organizational-units'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: Union[
            create_organizational_unit_no_task_response_v1.CreateOrganizationalUnitNoTaskResponseV1,
            create_organizational_unit_response_v1.CreateOrganizationalUnitResponseV1,
        ]
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
            error_str = (
                f'create_organizational_unit for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_organizational_unit(
        self, id: str | None = None, embed: str | None = None, **kwargs
    ) -> read_organizational_unit_response_v1.ReadOrganizationalUnitResponseV1:
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return (
                read_organizational_unit_response_v1.ReadOrganizationalUnitResponseV1.from_response(
                    response
                )
            )

        # Prepare query URL
        _url_path = '/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: read_organizational_unit_response_v1.ReadOrganizationalUnitResponseV1
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
            error_str = f'read_organizational_unit for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_organizational_unit(
        self, id: str | None = None, embed: str | None = None, **kwargs
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return (
                delete_organizational_unit_response.DeleteOrganizationalUnitResponse.from_response(
                    response
                )
            )

        # Prepare query URL
        _url_path = '/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: delete_organizational_unit_response.DeleteOrganizationalUnitResponse
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
            error_str = (
                f'delete_organizational_unit for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def patch_organizational_unit(
        self,
        id: str | None = None,
        embed: str | None = None,
        body: patch_organizational_unit_v1_request.PatchOrganizationalUnitV1Request | None = None,
        **kwargs,
    ) -> Union[
        patch_organizational_unit_no_task_response_v1.PatchOrganizationalUnitNoTaskResponseV1,
        patch_organizational_unit_response_v1.PatchOrganizationalUnitResponseV1,
    ]:
        """Patch the specified organizational unit.
        The complete updated attribute(s) of the organizational unit must be provided in
        the request. Adding or removing entities from the OU is an asynchronous
        operation
        and has an associated task. When the request has entities to be added or
        removed,
        the response contains a task ID that can be used to track the progress of the
        operation.

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

        """

        def get_instance_from_response(response: requests.Response) -> Any:

            obj: Any

            obj = patch_organizational_unit_no_task_response_v1.PatchOrganizationalUnitNoTaskResponseV1.from_response(
                resp
            )
            if resp.status_code == 200:
                return obj

            obj = patch_organizational_unit_response_v1.PatchOrganizationalUnitResponseV1.from_response(
                resp
            )
            if resp.status_code == 202:
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for patch_organizational_unit.', resp=resp
            )

        # Prepare query URL
        _url_path = '/organizational-units/{id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'id': id})
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: Union[
            patch_organizational_unit_no_task_response_v1.PatchOrganizationalUnitNoTaskResponseV1,
            patch_organizational_unit_response_v1.PatchOrganizationalUnitResponseV1,
        ]
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
            error_str = (
                f'patch_organizational_unit for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class OrganizationalUnitsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for organizational-units resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = OrganizationalUnitsV1Controller(config)

    def list_organizational_units(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: organizational_units_types.ListOrganizationalUnitsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_organizational_units_response_v1.ListOrganizationalUnitsResponseV1]:
        """Returns a list of organizational units.

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

        """
        start = start or '1'
        while True:
            response = self.controller.list_organizational_units(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
