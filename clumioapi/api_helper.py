#
# Copyright 2023. Clumio, A Commvault Company.
#

import dataclasses
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


def to_filter_query_str(filter: Any, filter_cls: Any = None) -> str | None:
    """Serialize a controller ``filter`` argument into the API query string.

    Accepts three forms:

    * a ``...FilterT`` pydantic object (exposes a ``query_str`` property);
    * a plain dict copied straight from the API reference, matching the API JSON
      1:1 (snake_case / dotted keys, ``$``-prefixed operators), serialized as-is;
    * a legacy dict keyed by ``filter_cls``'s PascalCase field names, coerced
      through ``filter_cls`` for backward compatibility.
    """
    if not filter:
        return None
    if hasattr(filter, 'query_str'):
        return filter.query_str
    if filter_cls is not None and _is_legacy_filter_dict(filter, filter_cls):
        return filter_cls(**filter).query_str
    return json.dumps(filter, separators=(',', ':'))


def _is_legacy_filter_dict(filter: dict, filter_cls: Any) -> bool:
    """Whether ``filter`` is keyed by ``filter_cls``'s pydantic field names.

    Legacy callers passed dicts keyed by the model's PascalCase field names; the
    plain-dict surface uses the snake_case / dotted API field names. The two key
    sets never overlap, so membership in ``model_fields`` cleanly identifies the
    old form (and coerces it through the model to preserve its serialization).
    """
    fields = filter_cls.model_fields
    return all(key in fields for key in filter)


def to_dictionary(value: Any) -> Any:
    """Recursively convert a model into its API dictionary representation.

    Each model exposes a ``_names`` mapping from its Python attribute name to
    the exact API key. Keys that cannot be recovered from the attribute name are
    preserved via that mapping; any attribute missing from it falls back to
    ``camel_to_snake``. For example::

        GCPStringOperatorModel(Eq='us', NotIn=['eu']).dict()
            -> {'$eq': 'us', '$in': None, '$not_eq': None, '$not_in': ['eu']}
            #   'Eq'/'NotIn' come from _names; a plain 'UserId' would become 'user_id'
    """
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        names = getattr(value, '_names', {})
        result: Dict[str, Any] = {}
        for field in dataclasses.fields(value):
            attr = field.name
            result[names.get(attr, camel_to_snake(attr))] = to_dictionary(getattr(value, attr))
        return result
    if isinstance(value, (list, tuple)):
        return [to_dictionary(item) for item in value]
    if isinstance(value, dict):
        return {key: to_dictionary(item) for key, item in value.items()}
    return value
