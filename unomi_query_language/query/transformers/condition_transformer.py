from lark import Token
from unomi_query_language.query.mappers.operation_mapper import operation_mapper
from unomi_query_language.query.transformers.function_transformer import FunctionTransformer
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class ConditionTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cmp = operation_mapper
        self.namespace('uql_function__', FunctionTransformer())

    def and_expr(self, args):
        return "BOOLEAN-CONDITION", {
            "bool": "and",
            "subConditions": [args[0], args[2]]
        }

    def or_expr(self, args):
        return "BOOLEAN-CONDITION", {
            "bool": "or",
            "subConditions": [args[0], args[2]]
        }

    def OP_FIELD(self, args):

        if ':' in args:
            splited_args = args.split(":")
            type = splited_args[0]
            field = splited_args[1]
            return {
                'field': {
                    'unomi-type': type,
                    'field': field
                }
            }
        else:
            return {
                'field': {
                    'field': args.value
                }
            }

    def op_condition(self, args):

        args = {
            'field': args[0]['field'],
            'op': args[1]['op'],
            'values': args[2] if len(args) > 2 else None,
        }

        return 'CONDITION', args

    def op_between(self, args):

        args[1] = {
            'op': {
                'unomi-op': self._cmp['between'],
            }
        }

        return self.op_condition(args)

    def op_exists(self, args):

        args.append({'op': {
            'unomi-op': self._cmp['exists'],
        }})

        return self.op_condition(args)

    def op_not_exists(self, args):

        args.append({'op': {
            'unomi-op': self._cmp['not exists'],
        }})

        return self.op_condition(args)

    def op_is_null(self, args):

        args = [
            args[0],
            {
                'op': {
                    'unomi-op': self._cmp['is null'],
                }
            },
            {
                'value': {
                    'type': 'null',
                    "unomi-type": 'propertyValue',
                    'value': 'null'
                }
            }
        ]

        return self.op_condition(args)

    def OP(self, args):
        return {
            'op': {
                'unomi-op': self._cmp[str(args)],
            }
        }

    def op_value(self, args):
        token = args[0]  # type: Token
        if isinstance(token, Token):
            return token.value
        else:
            return token

    def OP_BOOL(self, args):
        return {
            'value': {
                'type': 'bool',
                "unomi-type": 'propertyValue',
                'value': True if args.value.lower() == 'true' else False
            }
        }

    def OP_INTEGER(self, args):
        return {
            'value': {
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': int(args.value)
            }
        }

    def OP_FLOAT(self, args):
        return {
            'value': {
                'type': 'number',
                "unomi-type": 'propertyValueDouble',
                'value': float(args.value)
            }
        }

    def OP_STRING(self, args):
        string = str(args.value.strip('"'))
        string = string.replace('(', "\"")

        return {
            'value': {
                'unomi-type': "propertyValue",
                'type': 'string',
                'value': string.replace(")", "\"")
            }

        }

    def op_array(self, args):
        return {
            'value': {
                "unomi-type": "propertyValues",
                'type': 'array',
                'value': [v['value']['value'] for v in args]
            }
        }

    def op_dict(self, args):
        value = args[0] if len(args) > 0 else {}
        if len(args) > 1:
            value.update(args[1])

        return {
            'value': {
                "unomi-type": "propertyValues",
                'type': 'dict',
                'value': value
            }
        }

    def pair(self, args):
        key, value = args
        return {key['value']['value']: value['value']['value']}

    def op_range(self, args):
        values = [v['value']['value'] for v in args]
        return {
            'value': {
                "unomi-type": "propertyValuesInteger",
                'type': 'range',
                'value': values
            }
        }

    def OP_NULL(self, args):
        return {
            'value': {
                "unomi-type": "propertyValue",
                'type': 'null',
                'value': None
            }
        }

    def OP_TIME(self, args):
        value = int(args.value[:-1])
        type = args.value[-1]
        if type == "s":
            value = value * 1000
        elif type == 'h':
            value = value * 1000 * 60
        elif value == 'd':
            value = value * 1000 * 60 * 24
        else:
            raise ValueError("Unknown time type {}.".format(type))

        return {
            'value': {
                'unomi-type': "propertyValueInteger",
                'type': 'number',
                'value': value
            }
        }
