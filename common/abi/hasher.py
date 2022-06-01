import hashlib
from typing import Any, Callable

from tonclient.types import AbiContract, AbiFunction, AbiEvent, AbiData, AbiParam


class AbiHasher:

    def hash(self, abi: AbiContract) -> str:
        flatten = self.flatten(abi)
        return hashlib.sha256(flatten.encode()).hexdigest()

    def flatten(self, abi: AbiContract) -> str:
        version = self._str(abi.version)
        abi_version = self._str(abi.abi_version)
        headers = self.str_headers(abi.header)
        functions = self.str_inner(self.str_function, abi.functions)
        events = self.str_inner(self.str_event, abi.events)
        data = self.str_inner(self.str_data, abi.data)
        fields = self.str_inner(self.str_param, abi.fields)
        return self._join_brackets([version, abi_version, headers, functions, events, data, fields])

    @staticmethod
    def str_headers(headers: list[str] | None) -> str:
        if headers is None:
            return ''
        return ','.join(headers)

    def str_inner(self, handler: Callable, values: list) -> str:
        if values is None or len(values) == 0:
            return ''
        values = sorted(values, key=lambda value: value.name)
        values_str = [handler(value) for value in values]
        return self._join_brackets(values_str)

    def str_function(self, function: AbiFunction) -> str:
        inputs = self.str_params(function.inputs)
        outputs = self.str_params(function.outputs)
        function_id = self._str(function.id)
        return f'{function.name},[{inputs}],[{outputs}],{function_id}'

    def str_event(self, event: AbiEvent) -> str:
        inputs = self.str_params(event.inputs)
        function_id = self._str(event.id)
        return f'{event.name},[{inputs}],{function_id}'

    def str_data(self, data: AbiData) -> str:
        # ignore key
        components = self.str_params(data.components)
        return f'{data.name},{data.type},[{components}]'

    def str_params(self, params: list[AbiParam] | None) -> str:
        if params is None:
            return ''
        values = [self.str_param(param) for param in params]
        return self._join_brackets(values)

    def str_param(self, param: AbiParam) -> str:
        components = self.str_params(param.components)
        return f'{param.name},{param.type},[{components}]'

    @staticmethod
    def _join_brackets(values: list) -> str:
        if len(values) == 0:
            return ''
        return '(' + '),('.join(values) + ')'

    @staticmethod
    def _str(value: Any, default: str = '') -> str:
        if value is None:
            return default
        return str(value)
