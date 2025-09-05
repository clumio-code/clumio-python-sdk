#
# Copyright 2025. Clumio, A Commvault Company.
#
from typing import Any

from clumioapi.api_helper import camel_to_snake
from pydantic import BaseModel


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

        def format_value(value: Any, prefix: str = '') -> str:
            """Formats the value for inclusion in the query string, handling nested objects."""
            if isinstance(value, dict):
                if value and (key := list(value.keys())[0]).lower() != key:
                    # Handle nested objects like SubFilterType
                    result = ''
                    new_prefix = (
                        f'{prefix}.{camel_to_snake(key)}' if prefix else camel_to_snake(key)
                    )
                    result += format_value(value[key], new_prefix)
                    return result
                dict_str = ''
                for k, v in value.items():
                    if dict_str:
                        dict_str += ', '
                    dict_str += f'"${k}":{format_value(v)}'
                return f'{prefix}:{{{dict_str}}}' if prefix else f'{{{dict_str}}}'
            if isinstance(value, bool):
                formatted_bool = str(value).lower()
                return f'{prefix}:{formatted_bool}' if prefix else formatted_bool
            if isinstance(value, str):
                formatted_str = f'"{value}"'
                return f'{prefix}:{formatted_str}' if prefix else formatted_str
            if isinstance(value, list):
                formatted_list = ', '.join(format_value(v) for v in value)
                return f'{prefix}:[{formatted_list}]' if prefix else f'[{formatted_list}]'
            raise ValueError(f'Unsupported value type: {type(value)}')

        converted_str_list: list[str] = []
        for key, value in self.model_dump(exclude_none=True).items():
            converted_str_list.append(
                f'"{format_value(value, camel_to_snake(key)).replace(':', '":', 1)}'
            )
        return f'{{{','.join(converted_str_list)}}}'
