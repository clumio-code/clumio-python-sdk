#
# Copyright 2023. Clumio, A Commvault Company.
#

import dataclasses
import enum
import json
import re
from typing import Any, Dict, Mapping
from urllib import parse

import jsonpickle

"""A Helper module for various functions associated with API Calls."""


def json_deserialize(json_string, unboxing_function: Any = None) -> Any:
    """JSON Deserialization of a given string.

    Args:
        json_string: The JSON serialized string to deserialize.
        unboxing_function (Any): Function used to convert the json string
            to a class instance.
    Returns:
        An object representing the data contained in the JSON serialized string.
    """
    if json_string is None:
        return None

    try:
        decoded = jsonpickle.decode(json_string)
    except (json.decoder.JSONDecodeError, ValueError):
        return json_string

    if not unboxing_function:
        return decoded
    elif isinstance(decoded, list):
        return [unboxing_function(element) for element in decoded]
    else:
        return unboxing_function(decoded)


def append_url_with_template_parameters(
    url: str, parameters: Mapping[str, Any], encode: bool = True
) -> str:
    """Replaces template parameters in the given url.

    Args:
        url: The query url string to replace the template parameters.
        parameters: The parameters to replace in the url.
        encode: Flag to indicate whether the request parameters should be encoded.
    Returns:
        URL with replaced parameters.
    """
    # Parameter validation
    if not url:
        raise ValueError('URL is None.')
    if not parameters:
        return url

    # Iterate and replace parameters
    for key in parameters:
        element = parameters[key]

        # Load parameter value
        if not element:
            replace_value = ''
        elif isinstance(element, list):
            replace_value = '/'.join(
                (parse.quote(str(x), safe='') if encode else str(x)) for x in element
            )
        else:
            replace_value = parse.quote(str(element), safe='') if encode else str(element)

        url = url.replace(f'{{{key}}}', str(replace_value))

    return url


def camel_to_snake(name: str) -> str:
    """Utility to convert string from camel case to snake case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    return name.replace('__', '_')
