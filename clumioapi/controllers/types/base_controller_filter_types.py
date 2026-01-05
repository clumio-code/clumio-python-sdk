#
# Copyright 2025. Clumio, A Commvault Company.
#
from typing import Any, Final

from clumioapi.api_helper import camel_to_snake
from pydantic import BaseModel

operations: Final[list[str]] = [
    'eq',
    'not_eq',
    'neq',
    'gte',
    'lte',
    'co',
    'regex',
    'contains',
    'not_contains',
    'gt',
    'lt',
    'in',
    'not_in',
    'all',
    'begins_with',
    'not_any',
    'not_all',
]


class BaseControllerFilterTypes(BaseModel):
    """Base class for filter types used in controllers."""

    @property
    def query_str(self) -> str:
        """Generates a query string from the filter attributes.

        Example:
            ```
            filter = BaseControllerFilterTypes()
            filter['Param1'] = {'eq': 'value1'}
            filter['Param2'] = {'gt': 10}
            filter['Param3'] = SubFilterType(SubFilterField={'eq': 'value3'})
            filter.query_str == '{
                param1: {"$eq": "value1"},
                param2: {"$gt": 10},
                param3.sub_filter_field: {"$eq": "value3"}
            }'
            ```
        """

        def _format_dict_value(value: dict) -> str:
            """Formats a dictionary value for inclusion in the query string."""
            dict_str = ''
            for k, v in value.items():
                if dict_str:
                    dict_str += ','
                dict_str += f'"{'$' if k in operations else ''}{k.lower()}":{format_value(v)}'
            return f'{{{dict_str}}}'

        def _format_nested_filter(value: BaseControllerFilterTypes, parent_key: str) -> str:
            """Formats a nested filter object for inclusion in the query string."""
            nested_str = value.query_str[1:-1]  # Remove the surrounding braces
            formatted_str = ''
            for part in nested_str.split(','):
                key, val = part.split(':', 1)
                formatted_str += f',"{parent_key}.{key.replace('"','')}":{val}'
            return formatted_str.strip(',')

        def format_value(value: Any, prefix: str = '') -> str:
            """Formats the value for inclusion in the query string, handling nested objects."""
            if isinstance(value, dict):
                if not value:
                    return f'"{prefix}":{{}}' if prefix else '{}'
                # Check if the dict is a tag
                is_tag = False
                if ['Key', 'Value'] == list(value.keys()):
                    is_tag = True
                if not is_tag and (key := list(value.keys())[0]).lower() != key:
                    # Handle nested objects like SubFilterType
                    result = ''
                    new_prefix = (
                        f'{prefix}.{camel_to_snake(key)}' if prefix else camel_to_snake(key)
                    )
                    result += format_value(value[key], new_prefix)
                    return result
                dict_str = _format_dict_value(value)
                return f'"{prefix}":{dict_str}' if prefix else dict_str
            if isinstance(value, bool):
                formatted_bool = str(value).lower()
                return f'"{prefix}":{formatted_bool}' if prefix else formatted_bool
            if isinstance(value, str):
                formatted_str = f'"{value}"'
                return f'"{prefix}":{formatted_str}' if prefix else formatted_str
            if isinstance(value, list):
                formatted_list = ', '.join(format_value(v) for v in value)
                return f'"{prefix}":[{formatted_list}]' if prefix else f'[{formatted_list}]'
            if isinstance(value, int):
                return f'"{prefix}":{value}' if prefix else str(value)
            if isinstance(value, BaseControllerFilterTypes):
                return _format_nested_filter(value, prefix)
            raise ValueError(f'Unsupported value type: {type(value)}')

        converted_str_list: list[str] = []
        for key in self.model_fields_set:
            value = getattr(self, key)
            if value is not None:
                converted_str_list.append(format_value(value, camel_to_snake(key)))
        return f'{{{','.join(converted_str_list)}}}'
