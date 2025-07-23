#
# Copyright 2023. Clumio, A Commvault Company.
#

import enum
import json
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


def to_dictionary(obj: Any) -> Dict[str, Any]:
    """Creates a dictionary representation of a class instance. The
    keys are taken from the API description and may differ from language
    specific variable names of properties.

    Args:
        obj: The object to be converted into a dictionary.

    Returns:
        dictionary: A dictionary form of the model with properties in
        their API formats.
    """
    dictionary: dict[str, Any] = dict()
    # Loop through all properties in this model
    for name in obj._names:
        value = getattr(obj, name)
        attr_name = obj._names[name]
        if isinstance(value, list):
            dictionary[attr_name] = [_to_dictionary_or_value(item) for item in value]
        elif isinstance(value, dict):
            dictionary[attr_name] = {
                child_key: _to_dictionary_or_value(child_value)
                for child_key, child_value in value.items()
            }
        elif isinstance(value, enum.Enum):
            dictionary[attr_name] = value.name
        else:
            dictionary[attr_name] = _to_dictionary_or_value(value)

    # Return the result
    return dictionary


def _to_dictionary_or_value(item: Any) -> Any:
    """Convert to dictionary if it has the attribute _names or return as is."""
    return to_dictionary(item) if hasattr(item, '_names') else item
